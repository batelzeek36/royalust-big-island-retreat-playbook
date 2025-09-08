// persist checkbox state
const persistKey = (k) => `royalust:playbook:${k}`;
function restore() {
  document.querySelectorAll('.cb').forEach(cb => {
    const k = persistKey(cb.dataset.key);
    const v = localStorage.getItem(k);
    if (v !== null) { cb.checked = v === '1'; }
    cb.addEventListener('change', () => localStorage.setItem(k, cb.checked ? '1' : '0'));
  });
}
// print
document.getElementById('printBtn').addEventListener('click', e => { e.preventDefault(); window.print(); });
// year
document.getElementById('yr').textContent = new Date().getFullYear();
// search filter
const input = document.getElementById('search');
input.addEventListener('input', () => {
  const q = input.value.toLowerCase();
  document.querySelectorAll('section, article, details').forEach(el => {
    if (el.matches('details')) {
      // open matching accordions
      const text = el.innerText.toLowerCase();
      if (q && text.includes(q)) el.open = true;
    }
    if (el.matches('article.card, section.card, details')) {
      const text = el.innerText.toLowerCase();
      el.style.display = text.includes(q) ? '' : (q ? 'none' : '');
    }
  });
});
restore();