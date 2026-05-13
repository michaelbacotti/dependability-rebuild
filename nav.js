// nav.js — Dependability Holdings LLC
// Top utility bar + category tab bar
(function () {

 // ── Utility Bar ──────────────────────────────────────────
 var utility = document.getElementById('site-utility');
 if (utility) {
  utility.innerHTML = [
   '<div class="utility-bar">',
   ' <div class="brand"><a href="/index.html">DEPENDABILITY</a></div>',
   ' <div class="utility-links">',
   '  <a href="/about.html">About</a>',
   '  <a href="/methodology.html">Methodology</a>',
   '  <a href="/about.html#contact">Contact</a>',
   ' </div>',
   '</div>'
  ].join('\n');
 }

 // ── Category Tab Bar ───────────────────────────────────────
 var nav = document.getElementById('site-nav');
 if (nav) {
  nav.innerHTML = [
   '<div class="tab-bar">',
   ' <a href="/index.html">Overview</a>',
   ' <a href="/forecast.html">Forecast</a>',
   ' <a href="/commentary.html">Market Commentary</a>',
   ' <a href="/education.html">Education</a>',
   ' <a href="/strategies.html">Options Strategies</a>',
   ' <a href="/about.html">About</a>',
   '</div>'
  ].join('\n');
 }

 // ── Active tab highlight ───────────────────────────────────
 var path = window.location.pathname;
 var tabs = document.querySelectorAll('.tab-bar a');
 tabs.forEach(function (tab) {
  var href = tab.getAttribute('href');
  if (href === path || (href !== '/index.html' && path.startsWith(href))) {
   tab.classList.add('active');
  }
  if (href === '/index.html' && (path === '/' || path === '/index.html')) {
   tab.classList.add('active');
  }
 });

})();