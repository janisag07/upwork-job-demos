// ── WhatsApp Business Monitor — App Logic ──

(function () {
  // ── Clock ──
  function updateClock() {
    const el = document.getElementById('clock');
    if (el) el.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  }
  setInterval(updateClock, 1000);
  updateClock();

  // ── View Switching ──
  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const target = btn.dataset.view;
      document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
      document.getElementById('view-' + target).classList.add('active');
    });
  });

  // ── Helpers ──
  function timeAgo(ts) {
    const diff = Math.floor((Date.now() - ts) / 60000);
    if (diff < 1) return 'just now';
    if (diff < 60) return diff + 'm ago';
    return Math.floor(diff / 60) + 'h ago';
  }

  function timeRemaining(ts) {
    const diff = Math.floor((ts - Date.now()) / 60000);
    if (diff < 0) return 'BREACHED ' + Math.abs(diff) + 'm ago';
    if (diff < 60) return diff + 'm remaining';
    return Math.floor(diff / 60) + 'h ' + (diff % 60) + 'm remaining';
  }

  function iconSVG(type) {
    const icons = {
      clock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
      alert: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
      user: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
      message: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
      action: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
      check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
    };
    return icons[type] || icons.message;
  }

  function priorityClass(p) {
    return { P1: 'priority-p1', P2: 'priority-p2', P3: 'priority-p3', P4: 'priority-p4' }[p] || '';
  }

  function statusLabel(s) {
    return { 'new': 'New', 'in-progress': 'In Progress', 'waiting': 'Waiting', 'resolved': 'Resolved' }[s] || s;
  }

  // ── Alerts Feed ──
  function renderAlerts(filter) {
    const list = document.getElementById('alerts-list');
    const filtered = filter === 'all' ? ALERTS : ALERTS.filter(a => a.type === filter);
    list.innerHTML = filtered.map(a => `
      <li class="alert-item alert-${a.type}" data-thread="${a.thread}">
        <div class="alert-icon">${iconSVG(a.icon)}</div>
        <div class="alert-body">
          <div class="alert-top">
            <span class="alert-title">${a.title}</span>
            <span class="alert-time">${timeAgo(a.time)}</span>
          </div>
          <p class="alert-text">${a.body}</p>
        </div>
      </li>
    `).join('');

    list.querySelectorAll('.alert-item').forEach(item => {
      item.addEventListener('click', () => {
        const tid = item.dataset.thread;
        openThread(tid);
      });
    });
  }

  document.querySelectorAll('.alerts-panel .pill').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.alerts-panel .pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderAlerts(btn.dataset.filter);
    });
  });

  renderAlerts('all');

  // ── Priority Bars ──
  function renderPriority() {
    const container = document.getElementById('priority-bars');
    const max = Math.max(...PRIORITY_DATA.map(d => d.count));
    container.innerHTML = PRIORITY_DATA.map(d => `
      <div class="pbar-row">
        <span class="pbar-label">${d.label}</span>
        <div class="pbar-track">
          <div class="pbar-fill" style="width:${(d.count / max) * 100}%;background:${d.color}"></div>
        </div>
        <span class="pbar-count">${d.count}</span>
      </div>
    `).join('');
  }
  renderPriority();

  // ── SLA Gauges ──
  function renderSLA() {
    const container = document.getElementById('sla-gauges');
    container.innerHTML = SLA_DATA.map(d => {
      const danger = d.compliance < d.target;
      return `
        <div class="sla-row ${danger ? 'sla-danger' : 'sla-ok'}">
          <div class="sla-info">
            <span class="sla-label">${d.label}</span>
            <span class="sla-target">Target: ${d.target}%</span>
          </div>
          <div class="sla-bar-track">
            <div class="sla-bar-fill" style="width:${d.compliance}%"></div>
            <div class="sla-bar-target" style="left:${d.target}%"></div>
          </div>
          <span class="sla-value ${danger ? 'text-danger' : ''}">${d.compliance}%</span>
        </div>
      `;
    }).join('');
  }
  renderSLA();

  // ── Threads List ──
  let activeThreadId = null;

  function renderThreads(filter) {
    const list = document.getElementById('threads-list');
    const filtered = filter === 'all' ? THREADS : THREADS.filter(t => t.status === filter);
    list.innerHTML = filtered.map(t => `
      <div class="thread-card ${t.id === activeThreadId ? 'selected' : ''} ${t.sla.breached ? 'sla-breached' : ''}" data-id="${t.id}">
        <div class="thread-avatar ${priorityClass(t.priority)}">${t.contact.avatar}</div>
        <div class="thread-info">
          <div class="thread-top-row">
            <span class="thread-name">${t.contact.name}</span>
            <span class="badge badge-${t.priority.toLowerCase()}">${t.priority}</span>
          </div>
          <p class="thread-subject">${t.subject}</p>
          <div class="thread-meta">
            <span class="thread-status status-${t.status}">${statusLabel(t.status)}</span>
            <span class="thread-assignee">${t.assignee}</span>
            ${t.sla.breached ? '<span class="sla-breach-tag">SLA BREACHED</span>' : ''}
          </div>
        </div>
        <div class="thread-actions-count" title="Extracted actions">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
          ${t.actions.length}
        </div>
      </div>
    `).join('');

    list.querySelectorAll('.thread-card').forEach(card => {
      card.addEventListener('click', () => {
        activeThreadId = card.dataset.id;
        renderThreads(getCurrentTriageFilter());
        renderThreadDetail(card.dataset.id);
      });
    });
  }

  function getCurrentTriageFilter() {
    const active = document.querySelector('[data-triage].active');
    return active ? active.dataset.triage : 'all';
  }

  function renderThreadDetail(id) {
    const t = THREADS.find(th => th.id === id);
    if (!t) return;
    const detail = document.getElementById('thread-detail');
    const slaText = t.sla.breached ? timeRemaining(t.sla.deadline) : timeRemaining(t.sla.deadline);
    const slaClass = t.sla.breached ? 'sla-breach-tag' : (t.sla.deadline - Date.now() < 30 * 60000 ? 'sla-warn-tag' : 'sla-ok-tag');

    detail.innerHTML = `
      <div class="detail-header">
        <div class="detail-contact">
          <div class="detail-avatar ${priorityClass(t.priority)}">${t.contact.avatar}</div>
          <div>
            <h3>${t.contact.name}</h3>
            <span class="detail-company">${t.contact.company} &middot; ${t.contact.phone}</span>
          </div>
        </div>
        <div class="detail-badges">
          <span class="badge badge-${t.priority.toLowerCase()}">${t.priority}</span>
          <span class="thread-status status-${t.status}">${statusLabel(t.status)}</span>
          <span class="${slaClass}">${slaText}</span>
        </div>
      </div>

      <div class="detail-body">
        <div class="detail-conversation">
          <h4>Conversation</h4>
          <div class="messages">
            ${t.messages.map(m => `
              <div class="msg msg-${m.from}">
                <div class="msg-bubble">
                  <p>${m.text}</p>
                  <span class="msg-time">${m.time}</span>
                </div>
              </div>
            `).join('')}
          </div>
        </div>

        <div class="detail-actions-panel">
          <h4>Extracted Actions</h4>
          <ul class="action-list">
            ${t.actions.map(a => `
              <li class="action-item ${a.done ? 'action-done' : ''}">
                <span class="action-check">${a.done ? '&#10003;' : ''}</span>
                <div class="action-info">
                  <span class="action-text">${a.text}</span>
                  <span class="action-type badge-action badge-${a.type}">${a.type}</span>
                </div>
              </li>
            `).join('')}
          </ul>
          <div class="detail-assignee">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            Assigned to: <strong>${t.assignee}</strong>
          </div>
        </div>
      </div>
    `;
  }

  document.querySelectorAll('[data-triage]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('[data-triage]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderThreads(btn.dataset.triage);
    });
  });

  renderThreads('all');

  // ── Escalations ──
  function renderEscalations() {
    const list = document.getElementById('esc-list');
    list.innerHTML = ESCALATIONS.map(e => `
      <div class="esc-card esc-level-${e.level}">
        <div class="esc-card-header">
          <div class="esc-title-row">
            <span class="esc-level-badge">Level ${e.level}</span>
            <h3>${e.thread.subject}</h3>
          </div>
          <div class="esc-meta">
            <span class="badge badge-${e.thread.priority.toLowerCase()}">${e.thread.priority}</span>
            <span>${e.thread.contact.name} &middot; ${e.thread.contact.company}</span>
            <span>Owner: <strong>${e.owner}</strong></span>
            <span>Escalated ${timeAgo(e.escalatedAt)}</span>
          </div>
        </div>
        <div class="esc-reason">
          <strong>Reason:</strong> ${e.reason}
        </div>
        <div class="esc-timeline">
          <h4>Timeline</h4>
          <ul class="timeline-list">
            ${e.timeline.map(t => `
              <li class="timeline-item">
                <span class="timeline-time">${t.time}</span>
                <span class="timeline-event">${t.event}</span>
              </li>
            `).join('')}
          </ul>
        </div>
        <div class="esc-actions-row">
          <button class="btn btn-primary" onclick="this.textContent='Acknowledged';this.disabled=true">Acknowledge</button>
          <button class="btn btn-outline" onclick="this.textContent='Escalated to L${e.level + 1}';this.disabled=true">Escalate to L${e.level + 1}</button>
          <button class="btn btn-ghost" onclick="openThread('${e.thread.id}')">View Thread</button>
        </div>
      </div>
    `).join('');
  }
  renderEscalations();

  // ── Open Thread helper (navigates to thread view) ──
  window.openThread = function (tid) {
    activeThreadId = tid;
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('[data-view="threads"]').classList.add('active');
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    document.getElementById('view-threads').classList.add('active');
    document.querySelectorAll('[data-triage]').forEach(b => b.classList.remove('active'));
    document.querySelector('[data-triage="all"]').classList.add('active');
    renderThreads('all');
    renderThreadDetail(tid);
  };

  // ── Simulated live alert injection ──
  const liveAlerts = [
    { type: 'warning', title: 'Response Time Warning', body: 'Average first-response time increased to 12 min (target: 5 min)', icon: 'clock' },
    { type: 'info', title: 'Action Completed', body: 'Nadia K. completed "Provide updated ETA" for TechBrasil thread', icon: 'check' },
    { type: 'critical', title: 'New P1 Thread', body: 'Incoming P1 from +234 801 234 5678 — payment processing failure', icon: 'alert' },
    { type: 'info', title: 'Template Approved', body: 'Meta approved PacificTrade spring campaign template', icon: 'action' },
    { type: 'warning', title: 'Queue Building', body: '3 threads waiting for agent assignment > 10 minutes', icon: 'user' },
  ];
  let liveIdx = 0;

  setInterval(() => {
    const a = liveAlerts[liveIdx % liveAlerts.length];
    liveIdx++;
    const newAlert = { ...a, id: 'live-' + liveIdx, time: Date.now(), thread: 't1' };
    ALERTS.unshift(newAlert);
    if (ALERTS.length > 20) ALERTS.pop();
    const currentFilter = document.querySelector('.alerts-panel .pill.active');
    renderAlerts(currentFilter ? currentFilter.dataset.filter : 'all');

    // Flash effect
    const first = document.querySelector('.alert-item');
    if (first) {
      first.classList.add('alert-flash');
      setTimeout(() => first.classList.remove('alert-flash'), 1500);
    }
  }, 8000);

})();
