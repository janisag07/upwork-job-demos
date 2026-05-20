import json, re, time, urllib.request, websocket
PORT=18810
ORIGIN=f'http://127.0.0.1:{PORT}'
JOBS=[
 ('1','AI Agent & Automation Specialist | Chatbots, n8n Workflows, OpenAI Integrations','~022057057657527907698',10000),
 ('3','Google Sheets / Apps Script Developer for ATS Job-Posting Data Pipeline','~022057128500223180315',500),
 ('4','Hubspot Landing Page Web Developer','~022057159364433087775',300),
 ('5','AI Automation & Integration Expert','~022057115799573935474',500),
]
pages=json.load(urllib.request.urlopen(ORIGIN+'/json',timeout=5))
page=next((p for p in pages if p.get('type')=='page' and 'upwork.com' in p.get('url','')), next(p for p in pages if p.get('type')=='page'))
ws=websocket.create_connection(page['webSocketDebuggerUrl'], origin=ORIGIN, timeout=30)
i=0
def call(m,p=None):
    global i
    i+=1
    ws.send(json.dumps({'id':i,'method':m,'params':p or {}}))
    while True:
        msg=json.loads(ws.recv())
        if msg.get('id')==i:
            return msg.get('result',{})
call('Runtime.enable'); call('Page.enable')
def ev(expr):
    return call('Runtime.evaluate',{'expression':expr,'returnByValue':True,'awaitPromise':True}).get('result',{}).get('value')
res=[]
for no,title,jid,budget in JOBS:
    url=f'https://www.upwork.com/nx/proposals/job/{jid}/apply/'
    call('Page.navigate',{'url':url}); time.sleep(6)
    data=json.loads(ev('JSON.stringify({title:document.title,href:location.href,text:document.body.innerText,inputs:[...document.querySelectorAll("input,textarea,button,[role=button]")].filter(e=>!!e.offsetParent).slice(0,80).map(e=>({tag:e.tagName,type:e.type||e.getAttribute("role"),text:(e.innerText||e.value||e.getAttribute("aria-label")||e.placeholder||"").trim().slice(0,120),disabled:!!e.disabled}))})'))
    text=data['text'] or ''
    res.append({
        'no':no,'title':title,'jid':jid,'budget':budget,'apply_url':url,
        'loaded_title':data['title'],'href':data['href'],'text_head':text[:2500],
        'is_login': 'Log in to Upwork' in text or data['title'].lower().startswith('upwork login') or '/ab/account-security/login' in data['href'],
        'is_apply_form': 'Submit a proposal' in text or 'Cover Letter' in text or 'Send for' in text,
        'no_longer_available':'no longer available' in text.lower(),
        'already_submitted':'already submitted' in text.lower() or 'active, or declined proposal' in text.lower(),
        'earnings_10k':'Earnings: At Least 10000' in text or 'At least $10k earned' in text or 'At Least 10000' in text,
        'preferred_warning':'You do not meet all the client' in text,
        'connects': re.findall(r'(\d+)\s+Connects', text)[:10],
        'buttons': data['inputs'][-20:]
    })
print(json.dumps({'checked_at':time.strftime('%Y-%m-%d %H:%M:%S'),'results':res},ensure_ascii=False,indent=2))
ws.close()
