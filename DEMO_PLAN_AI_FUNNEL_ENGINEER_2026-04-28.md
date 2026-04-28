# AI Funnel Engineer Demo Plan — 2026-04-28

## Job
AI Funnel Engineer — $1,000/month fixed/ongoing, 20 Connects

## Client stack / needs
- Instagram DM → call booking funnel
- LLM setters via ManyChat, n8n, GoHighLevel, PostgreSQL
- GHL SMS follow-up triggered by LLM events: booked, no-show, stalled lead
- iMessage vs GHL delivery/response comparison
- Meta CAPI events: ViewContent, Lead, Purchase
- Pixel/custom conversion debugging, event deduplication, attribution
- n8n workflow reliability, error handling, monitoring
- A/B testing messaging/timing/channel/qualification flow
- Claude Code → Git → Deploy, Docker/Hetzner VPS

## Demo concept
`ai-funnel-engineer-command-center`: client-facing interactive command center showing:
- End-to-end lead path from Meta/IG click → ManyChat → LLM qualification → n8n orchestration → GHL booking/SMS → Meta CAPI attribution
- Funnel health KPIs and drop-off monitoring
- Event router with LLM events triggering GHL SMS sequences
- Meta CAPI event validation/deduplication board
- A/B testing controls for channel/timing/copy that update metrics
- Incident monitor for broken automations

## Offer positioning
Not just building workflows — bulletproofing revenue attribution and follow-up reliability so every lead is tracked from ad click to signed client.
