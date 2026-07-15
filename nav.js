// nav.js — Dependability Holdings LLC
// Row 1: DEPENDABILITY wordmark + centered tagline + right nav links
// Row 2: section tab bar (Overview / Morning / Afternoon / Strategies / Education / Articles)
//
// Mike 2026-07-15: tab labels updated to reflect the new editorial split:
//   - /commentary/ → "Morning" (AM cron writes daily Mon-Fri 7am ET)
//   - /forecast/   → "Afternoon" (PM cron writes daily; label changed from "Forecast")
//   - /strategies/ → "Strategies" (unchanged — Options Strategies kept)
//   - /education/  → "Education" (unchanged — investment education about market technicals)
//   - /articles/   → "Articles" (NEW — complete archive of every published piece)
(function () {

 // ── Row 1: Top Black Bar ──────────────────────────────────
 var utility = document.getElementById('site-utility');
 if (utility) {
  utility.innerHTML = [
   '<nav class="top-bar">',
   ' <a href="/" class="top-wordmark">DEPENDABILITY</a>',
   ' <span class="top-tagline">Independent market research and options analysis</span>',
   ' <div class="top-links">',
   '  <a href="/about/">About</a>',
   '  <a href="/methodology">Methodology</a>',
   '  <a href="/about#contact">Contact</a>',
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
   '  <a href="/index">Overview</a>',
   '  <a href="/commentary/">Morning</a>',
   '  <a href="/forecast/">Afternoon</a>',
   '  <a href="/strategies/">Strategies</a>',
   '  <a href="/education/">Education</a>',
   '  <a href="/articles/">Articles</a>',
   ' </div>',
   '</div>'
  ].join('\n');
 }

 // ── Active tab highlight ───────────────────────────────────
 var path = window.location.pathname;
 var tabs = document.querySelectorAll('.tab-bar a');
 tabs.forEach(function (tab) {
  var href = tab.getAttribute('href');
  if (href === path || (href !== '/index' && path.startsWith(href))) {
   tab.classList.add('active');
  }
  if (href === '/index' && (path === '/' || path === '/index')) {
   tab.classList.add('active');
  }
 });

})();