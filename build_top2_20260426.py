from pathlib import Path
from textwrap import dedent

ROOT = Path('/Users/nani/workspace/upwork-job-demos/publish')
ROOT.mkdir(parents=True, exist_ok=True)

def write(slug, title, subtitle, accent, sections, metrics, events, cta):
    metric_html = ''.join(f'<div class="metric"><b>{v}</b><span>{k}</span></div>' for k,v in metrics)
    section_html = ''.join(f'<section class="card"><h2>{h}</h2><p>{p}</p>{body}</section>' for h,p,body in sections)
    event_html = ''.join(f'<li><span>{t}</span>{d}</li>' for t,d in events)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<style>
:root{{--accent:{accent};--bg:#070b14;--panel:#0f1726;--panel2:#121d31;--text:#eef5ff;--muted:#9fb0c8;--line:rgba(255,255,255,.11)}}
*{{box-sizing:border-box}} body{{margin:0;background:radial-gradient(circle at 20% 0%, color-mix(in srgb,var(--accent) 24%, transparent), transparent 34%),linear-gradient(135deg,#070b14,#0b1020 44%,#05070c);font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Arial;color:var(--text)}}
.wrap{{max-width:1180px;margin:0 auto;padding:34px 18px 60px}} .hero{{display:grid;grid-template-columns:1.02fr .98fr;gap:22px;align-items:stretch}}
.badge{{display:inline-flex;gap:8px;align-items:center;border:1px solid var(--line);background:rgba(255,255,255,.06);padding:8px 12px;border-radius:999px;color:#dce8ff;font-size:13px}}
h1{{font-size:clamp(34px,5vw,64px);line-height:.95;margin:22px 0 14px;letter-spacing:-.05em}} .lead{{font-size:18px;line-height:1.55;color:var(--muted);max-width:680px}}
.disclaimer{{margin:18px 0 20px;padding:12px 14px;border:1px solid rgba(255,255,255,.13);border-radius:14px;background:rgba(255,255,255,.055);color:#c8d6ee;font-size:13px}}
.actions{{display:flex;gap:12px;flex-wrap:wrap;margin-top:20px}} .btn{{border:0;border-radius:14px;padding:13px 17px;background:var(--accent);color:#06101f;font-weight:800;text-decoration:none;box-shadow:0 18px 50px color-mix(in srgb,var(--accent) 30%, transparent)}} .btn.secondary{{background:rgba(255,255,255,.08);color:var(--text);border:1px solid var(--line);box-shadow:none}}
.panel{{background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.035));border:1px solid var(--line);border-radius:28px;padding:18px;box-shadow:0 30px 90px rgba(0,0,0,.35)}}
.metrics{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:16px}} .metric{{background:rgba(255,255,255,.06);border:1px solid var(--line);padding:18px;border-radius:20px}} .metric b{{display:block;font-size:28px}} .metric span{{color:var(--muted);font-size:13px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px}} .card{{background:rgba(255,255,255,.055);border:1px solid var(--line);border-radius:24px;padding:20px;min-height:185px}} h2{{margin:0 0 8px;font-size:20px}} .card p{{color:var(--muted);line-height:1.48;margin:0 0 14px}} .pill{{display:inline-block;margin:4px 5px 0 0;padding:7px 10px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid var(--line);font-size:12px;color:#d6e4ff}}
.timeline{{list-style:none;padding:0;margin:14px 0 0}} .timeline li{{display:flex;gap:12px;padding:13px 0;border-bottom:1px solid var(--line);color:#d4e0f2}} .timeline li span{{min-width:90px;color:var(--accent);font-weight:800}}
.mock{{display:grid;gap:12px}} .row{{display:flex;justify-content:space-between;gap:10px;background:rgba(255,255,255,.06);border:1px solid var(--line);padding:13px;border-radius:15px;color:#dce8ff}} .row small{{color:var(--muted)}}
@media(max-width:850px){{.hero,.grid{{grid-template-columns:1fr}}h1{{font-size:42px}}.metrics{{grid-template-columns:1fr 1fr}}}}
</style>
</head>
<body><main class="wrap">
<div class="hero"><div class="panel"><span class="badge">⚡ Client-specific demo · built for this Upwork project</span><h1>{title}</h1><p class="lead">{subtitle}</p><div class="disclaimer">Disclaimer: All displayed data, names, messages, and metrics are fictional and shown for visual demonstration purposes only.</div><div class="actions"><a class="btn" href="#workflow">View workflow</a><a class="btn secondary" href="#handoff">Implementation plan</a></div><div class="metrics">{metric_html}</div></div>
<div class="panel"><h2>Live operations preview</h2><div class="mock">{cta}</div><ul class="timeline">{event_html}</ul></div></div>
<div class="grid" id="workflow">{section_html}</div>
<section class="card" id="handoff" style="margin-top:16px"><h2>Lean delivery plan</h2><p>Start with a working MVP, test the core data flow end-to-end, then polish UI, edge cases, and handover documentation. Clear communication, short feedback loops, and a walkthrough video included.</p><span class="pill">MVP-first</span><span class="pill">Tested automations</span><span class="pill">Clean handover</span><span class="pill">Fast iteration</span></section>
</main></body></html>'''
    out = ROOT / slug / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')

write(
 'competition-automation-leaderboard',
 'Competition Landing Page + Automation System',
 'A production-style landing page concept with real-time leaderboard data, Airtable-managed missions, Supabase voting, Make.com triggers, and Brevo email follow-up — designed for a 5–7 day implementation sprint.',
 '#6ee7ff',
 [
  ('Live leaderboard', 'Search, filter, rank badges, participant cards, and real-time score updates from Supabase.', '<span class="pill">Supabase realtime</span><span class="pill">Search/filter</span><span class="pill">Top 3 styling</span>'),
  ('Voting + email capture', 'Vote modal requires email, creates/logs account state, prevents duplicate vote issues, and triggers confirmation flow.', '<span class="pill">Vote logging</span><span class="pill">Email capture</span><span class="pill">Validation</span>'),
  ('Airtable mission CMS', 'Operators add mission rows in Airtable and the landing page updates without code changes.', '<span class="pill">Airtable CMS</span><span class="pill">Make.com sync</span><span class="pill">Brevo trigger</span>'),
 ],
 [('5–7d','Target sprint'),('4','Core systems'),('Live','Leaderboard'),('0-code','Mission updates')],
 [('Airtable','New mission published'),('Make.com','Syncs mission + triggers Brevo'),('Supabase','Stores votes and leaderboard'),('Page','Updates leaderboard instantly')],
 '<div class="row"><b>Mission 01 · Catalyst Users</b><small>+240 pts</small></div><div class="row"><b>Vote captured</b><small>Brevo email queued</small></div><div class="row"><b>Leaderboard</b><small>Realtime refresh</small></div>'
)

write(
 'healthcare-airtable-zapier-os',
 'Healthcare Coordination Airtable + Zapier OS',
 'A clean operational system for patients, appointments, rides, clinics, invoices, reminders, no-shows, and QuickBooks handoff — built so a non-technical healthcare team can run it daily.',
 '#8bffb0',
 [
  ('Airtable base structure', 'Patients, appointments, clinics, rides, invoices, and status tracking with simple views for coordinators.', '<span class="pill">Patients</span><span class="pill">Appointments</span><span class="pill">Invoices</span>'),
  ('Zapier automation layer', 'Acuity creates appointment records, Spruce sends reminders, no-shows trigger follow-ups, invoice-ready items prepare QuickBooks.', '<span class="pill">Acuity</span><span class="pill">Spruce</span><span class="pill">QuickBooks-ready</span>'),
  ('Team handover', 'Tested end-to-end flows, a simple operating SOP, and a short walkthrough video for the team.', '<span class="pill">1–2 weeks</span><span class="pill">Test checklist</span><span class="pill">Walkthrough</span>'),
 ],
 [('1','Central base'),('6','Core tables'),('12+','Automation checks'),('Simple','Team handover')],
 [('Acuity','New appointment created'),('Airtable','Patient + ride linked'),('Spruce','Reminder/no-show message sent'),('QuickBooks','Invoice queue prepared')],
 '<div class="row"><b>Patient: Maria L.</b><small>Ride scheduled</small></div><div class="row"><b>Clinic appointment</b><small>Acuity synced</small></div><div class="row"><b>No-show workflow</b><small>Follow-up ready</small></div>'
)
print('generated')
