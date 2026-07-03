// footer.js — Dependability Holdings LLC
(function () {
 function populateFooter() {
  var footer = document.getElementById('site-footer');
  if (!footer) return;
  if (footer.innerHTML.trim() !== '') return; // already populated
  footer.innerHTML = [
   '<div class="main-footer">',
   ' <div class="footer-grid">',
   '  <div class="footer-brand">',
   '   <h4>Dependability Holdings LLC</h4>',
   '   <p>Independent financial research and market analysis. '
   +    'Our work focuses on options market dynamics, volatility '
   +    'regimes, and macro-driven positioning.</p>',
   '  </div>',
   '  <div class="footer-nav">',
   '   <h5>Research</h5>',
   '   <ul>',
   '    <li><a href="/forecast/">S&amp;P 500 &amp; VIX Forecast</a></li>',
   '    <li><a href="/commentary/">Market Commentary</a></li>',
   '    <li><a href="/education/">Education</a></li>',
   '    <li><a href="/strategies/">Options Strategies</a></li>',
   '   </ul>',
   '  </div>',
   '  <div class="footer-nav">',
   '   <h5>Company</h5>',
   '   <ul>',
   '    <li><a href="/about/">About</a></li>',
   '    <li><a href="/methodology">Methodology</a></li>',
   '    <li><a href="/contact/">Contact</a></li>',
   '   </ul>',
   '  </div>',
   '  <div class="footer-nav">',
   '   <h5>Legal</h5>',
   '   <ul>',
   '    <li><a href="/privacy/">Privacy Policy</a></li>',
   '    <li><a href="/disclaimer/">Investment Disclaimer</a></li>',
   '   </ul>',
   '  </div>',
   ' </div>',
   ' <div class="footer-bottom">',
   '  <p>&copy; 2026 Dependability Holdings LLC. All rights reserved.</p>',
   '  <p>For informational purposes only. Not investment advice. '
   +    'See our <a href="/methodology">full disclosures</a>.</p>',
   ' </div>',
   '</div>'
  ].join('\n');
 }

 // Try immediately, then on DOMContentLoaded, then on load
 if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', populateFooter);
 } else {
  populateFooter();
 }
 window.addEventListener('load', populateFooter);
})();