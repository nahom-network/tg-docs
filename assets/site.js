(() => {
  const search = document.querySelector('#section-search');
  const list = document.querySelector('#section-list');
  const status = document.querySelector('#catalog-status');
  const summary = document.querySelector('#search-summary');
  const copyButton = document.querySelector('#copy-link');
  let sections = [];

  function absoluteIndexUrl() {
    return new URL('llms.txt', window.location.href).href;
  }

  function render() {
    const query = search.value.trim().toLocaleLowerCase();
    const filtered = sections.filter(section => [section.title, section.group, section.description].some(value => (value || '').toLocaleLowerCase().includes(query)));
    if (!sections.length) return;
    summary.textContent = query ? `${filtered.length} of ${sections.length} sections` : `${sections.length} sections${window.docsManifest?.updated_at ? ` · updated ${new Date(window.docsManifest.updated_at).toLocaleDateString()}` : ''}`;
    if (!filtered.length) {
      list.innerHTML = '<p class="empty-state">No sections match that search. Try a method name, type, or topic.</p>';
      return;
    }
    const groups = new Map();
    filtered.forEach(section => {
      const group = section.group || 'Other';
      if (!groups.has(group)) groups.set(group, []);
      groups.get(group).push(section);
    });
    list.innerHTML = [...groups].map(([group, items]) => `<section class="group-block"><h3 class="group-title">${escapeHtml(group)}</h3><div class="group-links">${items.map(section => `<a class="section-link" href="${safePath(section.path)}"><span><span class="section-name">${escapeHtml(section.title)}</span>${section.description ? `<span class="section-description">${escapeHtml(section.description)}</span>` : ''}</span><span class="section-arrow" aria-hidden="true">↗</span></a>`).join('')}</div></section>`).join('');
  }

  function escapeHtml(value) {
    return String(value || '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
  }

  function safePath(path) {
    const value = String(path || '');
    return /^sections\/[a-zA-Z0-9_-]+\.md$/.test(value) ? value : 'llms.txt';
  }

  search.addEventListener('input', render);
  document.addEventListener('keydown', event => {
    if (event.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName) && !event.ctrlKey && !event.metaKey && !event.altKey) {
      event.preventDefault(); search.focus();
    }
    if (event.key === 'Escape' && document.activeElement === search) { search.value = ''; render(); search.blur(); }
  });

  copyButton.addEventListener('click', async () => {
    const text = absoluteIndexUrl();
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(text);
      else {
        const field = document.createElement('textarea');
        field.value = text; field.setAttribute('readonly', ''); field.style.position = 'fixed'; field.style.opacity = '0';
        document.body.appendChild(field); field.select();
        const copied = document.execCommand('copy'); field.remove();
        if (!copied) throw new Error('Clipboard unavailable');
      }
      copyButton.classList.add('is-copied'); copyButton.innerHTML = '<span aria-hidden="true">✓</span> Copied';
      window.setTimeout(() => { copyButton.classList.remove('is-copied'); copyButton.innerHTML = '<span aria-hidden="true">⧉</span> Copy llms.txt link'; }, 2000);
    } catch (_) {
      copyButton.innerHTML = '<span aria-hidden="true">↗</span> Open llms.txt';
      copyButton.onclick = () => { window.location.href = 'llms.txt'; };
    }
  });

  fetch('docs.json').then(response => {
    if (!response.ok) throw new Error('Manifest unavailable');
    return response.json();
  }).then(manifest => {
    window.docsManifest = manifest;
    if (!Array.isArray(manifest.sections)) throw new Error('Invalid section catalog');
    sections = manifest.sections;
    status.textContent = manifest.page_count ? `${manifest.page_count} pages in the mirror` : `${sections.length} sections in the mirror`;
    render();
  }).catch(() => {
    status.textContent = 'Direct reference links available';
    if (!list.querySelector('.section-link')) {
      list.innerHTML = '<div class="catalog-error"><strong>Section catalog unavailable.</strong> The searchable index could not load. Read the <a href="llms.txt">LLM index</a> or <a href="llms-full.txt">complete reference</a> instead.</div>';
    }
    summary.textContent = '';
  });
})();
