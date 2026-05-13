// nav.js — Dependability Holdings LLC
// Row 1: DEPENDABILITY wordmark + centered tagline + right nav links
// Row 2: section tab bar (Overview / Forecast / Commentary / Education / Strategies)
(function () {

 // ── Row 1: Top Black Bar ──────────────────────────────────
 var utility = document.getElementById('site-utility');
 if (utility) {
  utility.innerHTML = [
   '<nav class="top-bar">',
   ' <a href="/" class="top-wordmark">DEPENDABILITY</a>',
   ' <span class="top-tagline">Independent market research and options analysis</span>',
   ' <div class="top-links">',
   '  <a href="/about.html">About</a>',
   '  <a href="/methodology.html">Methodology</a>',
   '  <a href="/about.html#contact">Contact</a>',
   ' </div>',
   '</nav>'
  ].join('\n');
 }

 // ── Row 2: Section Tab Bar ───────────────────────────────
 var nav = document.getElementById('site-nav');
 if (nav) {
  nav.innerHTML = [
   '<div class="tab-bar">',
   ' <div class="tab-bar-inner">',
   '  <a href="/index.html">Overview</a>',
   '  <a href="/forecast.html">Forecast</a>',
   '  <a href="/commentary.html">Market Commentary</a>',
   '  <a href="/education.html">Education</a>',
   '  <a href="/strategies.html">Options Strategies</a>',
   ' </div>',
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