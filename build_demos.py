from pathlib import Path
import textwrap, json, re
root = Path('/Users/nani/workspace/upwork-job-demos/publish')
root.mkdir(parents=True, exist_ok=True)

jobs = [
    {
        'slug':'real-estate-53k-command-center',
        'title':'Real Estate AI Workflow Command Center',
        'eyebrow':'Premium demo for $53k fixed-price milestone proposal',
        'subtitle':'A production-style operations cockpit connecting Follow Up Boss, Zapier, OpenAI/Claude, Asana, Google Workspace, Plaud, and transaction workflows into one automated real-estate pipeline.',
        'accent':'#22c55e',
        'dark':'#06130d',
        'cta':'View the 6-department automation blueprint',
        'stats':[('Projected Build','5–7 months → faster delivery plan'),('Fixed Price','$53,000'),('Milestones','8 structured phases'),('Departments','6 connected workflows')],
        'sections':['Lead intake → AI comp / ARV analysis','AI appointment scheduling + routing criteria','Sales prep notes generated from seller data','Plaud transcription → structured Follow Up Boss notes','Contract/title request automation','Pricing strategy engine + Mevlo marketplace packet'],
        'cards':[('Lead Intake Agent','New seller lead captured, enriched, scored, and pushed into Follow Up Boss with motivation notes.'),('ARV/Comp Analyzer','Claude/OpenAI compares property data, notes risk factors, and produces an underwriting-ready summary.'),('Appointment Prep','Before the appointment, the rep gets seller context, objection forecast, suggested offer range, and call strategy.'),('Transaction Coordinator','Docs, title requests, Asana tasks, and Slack notifications are generated without manual copy-paste.')],
        'timeline':['Discovery + architecture map','FUB/Zapier backbone + error handling','AI comp engine + seller scoring','Appointment + Plaud workflow','Docs/title/transaction automation','Pricing/disposition engine','QA, monitoring, handover','Ongoing optimization option'],
        'mock':'premium_real_estate'
    },
    {
        'slug':'real-estate-ai-lead-agents',
        'title':'24/7 Real Estate AI Lead Agents',
        'eyebrow':'Demo for $10,000 fixed-price lead generation system',
        'subtitle':'Seller and buyer AI agents that research, score, route, and follow up with high-intent leads inside the CRM.',
        'accent':'#60a5fa','dark':'#06111f','cta':'Explore seller + buyer lead agents',
        'stats':[('Budget','$10,000 fixed'),('Agents','Seller + Buyer'),('CRM','Follow Up Boss'),('Mode','24/7 automated')],
        'sections':['Predictive seller motivation scoring','Buyer content/ad angle generation','CRM tagging + routing','Follow-up sequence suggestions','Lead source intelligence','Appointment push workflows'],
        'cards':[('Seller Signal Agent','Divorce, probate, relocation, expired listing, and distress indicators are summarized into one confidence score.'),('Buyer Demand Agent','Uses market trends and off-market inventory to suggest content/ad angles that push buyers to book showings.'),('CRM Router','Tags leads by urgency, source, motivation, property type, and next best action.'),('Messaging Copilot','Creates personalized SMS/email openers based on lead motivation.')],
        'timeline':['Lead source mapping','Scoring model design','CRM integration','Follow-up flows','Dashboard + reporting'],
        'mock':'lead_agents'
    },
    {
        'slug':'trades-ai-sms-answering-platform',
        'title':'Velloos-Style AI SMS Answering Platform',
        'eyebrow':'Demo for $3,500 GoHighLevel SaaS build',
        'subtitle':'An SMS-first AI answering and booking platform for HVAC, plumbing, and electricians — with missed-call response, qualification, scheduling, and usage billing.',
        'accent':'#f59e0b','dark':'#1d1202','cta':'Open trades SMS platform demo',
        'stats':[('Budget','$3,000–$3,500'),('Verticals','HVAC / Plumbing / Electric'),('Backend','GoHighLevel SaaS'),('Timeline','6–8 weeks')],
        'sections':['Missed call → instant SMS response','Trade-specific qualification flows','Calendar booking + job library','Tiered portal feature gates','SMS usage tracking + overage logic','Demo numbers for each vertical'],
        'cards':[('Missed-Call Responder','Automatically texts callers back, asks the right questions, and prevents lost jobs.'),('Job Library','Uses uploaded services, pricing, and duration to qualify and schedule correctly.'),('Client Portal','Starter, Trade-Specific, and Elite feature gating with clear usage metrics.'),('Review Recovery','After a completed job, the system requests Google reviews and follows up intelligently.')],
        'timeline':['GHL SaaS structure','AI flows per vertical','Calendar + job library','Portal + billing logic','Demo numbers + QA'],
        'mock':'trades'
    },
    {
        'slug':'whatsapp-clinic-booking-bot',
        'title':'WhatsApp Clinic Booking Bot',
        'eyebrow':'Demo for medical clinic WhatsApp + Voiceflow + Make job',
        'subtitle':'Patient-friendly WhatsApp automation for appointment booking, intake questions, CRM sync, and staff handoff.',
        'accent':'#10b981','dark':'#031a13','cta':'Test clinic booking flow visually',
        'stats':[('Budget','$200 fixed'),('Channel','WhatsApp'),('Tools','Voiceflow + Make'),('Outcome','Appointments booked')],
        'sections':['Patient intent detection','Appointment slot selection','CRM/contact sync','Healthcare-friendly handoff','No-show reminder flow','Privacy-aware intake'],
        'cards':[('Appointment Bot','Guides patients from greeting to booked slot without confusing menus.'),('CRM Sync','Creates or updates patient records and flags reason for visit.'),('Staff Handoff','Escalates complex messages with a clean context summary.'),('Reminder Flow','Sends confirmation and reminder templates to reduce no-shows.')],
        'timeline':['Flow mapping','WhatsApp setup','CRM sync','Booking rules','Testing'],
        'mock':'clinic'
    },
    {
        'slug':'optimum-intelligence-automation-suite',
        'title':'Optimum Intelligence Automation Suite',
        'eyebrow':'Demo for WhatsApp chatbot + customer service + booking systems',
        'subtitle':'A scalable client automation suite combining WhatsApp support, lead capture, appointment booking, and business dashboard views.',
        'accent':'#8b5cf6','dark':'#13091f','cta':'Open automation suite demo',
        'stats':[('Budget','$300 fixed'),('Potential','Long-term projects'),('Channels','WhatsApp + Web'),('Use cases','Support + Booking')],
        'sections':['WhatsApp customer service bot','Appointment booking workflow','Lead qualification + CRM push','Reusable client templates','Admin dashboard','Escalation + analytics'],
        'cards':[('Client Template Library','Reusable automation packages for clinics, salons, agencies, and service businesses.'),('Booking Engine','Captures service type, location, preferred time, and contact details.'),('Support Agent','Answers FAQs, collects context, and escalates with summaries.'),('Performance View','Shows conversations, bookings, missed leads, and conversion rate.')],
        'timeline':['Base WhatsApp bot','Booking module','CRM connector','Dashboard','Template packaging'],
        'mock':'optimum'
    },
    {
        'slug':'tesla-parts-sniper-system',
        'title':'Tesla Parts Sniper Automation System',
        'eyebrow':'Demo for automated Tesla parts hunting dashboard',
        'subtitle':'A polished parts monitoring system that searches marketplaces, scores matches, alerts instantly, and tracks seller outreach.',
        'accent':'#ef4444','dark':'#1f0606','cta':'View parts sniper dashboard',
        'stats':[('Budget','$350 fixed'),('Sources','Marketplace / eBay / Craigslist'),('Alerts','SMS + Email'),('Scoring','Smart match score')],
        'sections':['Vehicle/part search profiles','Marketplace monitoring','Color/year/model matching','Seller outreach workflow','Duplicate detection','Deal status tracking'],
        'cards':[('Search Profile','Enter year, model, VIN, color, region, and needed parts once.'),('Match Scoring','Ranks listings by part fit, color, price, distance, and freshness.'),('Instant Alerts','Sends high-score matches before other buyers move.'),('Pipeline Tracker','Tracks contacted, waiting, bought, pass, duplicate, and notes.')],
        'timeline':['Dashboard build','Source connector strategy','Scoring logic','Alerts','Seller workflow'],
        'mock':'tesla'
    },
    {
        'slug':'golf-affiliate-content-automation',
        'title':'Golf Affiliate Content Automation Studio',
        'eyebrow':'Demo for golf training aid TikTok/Instagram automation',
        'subtitle':'AI-assisted content engine for golf affiliate accounts: scripts, hooks, captions, scheduling, affiliate links, and monthly reporting.',
        'accent':'#84cc16','dark':'#101a05','cta':'Open content automation demo',
        'stats':[('Budget','$500 fixed'),('Content','20–30 scripts/month'),('Platforms','TikTok + Instagram'),('Goal','Affiliate clicks')],
        'sections':['Product research + script generation','Hook/caption creation','Affiliate link tracking','Posting schedule calendar','Trend/audio research','Monthly performance report'],
        'cards':[('Script Generator','Turns golf products into before/after, tip, review, and trend scripts.'),('Affiliate Tracker','Shows clicks, top products, and content-to-sale attribution.'),('Content Calendar','Plans Reels/TikToks with hooks, captions, hashtags, and CTA.'),('Performance Report','Monthly view of views, followers, top posts, and click-through rate.')],
        'timeline':['Brand setup','Affiliate links','Script batches','Scheduling workflow','Reporting dashboard'],
        'mock':'golf'
    },
]

CSS = r'''
:root{--accent:#22c55e;--dark:#06130d;--muted:#9ca3af;--card:rgba(255,255,255,.08);--line:rgba(255,255,255,.14)}
*{box-sizing:border-box} body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Arial;background:radial-gradient(circle at 20% 0%,color-mix(in srgb,var(--accent) 30%,transparent),transparent 35%),linear-gradient(135deg,var(--dark),#050505 60%,#101010);color:#fff;min-height:100vh} a{color:inherit}.wrap{max-width:1180px;margin:0 auto;padding:34px 22px 70px}.top{display:flex;justify-content:space-between;gap:18px;align-items:center;margin-bottom:34px}.brand{display:flex;gap:12px;align-items:center}.logo{width:42px;height:42px;border-radius:14px;background:linear-gradient(135deg,var(--accent),#fff);box-shadow:0 0 40px color-mix(in srgb,var(--accent) 55%,transparent)}.pill,.disclaimer{border:1px solid var(--line);background:rgba(255,255,255,.07);backdrop-filter:blur(20px);border-radius:999px;padding:9px 13px;color:#d1d5db;font-size:13px}.hero{display:grid;grid-template-columns:1.02fr .98fr;gap:26px;align-items:center}.eyebrow{color:var(--accent);font-weight:800;letter-spacing:.08em;text-transform:uppercase;font-size:12px}h1{font-size:clamp(38px,6vw,76px);line-height:.95;margin:12px 0 18px;letter-spacing:-.06em}.subtitle{color:#d1d5db;font-size:18px;line-height:1.6;max-width:720px}.actions{display:flex;gap:12px;margin-top:24px;flex-wrap:wrap}.btn{border:0;border-radius:16px;background:var(--accent);color:#04100a;padding:14px 18px;font-weight:900;box-shadow:0 18px 60px color-mix(in srgb,var(--accent) 30%,transparent)}.btn.secondary{background:rgba(255,255,255,.08);color:#fff;border:1px solid var(--line);box-shadow:none}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:30px 0}.stat{border:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.10),rgba(255,255,255,.045));border-radius:22px;padding:18px}.stat b{display:block;font-size:24px;letter-spacing:-.04em}.stat span{color:var(--muted);font-size:13px}.panel{border:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.12),rgba(255,255,255,.05));border-radius:30px;padding:18px;box-shadow:0 30px 100px rgba(0,0,0,.45)}.screen{background:#080b10;border-radius:24px;overflow:hidden;border:1px solid rgba(255,255,255,.1)}.bar{height:44px;background:#0e1117;display:flex;align-items:center;gap:8px;padding:0 15px}.dot{width:10px;height:10px;border-radius:50%;background:#ef4444}.dot:nth-child(2){background:#f59e0b}.dot:nth-child(3){background:#22c55e}.dash{padding:16px;display:grid;grid-template-columns:1fr 1fr;gap:12px}.widget{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:14px}.widget h3{font-size:13px;margin:0 0 10px;color:#d1d5db}.big{font-size:32px;font-weight:900;letter-spacing:-.05em}.progress{height:9px;border-radius:99px;background:#1f2937;overflow:hidden;margin-top:8px}.progress i{display:block;height:100%;background:linear-gradient(90deg,var(--accent),#fff);border-radius:99px}.list{display:grid;gap:8px}.item{display:flex;justify-content:space-between;gap:12px;padding:10px;border-radius:14px;background:rgba(255,255,255,.05);font-size:13px}.item strong{color:#fff}.item span{color:var(--accent);font-weight:800}.section{margin-top:34px}.section h2{font-size:34px;letter-spacing:-.04em;margin:0 0 16px}.cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}.card{border:1px solid var(--line);background:rgba(255,255,255,.06);border-radius:24px;padding:22px}.card h3{margin:0 0 8px}.card p{color:#cbd5e1;line-height:1.55;margin:0}.workflow{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.step{position:relative;border:1px solid var(--line);background:rgba(255,255,255,.05);border-radius:22px;padding:18px;min-height:104px}.step b{color:var(--accent)}.demo-row{display:grid;grid-template-columns:1.1fr .9fr;gap:18px}.chat{display:grid;gap:10px}.bubble{max-width:86%;padding:12px 14px;border-radius:17px;background:rgba(255,255,255,.1);color:#e5e7eb}.bubble.me{justify-self:end;background:color-mix(in srgb,var(--accent) 35%,#111);border:1px solid color-mix(in srgb,var(--accent) 45%,transparent)}.footer{margin-top:42px;color:#9ca3af;font-size:13px;text-align:center}.tag{display:inline-block;margin:4px 6px 0 0;border:1px solid rgba(255,255,255,.14);padding:7px 10px;border-radius:99px;color:#cbd5e1;background:rgba(255,255,255,.05);font-size:12px}.premium-note{margin-top:16px;border:1px solid color-mix(in srgb,var(--accent) 50%,transparent);background:color-mix(in srgb,var(--accent) 12%,transparent);border-radius:18px;padding:14px;color:#ecfdf5}.milestone{display:flex;gap:12px;align-items:flex-start}.num{min-width:30px;height:30px;border-radius:10px;background:var(--accent);color:#06130d;display:grid;place-items:center;font-weight:900}@media(max-width:900px){.hero,.cols,.demo-row{grid-template-columns:1fr}.grid{grid-template-columns:repeat(2,1fr)}.workflow{grid-template-columns:1fr}.top{align-items:flex-start;flex-direction:column}.dash{grid-template-columns:1fr}h1{font-size:44px}}
'''

mock_js = r'''
function fillMock(type){
 const lists={
 premium_real_estate:[['New Seller Lead','Motivation 91%'],['ARV Analysis','Range $412k–$438k'],['Plaud Notes','Synced to FUB'],['Title Request','Draft ready']],
 lead_agents:[['Probate Signal','High intent'],['Expired Listing','Message angle ready'],['Buyer Campaign','3 ad hooks'],['CRM Route','Hot seller queue']],
 trades:[['Missed Call','SMS sent in 14 sec'],['HVAC Booking','Friday 2:30 PM'],['SMS Usage','72 / 500'],['Review Request','Queued']],
 clinic:[['New Patient','Dermatology consult'],['Slot Selected','Tomorrow 10:30'],['CRM Sync','Contact updated'],['Reminder','24h before visit']],
 optimum:[['WhatsApp Lead','Qualified'],['Booking Flow','Active'],['Support Case','Escalated'],['Conversion','38%']],
 tesla:[['Model 3 Door','94% match'],['eBay Motors','Alert sent'],['Craigslist LA','Possible duplicate'],['Seller Contact','Template ready']],
 golf:[['Product Script','Orange Whip trainer'],['Hook Score','88/100'],['Affiliate CTR','6.2%'],['Reel Schedule','5 posts ready']]
 };
 const rows=lists[type]||lists.premium_real_estate;
 document.querySelectorAll('[data-mock-list]').forEach(el=>{el.innerHTML=rows.map(r=>`<div class="item"><strong>${r[0]}</strong><span>${r[1]}</span></div>`).join('')});
}
'''

def html(job):
    sections = ''.join(f'<span class="tag">{s}</span>' for s in job['sections'])
    stats = ''.join(f'<div class="stat"><span>{k}</span><b>{v}</b></div>' for k,v in job['stats'])
    cards = ''.join(f'<div class="card"><h3>{t}</h3><p>{p}</p></div>' for t,p in job['cards'])
    timeline = ''.join(f'<div class="step milestone"><div class="num">{i}</div><div><b>Phase {i}</b><p style="margin:7px 0 0;color:#cbd5e1">{t}</p></div></div>' for i,t in enumerate(job['timeline'],1))
    premium = ''
    if job['slug']=='real-estate-53k-command-center':
        premium = '<div class="premium-note"><b>Proposal positioning:</b> Janis can offer this as a fixed $53,000 build, split into clear milestones. The client gets cost certainty, faster delivery than the hourly 5–7 month estimate, and a structured rollout with weekly proof.</div>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{job['title']}</title><style>{CSS}</style></head><body style="--accent:{job['accent']};--dark:{job['dark']}"><div class="wrap"><header class="top"><div class="brand"><div class="logo"></div><div><b>Janis Agic — AI Automation Demo</b><div style="color:#9ca3af;font-size:13px">Client-facing visual prototype</div></div></div><div class="pill">Fictional demo data • Built for proposal review</div></header><main class="hero"><section><div class="eyebrow">{job['eyebrow']}</div><h1>{job['title']}</h1><p class="subtitle">{job['subtitle']}</p><div class="disclaimer" style="display:inline-block;margin-top:12px;border-radius:14px">Disclaimer: All displayed data, names, messages, and metrics are fictional and shown for visual demonstration purposes only.</div>{premium}<div class="actions"><a class="btn">{job['cta']}</a><a class="btn secondary" href="#workflow">Workflow plan</a></div></section><section class="panel"><div class="screen"><div class="bar"><i class="dot"></i><i class="dot"></i><i class="dot"></i><span style="color:#9ca3af;margin-left:8px;font-size:13px">live-ops.demo/janis</span></div><div class="dash"><div class="widget"><h3>Automation Health</h3><div class="big">98%</div><div class="progress"><i style="width:98%"></i></div></div><div class="widget"><h3>Manual Work Reduced</h3><div class="big">72%</div><div class="progress"><i style="width:72%"></i></div></div><div class="widget" style="grid-column:1/-1"><h3>Live System Events</h3><div class="list" data-mock-list></div></div></div></div></section></main><section class="grid">{stats}</section><section class="section demo-row"><div><h2>What this demo proves</h2><div>{sections}</div></div><div class="chat panel"><div class="bubble">Client asks: “Can this reduce manual work without breaking our process?”</div><div class="bubble me">Yes — the system keeps humans in control, automates the repetitive work, and routes edge cases with full context.</div><div class="bubble">What makes it reliable?</div><div class="bubble me">Structured workflows, audit logs, milestone rollout, error handling, and clear handoff documentation.</div></div></section><section class="section"><h2>Core modules</h2><div class="cols">{cards}</div></section><section class="section" id="workflow"><h2>Implementation workflow</h2><div class="workflow">{timeline}</div></section><div class="footer">Prepared as a visual sales demo for Janis Agic. Not connected to real client data.</div></div><script>{mock_js}\nfillMock('{job['mock']}')</script></body></html>'''

index_cards=[]
for job in jobs:
    d=root/job['slug']; d.mkdir(exist_ok=True)
    (d/'index.html').write_text(html(job))
    index_cards.append(f'<li><a href="{job["slug"]}/">{job["title"]}</a></li>')
(root/'index.html').write_text('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Janis Upwork Demos</title><style>body{font-family:Inter,system-ui;background:#050505;color:white;padding:40px}a{color:#22c55e;font-size:22px;line-height:2}</style></head><body><h1>Janis Upwork Demos — internal index</h1><ul>'+''.join(index_cards)+'</ul></body></html>')
print(json.dumps([job['slug'] for job in jobs], indent=2))
