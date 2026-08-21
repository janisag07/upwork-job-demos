# Upwork Proposal Pack — Jobs 1 and 2 — 2026-08-21

Status: prepared; demos built, independently reviewed, published and live-verified (GitHub Pages `built`, both URLs HTTP 200). Submission remains blocked until Janis manually logs into the dedicated Upwork Chrome profile so live gates, Connects and additional questions can be verified.

## Job 1 — Full-Stack Developer Needed to Build Custom Email Automation & Drip Campaign Tool

- Job ID: `022090832683073754745`
- URL: https://www.upwork.com/jobs/~022090832683073754745
- Bid: **$3,000 fixed**
- Duration: **Less than 1 month**
- Boost: **0 Connects**
- Demo URL: `https://janisag07.github.io/upwork-job-demos/publish/email-drip-delivery-control-center/index.html?v=863c6a8`
- Related proof: `https://janisag07.github.io/upwork-job-demos/publish/mailchimp-make-daily-email-automation/index.html`

### Cover letter

GALAXY

Hi,

I would build this as a small self-hosted product, not as a chain of fragile cron jobs. I made a job-specific proof of approach here:

https://janisag07.github.io/upwork-job-demos/publish/email-drip-delivery-control-center/index.html?v=863c6a8

It maps signup, contact state, delayed sequence steps, provider delivery, bounce and unsubscribe webhooks, retry handling, suppression and operator review. The controls use fictional sample data, but the state model mirrors the system I would implement.

My recommended stack is FastAPI, PostgreSQL, Redis/Celery and React, packaged with Docker Compose. PostgreSQL owns contact, campaign and send state. Redis/Celery handles durable delayed work and retries. A provider adapter keeps SES, SendGrid or Mailgun details out of the campaign logic.

For delayed sends, each sequence step creates a scheduled job with an idempotency key. A worker claims due jobs, records the attempt and sends through the provider adapter. Provider webhooks reconcile the final outcome. Transient errors retry with backoff; exhausted jobs move to a dead-letter review queue. Unsubscribed, bounced or complained contacts are suppressed before any provider call.

I would split the $3,000 build into:
- $700: architecture, data model, queue and webhook contracts, sandbox acceptance tests
- $1,300: contacts, campaigns, sequence engine, provider integration and webhook reconciliation
- $1,000: dashboard, Docker deployment, automated tests, README and handoff

A related email automation proof is here:
https://janisag07.github.io/upwork-job-demos/publish/mailchimp-make-daily-email-automation/index.html

Best,
Janis

### Prepared answers if the Apply page separates the questions

**Recommended stack and why**

FastAPI + PostgreSQL + Redis/Celery + React, deployed with Docker Compose. FastAPI gives typed API and webhook contracts, PostgreSQL keeps campaign and contact state transactional, Redis/Celery provides durable delayed execution and retry control, and the provider adapter keeps SES/SendGrid/Mailgun replaceable.

**How background and delayed jobs are handled**

Each sequence step creates a scheduled job with an idempotency key and intended send time. Workers claim due jobs, lock the send record, call the provider adapter and record the attempt. Provider webhooks reconcile delivered, bounced, complained or unsubscribed outcomes. Transient failures retry with backoff; exhausted jobs enter a dead-letter review queue. Suppression state is checked before every send.

**Similar links**

1. Job-specific email delivery control proof: https://janisag07.github.io/upwork-job-demos/publish/email-drip-delivery-control-center/index.html?v=863c6a8
2. Related email automation proof: https://janisag07.github.io/upwork-job-demos/publish/mailchimp-make-daily-email-automation/index.html

---

## Job 2 — Pipedrive CRM Implementation Specialist

- Job ID: `022090412037741657910`
- URL: https://www.upwork.com/jobs/~022090412037741657910
- Bid: **$2,000 fixed**
- Duration: **Less than 1 month**, subject to spreadsheet quality and account access
- Boost: **0 Connects**
- Demo URL: `https://janisag07.github.io/upwork-job-demos/publish/pipedrive-construction-relationship-ops/index.html?v=863c6a8`

### Cover letter

Hi,

I mapped your spreadsheet-to-Pipedrive rollout into a job-specific proof here:

https://janisag07.github.io/upwork-job-demos/publish/pipedrive-construction-relationship-ops/index.html?v=863c6a8

It uses the two workflows from your post: Relationship Development from target identification through bidder-list qualification, and Project Opportunities from early discovery through estimating, proposal, decision and award/loss/deferment. It also shows migration QA, duplicate organizations, missing owners, overdue next actions and the reporting fields a construction team needs.

I would not move every spreadsheet tab on day one. The safe first milestone is discovery, a field map, duplicate rules and a 25-row test migration with written acceptance criteria. Backlog and active-project reporting can stay in the spreadsheet until Pipedrive reporting and ownership are proven.

I would split the $2,000 project into:
- $500: discovery, field map, pipeline design and 25-row migration test
- $1,000: Pipedrive configuration, cleaned migration, ownership rules and follow-up automation
- $500: reporting, Microsoft/email checks, training, documentation and white-label handoff

I can coordinate inside Accredited AI's client-facing process and keep configuration decisions, exclusions and handoff notes clear.

Best,
Janis

### Prepared answer if asked for approach

I would begin with the spreadsheet structure and the team's actual relationship/opportunity decisions, then map only the fields and stages that drive action. A 25-row migration test would confirm organization dedupe, owners, dates, bidder-list state, project value and next actions before the remaining data moves. Backlog or active-project tabs stay in the spreadsheet until Pipedrive has equivalent reporting and the client accepts it.

## Internal final-submit checks

- Confirm both demo links still use the published demo commit `863c6a8`.
- Open each live URL and verify HTTP 200 plus correct title/content.
- Inspect every additional Apply-page question and answer it once, specifically.
- Stop if either form requires a prior-client/certification link Janis cannot truthfully provide.
- Stop if a 10k/location gate is material.
- Stop if Connects are insufficient. No purchase was authorized.
- Confirm bid, duration and zero boost before the single submit click.
- Verify each result in Submitted Proposals and Connects History before reporting success.
