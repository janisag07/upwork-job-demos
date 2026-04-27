from pathlib import Path

slug = 'n8n-ai-rag-report-agent'
out = Path('/Users/nani/workspace/upwork-job-demos/publish') / slug
out.mkdir(parents=True, exist_ok=True)
html = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>n8n AI RAG Report Agent — Workflow Blueprint</title>
  <style>
    :root{--bg:#07111f;--panel:#0d1b2f;--panel2:#13243d;--text:#eef6ff;--muted:#96abc6;--green:#38d997;--blue:#61a5ff;--amber:#f8bf39;--red:#fb7185;--line:rgba(255,255,255,.11)}
    *{box-sizing:border-box}body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial;background:radial-gradient(circle at 10% 0%,#163b61 0,#07111f 38%,#040811 100%);color:var(--text)}
    .wrap{max-width:1180px;margin:0 auto;padding:34px 18px 56px}.hero{display:grid;grid-template-columns:1.08fr .92fr;gap:20px;align-items:stretch}.card{background:linear-gradient(180deg,rgba(19,36,61,.94),rgba(8,17,31,.96));border:1px solid var(--line);border-radius:24px;box-shadow:0 24px 80px rgba(0,0,0,.28)}
    .main{padding:34px}.eyebrow{color:var(--green);font-weight:850;letter-spacing:.12em;text-transform:uppercase;font-size:12px}h1{font-size:43px;line-height:1.02;margin:14px 0 14px}p{color:var(--muted);line-height:1.62}.actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:20px}.pill{padding:11px 14px;border-radius:999px;background:rgba(97,165,255,.12);border:1px solid rgba(97,165,255,.25);font-weight:800;color:#dbeafe}.pill.green{background:rgba(56,217,151,.13);border-color:rgba(56,217,151,.24);color:#c7f9df}.side{padding:22px;display:grid;gap:13px}.metric{padding:17px;border-radius:18px;background:rgba(255,255,255,.045);border:1px solid var(--line)}.metric b{display:block;font-size:27px}.metric span{font-size:13px;color:var(--muted)}
    .section{margin-top:24px;padding:24px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin-top:20px}.box{padding:20px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}.box strong{display:block;margin-bottom:7px}.mini{font-size:13px;color:var(--muted)}.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.step{position:relative;padding:17px;border-radius:18px;background:rgba(255,255,255,.04);border:1px solid var(--line)}.num{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,var(--green),var(--blue));font-weight:900;margin-bottom:10px}.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}.code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;background:#050b14;border:1px solid var(--line);border-radius:16px;padding:16px;color:#bdfbd8;overflow:auto;font-size:13px;line-height:1.55}.row{display:grid;grid-template-columns:24px 1fr auto;gap:12px;align-items:center;padding:13px;border-radius:15px;background:rgba(255,255,255,.04);border:1px solid var(--line);margin:10px 0}.dot{width:13px;height:13px;border-radius:50%;background:var(--green);box-shadow:0 0 0 5px rgba(56,217,151,.12)}.dot.warn{background:var(--amber);box-shadow:0 0 0 5px rgba(248,191,57,.12)}.tag{font-size:12px;font-weight:850;padding:7px 10px;border-radius:999px;background:rgba(255,255,255,.06);border:1px solid var(--line);white-space:nowrap}.footer{text-align:center;margin-top:23px;font-size:13px;color:var(--muted)}@media(max-width:900px){.hero,.grid,.flow,.two{grid-template-columns:1fr}h1{font-size:32px}.wrap{padding:18px 12px 34px}.main{padding:24px}.row{grid-template-columns:22px 1fr}.tag{grid-column:2}}
  </style>
</head>
<body>
  <main class="wrap">
    <section class="hero">
      <div class="main card">
        <div class="eyebrow">n8n + AI Agent + RAG + Reports</div>
        <h1>Industrial Engineering AI Agent workflow blueprint.</h1>
        <p>A focused n8n architecture for turning ISO PDFs, ergonomics handbooks and technical manuals into a searchable RAG assistant that generates structured reports, Google Sheets summaries and dashboard-ready data.</p>
        <div class="actions"><div class="pill green">Workflow architecture</div><div class="pill">RAG + vector DB</div><div class="pill">PDF reports + Sheets</div></div>
      </div>
      <div class="side card">
        <div class="metric"><b>5 modules</b><span>ingestion, retrieval, chat, report generation, dashboard output</span></div>
        <div class="metric"><b>n8n-first</b><span>designed around nodes, webhooks, credentials and testable steps</span></div>
        <div class="metric"><b>MVP-safe</b><span>clear first version, then improve retrieval quality and formatting</span></div>
      </div>
    </section>

    <section class="grid">
      <div class="box"><strong>Document ingestion</strong><div class="mini">Upload PDFs, split content into chunks, attach metadata like standard, chapter, page and topic.</div></div>
      <div class="box"><strong>RAG retrieval</strong><div class="mini">Store embeddings in Supabase/Pinecone and retrieve top matching passages before each answer.</div></div>
      <div class="box"><strong>Report output</strong><div class="mini">Generate technical summaries, PDF reports and Google Sheets rows for dashboards.</div></div>
    </section>

    <section class="card section">
      <h2>Proposed n8n workflow</h2>
      <div class="flow">
        <div class="step"><div class="num">1</div><strong>PDF intake</strong><div class="mini">Drive/Form/Webhook trigger receives manuals and ISO docs.</div></div>
        <div class="step"><div class="num">2</div><strong>Chunk + embed</strong><div class="mini">Extract text, split, create embeddings, save metadata.</div></div>
        <div class="step"><div class="num">3</div><strong>Chat query</strong><div class="mini">n8n Chat/Webhook captures question and project context.</div></div>
        <div class="step"><div class="num">4</div><strong>RAG answer</strong><div class="mini">Retrieve sources, call LLM, cite evidence and assumptions.</div></div>
        <div class="step"><div class="num">5</div><strong>Report + dashboard</strong><div class="mini">Create PDF, append Sheets rows, sync Looker Studio source.</div></div>
      </div>
    </section>

    <section class="two">
      <div class="card section">
        <h2>n8n node map</h2>
        <div class="code">Webhook / Chat Trigger
→ Google Drive: download PDF
→ PDF Extract / Code node: clean text
→ Split in Batches: chunk pages
→ OpenAI Embeddings
→ Supabase/Pinecone: upsert vectors
→ User query webhook
→ Vector search top_k=5
→ LLM: answer + report outline
→ HTML/PDF generation
→ Google Sheets append
→ Looker Studio data source</div>
      </div>
      <div class="card section">
        <h2>Delivery checklist</h2>
        <div class="row"><div class="dot"></div><div><strong>Working n8n workflow</strong><div class="mini">Credentials, nodes, triggers and test cases documented.</div></div><div class="tag">Core</div></div>
        <div class="row"><div class="dot"></div><div><strong>Vector database setup</strong><div class="mini">Supabase or Pinecone schema with source metadata.</div></div><div class="tag">RAG</div></div>
        <div class="row"><div class="dot warn"></div><div><strong>PDF report formatting</strong><div class="mini">Can start simple, then improve layout after output sample approval.</div></div><div class="tag">Iterate</div></div>
        <div class="row"><div class="dot"></div><div><strong>Google Sheets + dashboard data</strong><div class="mini">Structured rows for Looker Studio or similar visualization.</div></div><div class="tag">Output</div></div>
      </div>
    </section>

    <section class="card section">
      <h2>Why this fits a lean first milestone</h2>
      <p>The fastest safe version is not a giant custom app first. It is an n8n workflow that proves: documents can be ingested, the agent can retrieve grounded passages, and reports/summaries can be generated consistently. After that, the chat UI and report design can be polished.</p>
    </section>

    <div class="footer">Prepared as a proof-of-understanding for an n8n AI Agent / RAG document-reporting project.</div>
  </main>
</body>
</html>'''
(out/'index.html').write_text(html, encoding='utf-8')
print(out/'index.html')
