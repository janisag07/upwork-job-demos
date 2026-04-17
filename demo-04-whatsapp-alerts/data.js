// ── Mock data for WhatsApp Business Monitor demo ──

const CONTACTS = [
  { id: 'c1', name: 'Maria Santos', phone: '+55 11 9876-5432', company: 'TechBrasil Ltda', avatar: 'MS' },
  { id: 'c2', name: 'Ahmed Khalil', phone: '+971 50 123 4567', company: 'Gulf Imports LLC', avatar: 'AK' },
  { id: 'c3', name: 'Sophie Martin', phone: '+33 6 12 34 56 78', company: 'EuroLogistics', avatar: 'SM' },
  { id: 'c4', name: 'James Chen', phone: '+1 415-555-0192', company: 'PacificTrade Inc', avatar: 'JC' },
  { id: 'c5', name: 'Priya Sharma', phone: '+91 98765 43210', company: 'Delhi Fresh Foods', avatar: 'PS' },
  { id: 'c6', name: 'Carlos Ruiz', phone: '+52 55 1234 5678', company: 'MexiSupply SA', avatar: 'CR' },
  { id: 'c7', name: 'Fatima Al-Hassan', phone: '+966 50 987 6543', company: 'Riyadh Retail Group', avatar: 'FA' },
  { id: 'c8', name: 'Liam O\'Brien', phone: '+353 87 123 4567', company: 'Celtic Commerce', avatar: 'LO' },
];

const AGENTS = ['Nadia K.', 'Tom W.', 'Ravi P.', 'Unassigned'];

const THREADS = [
  {
    id: 't1', contact: CONTACTS[0], priority: 'P1', status: 'new',
    subject: 'Bulk order shipment delayed 3 days',
    sla: { deadline: Date.now() + 25 * 60000, breached: false },
    assignee: AGENTS[0],
    messages: [
      { from: 'contact', time: '09:12', text: 'Hi, our order #4821 was supposed to arrive Monday. It\'s Wednesday and tracking still shows "processing". This is affecting our production line.' },
      { from: 'contact', time: '09:14', text: 'We have a factory deadline Friday. If this doesn\'t ship today we need to cancel and find another supplier.' },
      { from: 'agent', time: '09:18', text: 'Maria, I\'m escalating this to our logistics team right now. Let me get an updated ETA within the hour.' },
      { from: 'contact', time: '09:20', text: 'Please do. We\'ve been a loyal customer for 2 years. This is very disappointing.' },
    ],
    actions: [
      { text: 'Escalate to logistics for immediate shipment status', type: 'escalation', done: true },
      { text: 'Provide updated ETA to customer within 1 hour', type: 'follow-up', done: false },
      { text: 'Offer expedited shipping at no extra cost', type: 'resolution', done: false },
    ]
  },
  {
    id: 't2', contact: CONTACTS[1], priority: 'P2', status: 'in-progress',
    subject: 'Invoice discrepancy on last 3 orders',
    sla: { deadline: Date.now() + 180 * 60000, breached: false },
    assignee: AGENTS[1],
    messages: [
      { from: 'contact', time: '10:05', text: 'I noticed the invoices for orders #7890, #7891 and #7892 all have incorrect VAT rates. We\'re being charged 15% instead of the agreed 5% for free zone entities.' },
      { from: 'agent', time: '10:12', text: 'Thank you for flagging this, Ahmed. I\'ll pull up those invoices now and verify the VAT configuration on your account.' },
      { from: 'contact', time: '10:14', text: 'This needs to be corrected before our quarterly audit next week.' },
    ],
    actions: [
      { text: 'Review VAT configuration for Gulf Imports LLC account', type: 'investigation', done: true },
      { text: 'Issue corrected invoices for orders #7890-#7892', type: 'resolution', done: false },
      { text: 'Confirm free-zone VAT exemption documentation is on file', type: 'follow-up', done: false },
    ]
  },
  {
    id: 't3', contact: CONTACTS[2], priority: 'P1', status: 'in-progress',
    subject: 'API integration returning 500 errors',
    sla: { deadline: Date.now() - 15 * 60000, breached: true },
    assignee: AGENTS[2],
    messages: [
      { from: 'contact', time: '08:30', text: 'Our WhatsApp Business API integration started throwing 500 errors about 2 hours ago. None of our automated order confirmations are going out.' },
      { from: 'agent', time: '08:45', text: 'Sophie, we\'re seeing elevated error rates on our side as well. Engineering is investigating.' },
      { from: 'contact', time: '09:00', text: 'This is impacting all our customer communications. We process about 500 orders/hour and none of them are getting confirmations.' },
      { from: 'agent', time: '09:10', text: 'Understood the severity. I\'ve flagged this as critical internally. Can you share the error response body you\'re receiving?' },
      { from: 'contact', time: '09:12', text: '{"error":"internal_server_error","message":"webhook_delivery_failed","code":500}' },
    ],
    actions: [
      { text: 'Engage engineering on webhook delivery failures (P1)', type: 'escalation', done: true },
      { text: 'Request error logs from customer for diagnosis', type: 'investigation', done: true },
      { text: 'Provide customer with manual order confirmation template', type: 'workaround', done: false },
      { text: 'Post-incident review and RCA within 48 hours', type: 'follow-up', done: false },
    ]
  },
  {
    id: 't4', contact: CONTACTS[3], priority: 'P3', status: 'waiting',
    subject: 'Request for bulk messaging template approval',
    sla: { deadline: Date.now() + 1440 * 60000, breached: false },
    assignee: AGENTS[0],
    messages: [
      { from: 'contact', time: 'Yesterday 14:20', text: 'We\'d like to get approval for a new promotional template for our spring campaign. I\'ve attached the template text.' },
      { from: 'agent', time: 'Yesterday 14:35', text: 'Thanks James! I\'ll submit this to Meta for template review. Typical turnaround is 24-48 hours.' },
      { from: 'contact', time: 'Yesterday 14:37', text: 'Great, our campaign launches next Monday so hoping for quick approval.' },
    ],
    actions: [
      { text: 'Submit template to Meta for review', type: 'follow-up', done: true },
      { text: 'Notify customer when template is approved/rejected', type: 'follow-up', done: false },
    ]
  },
  {
    id: 't5', contact: CONTACTS[4], priority: 'P2', status: 'new',
    subject: 'Chatbot misrouting customer complaints',
    sla: { deadline: Date.now() + 90 * 60000, breached: false },
    assignee: AGENTS[3],
    messages: [
      { from: 'contact', time: '11:02', text: 'Our customers are complaining that the chatbot keeps sending them to the wrong department. Refund requests are going to Sales instead of Support.' },
      { from: 'contact', time: '11:04', text: 'This has been happening since the flow update last Friday. Can someone look at the routing rules?' },
    ],
    actions: [
      { text: 'Audit chatbot routing rules changed in last Friday\'s update', type: 'investigation', done: false },
      { text: 'Assign to technical support team', type: 'triage', done: false },
      { text: 'Test refund-request flow end-to-end after fix', type: 'verification', done: false },
    ]
  },
  {
    id: 't6', contact: CONTACTS[5], priority: 'P4', status: 'resolved',
    subject: 'How to set up auto-reply for holidays',
    sla: { deadline: Date.now() + 2880 * 60000, breached: false },
    assignee: AGENTS[1],
    messages: [
      { from: 'contact', time: 'Yesterday 16:00', text: 'Hello, we have a national holiday next week and want to set up an automatic reply. How do we configure this?' },
      { from: 'agent', time: 'Yesterday 16:10', text: 'Hi Carlos! Go to Settings > Business Tools > Away Message. You can set custom hours and your away message there.' },
      { from: 'contact', time: 'Yesterday 16:15', text: 'Found it, thank you! Very easy.' },
    ],
    actions: [
      { text: 'Provide setup instructions for auto-reply', type: 'resolution', done: true },
    ]
  },
  {
    id: 't7', contact: CONTACTS[6], priority: 'P1', status: 'new',
    subject: 'Payment gateway timeout on checkout messages',
    sla: { deadline: Date.now() + 40 * 60000, breached: false },
    assignee: AGENTS[3],
    messages: [
      { from: 'contact', time: '11:30', text: 'Our WhatsApp checkout flow is broken. Customers click "Pay Now" and get a timeout error. We\'re losing sales every minute this is down.' },
      { from: 'contact', time: '11:32', text: 'This is our peak hour. We need this fixed IMMEDIATELY.' },
    ],
    actions: [
      { text: 'Triage as P1 — revenue impact, assign to payments team', type: 'triage', done: false },
      { text: 'Check payment gateway status and API health', type: 'investigation', done: false },
      { text: 'Notify customer with workaround (direct payment link)', type: 'workaround', done: false },
    ]
  },
  {
    id: 't8', contact: CONTACTS[7], priority: 'P3', status: 'in-progress',
    subject: 'Add new team members to business account',
    sla: { deadline: Date.now() + 600 * 60000, breached: false },
    assignee: AGENTS[2],
    messages: [
      { from: 'contact', time: '10:30', text: 'We\'re expanding our support team by 3 agents. Can you help us add them to the WhatsApp Business account?' },
      { from: 'agent', time: '10:45', text: 'Of course, Liam. I\'ll need their names, email addresses, and the roles you\'d like them to have. I\'ll send over the invitation links.' },
      { from: 'contact', time: '10:50', text: 'Sending those details now via email.' },
    ],
    actions: [
      { text: 'Wait for team member details via email', type: 'follow-up', done: false },
      { text: 'Create accounts and send invitation links', type: 'resolution', done: false },
    ]
  },
];

const ALERTS = [
  { id: 'a1', type: 'critical', time: Date.now() - 2 * 60000, title: 'SLA Breach', body: 'EuroLogistics thread exceeded 60-min response SLA', thread: 't3', icon: 'clock' },
  { id: 'a2', type: 'critical', time: Date.now() - 8 * 60000, title: 'Payment Gateway Down', body: 'Riyadh Retail checkout flow returning timeouts', thread: 't7', icon: 'alert' },
  { id: 'a3', type: 'warning', time: Date.now() - 12 * 60000, title: 'P1 Unassigned', body: 'Payment gateway thread has no assigned agent', thread: 't7', icon: 'user' },
  { id: 'a4', type: 'warning', time: Date.now() - 18 * 60000, title: 'SLA At Risk', body: 'TechBrasil shipment thread — 25 min to SLA deadline', thread: 't1', icon: 'clock' },
  { id: 'a5', type: 'info', time: Date.now() - 25 * 60000, title: 'New Thread', body: 'Delhi Fresh Foods reported chatbot routing issue', thread: 't5', icon: 'message' },
  { id: 'a6', type: 'warning', time: Date.now() - 35 * 60000, title: 'Chatbot Errors', body: 'Refund routing misconfig detected — 23 affected conversations', thread: 't5', icon: 'alert' },
  { id: 'a7', type: 'info', time: Date.now() - 45 * 60000, title: 'Action Extracted', body: '3 action items auto-extracted from EuroLogistics thread', thread: 't3', icon: 'action' },
  { id: 'a8', type: 'info', time: Date.now() - 60 * 60000, title: 'Thread Resolved', body: 'MexiSupply auto-reply setup completed', thread: 't6', icon: 'check' },
  { id: 'a9', type: 'critical', time: Date.now() - 75 * 60000, title: 'API Errors Spike', body: '500 errors on webhook delivery — 12 customers affected', thread: 't3', icon: 'alert' },
  { id: 'a10', type: 'info', time: Date.now() - 90 * 60000, title: 'Agent Assignment', body: 'Tom W. assigned to Gulf Imports invoice thread', thread: 't2', icon: 'user' },
];

const ESCALATIONS = [
  {
    id: 'e1',
    thread: THREADS[2], // EuroLogistics
    reason: 'SLA breached — customer experiencing production outage due to API 500 errors. 500+ orders/hour impacted.',
    escalatedAt: Date.now() - 20 * 60000,
    level: 2,
    owner: 'Engineering Lead',
    status: 'active',
    timeline: [
      { time: '08:30', event: 'Customer reported API 500 errors' },
      { time: '08:45', event: 'Agent acknowledged, began investigation' },
      { time: '09:00', event: 'Customer escalated — production impact confirmed' },
      { time: '09:10', event: 'SLA timer expired (60 min)' },
      { time: '09:15', event: 'Auto-escalated to Level 2 — Engineering Lead notified' },
    ]
  },
  {
    id: 'e2',
    thread: THREADS[0], // TechBrasil
    reason: 'High-value customer ($240K annual) threatening to cancel. Shipment delay impacting their production line with Friday deadline.',
    escalatedAt: Date.now() - 5 * 60000,
    level: 1,
    owner: 'Account Manager',
    status: 'active',
    timeline: [
      { time: '09:12', event: 'Customer reported 3-day shipment delay' },
      { time: '09:14', event: 'Customer threatened cancellation' },
      { time: '09:18', event: 'Agent escalated to logistics' },
      { time: '09:22', event: 'Auto-escalated to Level 1 — Account Manager notified' },
    ]
  },
];

const PRIORITY_DATA = [
  { label: 'P1 — Critical', count: 3, color: '#ef4444' },
  { label: 'P2 — High', count: 2, color: '#f59e0b' },
  { label: 'P3 — Medium', count: 2, color: '#3b82f6' },
  { label: 'P4 — Low', count: 1, color: '#6b7280' },
];

const SLA_DATA = [
  { label: 'P1 Response (15 min)', compliance: 67, target: 95 },
  { label: 'P2 Response (60 min)', compliance: 100, target: 90 },
  { label: 'P1 Resolution (4 hr)', compliance: 50, target: 90 },
  { label: 'P2 Resolution (24 hr)', compliance: 100, target: 85 },
];
