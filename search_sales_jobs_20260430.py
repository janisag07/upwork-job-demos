import json, re, time, urllib.parse, urllib.request, websocket
PORT=18802; ORIGIN=f'http://127.0.0.1:{PORT}'
queries=[
 '"Sales Pipeline" Zapier Pipedrive Notion fixed price',
 '"HubSpot Sales Hub" Pipeline Sequences LinkedIn fixed price',
 '"CRM automation" "lead follow up" fixed price',
 '"Gmail inbound" "AI classification" Pipedrive fixed price',
 '"sales automation" "Pipedrive" "AI" fixed price',
]
class C:
 def __init__(self):
  pages=[p for p in json.load(urllib.request.urlopen(ORIGIN+'/json',timeout=5)) if p.get('type')=='page']
  page=next((p for p in pages if 'upwork.com' in p.get('url','')), pages[0])
  self.ws=websocket.create_connection(page['webSocketDebuggerUrl'],origin=ORIGIN,timeout=30); self.i=0
  self.call('Runtime.enable'); self.call('Page.enable')
 def call(self,m,p=None):
  self.i+=1; self.ws.send(json.dumps({'id':self.i,'method':m,'params':p or {}}))
  while True:
   msg=json.loads(self.ws.recv())
   if msg.get('id')==self.i: return msg.get('result',{})
 def ev(self,e): return self.call('Runtime.evaluate',{'expression':e,'returnByValue':True,'awaitPromise':True}).get('result',{}).get('value')
 def nav(self,u,w=6): self.call('Page.navigate',{'url':u}); time.sleep(w)

def classify(txt):
 if 'Hourly' in txt: return 'skip-hourly'
 props=(re.search(r'Proposals:\s*([^\n]+)',txt) or ['',''])[1]
 verified='Payment verified' in txt
 spend=(re.search(r'\$[\d.KM+]+\s*\n?spent|\$[\d.KM+]+ spent',txt) or [''])[0].replace('\n',' ')
 budget=(re.search(r'Est\. budget:\s*\$([\d,]+(?:\.\d+)?)',txt) or ['','0'])[1]
 posted=(re.search(r'Posted [^\n]+',txt) or [''])[0]
 if not verified: grade='C'
 elif props in ['Less than 5','5 to 10'] and float(budget.replace(',','') or 0)>=500: grade='A'
 elif props in ['Less than 5','5 to 10','10 to 15']: grade='B'
 else: grade='C'
 return dict(proposals=props,verified=verified,spend=spend,budget=budget,posted=posted,grade=grade)

c=C(); results=[]; seen=set()
try:
 for q in queries:
  c.nav('https://www.upwork.com/nx/search/jobs/?sort=recency&q='+urllib.parse.quote(q))
  cards=json.loads(c.ev(r"""
  JSON.stringify([...document.querySelectorAll('article, section, div[data-test]')].map(el=>{
    const text=(el.innerText||'').trim();
    const a=el.querySelector('a[href*="/jobs/"]');
    return {text, url:a?a.href:null, title:a?(a.innerText||a.textContent||'').trim():''};
  }).filter(x=>x.url&&x.text.includes('Proposals:')).slice(0,20))
  """) or '[]')
  for card in cards:
   title=re.sub(r'\s+',' ',card['title']).strip()
   if not title or len(title)<8: continue
   key=card['url'].split('?')[0]
   if key in seen: continue
   seen.add(key)
   if 'Fixed price' not in card['text']: continue
   meta=classify(card['text'])
   if not isinstance(meta, dict): continue
   if any(bad in card['text'] for bad in ['Applied','You applied']): continue
   results.append({**meta,'title':title,'url':card['url'],'query':q,'excerpt':card['text'][:1400]})
finally:
 c.ws.close()
print(json.dumps(results[:20],ensure_ascii=False,indent=2))
