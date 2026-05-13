// footer.js — Dependability Holdings LLC
(function () {
 var footer = document.getElementById('site-footer');
 if (footer) {
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
   '    <li><a href="/forecast.html">S&amp;P 500 &amp; VIX Forecast</a></li>',
   '    <li><a href="/commentary.html">Market Commentary</a></li>',
   '    <li><a href="/education.html">Options Education</a></li>',
   '    <li><a href="/strategies.html">Options Strategies</a></li>',
   '   </ul>',
   '  </div>',
   '  <div class="footer-nav">',
   '   <h5>Company</h5>',
   '   <ul>',
   '    <li><a href="/about.html">About</a></li>',
   '    <li><a href="/methodology.html">Methodology</a></li>',
   '    <li><a href="/contact.html">Contact</a></li>',
   '   </ul>',
   '  </div>',
   '  <div class="footer-nav">',
   '   <h5>Legal</h5>',
   '   <ul>',
   '    <li><a href="/privacy.html">Privacy Policy</a></li>',
   '    <li><a href="/disclaimer.html">Investment Disclaimer</a></li>',
   '   </ul>',
   '  </div>',
   ' </div>',
   ' <div class="footer-bottom">',
   '  <p>&copy; 2026 Dependability Holdings LLC. All rights reserved.</p>',
   '  <p>For informational purposes only. Not investment advice. '
   +    'See our <a href="/methodology.html">full disclosures</a>.</p>',
   ' </div>',
   '</div>'
  ].join('\n');
 }
})();