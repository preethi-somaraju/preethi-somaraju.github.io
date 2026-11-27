// Wires the header toggle. The theme itself is applied by an inline snippet in
// each page's <head>, before first paint, so there is no flash of the wrong one.
(function () {
  var btn = document.getElementById('themeBtn');
  if (!btn) return;
  var lbl = document.getElementById('themeLbl');
  function sync() {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (lbl) lbl.textContent = dark ? 'Light' : 'Dark';
    btn.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
  }
  btn.addEventListener('click', function () {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (dark) document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', 'dark');
    try { localStorage.setItem('theme', dark ? 'light' : 'dark'); } catch (e) {}
    sync();
  });
  sync();
})();
