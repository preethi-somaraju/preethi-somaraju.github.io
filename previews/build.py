"""Generate homepage aesthetic variants for review.

    python previews/build.py

Same content in every variant; only the theme changes. Nothing here is linked
from the site — delete this folder once a direction is chosen.
"""
import pathlib

OUT = pathlib.Path(__file__).parent

BODY = """
<header class="hero">
  <div class="wrap">
    {badge}
    <h1>Preethi Somaraju</h1>
    <p class="role">{role}</p>
    <p class="lede">I build the pipelines and reporting layers that teams actually
    run on. A decade across semiconductor test, higher education and consulting,
    now going deep on AWS data engineering &mdash; in public, one lab a week.</p>
    <div class="cta">
      <a class="btn btn-main" href="#labs">See the AWS labs</a>
      <a class="btn btn-ghost" href="#">GitHub</a>
      <a class="btn btn-ghost" href="#">LinkedIn</a>
      <a class="btn btn-ghost" href="#">Résumé</a>
    </div>
    <div class="stats">
      <div class="stat"><b>10+ yrs</b><span>Data engineering</span></div>
      <div class="stat"><b>52</b><span>AWS labs, 1 shipped</span></div>
      <div class="stat"><b>MS</b><span>Data Science, UNT</span></div>
      <div class="stat"><b>Azure</b><span>Production pipelines</span></div>
    </div>
  </div>
</header>

<section id="labs">
  <div class="wrap">
    <p class="eyebrow">What I'm doing now</p>
    <h2>52 weeks of AWS data engineering labs</h2>
    <p class="sec-lede">One lab a week for a year, from an empty AWS account to a
    capstone lakehouse. Terraform for everything, torn down after each lab.</p>
    <div class="feature">
      <h3>Built, tested, written up &mdash; every week</h3>
      <p>Each lab records positive <em>and</em> negative tests with real command
      output, an architecture diagram using official AWS icons, and a write-up
      that includes what went wrong.</p>
      <div class="phases">
        <span class="chip">Identity &amp; security</span><span class="chip">Lake &amp; catalog</span>
        <span class="chip">Batch ETL</span><span class="chip">Streaming</span>
        <span class="chip">Warehousing</span><span class="chip">Orchestration</span>
        <span class="chip">Governance &amp; ML</span><span class="chip">Capstone</span>
      </div>
      <div class="progress"><i></i></div>
      <p class="progress-label">Week 1 of 52 &mdash; Lab 01 shipped</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Selected work</p>
    <h2>Projects</h2>
    <div class="grid">
      <article class="card"><h3>AWS analytics pipeline &mdash; NYC taxi</h3>
        <p>S3, Glue and Athena over NYC TLC trip records, partitioned to keep
        scanned bytes &mdash; and cost &mdash; down.</p>
        <div class="tags"><span class="tag">AWS</span><span class="tag">Glue</span><span class="tag">Athena</span></div></article>
      <article class="card"><h3>Cloud telemetry ETL pipeline</h3>
        <p>Sensor events ingested, transformed and loaded into Azure SQL,
        replacing manual collection.</p>
        <div class="tags"><span class="tag">Azure</span><span class="tag">Python</span></div></article>
      <article class="card"><h3>Retail demand forecasting</h3>
        <p>Regression time-series model with seasonal lag features and rolling
        averages over daily sales.</p>
        <div class="tags"><span class="tag">scikit-learn</span><span class="tag">pandas</span></div></article>
    </div>
  </div>
</section>
"""

SHARED = """
*{box-sizing:border-box;margin:0;padding:0}
.wrap{max-width:62rem;margin:0 auto;padding:0 1.6rem}
section{padding:3.5rem 0}
.cta{display:flex;flex-wrap:wrap;gap:.6rem;margin-bottom:2.2rem}
.btn{display:inline-block;padding:.6rem 1.2rem;font-size:.93rem;font-weight:600}
.stats{display:flex;flex-wrap:wrap;gap:2.4rem;padding-top:1.6rem}
.stat b{display:block;font-size:1.45rem;font-weight:800;line-height:1.2}
.stat span{font-size:.82rem}
.phases{display:flex;flex-wrap:wrap;gap:.4rem;margin:1.1rem 0}
.chip{padding:.25rem .6rem;font-size:.78rem}
.progress{height:5px;border-radius:3px;overflow:hidden;margin-bottom:.5rem}
.progress i{display:block;height:100%;width:2%}
.progress-label{font-size:.8rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(16rem,1fr));gap:1.1rem}
.card{padding:1.3rem 1.4rem}
.card h3{font-size:1rem;font-weight:700;margin-bottom:.35rem}
.card p{font-size:.92rem;margin-bottom:.8rem}
.tags{display:flex;flex-wrap:wrap;gap:.3rem}
.tag{padding:.15rem .5rem;font-size:.75rem}
.eyebrow{font-size:.75rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase;margin-bottom:.4rem}
.sec-lede{margin-bottom:1.6rem;max-width:44rem}
"""

THEMES = {
# ---------------------------------------------------------------- 1
"01-console": dict(
  name="Console — AWS dashboard",
  badge='<span class="badge"><span class="dot"></span> Open to data engineering roles · Houston, TX</span>',
  role='Data Engineer &mdash; <em>building on AWS</em>',
  css="""
body{font-family:"Amazon Ember","Segoe UI",system-ui,Arial,sans-serif;font-size:17px;
     line-height:1.62;color:#161c24;background:#fff}
.hero{background:#f6f8fa;border-bottom:1px solid #e3e7ea;padding:3.6rem 0 2.6rem}
.badge{display:inline-flex;align-items:center;gap:.5rem;background:#eaf7ee;color:#1d6f3f;
       border:1px solid #bfe3cc;border-radius:999px;padding:.3rem .85rem;font-size:.8rem;
       font-weight:600;margin-bottom:1.1rem}
.dot{width:7px;height:7px;border-radius:50%;background:#2e9e5b}
h1{font-size:2.9rem;font-weight:800;letter-spacing:-.025em;color:#232f3e;margin-bottom:.4rem}
.role{font-size:1.15rem;font-weight:600;color:#232f3e;margin-bottom:.8rem}
.role em{color:#ff9900;font-style:normal}
.lede{color:#5a6672;max-width:42rem;margin-bottom:1.6rem}
.btn-main{background:#232f3e;color:#fff;border-radius:4px}
.btn-ghost{border:1px solid #232f3e;color:#232f3e;border-radius:4px}
.stats{border-top:1px solid #e3e7ea}
.stat b{color:#232f3e}.stat span{color:#5a6672}
.eyebrow{color:#ff9900}
h2{font-size:1.6rem;color:#232f3e;font-weight:700;margin-bottom:.5rem}
.sec-lede{color:#5a6672}
section+section{border-top:1px solid #e3e7ea}
.feature{background:#232f3e;color:#eef2f5;border-radius:8px;padding:2rem;position:relative;overflow:hidden}
.feature::after{content:"";position:absolute;top:0;left:0;width:5px;height:100%;background:#ff9900}
.feature h3{font-size:1.3rem;color:#fff;margin-bottom:.5rem}
.feature p{color:#c3ccd4;max-width:40rem}
.chip{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);color:#dbe3ea;border-radius:3px}
.progress{background:rgba(255,255,255,.14)}.progress i{background:#ff9900}
.progress-label{color:#9fb0bf}
.card{background:#fff;border:1px solid #e3e7ea;border-radius:6px}
.card h3{color:#232f3e}.card p{color:#5a6672}
.tag{background:#f6f8fa;border:1px solid #e3e7ea;border-radius:3px;color:#5a6672}
"""),
# ---------------------------------------------------------------- 2
"02-terminal": dict(
  name="Terminal — engineer-forward",
  badge='<span class="badge">● available for hire — houston, tx</span>',
  role='<span class="prompt">$</span> data engineer --cloud aws',
  css="""
body{font-family:"JetBrains Mono","SF Mono",Consolas,"Courier New",monospace;
     font-size:15.5px;line-height:1.7;color:#d7dde3;background:#0f1419}
.hero{background:#12181f;border-bottom:1px solid #222c36;padding:3.4rem 0 2.6rem}
.badge{display:inline-block;color:#4ade80;font-size:.8rem;margin-bottom:1.1rem;
       border:1px solid #1e3a2a;background:#0e1a13;padding:.25rem .7rem;border-radius:3px}
h1{font-size:2.5rem;font-weight:700;color:#f0f4f8;letter-spacing:-.02em;margin-bottom:.5rem}
.role{font-size:1rem;color:#7dd3fc;margin-bottom:.9rem}
.prompt{color:#4ade80}
.lede{color:#8b98a5;max-width:42rem;margin-bottom:1.6rem;font-size:.95rem}
.btn-main{background:#4ade80;color:#0f1419;border-radius:3px}
.btn-ghost{border:1px solid #2b3844;color:#d7dde3;border-radius:3px}
.stats{border-top:1px solid #222c36}
.stat b{color:#f0f4f8;font-size:1.3rem}.stat span{color:#6b7885}
.eyebrow{color:#4ade80}
h2{font-size:1.4rem;color:#f0f4f8;font-weight:700;margin-bottom:.5rem}
.sec-lede{color:#8b98a5;font-size:.95rem}
section+section{border-top:1px solid #222c36}
.feature{background:#161d26;border:1px solid #222c36;border-left:3px solid #4ade80;
         border-radius:4px;padding:1.9rem}
.feature h3{font-size:1.15rem;color:#f0f4f8;margin-bottom:.5rem}
.feature p{color:#8b98a5;max-width:40rem;font-size:.94rem}
.chip{background:#0f1419;border:1px solid #2b3844;color:#7dd3fc;border-radius:3px}
.progress{background:#222c36}.progress i{background:#4ade80}
.progress-label{color:#6b7885}
.card{background:#12181f;border:1px solid #222c36;border-radius:4px}
.card h3{color:#f0f4f8}.card p{color:#8b98a5}
.tag{background:#0f1419;border:1px solid #2b3844;border-radius:3px;color:#7dd3fc}
"""),
# ---------------------------------------------------------------- 3
"03-editorial": dict(
  name="Editorial — serif, confident",
  badge='<span class="badge">Open to data engineering roles · Houston, TX</span>',
  role='Data Engineer, building on AWS',
  css="""
body{font-family:Georgia,"Iowan Old Style","Times New Roman",serif;font-size:18px;
     line-height:1.7;color:#1b1b19;background:#fdfcf9}
.hero{padding:4.5rem 0 3rem;border-bottom:2px solid #1b1b19}
.badge{display:inline-block;font-family:system-ui,sans-serif;font-size:.74rem;
       letter-spacing:.09em;text-transform:uppercase;color:#8a6a2f;
       border-bottom:1px solid #d9c9a3;padding-bottom:.25rem;margin-bottom:1.6rem}
h1{font-size:3.6rem;font-weight:400;letter-spacing:-.03em;line-height:1.02;margin-bottom:.6rem}
.role{font-size:1.25rem;font-style:italic;color:#6b6a63;margin-bottom:1.2rem}
.lede{font-size:1.12rem;color:#3e3d39;max-width:38rem;margin-bottom:1.8rem}
.btn{font-family:system-ui,sans-serif;font-size:.86rem}
.btn-main{background:#1b1b19;color:#fdfcf9}
.btn-ghost{border:1px solid #c9c6bb;color:#1b1b19}
.stats{border-top:1px solid #ddd9cd}
.stat b{font-size:1.55rem;font-weight:400}.stat span{font-family:system-ui,sans-serif;color:#6b6a63}
.eyebrow{font-family:system-ui,sans-serif;color:#8a6a2f}
h2{font-size:2.1rem;font-weight:400;letter-spacing:-.02em;margin-bottom:.5rem}
.sec-lede{color:#6b6a63}
section+section{border-top:1px solid #ddd9cd}
.feature{background:#1b1b19;color:#f3f1ea;padding:2.4rem 2.2rem}
.feature h3{font-size:1.5rem;font-weight:400;color:#fff;margin-bottom:.6rem}
.feature p{color:#b8b5aa;max-width:40rem}
.chip{font-family:system-ui,sans-serif;border:1px solid #4a4843;color:#d6d3c8}
.progress{background:#3a3833}.progress i{background:#c9a14a}
.progress-label{font-family:system-ui,sans-serif;color:#908d83}
.card{border:1px solid #ddd9cd;background:#fff}
.card h3{font-weight:400;font-size:1.15rem}
.card p{color:#6b6a63}
.tag{font-family:system-ui,sans-serif;border:1px solid #ddd9cd;color:#6b6a63}
"""),
# ---------------------------------------------------------------- 4
"04-gradient": dict(
  name="Gradient — modern, high contrast",
  badge='<span class="badge"><span class="dot"></span> Open to data engineering roles · Houston, TX</span>',
  role='Data Engineer &mdash; <em>building on AWS</em>',
  css="""
body{font-family:"Inter","Segoe UI",system-ui,Arial,sans-serif;font-size:17px;
     line-height:1.62;color:#15141b;background:#fff}
.hero{background:linear-gradient(135deg,#4f46e5 0%,#7c3aed 48%,#db2777 100%);
      color:#fff;padding:4.2rem 0 3.2rem}
.badge{display:inline-flex;align-items:center;gap:.5rem;background:rgba(255,255,255,.16);
       border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:.3rem .9rem;
       font-size:.8rem;font-weight:600;margin-bottom:1.2rem;backdrop-filter:blur(6px)}
.dot{width:7px;height:7px;border-radius:50%;background:#4ade80}
h1{font-size:3.2rem;font-weight:800;letter-spacing:-.035em;margin-bottom:.4rem}
.role{font-size:1.2rem;font-weight:600;margin-bottom:.9rem;color:#f3e8ff}
.role em{color:#fde047;font-style:normal}
.lede{color:#e9e2f8;max-width:42rem;margin-bottom:1.7rem}
.btn-main{background:#fff;color:#4f46e5;border-radius:7px}
.btn-ghost{border:1px solid rgba(255,255,255,.45);color:#fff;border-radius:7px}
.stats{border-top:1px solid rgba(255,255,255,.22)}
.stat b{color:#fff}.stat span{color:#ddd3f5}
.eyebrow{color:#7c3aed}
h2{font-size:1.8rem;font-weight:800;letter-spacing:-.02em;color:#15141b;margin-bottom:.5rem}
.sec-lede{color:#5b5668}
section+section{border-top:1px solid #ece9f2}
.feature{background:#15141b;color:#efecf6;border-radius:14px;padding:2.2rem;
         box-shadow:0 18px 40px -18px rgba(79,70,229,.5)}
.feature h3{font-size:1.35rem;color:#fff;margin-bottom:.5rem}
.feature p{color:#bab4cc;max-width:40rem}
.chip{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);
      color:#d9d3e8;border-radius:999px}
.progress{background:rgba(255,255,255,.14)}
.progress i{background:linear-gradient(90deg,#7c3aed,#db2777)}
.progress-label{color:#9a93ad}
.card{background:#fff;border:1px solid #ece9f2;border-radius:12px;
      box-shadow:0 2px 10px -4px rgba(21,20,27,.12)}
.card h3{color:#15141b}.card p{color:#5b5668}
.tag{background:#f6f4fb;border:1px solid #ece9f2;border-radius:999px;color:#6d6780}
"""),
}

PAGE = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{name} — preview</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{shared}{css}</style></head><body>{body}</body></html>"""

for slug, t in THEMES.items():
    html = PAGE.format(name=t["name"], shared=SHARED, css=t["css"],
                       body=BODY.format(badge=t["badge"], role=t["role"]))
    (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
    print(f"wrote {slug}.html  ({t['name']})")
