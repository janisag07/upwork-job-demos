from pathlib import Path
from textwrap import dedent
import html

ROOT = Path(__file__).resolve().parent
PUBLISH = ROOT / 'publish'

jobs = [
    {
        'slug': 'revops-automation-command-center',
        'title': 'RevOps Automation Command Center',
        'subtitle': 'n8n + CRM automation infrastructure for high-speed outbound teams',
        'client': 'Automation Specialist (RevOps)',
        'budget': '$1,000 fixed',
        'accent': '#7c3aed',
        'accent2': '#06b6d4',
        'price_note': 'Built as a fast fixed-price implementation: scope, build, deploy, document.',
        'hero': 'A production-style operations dashboard showing how positive replies, enrichment, CRM routing, Slack alerts, and campaign performance can be handled in one clean automation layer.',
        'metrics': [('Reply → Slack', '<60 sec'), ('Workflow build', '1–3 days'), ('CRM routing', 'Auto'), ('Data quality', 'Deduped')],
        'modules': [
            ('Positive Reply Detector', 'Classifies replies from Instantly/Email Bison and triggers enriched alerts only for real opportunities.'),
            ('CRM Deal Creator', 'Creates HubSpot/Salesforce/GHL deals, associates contacts, routes pipeline stage, and logs attribution.'),
            ('Waterfall Enrichment', 'Runs low-cost enrichment first, falls back to paid providers only when needed.'),
            ('Omni-channel Orchestration', 'Email → LinkedIn → SMS → call tasks with retry logic, rate limits, and failure alerts.'),
            ('Ops Dashboard', 'ClickUp/custom dashboard for reply rates, deal value, industries, campaign attribution, and stuck workflows.'),
            ('Railway Utilities', 'Small custom tools for CSV splitting, lead matching, landing-page generation, and webhook glue code.'),
        ],
        'events': [
            ('00:01', 'New positive email reply detected from campaign inbox'),
            ('00:07', 'Lead enriched with company, role, LinkedIn, ICP score'),
            ('00:19', 'HubSpot deal created and routed to correct pipeline'),
            ('00:34', 'Slack alert sent with context, next action, and source attribution'),
            ('00:52', 'Follow-up sequence paused and rep task created'),
        ],
        'stack': ['n8n', 'HubSpot / Salesforce / GHL', 'Slack', 'ClickUp', 'Instantly', 'Email Bison', 'HeyReach', 'Railway', 'APIs/Webhooks'],
        'cta': 'Designed to make RevOps automations reliable enough for real client delivery — not just pretty workflows.',
    },
    {
        'slug': 'med-spa-voice-agent-booking',
        'title': 'Med Spa AI Voice Booking Agent',
        'subtitle': '24/7 inbound call handling, FAQ answers, appointment booking, and human handoff',
        'client': 'Med Spa Voice Agent',
        'budget': '$500 fixed offer',
        'accent': '#ec4899',
        'accent2': '#f59e0b',
        'price_note': 'Client mentioned $750 budget; proposal positions a clean first version at $500 fixed.',
        'hero': 'A front-desk replacement workflow that answers inbound calls naturally, handles med-spa FAQs, books appointments into calendar, and logs every call summary for the team.',
        'metrics': [('Coverage', '24/7'), ('Missed calls', 'Reduced'), ('Booking flow', 'Calendar'), ('Fallback', 'Human handoff')],
        'modules': [
            ('Natural Voice Intake', 'Greets callers, understands requested service, asks the right qualification questions, and avoids robotic scripts.'),
            ('FAQ + Policy Answers', 'Handles pricing ranges, service descriptions, location, hours, prep notes, and common med-spa questions.'),
            ('Calendar Booking', 'Checks availability and books directly into Google Calendar or Calendly with confirmation details.'),
            ('Human Transfer / Message', 'Transfers urgent or complex calls to staff, or captures a clean message when no one is available.'),
            ('Call Summary Log', 'Stores caller, service interest, intent, booked slot, transcript summary, and follow-up status in Sheets/CRM.'),
            ('Testing + Guardrails', 'Includes realistic call tests, escalation rules, banned medical claims, and confidence thresholds.'),
        ],
        'events': [
            ('Call starts', 'Caller asks about Botox pricing and Saturday availability'),
            ('Intent captured', 'AI identifies service interest, preferred time, new/returning client status'),
            ('FAQ answered', 'Provides safe pricing range and recommends consultation for exact quote'),
            ('Booked', 'Calendly slot reserved and confirmation sent'),
            ('Logged', 'Call summary + appointment details saved to CRM/Google Sheet'),
        ],
        'stack': ['Vapi / Twilio Voice', 'ElevenLabs', 'Google Calendar / Calendly', 'Google Sheets / CRM', 'Zapier / Make / n8n', 'SMS/Email confirmations'],
        'cta': 'Built for med-spa customer experience: helpful, calm, realistic, and safe — not a gimmicky voice bot.',
    },
]

css = r'''
:root{--bg:#070811;--panel:#0f1324;--muted:#9ca3af;--text:#f8fafc;--line:rgba(255,255,255,.12);--accent:#7c3aed;--accent2:#06b6d4;}
*{box-sizing:border-box} body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:radial-gradient(circle at 20% 0%, color-mix(in srgb,var(--accent) 28%,transparent), transparent 30%),radial-gradient(circle at 90% 15%, color-mix(in srgb,var(--accent2) 24%,transparent), transparent 32%),var(--bg);color:var(--text);}
.wrap{max-width:1180px;margin:0 auto;padding:34px 22px 70px}.nav{display:flex;justify-content:space-between;align-items:center;margin-bottom:54px}.brand{display:flex;gap:12px;align-items:center;font-weight:800}.logo{width:38px;height:38px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));box-shadow:0 0 42px color-mix(in srgb,var(--accent) 45%,transparent)}.pill{border:1px solid var(--line);background:rgba(255,255,255,.06);border-radius:999px;padding:9px 13px;color:#dbeafe;font-size:13px}.hero{display:grid;grid-template-columns:1.02fr .98fr;gap:28px;align-items:center}.eyebrow{color:var(--accent2);font-weight:800;letter-spacing:.12em;text-transform:uppercase;font-size:12px}.hero h1{font-size:58px;line-height:.95;margin:16px 0 18px;letter-spacing:-.055em}.hero p{font-size:18px;line-height:1.65;color:#cbd5e1;max-width:720px}.disclaimer{margin:18px 0 0;display:inline-block;border:1px solid rgba(255,255,255,.15);background:rgba(255,255,255,.065);border-radius:14px;padding:10px 12px;color:#cbd5e1;font-size:13px}.actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}.btn{padding:13px 17px;border-radius:14px;border:1px solid var(--line);background:linear-gradient(135deg,var(--accent),var(--accent2));color:white;text-decoration:none;font-weight:800}.btn.secondary{background:rgba(255,255,255,.06)}.panel{border:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.035));border-radius:28px;box-shadow:0 22px 70px rgba(0,0,0,.35);overflow:hidden}.panel-head{padding:16px 18px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;color:#cbd5e1;font-size:13px}.screen{padding:20px}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.metric{background:rgba(0,0,0,.24);border:1px solid var(--line);border-radius:18px;padding:15px}.metric b{font-size:25px;display:block}.metric span{color:var(--muted);font-size:12px}.flow{margin-top:14px;display:grid;gap:10px}.event{display:grid;grid-template-columns:72px 1fr;gap:12px;align-items:center;background:rgba(255,255,255,.055);border:1px solid var(--line);border-radius:16px;padding:12px}.time{color:var(--accent2);font-weight:800;font-size:13px}.section{margin-top:34px}.section h2{font-size:30px;letter-spacing:-.03em;margin:0 0 18px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.card{border:1px solid var(--line);background:rgba(255,255,255,.055);border-radius:22px;padding:19px;min-height:170px}.card h3{margin:0 0 8px;font-size:17px}.card p{margin:0;color:#cbd5e1;line-height:1.55}.stack{display:flex;gap:10px;flex-wrap:wrap}.chip{border:1px solid color-mix(in srgb,var(--accent) 48%,white 8%);background:color-mix(in srgb,var(--accent) 18%,transparent);border-radius:999px;padding:9px 12px;color:#e5e7eb;font-weight:700;font-size:13px}.offer{display:grid;grid-template-columns:1fr 1fr;gap:16px}.big{padding:26px;border-radius:24px;border:1px solid var(--line);background:linear-gradient(135deg,color-mix(in srgb,var(--accent) 24%,transparent),rgba(255,255,255,.045))}.big b{font-size:36px;display:block;margin-bottom:6px}.footer{margin-top:42px;color:#94a3b8;text-align:center}.pulse{width:10px;height:10px;border-radius:50%;background:#22c55e;display:inline-block;margin-right:8px;box-shadow:0 0 0 8px rgba(34,197,94,.13)}
@media(max-width:900px){.hero,.offer{grid-template-columns:1fr}.hero h1{font-size:42px}.grid,.metrics{grid-template-columns:1fr 1fr}.nav{align-items:flex-start;gap:14px;flex-direction:column}}
@media(max-width:560px){.grid,.metrics{grid-template-columns:1fr}.wrap{padding:22px 14px 48px}.hero h1{font-size:36px}.event{grid-template-columns:1fr}.actions{flex-direction:column}.btn{text-align:center}}
'''

def render(job):
    style = css.replace('--accent:#7c3aed;', f"--accent:{job['accent']};").replace('--accent2:#06b6d4;', f"--accent2:{job['accent2']};")
    metrics = ''.join(f"<div class='metric'><b>{html.escape(v)}</b><span>{html.escape(k)}</span></div>" for k,v in job['metrics'])
    modules = ''.join(f"<article class='card'><h3>{html.escape(t)}</h3><p>{html.escape(d)}</p></article>" for t,d in job['modules'])
    events = ''.join(f"<div class='event'><div class='time'>{html.escape(t)}</div><div>{html.escape(d)}</div></div>" for t,d in job['events'])
    stack = ''.join(f"<span class='chip'>{html.escape(s)}</span>" for s in job['stack'])
    return f"""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(job['title'])}</title><style>{style}</style></head><body><main class='wrap'><nav class='nav'><div class='brand'><div class='logo'></div><div>Janis Agic<br><span style='color:#94a3b8;font-weight:600'>Automation demo</span></div></div><div class='pill'><span class='pulse'></span>{html.escape(job['budget'])}</div></nav><section class='hero'><div><div class='eyebrow'>{html.escape(job['client'])}</div><h1>{html.escape(job['title'])}</h1><p>{html.escape(job['hero'])}</p><div class='disclaimer'>Disclaimer: All displayed data, names, messages, and metrics are fictional and shown for visual demonstration purposes only.</div><div class='actions'><a class='btn' href='#workflow'>View workflow</a><a class='btn secondary' href='#stack'>Implementation stack</a></div></div><div class='panel'><div class='panel-head'><span>Live operations preview</span><span>Production concept</span></div><div class='screen'><div class='metrics'>{metrics}</div><div class='flow'>{events}</div></div></div></section><section class='section' id='workflow'><h2>What this first version would include</h2><div class='grid'>{modules}</div></section><section class='section offer'><div class='big'><b>{html.escape(job['budget'])}</b><p>{html.escape(job['price_note'])}</p></div><div class='big'><b>Clean handoff</b><p>Documented setup, account ownership on the client side, testing checklist, and a practical first version that can be improved after real usage.</p></div></section><section class='section' id='stack'><h2>Suggested stack</h2><div class='stack'>{stack}</div></section><section class='section big'><h2>Outcome</h2><p>{html.escape(job['cta'])}</p></section><div class='footer'>Prepared as a tailored Upwork proof-of-fit demo by Janis Agic.</div></main></body></html>"""

PUBLISH.mkdir(exist_ok=True)
for job in jobs:
    d = PUBLISH / job['slug']
    d.mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(render(job), encoding='utf-8')
print('generated', ', '.join(j['slug'] for j in jobs))
