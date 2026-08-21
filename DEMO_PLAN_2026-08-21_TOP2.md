# Demo Plan — Upwork Top 2 — 2026-08-21

Status: approved by Janis for demo-backed applications. Submission remains blocked until the dedicated Upwork profile is manually authenticated and all live Apply gates pass.

## Non-negotiable quality rules

- Build two separate client-facing static demo sites, one direct URL per job.
- English UI/copy because both job posts are English.
- Premium, calm, operational design; no generic AI gradients, fake testimonials, client logos, or invented results.
- Each hero must explain the exact client workflow and business outcome in five seconds.
- Include a visible, non-sticky note: `Proof of approach using fictional sample data. No client systems or data are connected.`
- Include exact tools/workflow terms from the job.
- Every visible control must work and visibly change output/state.
- Show error handling, duplicate protection, human review, acceptance criteria, and handoff—not only a decorative dashboard.
- Responsive at 390px and desktop widths; no horizontal overflow.
- Single `index.html` with inline CSS/JS per demo; no build step and no external dependencies.
- Do not touch unrelated files in this dirty repository.

---

## Job 1 — Full-Stack Developer Needed to Build Custom Email Automation & Drip Campaign Tool

- Job ID: `022090832683073754745`
- Public URL: https://www.upwork.com/jobs/~022090832683073754745
- Budget: $1,500–$3,000 fixed, three milestones
- Expected timeline: 3–4 weeks
- Required proposal opening: `GALAXY`
- Core stack requested: Python/FastAPI or Django, or Node.js; PostgreSQL/SQLite; Redis/Celery or BullMQ; React/Vue/server-rendered UI; Docker Compose; SendGrid/AWS SES/Mailgun.
- Core workflow: subscriber/sign-up → contact/tags/custom fields → drip sequence and delayed jobs → SMTP provider → delivery/bounce/unsubscribe webhooks → contact status/logging → operator dashboard.

### Demo slug

`publish/email-drip-delivery-control-center/index.html`

### Demo concept

**Self-Hosted Email Delivery Control Center** — a credible operator view showing how campaign orchestration, durable scheduling, provider webhooks, contact state, and deployment/handoff fit together.

### Required modules

1. **Sequence designer** — Email A immediately → wait 3 days → Email B → conditional branch.
2. **Durable queue monitor** — scheduled/running/retry/dead-letter states; provider selector for SES, SendGrid, and Mailgun.
3. **Contact state** — active/unsubscribed/bounced with tags and custom fields.
4. **Webhook event stream** — delivered, bounced, complained, unsubscribed; idempotency/event-ID protection.
5. **Architecture + three milestones** — FastAPI → PostgreSQL → Redis/Celery → provider API/webhooks → Docker Compose; Milestone 1 architecture/data model, Milestone 2 sending engine/webhooks, Milestone 3 UI/deployment/tests/handoff.

### Required interactions

- `Simulate signup` adds a contact and queue event, updates counters, and advances the visible sequence.
- Provider switch changes provider label and operational metrics/state.
- `Simulate bounce` updates the selected contact to bounced and suppresses future sends.
- `Simulate unsubscribe` updates status and event log.
- Queue/state filters visibly change rows.

### Positioning

The proof is not a fake completed client product. It proves that Janis understands the hard parts: durable delayed jobs, idempotent provider events, suppression state, retries/dead-letter handling, deployment, tests, and handoff.

---

## Job 2 — Pipedrive CRM Implementation Specialist

- Job ID: `022090412037741657910`
- Public URL: https://www.upwork.com/jobs/~022090412037741657910
- Budget: $2,000 fixed
- Client context: commercial construction company, approximately 6–7 employees, likely three initial Pipedrive users, coordinated/white-labeled through Accredited AI.
- Existing system: multi-tab spreadsheet for relationships, project opportunities, submitted bids, backlog, and active projects.
- Goal: migrate relationship/opportunity management without disrupting processes that should stay in the spreadsheet temporarily.

### Demo slug

`publish/pipedrive-construction-relationship-ops/index.html`

### Demo concept

**Construction Relationship & Opportunity Control Center** — a two-pipeline Pipedrive implementation map with migration QA, next-action accountability, and explicit spreadsheet coexistence.

### Exact workflow to mirror

**Pipeline 1 — Relationship Development**
- Target identified
- Research completed
- Introduction requested
- Initial contact
- Meeting scheduled
- Relationship nurturing
- Added to bidder list
- Qualified opportunity created

**Pipeline 2 — Project Opportunities**
- Opportunity identified
- Budget or preconstruction
- Bid/no-bid review
- Estimating
- Proposal submitted
- Client decision pending
- Funding or design pending
- Awarded / Lost / Deferred

### Required modules

1. **Two connected pipeline views** with real construction relationship/opportunity labels.
2. **Migration QA** — source rows, mapped fields, duplicate organizations, missing owners/next actions, accepted/rejected test rows.
3. **Relationship accountability** — owner, strength, last meaningful contact, next required action, overdue risk.
4. **Opportunity reporting** — project value, expected bid/decision dates, funding/permitting status, source and pipeline value.
5. **Spreadsheet coexistence + handoff** — show backlog/active-project tabs intentionally remaining in Sheets until acceptance criteria support migration; Microsoft/email/security discovery notes; training/documentation path.

### Required interactions

- Toggle between Relationship and Project Opportunity pipelines.
- Filter cards by owner/risk/status.
- Select a card to update a detail panel and next action.
- `Run migration check` visibly changes QA counters and shows dedupe/missing-field issues.
- `Move to next stage` advances the selected item and logs the change.

### Positioning

The demo should make the safe first milestone obvious: discovery + field map + 25-row migration test + acceptance criteria, before committing the entire spreadsheet and client operation to a broad fixed-price implementation.
