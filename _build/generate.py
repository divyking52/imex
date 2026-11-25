# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = (Path(__file__).parent / "shared.css").read_text(encoding="utf-8")
JS = (Path(__file__).parent / "shared.js").read_text(encoding="utf-8")

SERVICES = [
    ("sea-freight.html", "Sea Freight", "Complete sea freight for import and export, including inbound and outbound ocean solutions, FCL/LCL cross trade and door-to-door delivery."),
    ("lcl-consolidation.html", "Inbound/Outbound LCL Consolidation", "LCL consolidation from Indian ports and hinterland ICDs, with import consolidation from worldwide origins."),
    ("buyer-consolidation.html", "Buyer Consolidation", "Cost-effective consolidation for customers with multiple vendors who regularly order from a specific region or country."),
    ("global-fcl-forwarding.html", "Global FCL Forwarding", "Inbound and outbound full container load services, tailor-made to volume or a single route."),
    ("air-freight.html", "Air Freight", "Expert international air freight forwarding for a single shipment or a complex freight management programme."),
    ("customs-clearance.html", "Customs Clearance", "In-house customs clearance at major Indian ports, including export clearance and project logistics."),
    ("dgft-licensing.html", "DGFT / Licensing Works", "DGFT and related authority work, including licences and registrations connected to import-export needs."),
]
SERVICE_IMGS = {
    "sea-freight.html": "assets/images/background/banner_s.jpg",
    "lcl-consolidation.html": "assets/images/background/banner_olc.jpg",
    "buyer-consolidation.html": "assets/images/background/banner-1.jpg",
    "global-fcl-forwarding.html": "assets/images/links/stock-containers.jpg",
    "air-freight.html": "assets/images/background/banner_a.jpg",
    "customs-clearance.html": "assets/images/background/banner_cc.jpg",
    "dgft-licensing.html": "assets/images/background/banner_lic.jpg",
}

def nav(active):
    def a(href, label, key, extra=""):
        cls = "is-active" if active == key else ""
        return f'<a href="{href}" class="{cls}" data-vt="{extra or "wipe"}">{label}</a>'
    svc_items = '<li><a href="services.html" class="{}" data-vt="wipe">All services</a></li>'.format("is-active" if active=="services" else "") + "".join(
        f'<li><a href="{h}" class="{"is-active" if active==h else ""}" data-vt="zoom">{t}</a></li>'
        for h,t,_ in SERVICES
    )
    return f'''
<a class="skip" href="#main">Skip to content</a>
<div class="cursor"></div><div class="cursor-dot"></div>
<div class="imex-loader" id="imexLoader" role="status" aria-live="polite" aria-busy="true" aria-label="Loading IMEX">
  <div class="imex-loader-veil" aria-hidden="true"></div>
  <div class="imex-loader-stage">
    <svg class="imex-loader-route" viewBox="0 0 720 220" aria-hidden="true">
      <path class="imex-loader-lane" d="M48 168 C140 168 170 52 260 52 C350 52 380 168 470 168 C560 168 590 72 672 72"/>
      <path class="imex-loader-lane-draw" d="M48 168 C140 168 170 52 260 52 C350 52 380 168 470 168 C560 168 590 72 672 72"/>
      <circle class="imex-loader-node" cx="48" cy="168" r="5"/>
      <circle class="imex-loader-node" cx="260" cy="52" r="5"/>
      <circle class="imex-loader-node" cx="470" cy="168" r="5"/>
      <circle class="imex-loader-node" cx="672" cy="72" r="6"/>
      <g class="imex-loader-box" transform="translate(48 168)">
        <rect x="-14" y="-9" width="28" height="18" rx="2"/>
        <rect x="-14" y="-3" width="28" height="3" opacity=".35"/>
        <rect x="-14" y="3" width="28" height="3" opacity=".35"/>
      </g>
    </svg>
    <div class="imex-loader-brand">
      <span class="imex-loader-letter imex-loader-letter-im">I</span>
      <span class="imex-loader-letter imex-loader-letter-im">M</span>
      <span class="imex-loader-letter imex-loader-letter-ex">E</span>
      <span class="imex-loader-letter imex-loader-letter-ex">X</span>
    </div>
    <p class="imex-loader-tag">Clearing the route</p>
    <div class="imex-loader-meter" aria-hidden="true">
      <span class="imex-loader-bar"><i></i></span>
      <b class="imex-loader-pct">0</b>
    </div>
  </div>
</div>
<div class="vt-overlay" aria-hidden="true">
  <div class="vt-wipe"></div><div class="vt-route"></div><div class="vt-zoom"></div>
  <div class="vt-frag">{'<span></span>'*6}</div>
</div>
<header class="site-nav" id="siteNav">
  <a class="logo" href="index.html" data-vt="route"><img src="assets/logo/logo-black.png" alt="IMEX Clearing & Logistics Pvt. Ltd." width="150" height="50"></a>
  <ul class="nav-links">
    <li>{a("index.html","Home","home","route")}</li>
    <li>{a("about.html","About Us","about","frag")}</li>
    <li class="drop">
      <button type="button" aria-expanded="false" aria-haspopup="true">Services</button>
      <ul class="drop-menu" role="menu">{svc_items}</ul>
    </li>
    <li>{a("value-added-services.html","Value Added Services","vas","frag")}</li>
    <li>{a("tracking.html","Track & Trace","tracking","route")}</li>
    <li>{a("quote.html","Get a Quote","quote","zoom")}</li>
    <li>{a("contact.html","Contact","contact","wipe")}</li>
  </ul>
  <a class="nav-cta magnetic btn btn-cyan" href="quote.html" data-vt="zoom">Get a Quote</a>
  <button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
</header>
<nav class="mobile-panel" aria-label="Mobile">
  <a href="index.html">Home</a>
  <a href="about.html">About Us</a>
  <p style="margin:18px 0 6px;color:#00ADEF;letter-spacing:.2em;font-size:12px">SERVICES</p>
  <div class="sub">{''.join(f'<a href="{h}">{t}</a>' for h,t,_ in SERVICES)}</div>
  <a href="value-added-services.html">Value Added Services</a>
  <a href="tracking.html">Track & Trace</a>
  <a href="quote.html">Get a Quote</a>
  <a href="contact.html">Contact</a>
</nav>
'''

def footer():
    svc = "".join(f'<a href="{h}" data-vt="zoom">{t}</a>' for h,t,_ in SERVICES)
    return f'''
<footer class="site-foot">
  <div class="foot-horizon" aria-hidden="true"></div>
  <div class="wrap">
    <div class="foot-mast">
      <a class="foot-logo" href="index.html" data-vt="wipe">
        <img src="assets/logo/logo-white.png" alt="IMEX Clearing &amp; Logistics" width="150" height="50">
      </a>
      <a class="btn btn-cyan magnetic" href="quote.html" data-vt="zoom">Request a Quote <span class="arr">→</span></a>
      <div class="foot-ident">
        <p class="display foot-title">Imex International</p>
        <p class="foot-legalname">Clearing &amp; Logistics Private Limited</p>
      </div>
    </div>
    <div class="foot-rule" aria-hidden="true"></div>
    <div class="foot-body">
      <address class="foot-desk">
        <h3>Kanpur desk</h3>
        <p>No. 16, 1st Floor, Harmony Arcade,<br>17/1, Telegraph Road, The Mall,<br>Kanpur - 208001</p>
        <a href="tel:+915122391885"><span>Tel</span>+91 512-2391885</a>
        <a href="tel:+919335347057"><span>Mobile</span>+91 933 534 7057</a>
        <a href="mailto:sayyam7@imexclearing.com"><span>Email</span>sayyam7@imexclearing.com</a>
        <div class="foot-social">
          <a href="https://www.facebook.com/Imex-Clearing-Logistics-pvt-ltd-112181573833973/" target="_blank" rel="noopener noreferrer" aria-label="IMEX on Facebook">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14.2 8H16V5.6h-1.8c-2.2 0-3.6 1.4-3.6 3.7v1.4H9v2.7h1.6V19h2.8v-5.6h2.2l.5-2.7h-2.7V9.4c0-.7.3-1.4 1.2-1.4h.6z"/></svg>
          </a>
          <a href="https://www.instagram.com/imexclearing/" target="_blank" rel="noopener noreferrer" aria-label="IMEX on Instagram">
            <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.6" y="3.6" width="16.8" height="16.8" rx="5" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="3.6" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="17.1" cy="6.9" r="1.05" fill="currentColor"/></svg>
          </a>
        </div>
      </address>
      <nav class="foot-col" aria-label="Footer navigation">
        <h3>Navigate</h3>
        <a href="index.html">Home</a>
        <a href="about.html">About Us</a>
        <a href="services.html">Services</a>
        <a href="value-added-services.html">Value Added Services</a>
        <a href="tracking.html">Track &amp; Trace</a>
        <a href="quote.html">Get a Quote</a>
        <a href="contact.html">Contact</a>
        <div class="foot-tools">
          <a href="value-added-services.html">Trade tools</a>
          <a href="https://www.xe.com/currencyconverter/" target="_blank" rel="noopener">Currency converter</a>
        </div>
      </nav>
      <nav class="foot-col" aria-label="Footer services">
        <h3>Services</h3>
        {svc}
      </nav>
    </div>
    <div class="foot-bottom">
      <p>Imex International © Copyright 2020, All rights reserved</p>
      <p>Powered and by <a href="http://rootkittechnologies.com/" target="_blank" rel="noopener">RootKit Technologies</a></p>
    </div>
  </div>
</footer>
<button class="to-top" aria-label="Back to top">↑</button>
'''

def shell(page, title, desc, extra_css, body, scene="container"):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="icon" type="image/png" href="assets/logo/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.1.20/dist/lenis.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.min.js"></script>
  <style>
{CSS}
{extra_css}
  </style>
</head>
<body data-page="{page}" class="is-loading">
{nav(page)}
<main id="main">{body}</main>
{footer()}
<script>
{JS}
</script>
</body>
</html>
'''

def related(current):
    keys = [s[0] for s in SERVICES]
    i = keys.index(current)
    prevs = SERVICES[i-1]
    nexts = SERVICES[(i+1)%len(SERVICES)]
    others = "".join(
        f'''<a class="rel-card" href="{h}" data-vt="zoom">
          <img src="{SERVICE_IMGS[h]}" alt="{t}">
          <div class="rel-card-copy">
            <strong>{t}</strong>
            <span class="arr">→</span>
          </div>
        </a>'''
        for h,t,_ in SERVICES if h != current
    )
    return f'''
<section class="section related-sec">
  <div class="wrap">
    <p class="kicker">Related services</p>
    <h2 class="display related-title">Continue the journey</h2>
    <div class="related">{others}</div>
    <div class="pager">
      <a class="pager-link" href="{prevs[0]}" data-vt="wipe"><span>Previous</span><strong>← {prevs[1]}</strong></a>
      <a class="pager-link pager-next" href="{nexts[0]}" data-vt="zoom"><span>Next</span><strong>{nexts[1]} →</strong></a>
    </div>
  </div>
</section>
<section class="section quote-cta-band">
  <div class="wrap quote-cta-row">
    <h2 class="display">Need this movement quoted?</h2>
    <a class="btn btn-cyan magnetic" href="quote.html" data-vt="zoom">Request a Quote <span class="arr">→</span></a>
  </div>
</section>
'''

# ---------- PAGES ----------

home_css = '''
.home-about{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
.year-mask{font-size:clamp(90px,16vw,220px);font-weight:800;line-height:.8;color:transparent;-webkit-text-stroke:1px rgba(46,49,146,.35)}
.hero-stack{position:relative}
.hero-film{position:sticky;top:0;height:100vh;z-index:1;will-change:transform}
.hero-film-track{height:320vh;pointer-events:none}
@media (prefers-reduced-motion: reduce){
  .hero-film{position:relative}
  .hero-film-track{display:none;height:0}
  .story-band{border-radius:0;box-shadow:none}
}
.story-band{position:relative;z-index:3;overflow:hidden;background:linear-gradient(180deg,#f4f8fd 0%,#eaf2f8 100%);min-height:680px;border-radius:40px 40px 0 0;box-shadow:0 -32px 90px rgba(7,11,24,.38)}
.story-copy{position:relative;z-index:3;width:min(620px,46vw);margin-left:max(24px,calc((100vw - 1240px)/2));padding:96px 32px 88px 0;will-change:transform}
.story-year{font-family:var(--font);font-size:clamp(96px,13vw,176px);font-weight:800;line-height:.72;letter-spacing:-.06em;color:transparent;-webkit-text-stroke:2px rgba(0,173,239,.42);margin:0 0 -8px}
.story-title{position:relative;font-size:clamp(34px,4.4vw,58px);color:#1b2559;margin:0 0 14px}
.story-title span{color:#00ADEF}
.story-mark{position:absolute;left:-18px;top:.42em;width:9px;height:9px;background:#00ADEF}
.story-rule{display:block;width:72px;height:4px;background:#00ADEF;border-radius:4px;margin:0 0 22px}
.story-copy .lede{color:#4a5568;font-size:16px;line-height:1.7;max-width:54ch}
.story-copy .lede + .lede{margin-top:14px}
.story-actions{display:flex;flex-wrap:wrap;align-items:center;gap:18px;margin-top:28px}
.story-play{display:inline-flex;align-items:center;gap:12px;color:#1b2559;font-family:var(--font);font-size:14px;font-weight:700}
.story-play i{width:44px;height:44px;border-radius:50%;border:2px solid #00ADEF;display:grid;place-items:center;background:#fff}
.story-play svg{width:14px;height:14px;margin-left:2px}
.story-visual{position:absolute;right:0;top:0;bottom:0;width:54%;z-index:1;will-change:transform}
.story-yard{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:68% 40%}
.story-slash{position:absolute;left:-1px;top:0;height:100%;width:42%;z-index:2;pointer-events:none}
.story-truck{position:absolute;left:4%;bottom:16%;width:90%;max-width:640px;z-index:3;filter:drop-shadow(0 28px 36px rgba(10,24,48,.32));pointer-events:none}
.story-pills{position:absolute;left:10%;bottom:22px;z-index:4;display:flex;gap:10px;flex-wrap:wrap;max-width:86%}
.story-pill{display:flex;align-items:center;gap:10px;min-height:64px;padding:10px 16px 10px 12px;border-radius:14px;background:rgba(22,28,48,.92);color:#fff;box-shadow:0 12px 28px rgba(8,16,32,.28);backdrop-filter:blur(8px)}
.story-pill svg{width:28px;height:28px;flex:0 0 28px}
.story-pill b{display:block;font-family:var(--font);font-size:11px;font-weight:600;letter-spacing:.04em;color:rgba(255,255,255,.7)}
.story-pill strong{display:block;font-family:var(--font);font-size:13px;font-weight:800;line-height:1.2;margin-top:2px}
.story-corner{position:absolute;right:0;bottom:0;width:210px;height:160px;z-index:3;pointer-events:none;background:linear-gradient(135deg,transparent 48%,#1d4ed8 48.2%)}
.story-corner svg{position:absolute;right:8px;bottom:8px;width:120px;opacity:.35}
.globe-band{position:relative;min-height:100vh;display:flex;align-items:center;overflow:hidden;isolation:isolate}
.globe-band::before{content:"";position:absolute;inset:12% -8% auto;height:55%;background:radial-gradient(ellipse at 70% 40%,rgba(0,173,239,.16),transparent 62%);pointer-events:none;z-index:0}
.globe-band-grid{position:relative;z-index:1;display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;width:min(1280px,calc(100% - 40px));margin:0 auto}
.globe-copy{max-width:34ch}
.globe-copy .display{font-size:clamp(40px,6vw,84px)}
.globe-copy .lede{margin-top:18px}
.globe-frame{border-radius:28px;border:1px solid rgba(0,173,239,.32);background:
  radial-gradient(circle at 50% 40%,rgba(0,173,239,.28),transparent 42%),
  radial-gradient(circle at 50% 55%,#0d1a40 0%,#060a16 75%);
  box-shadow:inset 0 0 70px rgba(0,173,239,.1),0 28px 64px rgba(0,0,0,.32);overflow:hidden;height:min(70vh,640px);transform-origin:60% 50%;will-change:transform,opacity;perspective:1200px}
.globe-frame canvas{display:block;width:100%;height:100%}
@media(max-width:900px){.globe-band{min-height:auto;padding:72px 0}.globe-band-grid{grid-template-columns:1fr;gap:28px}.globe-frame{height:min(58vh,480px)}}
.vas-band{position:relative;overflow:hidden;isolation:isolate;background:linear-gradient(180deg,#f4f8fd 0%,#e7f1f8 100%);padding:96px 0 0}
.vas-band::before{content:"";position:absolute;inset:auto 0 0;height:1px;background:linear-gradient(90deg,transparent,rgba(0,173,239,.35),transparent);z-index:3}
.vas-shell{width:min(1280px,calc(100% - 40px));margin:0 auto;display:grid;grid-template-columns:minmax(260px,.78fr) 1.22fr;gap:28px 40px;align-items:end;min-height:620px}
.vas-copy{position:relative;z-index:2;padding:0 0 64px;max-width:420px}
.vas-kicker{display:inline-flex;align-items:center;gap:12px;margin:0 0 16px;font-family:var(--font);font-size:12px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:#00ADEF}
.vas-kicker i{display:block;width:36px;height:2px;background:#00ADEF;border-radius:2px}
.vas-title{margin:0 0 18px;font-size:clamp(40px,5.4vw,72px);line-height:.88;letter-spacing:-.05em;color:#1b2559}
.vas-lede{margin:0 0 28px;font-size:16px;line-height:1.7;color:#4a5568;max-width:36ch}
.vas-copy .btn{box-shadow:0 10px 24px rgba(46,49,146,.16)}
.vas-stage{position:relative;min-height:560px;border-radius:36px 36px 0 0;overflow:hidden;background:#10183f;box-shadow:0 28px 56px rgba(18,42,84,.14)}
.vas-media{position:absolute;inset:0}
.vas-media img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity .55s var(--ease),transform 1.1s var(--ease);filter:saturate(.88) contrast(1.02)}
.vas-media img.is-on{opacity:1;transform:scale(1)}
.vas-media::after{content:"";position:absolute;inset:0;background:linear-gradient(100deg,rgba(7,11,24,.72) 0%,rgba(7,11,24,.28) 42%,rgba(7,11,24,.45) 100%),linear-gradient(180deg,transparent 35%,rgba(7,11,24,.78));pointer-events:none}
.vas-index{position:relative;z-index:2;display:flex;flex-direction:column;justify-content:flex-end;height:100%;min-height:560px;padding:48px 28px 28px;max-width:460px}
.vas-index a{display:grid;grid-template-columns:14px 1fr auto;gap:8px 14px;align-items:center;padding:18px 0;border-top:1px solid rgba(255,255,255,.14);color:#fff;text-decoration:none;transition:color .25s,transform .25s var(--ease)}
.vas-index a:first-child{border-top:0}
.vas-index a i{display:block;width:10px;height:10px;border-radius:50%;border:1.5px solid rgba(0,173,239,.55);background:transparent;transition:background .25s,box-shadow .25s}
.vas-index a strong{font-family:var(--font);font-size:clamp(18px,2vw,24px);font-weight:700;letter-spacing:-.02em;line-height:1.15}
.vas-index a em{font-style:normal;font-family:var(--font);font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.42);justify-self:end}
.vas-index a.is-on,.vas-index a:hover{color:#fff;transform:translateX(4px)}
.vas-index a.is-on i,.vas-index a:hover i{background:#00ADEF;box-shadow:0 0 0 5px rgba(0,173,239,.18);border-color:#00ADEF}
.vas-index a.is-on strong,.vas-index a:hover strong{color:#00ADEF}
.vas-index a.is-on em,.vas-index a:hover em{color:rgba(255,255,255,.72)}
.vas-more{display:flex;flex-wrap:wrap;gap:10px 18px;margin-top:18px;padding-top:16px;border-top:1px solid rgba(255,255,255,.12)}
.vas-more a{display:inline;padding:0;border:0;transform:none;font-family:var(--font);font-size:13px;font-weight:600;color:rgba(255,255,255,.55)}
.vas-more a:hover{color:#00ADEF;transform:none}
.quote-band{position:relative;isolation:isolate;min-height:min(760px,94vh);overflow:hidden;background:
  radial-gradient(900px 520px at 18% 88%,rgba(0,173,239,.16),transparent 58%),
  radial-gradient(640px 380px at 72% 8%,rgba(90,140,255,.2),transparent 62%),
  linear-gradient(118deg,#10183f 0%,#18245e 28%,#24348f 52%,#1a2468 78%,#15205c 100%)}
.qb-light{position:absolute;inset:0;width:100%;height:100%;display:block;z-index:0;pointer-events:none}
.qb-blobs{position:absolute;inset:0;z-index:1;pointer-events:none;overflow:hidden}
.qb-blob{position:absolute;border-radius:50%;filter:blur(10px)}
.qb-blob-a{width:46vw;height:46vw;left:-12%;top:-28%;background:radial-gradient(circle,rgba(36,58,160,.55),transparent 68%)}
.qb-blob-b{width:38vw;height:38vw;left:18%;top:-18%;background:radial-gradient(circle,rgba(14,28,90,.5),transparent 70%)}
.qb-blob-c{width:28vw;height:28vw;left:8%;bottom:8%;background:radial-gradient(circle,rgba(0,173,239,.14),transparent 70%)}
.qb-globe{position:absolute;left:-8%;bottom:-18%;width:min(52vw,620px);height:auto;z-index:1;pointer-events:none;opacity:.9}
.qb-layout{position:relative;z-index:2;display:grid;grid-template-columns:.94fr 1.06fr;align-items:stretch;min-height:min(760px,94vh);width:min(1280px,calc(100% - 48px));margin:0 auto;padding:80px 8px 12px;gap:12px}
.qb-copy{position:relative;z-index:3;max-width:560px;padding:24px 12px 80px 8px;align-self:center}
.qb-kicker{display:inline-flex;align-items:center;gap:12px;margin:0 0 18px;font-family:var(--font);font-size:12px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:#00ADEF}
.qb-kicker i{display:block;width:36px;height:2px;background:#00ADEF;border-radius:2px;flex:0 0 36px}
.qb-title{font-size:clamp(42px,5.6vw,78px);color:#fff;max-width:9ch;line-height:.9;letter-spacing:-.05em;text-shadow:0 8px 28px rgba(8,16,40,.28)}
.qb-title .qb-line{white-space:nowrap}
.qb-lede{margin:22px 0 28px;max-width:38ch;color:rgba(255,255,255,.84);font-size:17px;line-height:1.7}
.qb-cta{box-shadow:0 14px 34px rgba(0,173,239,.4)}
.qb-cta:active{transform:scale(.97)}
.qb-flight{position:absolute;left:36%;bottom:14%;width:min(38vw,420px);height:160px;overflow:visible;pointer-events:none;z-index:4;grid-column:1/-1;grid-row:1}
.qb-dash{fill:none;stroke:rgba(255,255,255,.62);stroke-width:1.7;stroke-dasharray:6 8;stroke-linecap:round}
.qb-plane{transform-box:fill-box;transform-origin:center}
.qb-visual{position:relative;height:min(680px,86vh);min-height:560px;margin-right:-24px}
.qb-frame{position:absolute;left:10%;top:10%;width:76%;height:70%;border-radius:32px;overflow:hidden;transform:rotate(-12deg);z-index:1;border:10px solid rgba(255,255,255,.92);box-shadow:0 32px 64px rgba(16,36,90,.28),0 0 0 1px rgba(0,173,239,.12)}
.qb-yard{width:100%;height:100%;object-fit:cover;filter:saturate(.7) contrast(1.02);transform:scale(1.14) rotate(12deg)}
.qb-frame::after{content:"";position:absolute;inset:0;background:linear-gradient(160deg,rgba(255,255,255,.16),transparent 42%,rgba(20,40,90,.18))}
.qb-orbit{position:absolute;left:2%;top:2%;width:96%;height:96%;z-index:2;pointer-events:none;overflow:visible}
.qb-ring{fill:none;stroke:#00ADEF;stroke-width:2;opacity:.8}
.qb-ring-2{opacity:.35;stroke-width:1.3}
.qb-courier{position:absolute;left:50%;bottom:10px;height:86%;width:auto;max-width:none;z-index:3;filter:drop-shadow(0 22px 28px rgba(12,28,64,.32));pointer-events:none}
.qb-ground{position:absolute;left:28%;bottom:18px;width:54%;height:28px;border-radius:50%;background:radial-gradient(ellipse,rgba(12,28,64,.28),transparent 70%);z-index:2;pointer-events:none}
.qb-chip{position:absolute;z-index:4;width:56px;height:56px;border-radius:50%;background:#fff;display:grid;place-items:center;box-shadow:0 12px 28px rgba(20,48,110,.18);border:1px solid rgba(0,173,239,.18)}
.qb-chip svg{width:22px;height:22px}
.qb-chip-box{left:8%;bottom:30%}
.qb-chip-pin{right:10%;top:18%}
.track-band{position:relative;overflow:hidden;isolation:isolate;background:radial-gradient(920px 420px at 88% 18%,rgba(0,173,239,.16),transparent 58%),linear-gradient(180deg,#070b18 0%,#0a1024 58%,#070b18 100%);padding:108px 0 96px}
.track-band::before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent 0 72px,rgba(0,173,239,.035) 72px 73px),repeating-linear-gradient(0deg,transparent 0 72px,rgba(0,173,239,.03) 72px 73px);pointer-events:none;mask-image:linear-gradient(180deg,transparent,rgba(0,0,0,.9) 18%,rgba(0,0,0,.9) 82%,transparent);-webkit-mask-image:linear-gradient(180deg,transparent,rgba(0,0,0,.9) 18%,rgba(0,0,0,.9) 82%,transparent)}
.track-grid{position:relative;z-index:2;width:min(1280px,calc(100% - 40px));margin:0 auto;display:grid;grid-template-columns:minmax(280px,1fr) minmax(280px,.95fr);gap:28px 48px;align-items:center}
.track-copy{max-width:560px}
.track-kicker{display:inline-flex;align-items:center;gap:12px;margin:0 0 16px;font-family:var(--font);font-size:12px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:#00ADEF}
.track-kicker i{display:block;width:36px;height:2px;background:#00ADEF;border-radius:2px}
.track-title{margin:0 0 18px;font-size:clamp(36px,5vw,64px);line-height:.9;letter-spacing:-.05em;color:#fff;max-width:12ch}
.track-lede{margin:0 0 28px;max-width:40ch;font-size:16px;line-height:1.7;color:rgba(255,255,255,.72)}
.track-console{display:grid;gap:12px;padding:18px;border-radius:22px;background:rgba(255,255,255,.035);border:1px solid rgba(0,173,239,.22);box-shadow:inset 0 1px 0 rgba(255,255,255,.04)}
.track-console label{font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#00ADEF}
.track-row{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:stretch}
.track-row input{width:100%;min-width:0;padding:16px 18px;border-radius:14px;border:1px solid rgba(255,255,255,.16);background:rgba(7,11,24,.55);color:#fff;font-size:15px;outline:none;transition:border-color .25s,box-shadow .25s}
.track-row input::placeholder{color:rgba(255,255,255,.38)}
.track-row input:focus{border-color:var(--cyan);box-shadow:0 0 0 4px rgba(0,173,239,.16)}
.track-row .btn{white-space:nowrap;box-shadow:0 12px 28px rgba(0,173,239,.28)}
.track-note{min-height:1.4em;margin:4px 0 0;font-size:13px;color:rgba(255,255,255,.55)}
.track-open{display:inline-flex;margin-top:4px;align-self:start}
.track-radar{position:relative;min-height:460px;border-radius:28px;overflow:hidden;background:linear-gradient(160deg,rgba(18,28,68,.9),rgba(8,12,28,.96));border:1px solid rgba(0,173,239,.18);box-shadow:0 28px 64px rgba(0,0,0,.28)}
.track-radar-svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.track-radar-label{position:absolute;z-index:2;left:22px;top:22px;display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:999px;background:rgba(7,11,24,.55);border:1px solid rgba(0,173,239,.28);font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#fff}
.track-radar-label b{width:8px;height:8px;border-radius:50%;background:#00ADEF;box-shadow:0 0 0 5px rgba(0,173,239,.2)}
.track-stops{position:absolute;z-index:2;left:22px;right:22px;bottom:22px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.track-stops span{display:flex;flex-direction:column;gap:4px;padding:12px 12px 11px;border-radius:14px;background:rgba(7,11,24,.55);border:1px solid rgba(255,255,255,.08);font-family:var(--font)}
.track-stops strong{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#00ADEF}
.track-stops em{font-style:normal;font-size:13px;font-weight:600;color:rgba(255,255,255,.82)}
.track-route{fill:none;stroke:rgba(255,255,255,.22);stroke-width:2;stroke-dasharray:7 9;stroke-linecap:round}
.track-route-live{fill:none;stroke:#00ADEF;stroke-width:2.4;stroke-linecap:round;stroke-dasharray:420;stroke-dashoffset:420}
.track-node{fill:#070b18;stroke:#00ADEF;stroke-width:2}
.track-pulse{fill:rgba(0,173,239,.18);transform-origin:center;transform-box:fill-box}
.touch-band{position:relative;overflow:hidden;background:linear-gradient(180deg,#eaf6fc 0%,#dceef8 100%);padding:96px 0 0}
.touch-grid{width:min(1280px,calc(100% - 40px));margin:0 auto;display:grid;grid-template-columns:minmax(280px,.92fr) 1.08fr;gap:28px 40px;align-items:end;min-height:560px}
.touch-copy{position:relative;z-index:2;padding:0 0 64px}
.touch-kicker{display:inline-flex;align-items:center;gap:12px;margin:0 0 16px;font-family:var(--font);font-size:12px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:#00ADEF}
.touch-kicker i{display:block;width:36px;height:2px;background:#00ADEF;border-radius:2px}
.touch-title{margin:0 0 22px;font-size:clamp(48px,6.4vw,88px);line-height:.86;letter-spacing:-.055em;color:#1b2559}
.touch-addr{margin:0 0 28px;max-width:36ch;font-size:16px;line-height:1.7;color:#4a5568}
.touch-copy .btn{box-shadow:0 10px 24px rgba(46,49,146,.18)}
.touch-plate{position:relative;min-height:520px;border-radius:36px 36px 0 0;overflow:hidden;background:linear-gradient(160deg,#15205c 0%,#1a2468 48%,#10183f 100%);color:#fff;box-shadow:0 28px 56px rgba(18,42,84,.16)}
.touch-map{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.42;filter:invert(1) sepia(1) saturate(6) hue-rotate(166deg) brightness(.9);pointer-events:none}
.touch-plate::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,24,63,.15),rgba(16,24,63,.72) 70%);pointer-events:none}
.touch-pin{position:absolute;z-index:2;left:70%;top:22%;width:16px;height:16px;border-radius:50%;background:#00ADEF;box-shadow:0 0 0 10px rgba(0,173,239,.22),0 8px 18px rgba(0,173,239,.35)}
.touch-pin::after{content:"";position:absolute;left:50%;top:14px;width:2px;height:14px;background:#00ADEF;transform:translateX(-50%)}
.touch-lines{position:relative;z-index:3;display:flex;flex-direction:column;gap:0;padding:220px 28px 28px}
.touch-lines a{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:14px 0;border-top:1px solid rgba(255,255,255,.12);color:#fff;text-decoration:none}
.touch-lines a:hover b{color:#00ADEF}
.touch-lines a span{font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:#00ADEF}
.touch-lines a b{font-family:var(--font);font-size:15px;font-weight:600;letter-spacing:-.02em}
.touch-desks{position:relative;z-index:3;display:flex;gap:10px;padding:0 28px 28px;flex-wrap:wrap}
.touch-desks a{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid rgba(0,173,239,.28);color:#fff;font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.touch-desks a:hover{background:rgba(0,173,239,.18)}
.hero-film{height:100vh}
.hero-film-canvas{position:absolute;inset:0;width:100%;height:100%;display:block;background:#070b18}
.hero-film-scrim{position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(180deg,rgba(7,11,24,.4) 0%,rgba(7,11,24,.06) 32%,rgba(7,11,24,.16) 56%,rgba(7,11,24,.9) 100%)}
.hero-film-progress{position:absolute;left:0;bottom:0;height:3px;width:0;background:#00ADEF;z-index:3}
.hero-film .hero-copy{z-index:2;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(200px,.7fr);align-items:end;align-content:end;gap:24px 56px;width:min(1280px,calc(100% - 48px));height:100%;padding:0 0 56px;margin:0 auto}
.hero-film .hero-title-block{max-width:min(920px,100%)}
.hero-film .hero-lead{font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.34em;text-transform:uppercase;color:var(--cyan);margin:0 0 16px}
.hero-film h1{overflow:visible;font-size:clamp(48px,7.6vw,96px);max-width:14ch;line-height:.84;letter-spacing:-.055em}
.hero-film .hero-line{display:block;overflow:hidden}
.hero-film .hero-line>span{display:block}
.hero-film .hero-sub{margin:16px 0 0;font-family:var(--font-b);font-size:clamp(16px,1.7vw,21px);font-weight:400;letter-spacing:.02em;line-height:1.4;color:rgba(255,255,255,.9);text-transform:none;max-width:28ch;text-shadow:0 2px 18px rgba(7,11,24,.55)}
.hero-film .hero-actions{margin-top:26px}
.hero-film .hero-aside{justify-self:end;max-width:32ch;padding:0 0 8px 22px;border-left:2px solid #00ADEF}
.hero-film .hero-aside .lede{margin:0;font-size:15px;line-height:1.65;color:rgba(255,255,255,.92);max-width:none;text-shadow:0 2px 18px rgba(7,11,24,.65)}
.how-band{position:relative;overflow:hidden;isolation:isolate;background:radial-gradient(900px 420px at 86% 8%,rgba(0,173,239,.18),transparent 62%),linear-gradient(180deg,#eaf6fc 0%,#d8eef8 52%,#cfe8f5 100%);padding:92px 0 0}
.how-grid{width:min(1280px,calc(100% - 40px));margin:0 auto;display:grid;grid-template-columns:minmax(280px,.9fr) 1.2fr;gap:20px 36px;align-items:end;min-height:620px}
.how-copy{position:relative;z-index:2;padding:0 0 56px}
.how-kicker{display:inline-flex;align-items:center;gap:12px;margin:0 0 16px;font-family:var(--font);font-size:12px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:#00ADEF}
.how-kicker i{display:block;width:36px;height:2px;background:#00ADEF;border-radius:2px}
.how-title{margin:0 0 28px;font-size:clamp(46px,6.2vw,82px);line-height:.86;letter-spacing:-.055em}
.how-title span{display:block;color:transparent;-webkit-text-stroke:1.5px rgba(27,37,89,.28);paint-order:stroke fill;transition:color .35s ease,-webkit-text-stroke .35s ease}
.how-title span.is-on{color:#1b2559;-webkit-text-stroke:0}
.how-title span[data-step="1"].is-on{color:#00ADEF}
.how-log{list-style:none;display:flex;flex-direction:column;max-width:38ch;margin:0 0 28px}
.how-log li{display:grid;grid-template-columns:48px 1fr;gap:4px 12px;padding:14px 0;border-top:1px solid rgba(27,37,89,.12);opacity:.52;transition:opacity .35s ease}
.how-log li.is-on{opacity:1;transform:none}
.how-log b{grid-row:1/3;font-family:var(--font);font-size:26px;font-weight:800;color:#00ADEF;line-height:1;padding-top:2px}
.how-log h3{margin:0;font-family:var(--font);font-size:18px;font-weight:700;color:#1b2559;letter-spacing:-.02em}
.how-log p{margin:0;font-size:14px;line-height:1.5;color:#4a5568}
.how-copy .btn{box-shadow:0 10px 24px rgba(46,49,146,.18)}
.how-dock{position:relative;height:min(600px,76vh);min-height:500px;z-index:1}
.how-slab{position:absolute;inset:auto 0 0 auto;width:min(100%,760px);height:92%;border-radius:36px 36px 0 0;overflow:hidden;background:linear-gradient(180deg,rgba(255,255,255,.7),rgba(232,246,255,.2) 38%,rgba(210,232,246,.35)),repeating-linear-gradient(90deg,transparent 0 46px,rgba(0,173,239,.08) 46px 47px),repeating-linear-gradient(0deg,transparent 0 46px,rgba(0,173,239,.08) 46px 47px);box-shadow:0 28px 56px rgba(18,42,84,.14)}
.how-asphalt{position:absolute;left:-10%;right:-12%;bottom:22%;height:108px;background:linear-gradient(180deg,#243056,#151c38 55%,#10162c);transform:rotate(-4.5deg);box-shadow:0 18px 32px rgba(10,20,40,.28)}
.how-asphalt::after{content:"";position:absolute;inset:10px 0 auto;height:8px;background:repeating-linear-gradient(90deg,#00ADEF 0 18px,transparent 18px 34px);opacity:.35}
.how-fill{display:block;position:absolute;left:6%;top:50%;height:3px;width:78%;margin-top:-1px;background:#00ADEF;transform:scaleX(0);transform-origin:left center;will-change:transform;z-index:1}
.how-dash{display:block;position:absolute;left:6%;right:10%;top:50%;height:0;border-top:3px dashed rgba(255,255,255,.28);transform:translateY(-50%)}
.how-post{position:absolute;bottom:calc(22% + 86px);width:12px;height:54px;margin-left:-6px;background:#00ADEF;border-radius:3px 3px 0 0;box-shadow:0 8px 16px rgba(0,173,239,.28);z-index:2}
.how-post:nth-child(1){left:16%}
.how-post:nth-child(2){left:48%}
.how-post:nth-child(3){left:78%}
.how-post b{position:absolute;top:-30px;left:50%;transform:translateX(-50%);font-family:var(--font);font-size:13px;font-weight:800;color:#1b2559;letter-spacing:.04em}
.how-post.is-on{height:64px;background:#00ADEF}
.how-van-wrap{position:absolute;left:2%;bottom:10%;width:66%;max-width:580px;z-index:3;will-change:transform;pointer-events:none}
.how-van-wrap img{width:100%;height:auto;max-width:none;display:block;transform:rotate(-4.5deg);transform-origin:50% 92%;filter:drop-shadow(0 14px 12px rgba(10,24,48,.34))}
.how-flag{position:absolute;top:18px;right:18px;z-index:4;display:flex;align-items:center;gap:8px;padding:8px 12px 8px 10px;border-radius:999px;background:#fff;color:#1b2559;font-family:var(--font);font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;box-shadow:0 10px 24px rgba(20,40,80,.16)}
.how-flag i{width:8px;height:8px;border-radius:50%;background:#00ADEF;box-shadow:0 0 0 4px rgba(0,173,239,.2)}
@media(max-width:900px){
  .home-about{grid-template-columns:1fr}
  .hero-film-track{height:220vh}
  .story-band{border-radius:28px 28px 0 0}
  .story-copy{width:auto;margin:0;padding:72px 20px 24px}
  .story-visual{position:relative;width:100%;height:460px;bottom:auto}
  .story-slash{display:none}
  .story-truck{width:92%;left:4%;bottom:22%}
  .story-pills{left:16px;right:16px;max-width:none}
  .story-corner{width:140px;height:110px}
  .hero-film-scrim{background:linear-gradient(180deg,rgba(7,11,24,.58) 0%,rgba(7,11,24,.18) 26%,rgba(7,11,24,.42) 48%,rgba(7,11,24,.9) 72%,rgba(7,11,24,.96) 100%)}
  .hero-film .hero-copy{grid-template-columns:1fr;align-content:end;align-items:stretch;gap:18px;width:calc(100% - 40px);max-width:520px;margin:0 auto;padding:96px 0 max(24px,env(safe-area-inset-bottom,0px));box-sizing:border-box}
  .hero-film .hero-title-block{max-width:none}
  .hero-film .hero-lead{font-size:10px;letter-spacing:.2em;margin:0 0 10px}
  .hero-film h1{font-size:clamp(34px,10.5vw,48px);line-height:.9;letter-spacing:-.045em;max-width:12ch}
  .hero-film .hero-sub{margin:12px 0 0;font-size:15px;line-height:1.45;max-width:26ch}
  .hero-film .hero-actions{margin-top:18px;flex-direction:column;align-items:stretch;gap:10px;max-width:300px}
  .hero-film .hero-actions .btn{justify-content:center;width:100%;padding:14px 18px;font-size:11px;letter-spacing:.14em}
  .hero-film .hero-aside{justify-self:stretch;border-left:0;padding:14px 0 0;margin:2px 0 0;max-width:none;border-top:1px solid rgba(0,173,239,.4)}
  .hero-film .hero-aside .lede{font-size:13.5px;line-height:1.55;color:rgba(255,255,255,.86);text-shadow:0 2px 14px rgba(7,11,24,.7)}
  .how-grid{grid-template-columns:1fr;min-height:0}
  .how-copy{padding:0 0 8px}
  .how-title{font-size:clamp(42px,12vw,64px)}
  .how-dock{height:420px;min-height:400px}
  .how-slab{width:100%;height:100%;border-radius:28px 28px 0 0}
  .how-van-wrap{width:84%;max-width:none;bottom:8%;left:-2%}
  .how-asphalt{bottom:18%;height:86px}
  .touch-grid{grid-template-columns:1fr;min-height:0;gap:8px}
  .touch-copy{padding:0 0 12px}
  .touch-plate{min-height:400px;border-radius:28px 28px 0 0}
  .touch-lines{padding-top:92px}
  .touch-pin{left:78%;top:14%}
  .touch-lines a{flex-direction:column;align-items:flex-start;gap:4px}
  .qb-light{clip-path:inset(38% 0 0 0)}
  .qb-layout{grid-template-columns:1fr;padding:88px 4px 0;min-height:0;gap:0}
  .qb-copy{padding:0 8px 12px;max-width:none;z-index:3}
  .qb-title{max-width:none}
  .qb-title .qb-line{white-space:normal}
  .qb-visual{height:520px;min-height:500px;margin-right:0}
  .qb-flight{left:18px;bottom:auto;top:auto;position:relative;width:min(88vw,340px);height:90px;margin:8px 0 0}
  .qb-globe{width:90vw;opacity:.4;bottom:-8%;left:-18%}
  .qb-courier{height:92%;left:52%}
  .track-band{padding:84px 0 72px}
  .track-grid{grid-template-columns:1fr;gap:22px}
  .track-title{max-width:none}
  .track-row{grid-template-columns:1fr}
  .track-radar{min-height:360px}
  .track-stops{grid-template-columns:1fr;gap:8px}
  .vas-shell{grid-template-columns:1fr;min-height:0;gap:12px}
  .vas-copy{padding:0 0 12px;max-width:none}
  .vas-stage{min-height:520px;border-radius:28px 28px 0 0}
  .vas-index{min-height:520px;padding:36px 20px 22px;max-width:none}
}
@media(max-width:720px){
  .hero-film .hero-copy{width:calc(100% - 36px);gap:16px;padding:88px 0 max(20px,env(safe-area-inset-bottom,0px))}
  .hero-film .hero-lead{letter-spacing:.16em}
  .hero-film h1{font-size:clamp(32px,9.8vw,42px);max-width:11ch}
  .hero-film .hero-sub{font-size:14px;max-width:22ch}
  .hero-film .hero-actions{max-width:none}
  .hero-film .hero-aside .lede{font-size:13px;line-height:1.5}
}
'''

home = r'''
<div class="hero-stack">
<section class="hero hero-film">
  <canvas id="heroFrames" class="hero-film-canvas" data-frames="192" data-src="assets/images/hero-frames/frame-" width="1280" height="720" aria-hidden="true"></canvas>
  <div class="hero-film-scrim"></div>
  <div class="hero-film-progress" aria-hidden="true"></div>
  <div class="intro-line"></div>
  <div class="hero-copy">
    <div class="hero-title-block">
      <p class="hero-lead">IMEX Clearing & Logistics</p>
      <h1 class="display">
        <span class="hero-line"><span>Your one stop</span></span>
        <span class="hero-line"><span>solution</span></span>
      </h1>
      <p class="hero-sub">for all your import export needs</p>
      <div class="hero-actions">
        <a class="btn btn-cyan magnetic" href="quote.html" data-vt="zoom">Request a Quote <span class="arr">→</span></a>
        <a class="btn btn-ghost magnetic" href="services.html" data-vt="wipe">Explore services</a>
      </div>
    </div>
    <aside class="hero-aside">
      <p class="lede">Kanpur’s international freight forwarder and consolidator — sea, air, customs and licensing, from a single coordinated desk.</p>
    </aside>
  </div>
</section>
<div class="hero-film-track" aria-hidden="true"></div>
<section class="story-band" data-story-band>
  <div class="story-copy">
    <p class="story-year">1994</p>
    <h2 class="display story-title"><i class="story-mark" aria-hidden="true"></i>The story behind<br><span>every shipment</span></h2>
    <i class="story-rule" aria-hidden="true"></i>
    <p class="lede">Imex Clearing & Logistics Private Limited is one of Kanpur’s leading International freight forwarder and consolidator, specializing in multi-modal shipments from/to India. We provide the complete ambit of logistic services. The CONTAINER CORPORATION OF INDIA LIMITED for our outstanding performance in this field has awarded us for third time in a row.</p>
    <p class="lede">Being established in 1994, Foundation of “Imex Clearing” was the ultimate realization of the dream of Mr. Suresh Kumar Mishra. Who initially started air freights and custom clearance business to many challenging destinations all over the world. He made this challenge his specialty and later diversified and created a distinct brand image.</p>
    <div class="story-actions">
      <a class="btn btn-cyan magnetic" href="about.html" data-vt="frag">Explore Our Company <span class="arr">→</span></a>
      <a class="story-play" href="about.html" data-vt="frag"><i aria-hidden="true"><svg viewBox="0 0 12 12" fill="#00ADEF"><path d="M2 1.2v9.6L11 6z"/></svg></i> Our Journey</a>
    </div>
  </div>
  <div class="story-visual">
    <img class="story-yard" src="assets/images/hero-frames/frame-012.jpg" alt="" width="1280" height="720">
    <svg class="story-slash" viewBox="0 0 280 800" preserveAspectRatio="none" aria-hidden="true"><path fill="#f4f8fd" d="M280 0C150 240 130 520 0 800H0V0Z"/></svg>
    <img class="story-truck" src="assets/images/block/about-img.png" alt="IMEX logistics vehicle" width="580" height="404">
    <div class="story-pills">
      <div class="story-pill">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3.5" y="5" width="17" height="16" rx="2" stroke="#00ADEF" stroke-width="1.7"/><path d="M3.5 10h17M8 3.5v3M16 3.5v3" stroke="#00ADEF" stroke-width="1.7" stroke-linecap="round"/></svg>
        <span><b>Established in</b><strong>1994</strong></span>
      </div>
      <div class="story-pill">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6.5 9.5 12 4l5.5 5.5v2.2c0 3.6-2.3 6.3-5.5 8.3-3.2-2-5.5-4.7-5.5-8.3V9.5Z" stroke="#00ADEF" stroke-width="1.7" stroke-linejoin="round"/><path d="m9 12.2 2 2 4-4" stroke="#00ADEF" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span><b>Awarded by</b><strong>CONTAINER CORPORATION OF INDIA LIMITED</strong></span>
      </div>
    </div>
    <div class="story-corner" aria-hidden="true">
      <svg viewBox="0 0 160 160"><ellipse cx="110" cy="110" rx="70" ry="70" fill="none" stroke="#fff" stroke-width="1.2"/><ellipse cx="110" cy="110" rx="42" ry="70" fill="none" stroke="#fff" stroke-width="1"/><ellipse cx="110" cy="110" rx="70" ry="22" fill="none" stroke="#fff" stroke-width="1"/></svg>
    </div>
  </div>
</section>
</div>

<section class="section globe-band" data-globe-band>
  <div class="globe-band-grid">
    <div class="globe-copy">
      <p class="kicker">Partners across oceans</p>
      <h2 class="display">A global network of partners</h2>
      <p class="lede">With a global network of partners, Imex Clearing provides seamless shipping world over. Imex Clearing offers centralized customer services for international transport, logistics and supply chain management to enhance the productivity of your enterprise.</p>
    </div>
    <div class="scene-frame globe-frame">
      <canvas data-scene="globe" data-globe-scroll="1"></canvas>
    </div>
  </div>
</section>

<section class="rail-pin">
  <div class="rail">
''' + "".join(f'''
    <article class="rail-panel">
      <div class="rail-copy">
        <p class="kicker">0{i+1} / 07</p>
        <h3 class="display">{t}</h3>
        <p class="lede" style="margin:16px 0 24px">{d}</p>
        <a class="btn btn-cyan" href="{h}" data-vt="zoom">Explore Service <span class="arr">→</span></a>
      </div>
      <div class="rail-visual">
        <img src="{SERVICE_IMGS[h]}" alt="{t}">
      </div>
    </article>
''' for i,(h,t,d) in enumerate(SERVICES)) + '''
    <article class="rail-panel rail-end">
      <div class="rail-copy">
        <p class="kicker">The full list</p>
        <h3 class="display">Seven ways to move cargo</h3>
        <a class="btn btn-ghost" href="services.html" data-vt="wipe" style="margin-top:24px">Explore All Services <span class="arr">→</span></a>
      </div>
    </article>
  </div>
</section>

<section class="how-band" data-how-band>
  <div class="how-grid">
    <div class="how-copy">
      <p class="how-kicker"><i aria-hidden="true"></i> How it works</p>
      <h2 class="display how-title">
        <span data-step="0">Order.</span>
        <span data-step="1">Wait.</span>
        <span data-step="2">Deliver.</span>
      </h2>
      <ol class="how-log">
        <li data-step="0">
          <b>01</b>
          <h3>Order</h3>
          <p>Fill the form and submit your details</p>
        </li>
        <li data-step="1">
          <b>02</b>
          <h3>Wait</h3>
          <p>Wait while we process your details and contact you</p>
        </li>
        <li data-step="2">
          <b>03</b>
          <h3>Deliver</h3>
          <p>You confirm and we deliver your order</p>
        </li>
      </ol>
      <a class="btn btn-navy magnetic" href="quote.html" data-vt="zoom">Request a Quote <span class="arr">→</span></a>
    </div>
    <div class="how-dock" aria-hidden="true">
      <div class="how-slab">
        <div class="how-post"><b>01</b></div>
        <div class="how-post"><b>02</b></div>
        <div class="how-post"><b>03</b></div>
        <div class="how-asphalt">
          <i class="how-dash"></i>
          <i class="how-fill"></i>
        </div>
        <div class="how-van-wrap">
          <img src="assets/images/block/how-van.png" alt="IMEX delivery van" width="991" height="486" loading="lazy">
        </div>
        <span class="how-flag"><i></i> Destination</span>
      </div>
    </div>
  </div>
</section>

<section class="vas-band" data-vas-band>
  <div class="vas-shell">
    <div class="vas-copy">
      <p class="vas-kicker"><i aria-hidden="true"></i> Beyond transportation</p>
      <h2 class="display vas-title">Value added services</h2>
      <p class="vas-lede">Trade tools, container references, terms and useful government links published on IMEX.</p>
      <a class="btn btn-navy magnetic" href="value-added-services.html" data-vt="frag">Discover More <span class="arr">→</span></a>
    </div>
    <aside class="vas-stage">
      <div class="vas-media" aria-hidden="true">
        <img class="is-on" src="assets/images/links/stock-containers-alt.jpg" alt="" width="1600" height="1067" data-vas-img="0">
        <img src="assets/images/links/stock-incoterms.jpg" alt="" width="1600" height="1067" data-vas-img="1" loading="lazy">
        <img src="assets/images/links/stock-cargo.jpg" alt="" width="1200" height="1800" data-vas-img="2" loading="lazy">
      </div>
      <nav class="vas-index" aria-label="Value added services">
        <a href="value-added-services.html" data-vt="frag" data-vas-i="0" class="is-on"><i aria-hidden="true"></i><strong>Containers &amp; ULDs</strong><em>Reference</em></a>
        <a href="value-added-services.html" data-vt="frag" data-vas-i="1"><i aria-hidden="true"></i><strong>INCO Terms</strong><em>Contracts</em></a>
        <a href="value-added-services.html" data-vt="frag" data-vas-i="2"><i aria-hidden="true"></i><strong>Cargo Classifications</strong><em>Handling</em></a>
        <div class="vas-more">
          <a href="value-added-services.html" data-vt="frag">Charting Terms</a>
          <a href="value-added-services.html" data-vt="frag">International Trade Terms</a>
          <a href="https://www.xe.com/currencyconverter/" target="_blank" rel="noopener">Currency Converter</a>
        </div>
      </nav>
    </aside>
  </div>
</section>

<section class="quote-band" data-quote-band>
  <svg class="qb-light" viewBox="0 0 1440 760" preserveAspectRatio="none" aria-hidden="true">
    <defs>
      <linearGradient id="qbLg" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#e7f6ff"/>
        <stop offset=".42" stop-color="#c8ebff"/>
        <stop offset="1" stop-color="#dff4ff"/>
      </linearGradient>
    </defs>
    <path fill="url(#qbLg)" d="M760,-40 C640,160 860,340 560,780 L1520,780 L1520,-40 Z"/>
    <path fill="rgba(255,255,255,.22)" d="M1020,20 C1180,120 1320,50 1440,190 C1520,300 1440,470 1260,560 C1100,640 980,620 780,780 L1520,780 L1520,0 Z"/>
    <path fill="none" stroke="rgba(255,255,255,.5)" stroke-width="28" d="M1080,70 C1220,200 1380,150 1460,330"/>
  </svg>
  <div class="qb-blobs" aria-hidden="true">
    <span class="qb-blob qb-blob-a"></span>
    <span class="qb-blob qb-blob-b"></span>
    <span class="qb-blob qb-blob-c"></span>
  </div>
  <svg class="qb-globe" viewBox="0 0 520 360" aria-hidden="true">
    <defs>
      <radialGradient id="qbGlow" cx="50%" cy="70%" r="70%">
        <stop offset="0" stop-color="rgba(0,173,239,.32)"/>
        <stop offset="1" stop-color="rgba(0,173,239,0)"/>
      </radialGradient>
    </defs>
    <g class="qb-globe-spin">
      <circle cx="260" cy="300" r="250" fill="url(#qbGlow)"/>
      <ellipse cx="260" cy="300" rx="250" ry="250" fill="none" stroke="rgba(120,214,255,.78)" stroke-width="1.8"/>
      <ellipse cx="260" cy="300" rx="170" ry="250" fill="none" stroke="rgba(120,214,255,.48)" stroke-width="1.3"/>
      <ellipse cx="260" cy="300" rx="82" ry="250" fill="none" stroke="rgba(120,214,255,.48)" stroke-width="1.3"/>
      <line x1="10" y1="300" x2="510" y2="300" stroke="rgba(120,214,255,.42)" stroke-width="1.3"/>
      <ellipse cx="260" cy="228" rx="232" ry="56" fill="none" stroke="rgba(120,214,255,.5)" stroke-width="1.3"/>
      <ellipse cx="260" cy="164" rx="196" ry="40" fill="none" stroke="rgba(120,214,255,.42)" stroke-width="1.2"/>
      <ellipse cx="260" cy="108" rx="140" ry="24" fill="none" stroke="rgba(120,214,255,.38)" stroke-width="1.2"/>
    </g>
  </svg>
  <div class="qb-layout">
    <div class="qb-copy">
      <p class="qb-kicker"><i aria-hidden="true"></i> Enquiry</p>
      <h2 class="display qb-title"><span class="qb-line">Send us your</span><br>query</h2>
      <p class="lede qb-lede">Please fill in your details so that we can contact and update you about your query.</p>
      <a class="btn btn-cyan magnetic qb-cta" href="quote.html" data-vt="zoom">Request a Quote <span class="arr">→</span></a>
    </div>
    <svg class="qb-flight" viewBox="0 0 420 160" aria-hidden="true">
      <path class="qb-dash" d="M8,118 C70,108 110,42 188,38 C268,34 330,88 408,52"/>
      <g class="qb-plane">
        <path d="M0 7 L30 0 L13 11 L15 20 L20 11 Z" fill="#fff"/>
        <path d="M13 11 L15 20" stroke="rgba(180,210,230,.9)" stroke-width="1"/>
      </g>
    </svg>
    <div class="qb-visual">
      <div class="qb-frame">
        <img class="qb-yard" src="assets/images/hero-frames/frame-165.jpg" alt="" width="1280" height="720">
      </div>
      <svg class="qb-orbit" viewBox="0 0 500 500" aria-hidden="true">
        <ellipse class="qb-ring" cx="250" cy="258" rx="214" ry="90" transform="rotate(-18 250 258)"/>
        <ellipse class="qb-ring qb-ring-2" cx="250" cy="258" rx="188" ry="76" transform="rotate(14 250 258)"/>
      </svg>
      <i class="qb-ground" aria-hidden="true"></i>
      <img class="qb-courier" src="assets/images/block/Courier-Man.png" alt="Courier delivery representative" width="520" height="720">
      <span class="qb-chip qb-chip-box" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none"><rect x="4" y="7" width="16" height="12" rx="1.6" stroke="#00ADEF" stroke-width="1.8"/><path d="M4 10h16M12 7V5m-3 2 3-3 3 3" stroke="#00ADEF" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <span class="qb-chip qb-chip-pin" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none"><path d="M12 21s7-6.2 7-11.2A7 7 0 0 0 5 9.8C5 14.8 12 21 12 21Z" stroke="#00ADEF" stroke-width="1.8"/><circle cx="12" cy="9.8" r="2.2" stroke="#00ADEF" stroke-width="1.8"/></svg>
      </span>
    </div>
  </div>
</section>

<section class="track-band" data-track-band>
  <div class="track-grid">
    <div class="track-copy">
      <p class="track-kicker"><i aria-hidden="true"></i> Track &amp; Trace</p>
      <h2 class="display track-title">Now you can track your product easily</h2>
      <p class="track-lede">Use the original Track &amp; Trace destination used by IMEX. This page does not invent shipment status.</p>
      <form id="trackForm" class="track-console">
        <label for="awb">Tracking number</label>
        <div class="track-row">
          <input id="awb" name="awb" type="text" placeholder="Enter AWB / container / bill of lading" autocomplete="off">
          <button class="btn btn-cyan magnetic" type="submit">Track Your Shipment <span class="arr">→</span></button>
        </div>
        <p id="trackNote" class="track-note" role="status"></p>
        <a class="btn btn-ghost track-open" href="tracking.html" data-vt="route">Open tracking page <span class="arr">→</span></a>
      </form>
    </div>
    <aside class="track-radar" aria-hidden="true">
      <span class="track-radar-label"><b></b> Route board</span>
      <svg class="track-radar-svg" viewBox="0 0 640 520" preserveAspectRatio="xMidYMid slice">
        <defs>
          <radialGradient id="trackGlow" cx="50%" cy="42%" r="55%">
            <stop offset="0%" stop-color="rgba(0,173,239,.22)"/>
            <stop offset="100%" stop-color="rgba(0,173,239,0)"/>
          </radialGradient>
        </defs>
        <rect width="640" height="520" fill="url(#trackGlow)"/>
        <ellipse class="track-pulse" cx="320" cy="210" rx="210" ry="210" fill="none" stroke="rgba(0,173,239,.18)" stroke-width="1.2"/>
        <ellipse class="track-pulse" cx="320" cy="210" rx="150" ry="150" fill="none" stroke="rgba(0,173,239,.22)" stroke-width="1.2"/>
        <ellipse class="track-pulse" cx="320" cy="210" rx="90" ry="90" fill="none" stroke="rgba(0,173,239,.3)" stroke-width="1.4"/>
        <path class="track-route" d="M78 380 C160 300 210 250 280 220 C360 180 430 150 560 120"/>
        <path class="track-route-live" d="M78 380 C160 300 210 250 280 220 C360 180 430 150 560 120"/>
        <circle class="track-node" cx="78" cy="380" r="7"/>
        <circle class="track-node" cx="280" cy="220" r="7"/>
        <circle class="track-node" cx="560" cy="120" r="8"/>
        <g class="track-plane" transform="translate(280 220)">
          <path d="M0 0 L26 -6 L12 8 L14 16 L20 8 Z" fill="#fff"/>
        </g>
      </svg>
      <div class="track-stops">
        <span><strong>01</strong><em>Origin</em></span>
        <span><strong>02</strong><em>Route</em></span>
        <span><strong>03</strong><em>Portal</em></span>
      </div>
    </aside>
  </div>
</section>

<section class="touch-band" data-touch-band>
  <div class="touch-grid">
    <div class="touch-copy">
      <p class="touch-kicker"><i aria-hidden="true"></i> Kanpur</p>
      <h2 class="display touch-title">Get in<br>touch</h2>
      <p class="touch-addr">No. 16, 1st Floor, Harmony Arcade<br>17/1, Telegraph Road, The Mall<br>Kanpur - 208001</p>
      <a class="btn btn-navy magnetic" href="contact.html" data-vt="wipe">Contact Us <span class="arr">→</span></a>
    </div>
    <aside class="touch-plate">
      <img class="touch-map" src="assets/images/background/contact-map.png" alt="" width="1200" height="720">
      <span class="touch-pin" aria-hidden="true"></span>
      <div class="touch-lines">
        <a href="tel:+915122391885"><span>Tel</span><b>+91 512-2391885</b></a>
        <a href="tel:+919335347057"><span>Mobile</span><b>+91 933 534 7057</b></a>
        <a href="mailto:sayyam7@imexclearing.com"><span>Email</span><b>sayyam7@imexclearing.com</b></a>
      </div>
      <div class="touch-desks">
        <a href="mailto:imports@imexclearing.com">Imports desk</a>
        <a href="mailto:exports@imexclearing.com">Exports desk</a>
      </div>
    </aside>
  </div>
</section>
'''

about_css = '''
.about-hero{min-height:100vh;display:grid;grid-template-columns:1.2fr .8fr}
.about-hero .copy{display:flex;flex-direction:column;justify-content:flex-end;padding:140px 8vw 80px}
.timeline{display:flex;gap:48px;overflow:hidden}
.time-card{flex:0 0 70%;padding:48px;border-left:2px solid var(--cyan)}
.values{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.values article{padding:32px;border:1px solid var(--line);border-radius:20px;min-height:240px}
.about-cta{position:relative;min-height:70vh;display:flex;align-items:flex-end;overflow:hidden;padding:0}
.about-cta .about-cta-media{position:absolute;inset:0}
.about-cta .about-cta-media img{width:100%;height:100%;object-fit:cover;object-position:center 40%;transform:scale(1.04)}
.about-cta .overlay-scrim{z-index:1;background:linear-gradient(105deg,rgba(7,11,24,.86) 0%,rgba(7,11,24,.48) 52%,rgba(7,11,24,.7) 100%),linear-gradient(180deg,rgba(7,11,24,.15) 0%,rgba(7,11,24,.82) 100%)}
.about-cta .wrap{position:relative;z-index:2;padding:120px 0}
@media(max-width:900px){.about-hero,.values{grid-template-columns:1fr}.about-hero{min-height:auto}.about-cta{min-height:56vh}}
'''
about = r'''
<section class="about-hero light">
  <div class="copy">
    <p class="kicker ink">Company</p>
    <h1 class="display ink" data-split>About IMEX</h1>
    <p class="lede" style="margin-top:20px">The story behind every shipment — a Kanpur forwarder built on air freight, customs clearance, and a distinct brand image.</p>
  </div>
  <div class="img-clip">
    <img src="assets/images/background/banner-1.jpg" alt="Ship, truck and aircraft — IMEX multimodal logistics" data-parallax="-14">
    <div class="overlay-scrim"></div>
  </div>
</section>
<section class="section light">
  <div class="wrap" style="display:grid;grid-template-columns:.8fr 1.2fr;gap:48px">
    <div class="year-mask" style="font-size:clamp(80px,14vw,180px);color:transparent;-webkit-text-stroke:1px #2E3192">1994</div>
    <div>
      <h2 class="display ink" style="font-size:clamp(32px,4vw,56px)">Company introduction</h2>
      <p class="lede" data-reveal>Imex Clearing & Logistics Private Limited is one of Kanpur’s leading International freight forwarder and consolidator, specializing in multi-modal shipments from/to India. We provide the complete ambit of logistic services.</p>
    </div>
  </div>
</section>
<section class="section" style="background:var(--deep-2)">
  <div class="wrap">
    <p class="kicker">History</p>
    <h2 class="display" style="margin-bottom:32px">From a founder’s specialty to a full logistics house</h2>
    <div class="timeline">
      <article class="time-card" data-reveal>
        <p class="kicker">1994</p>
        <h3 class="display" style="font-size:36px;margin:10px 0">Foundation</h3>
        <p>Being established in 1994, Foundation of “Imex Clearing” was the ultimate realization of the dream of Mr. Suresh Kumar Mishra. Who initially started air freights and custom clearance business to many challenging destinations all over the world. He made this challenge his specialty and later diversified and created a distinct brand image.</p>
      </article>
      <article class="time-card" data-reveal>
        <p class="kicker">What we do</p>
        <h3 class="display" style="font-size:36px;margin:10px 0">The complete ambit</h3>
        <ul style="line-height:2">
          <li>Sea Freight</li><li>Outbound LCL Consolidation</li><li>Inbound LCL Consolidation</li>
          <li>Buyer Consolidation</li><li>Global FCL Forwarding</li><li>Air Freight</li>
          <li>Custom Clearance</li><li>DGFT / Licensing Works</li>
        </ul>
      </article>
    </div>
  </div>
</section>
<section class="section light">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center">
    <div>
      <p class="kicker ink">Achievement</p>
      <h2 class="display ink" style="font-size:clamp(32px,4vw,56px)">CONTAINER CORPORATION OF INDIA LIMITED</h2>
      <p class="lede" data-reveal>The CONTAINER CORPORATION OF INDIA LIMITED for our outstanding performance in this field has awarded us for third time in a row.</p>
    </div>
    <img src="assets/images/block/delivery.png" alt="IMEX Clearing fast product delivery services worldwide" loading="lazy">
  </div>
</section>
<section class="section paper">
  <div class="wrap">
    <p class="kicker ink">How we work</p>
    <h2 class="display ink" style="margin-bottom:28px">Statements from the company</h2>
    <div class="values">
      <article data-reveal><h3 class="display ink" style="font-size:28px">Fast delivery</h3><p>Proven track record of fast delivery</p></article>
      <article data-reveal><h3 class="display ink" style="font-size:28px">Secured service</h3><p>Stay secured be assured</p></article>
      <article data-reveal><h3 class="display ink" style="font-size:28px">Worldwide shipping</h3><p>Providing transportation services worldwide</p></article>
    </div>
    <p class="lede" style="margin-top:36px" data-reveal>Imex Clearing is specializes in providing fully integrated logistics solutions world-wide. All the functions are specially designed to ensure the rapid and safe transit of goods. Imex Clearing services are targeted at optimizing logistical operations.</p>
  </div>
</section>
<section class="section about-cta">
  <div class="about-cta-media">
    <img src="assets/images/links/stock-containers.jpg" alt="Shipping containers ready for movement" width="1600" height="1067" loading="lazy">
  </div>
  <div class="overlay-scrim"></div>
  <div class="wrap">
    <h2 class="display" style="font-size:clamp(36px,6vw,80px)">Ready for the next movement?</h2>
    <a class="btn btn-cyan magnetic" href="services.html" data-vt="wipe" style="margin-top:24px">Explore Our Services <span class="arr">→</span></a>
  </div>
</section>
'''

services_css = '''
.svc-hero{min-height:78vh}
.svc-hero .hero-canvas{overflow:hidden}
.svc-hero .hero-canvas img{width:100%;height:100%;object-fit:cover;object-position:center 48%;transform:scale(1.06)}
.svc-hero .overlay-scrim{z-index:1;background:linear-gradient(105deg,rgba(7,11,24,.82) 0%,rgba(7,11,24,.45) 48%,rgba(7,11,24,.62) 100%),linear-gradient(180deg,rgba(7,11,24,.2) 0%,rgba(7,11,24,.78) 100%)}
.svc-hero .hero-copy{z-index:2;max-width:min(1240px,calc(100% - 40px))}
.svc-block{min-height:100vh;display:grid;grid-template-columns:1.1fr .9fr;align-items:stretch}
.svc-block:nth-child(even){grid-template-columns:.9fr 1.1fr}
.svc-block:nth-child(even) .copy{order:2}
.svc-block .copy{padding:120px 8vw;display:flex;flex-direction:column;justify-content:center}
.svc-block .svc-visual{position:relative;min-height:420px;overflow:hidden}
.svc-block .svc-visual img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.svc-block:nth-child(3n){grid-template-columns:1fr;min-height:80vh}
@media(max-width:900px){.svc-block,.svc-block:nth-child(even){grid-template-columns:1fr;min-height:auto}.svc-block .svc-visual{min-height:320px}}
'''
svc_blocks = ""
for i,(h,t,d) in enumerate(SERVICES):
    img = SERVICE_IMGS[h]
    svc_blocks += f'''
<section class="svc-block {'light' if i%2==0 else ''}">
  <div class="copy">
    <p class="kicker">0{i+1} / 07</p>
    <h2 class="display {'ink' if i%2==0 else ''}" style="font-size:clamp(36px,6vw,84px)">{t}</h2>
    <p class="lede" style="margin:18px 0 28px">{d}</p>
    <a class="btn {'btn-navy' if i%2==0 else 'btn-cyan'} magnetic" href="{h}" data-vt="zoom">Explore More <span class="arr">→</span></a>
  </div>
  <div class="svc-visual">
    <img src="{img}" alt="{t}" loading="lazy">
  </div>
</section>
'''

services_page = f'''
<section class="hero svc-hero">
  <div class="hero-canvas">
    <img src="assets/images/background/banner-1.jpg" alt="Ship, truck and aircraft — IMEX multimodal logistics" width="1920" height="1080">
  </div>
  <div class="overlay-scrim"></div>
  <div class="hero-copy">
    <p class="kicker">Directory</p>
    <h1 class="display" data-split>Seven ways to move the world</h1>
    <p class="lede" style="margin-top:18px">Sea, air, consolidation, customs and licensing — each capability has its own page and original IMEX photograph.</p>
  </div>
</section>
{svc_blocks}
'''

def service_page(slug, title, kicker, scene, img, copy_html, extra="", layout="split"):
    if layout == "stack":
        main = f'''
<section class="section light">
  <div class="wrap">
    <p class="kicker ink">Service</p>
    <h2 class="display ink" style="font-size:clamp(40px,7vw,96px);max-width:16ch">{title}</h2>
    <div class="img-clip" style="min-height:52vh;margin:32px 0">
      <img src="{img}" alt="{title} — original IMEX photograph" loading="lazy">
    </div>
    <div style="max-width:72ch">{copy_html}
      <a class="btn btn-navy magnetic" href="quote.html" data-vt="zoom" style="margin-top:28px">Request a Quote <span class="arr">→</span></a>
    </div>
  </div>
</section>'''
    elif layout == "overlap":
        main = f'''
<section class="section" style="background:var(--deep-2)">
  <div class="wrap" style="position:relative">
    <div class="img-clip" style="min-height:70vh">
      <img src="{img}" alt="{title} — original IMEX photograph" loading="lazy">
    </div>
    <div style="background:#fff;color:var(--ink);padding:48px;border-radius:24px;margin-top:-120px;position:relative;max-width:720px">
      {copy_html}
      <a class="btn btn-navy magnetic" href="quote.html" data-vt="zoom" style="margin-top:28px">Request a Quote <span class="arr">→</span></a>
    </div>
  </div>
</section>'''
    elif layout == "columns":
        main = f'''
<section class="section light">
  <div class="wrap" style="display:grid;grid-template-columns:.7fr 1.3fr;gap:32px">
    <div class="img-clip" style="min-height:80vh">
      <img src="{img}" alt="{title} — original IMEX photograph" loading="lazy">
    </div>
    <div style="padding-top:40px">{copy_html}
      <a class="btn btn-navy magnetic" href="quote.html" data-vt="zoom" style="margin-top:28px">Request a Quote <span class="arr">→</span></a>
    </div>
  </div>
</section>'''
    else:
        main = f'''
<section class="section light">
  <div class="wrap" style="display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center">
    <div>
      <p class="kicker ink">Service</p>
      <h2 class="display ink" style="font-size:clamp(28px,4vw,48px);margin:8px 0 18px">{title}</h2>
      {copy_html}
      <a class="btn btn-navy magnetic" href="quote.html" data-vt="zoom" style="margin-top:28px">Request a Quote <span class="arr">→</span></a>
    </div>
    <div class="img-clip" style="min-height:380px">
      <img src="{img}" alt="{title} — original IMEX photograph" loading="lazy">
    </div>
  </div>
</section>'''
    return f'''
<section class="hero">
  <canvas id="scene" class="hero-canvas" data-scene="{scene}"></canvas>
  <div class="webgl-fallback"></div>
  <div class="hero-copy">
    <p class="kicker">{kicker}</p>
    <h1 class="display" data-split>{title}</h1>
  </div>
</section>
{main}
{extra}
{related(slug)}
'''

sea = service_page("sea-freight.html","Sea Freight","The ocean cargo experience","ocean","assets/images/background/banner_s.jpg",
'''<p class="lede">Imex Clearing & Logistics Private Limited offers complete sea freight solutions both for import and export. The company provides a wide range of services that include inbound, outbound ocean freight solutions, FCL/LCL cross trade and door-to-door delivery. Whether the requirement is consolidation, group page or full container load, our expert professionals are fully equipped to handle the job with a variety of options at the most competitive and reliable terms. We customize operations and handling services to match any specific requirement of door to door or port to port services.</p>''', extra='''<section class="section"><div class="wrap"><p class="kicker">Modes</p><h2 class="display" style="font-size:clamp(32px,5vw,64px)">Door to door or port to port</h2><p class="lede" style="margin-top:16px">Inbound, outbound, FCL/LCL cross trade and consolidation — the ocean surface of this page is procedural; the ship photograph is the original IMEX sea freight image.</p></div></section>''', layout="stack")

lcl = service_page("lcl-consolidation.html","Inbound/Outbound LCL Consolidation","Multiple shipments, one journey","packages","assets/images/background/banner_olc.jpg",
'''<p class="lede">Imex Clearing & Logistics Private Limited offers LCL consolidation services from all Indian ports and hinterland ICDs to worldwide destinations. The destinations covered are comprehensive and to name a few, we offer weekly consoles to Felixstowe/ Thames Port, Antwerp, Rotterdam, Hamburg, Le Havre, Marseilles, Barcelona, Durban, Dubai/Jebel Ali, Colombo, Singapore, New York, Los Angeles etc. In addition destinations are also served via trans-shipment hubs.</p>
<p class="lede" style="margin-top:16px">At Imex Clearing & Logistics Private Limited, we offer import LCL consolidation from worldwide origins. It is our Endeavour to offer fixed day direct sailings from majority of origins. We strive to maintain time bound and cost effective deliveries. Our overseas associates are carefully chosen after ensuring that they share the same philosophy. Our services and ex works charges are most competitive and are unmatched in the industry.</p>''', extra="", layout="overlap")

buyer = service_page("buyer-consolidation.html","Buyer Consolidation","Intelligent cargo assembly","buyer","assets/images/background/banner-1.jpg",
'''<p class="lede">Imex clearing & Logistics Private Limited core activity and capability is buyer’s consolidation, a cost effective and efficient solution for customers, who have multiple vendors and regularly order / purchase goods from a specific region or country. In addition, we provide vendor management, Inland movement, Ware-housing, direct deliveries to retail outlets, itemized deliveries and distribution. We are well connected globally to serve the customer by giving real time information on the product as it travels through the supply chain. We also have EDI transfers that can be tailor made to suit your information requirements.</p>''', extra='''<section class="section light"><div class="wrap" style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px"><article data-reveal><h3 class="display ink" style="font-size:22px">Vendor management</h3></article><article data-reveal><h3 class="display ink" style="font-size:22px">Inland movement</h3></article><article data-reveal><h3 class="display ink" style="font-size:22px">Ware-housing</h3></article><article data-reveal><h3 class="display ink" style="font-size:22px">EDI transfers</h3></article></div></section>''', layout="columns")

fcl = service_page("global-fcl-forwarding.html","Global FCL Forwarding","Full container global movement","fcl","assets/images/links/stock-containers.jpg",
'''<p class="lede">Imex Clearing & Logistics Private Limited, with the years of experience in freight forwarding offers inbound and outbound full container load services. Our solutions are tailor made to suit your requirement. We have exclusive service contracts with premium carriers that enable us to offer guaranteed space and competitive rates. We can handle large volumes on global basis or specific requirements on a single route.</p>''', extra='''<section class="section"><div class="wrap"><p class="giant">FCL</p><p class="lede">Guaranteed space and competitive rates through exclusive service contracts with premium carriers — stated exactly as on the original IMEX page.</p></div></section>''', layout="split")

air = service_page("air-freight.html","Air Freight","Logistics above the clouds","air","assets/images/background/banner_a.jpg",
'''<p class="lede">Imex Clearing & Logistics Private Limited specializes in providing expert international Air freight forwarding services to companies large and small. We manage the movement of a single shipment or a complex freight management programme providing a flexible approach and a personalized service to all customers. We facilitate customized and tailor-made air freight solutions including multi-modal land, sea, air combos for inbound and outbound cargo making us an integral partner with our clients. Our impeccable service is supported by preferred carrier programme. We have partnership agreements for complex freight management operations thereby providing access to competitive pricing and capacity.</p>''', extra='''<section class="section" style="background:linear-gradient(#070b18,#121a3a)"><div class="wrap"><p class="kicker">Preferred carrier programme</p><h2 class="display">Land, sea and air combos</h2><p class="lede" style="margin-top:16px">Customized multi-modal solutions for inbound and outbound cargo.</p></div></section>''', layout="stack")

customs = service_page("customs-clearance.html","Customs Clearance","The intelligence behind every shipment","scan","assets/images/background/banner_cc.jpg",
'''<p class="lede">Imex Clearing & Logistics Private Limited offers In-house Customs Clearance services at all major ports of India. We have specialty for all type of EXPORT CLEARANCE of goods like Machine, Food Items, Furniture, Chemicals Leather products and other project related items. We also offer clearance for all type of PROJECT LOGISTICS SERVICES so that our clients need not to worry for logistics as we focus on our client satisfaction.</p>
<p class="muted" style="margin-top:12px">No clearance timelines or approval guarantees are stated beyond this original description.</p>''', extra='''<section class="section paper"><div class="wrap"><p class="kicker ink">Export clearance speciality</p><div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:20px"><span class="chip ink">Machine</span><span class="chip ink">Food Items</span><span class="chip ink">Furniture</span><span class="chip ink">Chemicals</span><span class="chip ink">Leather products</span><span class="chip ink">Project related items</span></div></div></section>''', layout="columns")

dgft = service_page("dgft-licensing.html","DGFT / Licensing Works","Documentation meets global trade","docs","assets/images/background/banner_lic.jpg",
'''<p class="lede">Imex Clearing & Logistics Private Limited Also Offers Service Related To DGFT and other Major Authorities Like FASSAI, PLANT QUARANTINE, COUNCIL FOR LEATHER EXPORTS, ANIMAL QUARANTINE and other Agencies Which Has Collaborations With Customs For Benefits of The Importers and Exporters, we also get the issue of licenses like DFIA, EPCG, MEIS, Advance Licenses etc. We can provide a complete solution for you export import need so we provide a wide variety of services like gst registration,tademarks registration, issue of new importer exporter code(iec)/ ammendment,MSME registration. we have a complete solution for your legal problems related to customs also.</p>
<p class="muted" style="margin-top:12px">This page describes existing IMEX offerings only. It is not legal advice and does not issue licences on its own.</p>''', extra='''<section class="section light"><div class="wrap" style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px"><article class="contact-card"><h3 class="display ink" style="font-size:22px">Licences</h3><p>DFIA, EPCG, MEIS, Advance Licenses</p></article><article class="contact-card"><h3 class="display ink" style="font-size:22px">Registrations</h3><p>GST, trademarks, IEC issue/amendment, MSME</p></article><article class="contact-card"><h3 class="display ink" style="font-size:22px">Authorities</h3><p>DGFT, FSSAI, Plant Quarantine, CLE, Animal Quarantine</p></article></div></section>''', layout="overlap")

vas_css = '''
.vas-hero{min-height:78vh}
.vas-hero .hero-canvas{overflow:hidden}
.vas-hero .hero-canvas img{width:100%;height:100%;object-fit:cover;object-position:center 42%;transform:scale(1.06)}
.vas-hero .overlay-scrim{z-index:1;background:linear-gradient(100deg,rgba(7,11,24,.78) 0%,rgba(7,11,24,.42) 46%,rgba(7,11,24,.62) 100%),linear-gradient(180deg,rgba(7,11,24,.2) 0%,rgba(7,11,24,.72) 100%)}
.vas-hero .hero-copy{z-index:2;max-width:min(1240px,calc(100% - 40px))}
.vas-grid{display:grid;grid-template-columns:1.2fr .8fr;gap:22px}
.vas-grid article{border-radius:22px;overflow:hidden;background:#fff;color:var(--ink);border:1px solid var(--line)}
.vas-grid article:nth-child(1){grid-row:span 2}
.vas-grid img{width:100%;height:220px;object-fit:cover}
.vas-grid .pad{padding:24px}
.links-cols{display:grid;grid-template-columns:1fr 1fr;gap:32px}
@media(max-width:800px){.vas-grid,.links-cols{grid-template-columns:1fr}}
'''
vas = r'''
<section class="hero vas-hero">
  <div class="hero-canvas">
    <img src="assets/images/links/stock-docs-alt.jpg" alt="Container vessel on a trade lane at dusk" width="1920" height="1280">
  </div>
  <div class="overlay-scrim"></div>
  <div class="hero-copy">
    <p class="kicker">Resources</p>
    <h1 class="display" data-split>Beyond transportation</h1>
    <p class="lede">Value added services published on IMEX: trade tools, container references, terms and useful government links.</p>
  </div>
</section>
<section class="section light">
  <div class="wrap vas-grid">
    <article data-reveal>
      <img src="assets/images/links/stock-containers-alt.jpg" alt="Stacked shipping containers at a yard">
      <div class="pad"><h2 class="display ink" style="font-size:32px">Container and ULDs</h2><p>Reference material for container and unit load device types used in sea and air freight.</p></div>
    </article>
    <article data-reveal>
      <img src="assets/images/links/stock-incoterms.jpg" alt="Cargo being loaded for international delivery">
      <div class="pad"><h2 class="display ink" style="font-size:28px">INCO Terms</h2><p>International commercial terms used in freight contracts.</p></div>
    </article>
    <article data-reveal>
      <img src="assets/images/links/stock-cargo.jpg" alt="Warehouse cargo on racking">
      <div class="pad"><h2 class="display ink" style="font-size:28px">Cargo Classifications</h2><p>Classification references for cargo handling.</p></div>
    </article>
    <article data-reveal>
      <img src="assets/images/links/stock-cargo-2.jpg" alt="Sorted freight in a warehouse">
      <div class="pad"><h2 class="display ink" style="font-size:28px">Classification chart</h2><p>Additional cargo classification graphic from the original site.</p></div>
    </article>
    <article data-reveal>
      <img src="assets/images/links/shipping-terms-1-728.jpg" alt="Charting terms">
      <div class="pad"><h2 class="display ink" style="font-size:28px">Charting Terms</h2><p>Freight chartering vocabulary published by IMEX.</p></div>
    </article>
    <article data-reveal>
      <div class="pad">
        <h2 class="display ink" style="font-size:28px">Currency Converter</h2>
        <p>IMEX links to the XE currency converter for trade calculations.</p>
        <a class="btn btn-navy" href="https://www.xe.com/currencyconverter/" target="_blank" rel="noopener">Open XE <span class="arr">→</span></a>
      </div>
    </article>
  </div>
</section>
<section class="section paper">
  <div class="wrap">
    <p class="kicker ink">Useful links</p>
    <h2 class="display ink" style="margin-bottom:24px">Customs / Governments websites</h2>
    <div class="links-cols">
      <ul>
        <li><a href="http://www.accmumbai.gov.in/" target="_blank" rel="noopener">Air Cargo Customs Mumbai</a></li>
        <li><a href="http://www.jawaharcustoms.gov.in/" target="_blank" rel="noopener">Jawahar Custom House, Nhava Sheva</a></li>
        <li><a href="http://www.bchaa.com/" target="_blank" rel="noopener">Bombay custom house agent's association</a></li>
        <li><a href="http://www.cbec.gov.in/" target="_blank" rel="noopener">Central Board of Excise & Customs, India</a></li>
        <li><a href="http://www.concorindia.com/" target="_blank" rel="noopener">Container Corporation of India</a></li>
        <li><a href="http://www.finmin.nic.in/" target="_blank" rel="noopener">Ministry of Finance</a></li>
        <li><a href="http://www.dov.gov.in/" target="_blank" rel="noopener">Directorate of Valuation</a></li>
        <li><a href="http://www.goidirectory.nic.in/" target="_blank" rel="noopener">Directory of Government Websites</a></li>
      </ul>
      <div>
        <h3 class="display ink" style="font-size:22px;margin-bottom:12px">Other related websites</h3>
        <ul>
          <li><a href="http://www.iata.org/" target="_blank" rel="noopener">IATA</a></li>
          <li><a href="http://www.wcoomd.org/" target="_blank" rel="noopener">World Customs Organisation</a></li>
          <li><a href="http://www.wto.org/" target="_blank" rel="noopener">World Trade Organisation</a></li>
          <li><a href="http://www.ciionline.org/" target="_blank" rel="noopener">Confederation of Indian Industry</a></li>
          <li><a href="http://www.imcnet.org/" target="_blank" rel="noopener">Indian Merchant's Chambers</a></li>
          <li><a href="http://www.aepcindia.com/" target="_blank" rel="noopener">Apparel Export Promotion Council</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap" style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center">
    <h2 class="display">Move from reference to enquiry</h2>
    <a class="btn btn-cyan magnetic" href="quote.html" data-vt="zoom">Request a Quote <span class="arr">→</span></a>
  </div>
</section>
'''

quote_css = '''
.quote-hero{min-height:78vh}
.quote-hero .hero-canvas{overflow:hidden}
.quote-hero .hero-canvas img{width:100%;height:100%;object-fit:cover;object-position:center 58%;transform:scale(1.06)}
.quote-hero .overlay-scrim{z-index:1;background:linear-gradient(100deg,rgba(7,11,24,.78) 0%,rgba(7,11,24,.42) 48%,rgba(7,11,24,.58) 100%),linear-gradient(180deg,rgba(7,11,24,.18) 0%,rgba(7,11,24,.74) 100%)}
.quote-hero .hero-copy{z-index:2;max-width:min(1240px,calc(100% - 40px))}
.quote-layout{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;align-items:start}
.twin{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:900px){.quote-layout,.twin{grid-template-columns:1fr}}
'''
quote = r'''
<section class="hero quote-hero">
  <div class="hero-canvas">
    <img src="assets/images/links/stock-incoterms.jpg" alt="Freight being loaded at the start of a shipment" width="1920" height="1280">
  </div>
  <div class="overlay-scrim"></div>
  <div class="hero-copy">
    <p class="kicker">Enquiry</p>
    <h1 class="display" data-split>Your shipment starts here</h1>
    <p class="lede">Request a Quote — the same shipment and contact fields used on the original IMEX form. This page does not calculate prices.</p>
  </div>
</section>
<section class="section light">
  <div class="wrap quote-layout">
    <div>
      <h2 class="display ink" style="font-size:36px">Send us your query</h2>
      <p class="lede">Please fill in your details so that we can contact and update you about your query. Submitting opens your email client to sayyam7@imexclearing.com with the information below.</p>
      <img src="assets/images/block/Courier-Man.png" alt="Courier with package" style="max-height:420px;margin-top:24px" loading="lazy">
    </div>
    <form id="quoteForm" novalidate>
      <div class="twin">
        <div class="field"><input id="height" name="height" type="number" min="1" placeholder=" " required><label for="height">Height (cm)</label><p class="err">Required</p></div>
        <div class="field"><input id="width" name="width" type="number" min="1" placeholder=" " required><label for="width">Width (cm)</label><p class="err">Required</p></div>
        <div class="field"><input id="depth" name="depth" type="number" min="1" placeholder=" " required><label for="depth">Depth (cm)</label><p class="err">Required</p></div>
        <div class="field"><input id="weight" name="weight" type="number" min="0.1" step="0.1" placeholder=" " required><label for="weight">Weight (kg)</label><p class="err">Required</p></div>
      </div>
      <div class="twin">
        <div class="field"><input id="locations_from" name="country_from" type="text" placeholder=" " required><label for="locations_from">Country — From</label><p class="err">Required</p></div>
        <div class="field"><input id="locations_to" name="country_to" type="text" placeholder=" " required><label for="locations_to">Country — To</label><p class="err">Required</p></div>
        <div class="field"><input id="city_from" name="city_from" type="text" placeholder=" " required><label for="city_from">City — From</label><p class="err">Required</p></div>
        <div class="field"><input id="city_to" name="city_to" type="text" placeholder=" " required><label for="city_to">City — To</label><p class="err">Required</p></div>
      </div>
      <div class="field">
        <select id="service" name="package" required>
          <option value=""></option>
          <option>Sea Freight</option>
          <option>Outbound LCL Consolidation</option>
          <option>Inbound LCL Consolidation</option>
          <option>Buyer Consolidation</option>
          <option>Global FCL Forwarding</option>
          <option>Air Freight</option>
          <option>Custom Clearance</option>
          <option>DGFT / Licensing Works</option>
        </select>
        <label for="service">Package type</label>
        <p class="err">Select a service</p>
      </div>
      <div class="field"><input id="fname" name="full_name" type="text" placeholder=" " required><label for="fname">Full name</label><p class="err">Required</p></div>
      <div class="twin">
        <div class="field"><input id="mob" name="mobile" type="tel" placeholder=" " required><label for="mob">Mobile</label><p class="err">Required</p></div>
        <div class="field"><input id="altmob" name="alt_mobile" type="tel" placeholder=" "><label for="altmob">Alternative mobile</label></div>
      </div>
      <div class="field"><input id="email" name="email" type="email" placeholder=" " required><label for="email">Email</label><p class="err">Enter a valid email</p></div>
      <button class="btn btn-navy magnetic" type="submit">Submit the details <span class="arr">→</span></button>
      <p id="formStatus" class="form-status" role="status"></p>
    </form>
  </div>
</section>
'''

tracking = r'''
<section class="hero">
  <canvas id="scene" class="hero-canvas" data-scene="globe"></canvas>
  <div class="scan-line"></div>
  <div class="hero-copy">
    <p class="kicker">Follow your shipment</p>
    <h1 class="display" data-split>Track & Trace</h1>
    <p class="lede">Now you can track your product easily. Tracking opens the original IMEX destination: track-trace.com. No live statuses are invented here.</p>
  </div>
</section>
<section class="section">
  <div class="wrap track-box">
    <form id="trackForm">
      <label class="kicker" for="awb">Tracking number</label>
      <input id="awb" name="awb" type="text" placeholder="AWB / container / bill of lading">
      <button class="btn btn-cyan" type="submit">Track <span class="arr">→</span></button>
    </form>
    <p id="trackNote" class="muted" style="margin-top:14px">Original destination: https://www.track-trace.com/</p>
    <a class="btn btn-ghost" href="https://www.track-trace.com/" target="_blank" rel="noopener" style="margin-top:16px">Open Track & Trace</a>
  </div>
</section>
<section class="section light">
  <div class="wrap" style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:center">
    <h2 class="display ink">Need a person, not a tracker?</h2>
    <a class="btn btn-navy" href="contact.html" data-vt="wipe">Contact Us <span class="arr">→</span></a>
  </div>
</section>
'''

contact_css = '''
.contact-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:48px}
.contact-card{padding:28px;border-radius:20px;border:1px solid var(--line);margin-bottom:16px}
@media(max-width:900px){.contact-grid{grid-template-columns:1fr}}
'''
contact = r'''
<section class="hero" style="min-height:70vh">
  <div class="hero-canvas" style="background:url('assets/images/background/banner-1.jpg') center/cover"></div>
  <div class="overlay-scrim"></div>
  <div class="hero-copy">
    <p class="kicker">Kanpur</p>
    <h1 class="display" data-split>Connect with IMEX</h1>
    <p class="lede">Get in touch with us easily — import desk, export desk, and the Harmony Arcade office.</p>
  </div>
</section>
<section class="section light">
  <div class="wrap contact-grid">
    <div>
      <article class="contact-card" data-reveal>
        <p class="kicker ink">Address</p>
        <p>No. 16, 1st Floor, Harmony Arcade,<br>17/1, Telegraph Road, The Mall,<br>Kanpur - 208001</p>
      </article>
      <article class="contact-card" data-reveal>
        <p class="kicker ink">Main contact</p>
        <p><a href="tel:+915122391885">Tel: +91 512-2391885</a><br>
        <a href="tel:+919335347057">Mobile: +91 933 534 7057</a><br>
        <a href="mailto:sayyam7@imexclearing.com">sayyam7@imexclearing.com</a></p>
      </article>
      <article class="contact-card" data-reveal>
        <p class="kicker ink">For imports</p>
        <p><a href="mailto:imports@imexclearing.com">imports@imexclearing.com</a><br>
        <a href="tel:+915122363995">+91 512 236 3995</a></p>
      </article>
      <article class="contact-card" data-reveal>
        <p class="kicker ink">For exports</p>
        <p><a href="mailto:exports@imexclearing.com">exports@imexclearing.com</a><br>
        <a href="tel:+915122391885">+91 512 239 1885</a></p>
      </article>
      <article class="contact-card" data-reveal>
        <p class="kicker ink">Other numbers</p>
        <p><a href="tel:+919335347057">+91 933 534 7057</a><br>
        <a href="tel:+917798777318">+91 779 877 7318</a></p>
      </article>
      <article class="contact-card" data-reveal>
        <p class="kicker ink">Email address</p>
        <p><a href="mailto:suresh@imexclearing.com">suresh@imexclearing.com</a><br>
        <a href="mailto:sayyam7@imexclearing.com">sayyam7@imexclearing.com</a></p>
      </article>
      <a class="btn btn-navy magnetic" href="quote.html" data-vt="zoom">Send an enquiry <span class="arr">→</span></a>
    </div>
    <div>
      <div class="img-clip" style="min-height:520px">
        <img src="assets/images/background/contact-map.png" alt="IMEX contact map graphic">
      </div>
    </div>
  </div>
</section>
'''

PAGES = [
    ("index.html","home","IMEX International | Freight Forwarder & Customs Clearance, Kanpur",
     "Imex Clearing & Logistics Private Limited — Kanpur freight forwarder for sea, air, LCL, FCL, customs clearance and DGFT licensing since 1994.",
     home_css, home, "container"),
    ("about.html","about","About IMEX | Freight Forwarder & Logistics Company in Kanpur",
     "Established in 1994 by Mr. Suresh Kumar Mishra. IMEX is a Kanpur freight forwarder awarded by CONCOR for outstanding performance three times in a row.",
     about_css, about, ""),
    ("services.html","services","IMEX Services | Sea, Air, LCL, FCL, Customs & DGFT",
     "Seven IMEX capabilities: sea freight, LCL consolidation, buyer consolidation, global FCL, air freight, customs clearance and DGFT licensing.",
     services_css, services_page, ""),
    ("sea-freight.html","sea-freight.html","Sea Freight Services India | IMEX International Kanpur",
     "Complete sea freight for import and export including inbound and outbound ocean solutions, FCL/LCL cross trade and door-to-door delivery.",
     "", sea, "ocean"),
    ("lcl-consolidation.html","lcl-consolidation.html","Inbound & Outbound LCL Consolidation | IMEX Kanpur",
     "LCL consolidation from Indian ports and hinterland ICDs, plus import LCL from worldwide origins.",
     "", lcl, "packages"),
    ("buyer-consolidation.html","buyer-consolidation.html","Buyer Consolidation Services | IMEX International Kanpur",
     "Buyer’s consolidation with vendor management, warehousing, inland movement and EDI information as cargo moves through the supply chain.",
     "", buyer, "buyer"),
    ("global-fcl-forwarding.html","global-fcl-forwarding.html","Global FCL Forwarding Services | IMEX International Kanpur",
     "Inbound and outbound full container load services with carrier contracts for space and competitive rates.",
     "", fcl, "fcl"),
    ("air-freight.html","air-freight.html","Air Freight Services India | IMEX International Kanpur",
     "International air freight forwarding for a single shipment or a complex programme, including multi-modal land, sea and air combos.",
     "", air, "air"),
    ("customs-clearance.html","customs-clearance.html","Customs Clearance Services India | IMEX International Kanpur",
     "In-house customs clearance at major Indian ports, including export clearance of machines, food, furniture, chemicals and leather products.",
     "", customs, "scan"),
    ("dgft-licensing.html","dgft-licensing.html","DGFT & Licensing Works | IMEX International",
     "DGFT, FSSAI, plant and animal quarantine, leather export council work, plus DFIA, EPCG, MEIS, IEC, GST, MSME and trademark registrations.",
     "", dgft, "docs"),
    ("value-added-services.html","vas","Value Added Services | IMEX International Kanpur",
     "IMEX value added resources: ULDs, INCO terms, cargo classifications, charting terms, useful government links and currency converter.",
     vas_css, vas, "packages"),
    ("quote.html","quote","Get a Freight Quote | IMEX International Kanpur",
     "Request an IMEX freight quote with height, width, depth, weight, origin, destination and package type. Enquiries go to sayyam7@imexclearing.com.",
     quote_css, quote, "quote"),
    ("tracking.html","tracking","Track & Trace | IMEX International Kanpur",
     "Track IMEX shipments via the original Track & Trace destination at track-trace.com. This page does not invent live status.",
     "", tracking, "globe"),
    ("contact.html","contact","Contact IMEX International | Freight Forwarder Kanpur",
     "Contact IMEX in Kanpur: Harmony Arcade, The Mall. Imports, exports, telephone and email desks as published on the original site.",
     contact_css, contact, "container"),
]

def main():
    for filename, page, title, desc, extra, body, scene in PAGES:
        html = shell(page, title, desc, extra, body, scene)
        (ROOT / filename).write_text(html, encoding="utf-8")
        print("wrote", filename, len(html))

if __name__ == "__main__":
    main()
