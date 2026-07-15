// nav.js — Dependability Holdings LLC
// Row 1: DEPENDABILITY wordmark + centered tagline + right nav links
// Row 2: section tab bar (Overview / Market Commentary (dropdown) / Strategies / Education / Articles)
//
// Mike 2026-07-15 12:45 ET:
//   - Market Commentary tab replaces the standalone Morning + Afternoon tabs.
//     Hover over Market Commentary to reveal a dropdown:
//        • Morning Updates   → /commentary/
//        • Afternoon Updates → /forecast/
//   - Articles tab moved to position between Market Commentary and Strategies.
//
// Final tab order: Overview | Market Commentary ▾ | Articles | Strategies | Education
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
   '  <div class="dropdown">',
   '   <a href="/commentary/" class="dropdown-toggle" data-dropdown-target="commentary">Market Commentary &#9662;</a>',
   '   <div class="dropdown-content">',
   '    <a href="/commentary/">Morning Updates</a>',
   '    <a href="/forecast/">Afternoon Updates</a>',
   '   </div>',
   '  </div>',
   '  <a href="/articles/">Articles</a>',
   '  <a href="/strategies/">Strategies</a>',
   '  <a href="/education/">Education</a>',
   ' </div>',
   '</div>'
  ].join('\n');
 }

 // ── Active tab highlight ───────────────────────────────────
 var path = window.location.pathname;
 var tabs = document.querySelectorAll('.tab-bar-inner a');
 tabs.forEach(function (tab) {
  var href = tab.getAttribute('href');
  if (!href || href === '#') return;
  if (href === path || (href !== '/index' && path.startsWith(href))) {
   tab.classList.add('active');
  }
  if (href === '/index' && (path === '/' || path === '/index')) {
   tab.classList.add('active');
  }
 });

 // If we're on /commentary/ or /forecast/, also light up the Market Commentary parent
 if (path === '/commentary/' || path.startsWith('/commentary') ||
     path === '/forecast/'   || path.startsWith('/forecast')) {
  var parent = document.querySelector('.tab-bar-inner .dropdown-toggle');
  if (parent) parent.classList.add('active');
 }

 // ── Touch / click fallback for the dropdown (no hover on tablets) ──────────
 // First tap opens the dropdown; second tap navigates. Clicking inside the
 // dropdown navigates normally.
 var dropdown = document.querySelector('.tab-bar-inner .dropdown');
 if (dropdown) {
  var toggle = dropdown.querySelector('.dropdown-toggle');
  if (toggle) {
   toggle.addEventListener('click', function (e) {
    // If already open OR dropdown is hovered (handled by :hover CSS), let the
    // navigation happen. Otherwise, on touch devices, toggle open and prevent
    // navigation so the user can pick a submenu item.
    if (window.matchMedia('(hover: none)').matches && !dropdown.classList.contains('open')) {
     e.preventDefault();
     dropdown.classList.add('open');
     // Close on outside tap
     var closeHandler = function (ev) {
      if (!dropdown.contains(ev.target)) {
       dropdown.classList.remove('open');
       document.removeEventListener('click', closeHandler);
      }
     };
     setTimeout(function () { document.addEventListener('click', closeHandler); }, 0);
    }
   });
  }
 }

})();