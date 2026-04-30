#!/usr/bin/env python3
from pathlib import Path
from html import escape
import json, re, textwrap
BASE=Path('/Users/nani/workspace/upwork-job-demos')
PUB=BASE/'publish'
DATE='2026-04-30'
SHA='pending'

jobs=[
 dict(num=1, slug='ghl-roofing-lead-gen-command-center', title='GoHighLevel Roofing Lead Gen Command Center', budget='$200', stack='GoHighLevel · Roofing funnel · Domain · SMS/Email follow-up', color='#f97316',
      hero='A premium GHL-native roofing landing page concept built around booked inspections — not generic design.',
      metrics=[('48h','first version'),('3-step','lead capture flow'),('Mobile-first','roofing page'),('2–4/mo','repeat-page potential')],
      modules=['Roofing-specific hero with urgent estimate CTA','Trust blocks: reviews, badges, local service areas','GHL form + pipeline stage mapping','Thank-you route with SMS/email next steps','Domain/asset handoff checklist'],
      workflow=['Import client logo, colors and reference site','Build GHL page natively with mobile-first sections','Connect form, pipeline, notifications and calendar CTA','QA desktop/mobile + domain readiness checklist'],
      cta='Built to show the prospect: their existing brand, leveled up into a lead engine.'),
 dict(num=2, slug='ghl-home-services-automation-white-label', title='GoHighLevel Home Services Automation Builder', budget='$200', stack='GoHighLevel · Home Services · White-label workflows · Pipeline automation', color='#22c55e',
      hero='A reusable white-label automation layer for home-service leads: capture, qualify, remind, and move jobs through pipeline.',
      metrics=[('5 min','lead response target'),('4 stages','pipeline flow'),('2-way','SMS/email handoff'),('Reusable','white-label template')],
      modules=['Lead source routing from landing page/forms','Instant SMS + missed-call-style follow-up','Pipeline stages: New, Contacted, Booked, Won/Lost','Task creation for slow/no-response leads','White-label cloning checklist for new roofing clients'],
      workflow=['Map current GHL subaccount and pipeline','Build automations with clean naming and notes','Test lead scenarios: booked, no reply, wrong number','Deliver template that can be cloned for future clients'],
      cta='Positioned as a repeatable backend system, not a one-off automation.'),
 dict(num=3, slug='finance-quickbooks-automation-workbench', title='Finance + QuickBooks Automation Workbench', budget='$250', stack='Microsoft Forms · Power Automate · SharePoint · QuickBooks Online', color='#38bdf8',
      hero='A clean invoice-intake and accounting automation workflow for reducing manual entry and improving auditability.',
      metrics=[('4 fields','invoice intake core'),('Auto-save','SharePoint files'),('QBO-ready','approval/export path'),('Audit trail','every step logged')],
      modules=['Contractor invoice submission form','Attachment storage with standardized folder naming','Approval queue with entity/project classification','QuickBooks-ready data mapping','Exception list for missing info/duplicates'],
      workflow=['Define invoice fields and entity mapping','Create Microsoft Form + SharePoint library structure','Build Power Automate approval and file flow','Prepare QBO import/sync handoff and test cases'],
      cta='Shows the exact business value: less manual data entry, cleaner audit trail, scalable finance operations.'),
 dict(num=4, slug='hubspot-member-hub-content-library', title='HubSpot Member Hub & Gated Content Library', budget='$3,500', stack='HubSpot CMS · Memberships · Gated pages · Search/filter library', color='#f97316',
      hero='A premium HubSpot member hub concept for executive members: gated value, searchable content, and clear upgrade pressure.',
      metrics=[('4 pages','hub + landing build'),('Gated','member-only access'),('Search','content library UX'),('Executive','premium member experience')],
      modules=['Public membership landing pages with value framing','Gated member hub dashboard','Content library with filters/search by audience/topic','Featured reports/events/resource modules','Member analytics and admin handoff checklist'],
      workflow=['Align HubSpot theme, content model and membership rules','Build two public landing pages and two gated hub pages','Optimize resources library with search/filter UX','QA permissions, responsive states and editor handoff'],
      cta='Premium proof for Connex: members immediately see value, prospects see what they are missing.'),
 dict(num=6, slug='construction-job-posting-research-system', title='Construction Job Posting Research System', budget='$50', stack='Indeed/ZipRecruiter research · Google Sheets/Excel · Data QA', color='#f59e0b',
      hero='A fast research workflow that turns construction job posts into clean accounting-software lead lists.',
      metrics=[('8 columns','required fields'),('QA','duplicate checks'),('Source links','every row'),('Fast','review-play delivery')],
      modules=['Company/job-post collection board','Structured sheet schema matching requested fields','Category tagging: Accounting, Bookkeeping, PM, Estimating, Other','Duplicate and missing-website checks','Source-link handoff with date captured'],
      workflow=['Collect postings from Indeed and ZipRecruiter manually/safely','Normalize company, job title, category and location','Validate website/job link and posting date','Deliver clean spreadsheet + notes on sources used'],
      cta='Small-budget but strong-client proof: clean data, fast turnaround, no messy spreadsheet.'),
 dict(num=7, slug='alluvial-sankey-market-share-model', title='Alluvial / Sankey Market Share Model', budget='$50', stack='Data visualization · Sankey/Alluvial logic · Projection model', color='#a855f7',
      hero='A visual prototype for projecting market growth while showing new-player share capture without forcing wrong Sankey math.',
      metrics=[('Year 0–3','projection flow'),('6→11','market growth'),('Share capture','new player path'),('Exportable','chart-ready model')],
      modules=['Projection table separating market growth from share capture','Alluvial-style brand bands across years','New-player revenue path highlighted clearly','Notes explaining Sankey limitation and cleaner alternative','CSV-ready structure for final chart tool'],
      workflow=['Rebuild the data model so totals can grow by year','Separate node totals from share-transfer storytelling','Create a clear alluvial/Sankey-style visual','Deliver chart + data table + explanation for editable follow-up'],
      cta='Solves the actual issue: show increasing yearly revenue and share capture without misleading inflow/outflow constraints.'),
]

def html(j):
    color=j['color']
    metrics=''.join(f'<div class="metric"><b>{escape(a)}</b><span>{escape(b)}</span></div>' for a,b in j['metrics'])
    modules=''.join(f'<li>{escape(x)}</li>' for x in j['modules'])
    workflow=''.join(f'<div class="step"><span>{i:02d}</span><p>{escape(x)}</p></div>' for i,x in enumerate(j['workflow'],1))
    events=''.join(f'<div class="event"><b>{escape(x.split()[0])}</b><span>{escape(x)}</span></div>' for x in j['workflow'])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(j['title'])}</title><style>
:root{{--c:{color};--bg:#080b12;--panel:#111827;--muted:#9ca3af;--line:#263244}}*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Arial;background:radial-gradient(circle at top left,color-mix(in srgb,var(--c) 24%,transparent),transparent 34%),linear-gradient(180deg,#080b12,#0d111b 45%,#090b10);color:#f8fafc}}.wrap{{max-width:1160px;margin:0 auto;padding:42px 22px}}.badge{{display:inline-flex;gap:8px;align-items:center;border:1px solid color-mix(in srgb,var(--c) 45%,#334155);background:color-mix(in srgb,var(--c) 12%,#0f172a);padding:9px 13px;border-radius:999px;color:#e5e7eb;font-size:13px}}h1{{font-size:clamp(38px,6vw,76px);line-height:.94;margin:20px 0 18px;letter-spacing:-.06em}}.hero{{display:grid;grid-template-columns:1.1fr .9fr;gap:26px;align-items:stretch}}.lead{{font-size:20px;line-height:1.55;color:#d1d5db;max-width:730px}}.disclaimer{{margin:18px 0;padding:13px 15px;border-radius:16px;background:#0f172acc;border:1px solid #334155;color:#cbd5e1;font-size:13px}}.card{{background:linear-gradient(180deg,#121a2a,#0d1320);border:1px solid #263244;border-radius:28px;padding:24px;box-shadow:0 24px 80px #0008}}.metrics{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:26px 0}}.metric{{padding:18px;border-radius:22px;background:#0b1220;border:1px solid #253044}}.metric b{{display:block;font-size:25px;color:var(--c)}}.metric span{{color:var(--muted);font-size:13px}}h2{{font-size:28px;letter-spacing:-.03em;margin:0 0 16px}}ul{{margin:0;padding-left:20px;color:#dbeafe;line-height:1.95}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:20px}}.step{{display:flex;gap:14px;padding:14px 0;border-top:1px solid #263244}}.step span{{color:var(--c);font-weight:800}}.step p{{margin:0;color:#d1d5db}}.phone{{min-height:520px;border-radius:34px;background:#05070d;border:1px solid #344155;padding:18px;position:relative;overflow:hidden}}.screen{{height:100%;border-radius:24px;background:linear-gradient(180deg,#111827,#020617);padding:18px}}.event{{margin:12px 0;padding:14px;border-radius:18px;background:#0f172a;border:1px solid #263244}}.event b{{color:var(--c);display:block;margin-bottom:4px}}.event span{{color:#cbd5e1;font-size:13px}}.cta{{margin-top:24px;padding:20px;border-radius:22px;background:linear-gradient(90deg,color-mix(in srgb,var(--c) 30%,#111827),#111827);border:1px solid color-mix(in srgb,var(--c) 40%,#334155)}}.pill{{display:inline-block;margin:8px 8px 0 0;padding:10px 12px;border:1px solid #334155;border-radius:999px;color:#e5e7eb;background:#0b1220}}@media(max-width:820px){{.hero,.grid{{grid-template-columns:1fr}}.metrics{{grid-template-columns:1fr 1fr}}h1{{font-size:42px}}}}
</style></head><body><main class="wrap"><section class="hero"><div><div class="badge">Premium Upwork proof · {escape(j['budget'])} fixed · Job #{j['num']}</div><h1>{escape(j['title'])}</h1><p class="lead">{escape(j['hero'])}</p><div class="disclaimer">Disclaimer: All displayed data, names, messages, and metrics are fictional and shown for visual demonstration purposes only.</div><div>{''.join(f'<span class="pill">{escape(x)}</span>' for x in j['stack'].split(' · '))}</div></div><aside class="phone"><div class="screen"><h2>Live workflow preview</h2>{events}<div class="cta"><b>{escape(j['cta'])}</b></div></div></aside></section><section class="metrics">{metrics}</section><section class="grid"><div class="card"><h2>What I would build</h2><ul>{modules}</ul></div><div class="card"><h2>Execution plan</h2>{workflow}</div></section></main></body></html>'''

for j in jobs:
    d=PUB/j['slug']; d.mkdir(parents=True,exist_ok=True)
    (d/'index.html').write_text(html(j), encoding='utf-8')

plan=BASE/'DEMO_PLAN_2026-04-30_PREMIUM_BATCH.md'
plan.write_text('# Premium Upwork batch demos — 2026-04-30\n\n'+'\n'.join(f"- Job {j['num']}: {j['title']} — publish/{j['slug']}/ — {j['budget']}" for j in jobs)+'\n',encoding='utf-8')

letters=BASE/'premium_cover_letters_2026-04-30_jobs_1_2_3_4_6_7.md'
baseurl='https://janisag07.github.io/upwork-job-demos/publish'
with letters.open('w',encoding='utf-8') as f:
    f.write('# Premium cover letters — Jobs 1,2,3,4,6,7\n\n')
    for j in jobs:
        url=f"{baseurl}/{j['slug']}/index.html"
        f.write(f"## Job {j['num']} — {j['title']}\n\n")
        f.write(f"Hi,\n\nI can help with this. I put together a quick proof-of-approach here so you can see how I would structure it before we start:\n{url}\n\n")
        f.write(f"What matters most is making this useful quickly, not overcomplicating it. My approach would be:\n")
        for m in j['modules'][:4]: f.write(f"- {m}\n")
        f.write("\nI’m available to move fast, communicate clearly, and deliver a clean first version with simple handoff notes so you can actually use it right away.\n\nBest,\nJanis\n\n")
print('created', len(jobs), 'demos')
