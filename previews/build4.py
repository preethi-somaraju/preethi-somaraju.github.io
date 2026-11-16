"""Warm, quiet, typographic variants.

    python previews/build4.py

Rules for this batch: no pill badges, no gradients, no card shadows, no progress
bars, no Inter. Warm off-white paper, a real serif, hairline rules, dates set in
the margin. The design should recede and let the writing carry it.
"""
import pathlib

OUT = pathlib.Path(__file__).parent

HEAD = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{font}" rel="stylesheet">
<style>{css}</style></head><body>{body}</body></html>"""


# =====================================================================
# 12 — PAPER. EB Garamond, bone, terracotta hairline. Dates in the margin.
# =====================================================================
PAPER_FONT = "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap"
PAPER_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#f7f4ed;color:#2e2a24;font-family:"EB Garamond",Georgia,serif;
     font-size:21px;line-height:1.72;-webkit-font-smoothing:antialiased;
     font-feature-settings:"liga","kern"}
.sheet{max-width:46rem;margin:0 auto;padding:6rem 2rem 7rem}
a{color:#2e2a24;text-decoration:none;border-bottom:1px solid #c8a893;
  padding-bottom:1px}
a:hover{border-bottom-color:#2e2a24}

h1{font-size:2.6rem;font-weight:400;letter-spacing:-.01em;line-height:1.15;
   margin-bottom:.35rem}
.sub{font-style:italic;color:#6d6459;font-size:1.12rem;margin-bottom:2.6rem}

p{margin-bottom:1.15rem;max-width:34rem}
p.lead{font-size:1.15rem}

.rule{border:0;border-top:1px solid #e0d8c9;margin:3.2rem 0 2.4rem}

h2{font-size:.78rem;font-weight:500;letter-spacing:.2em;text-transform:uppercase;
   color:#a3907c;margin-bottom:1.6rem}

/* marginal dates */
.entry{display:grid;grid-template-columns:7.5rem 1fr;gap:1.6rem;margin-bottom:1.9rem}
.entry .when{font-size:.88rem;color:#9a8e7f;letter-spacing:.03em;padding-top:.42rem;
             font-variant-numeric:oldstyle-nums}
.entry h3{font-size:1.14rem;font-weight:500;margin-bottom:.1rem}
.entry .org{font-style:italic;color:#6d6459;font-size:1rem;margin-bottom:.3rem}
.entry p{font-size:1rem;color:#56504a;margin-bottom:0;max-width:30rem}

.links{margin-top:.4rem;font-size:1rem;color:#6d6459}
.links a{margin-right:.35rem}

@media(max-width:40rem){
  body{font-size:19px}
  .sheet{padding:3.5rem 1.5rem 5rem}
  .entry{grid-template-columns:1fr;gap:.2rem}
  .entry .when{padding-top:0}
}
"""

PAPER_BODY = """
<div class="sheet">

  <h1>Preethi Somaraju</h1>
  <p class="sub">Data engineer in Houston, Texas</p>

  <p class="lead">I build the pipelines and reporting layers that teams rely on
  to make decisions. Ten years of it &mdash; hardware telemetry at Qualcomm,
  a cloud ingestion pipeline at the University of North Texas, ETL and
  forecasting for consulting clients.</p>

  <p>For the past while I have been rebuilding that skill set on AWS, in the
  open. One lab a week for a year: Terraform for everything, tested properly,
  written up including the parts that went wrong. The first is
  <a href="#">account foundations</a> &mdash; why a budget alarm should exist
  before anything else does.</p>

  <p class="links"><a href="#">Writing</a> &middot; <a href="#">GitHub</a>
  &middot; <a href="#">LinkedIn</a> &middot; <a href="#">Résumé</a>
  &middot; <a href="#">Email</a></p>

  <hr class="rule">

  <h2>Work</h2>

  <div class="entry">
    <div class="when">2026 —</div>
    <div>
      <h3>AWS data engineering labs</h3>
      <p class="org">Self-directed, in public</p>
      <p>Fifty-two weeks, one lab a week, from an empty account to a capstone
      lakehouse. Infrastructure as code, positive and negative tests with real
      output, and a written record of each.</p>
    </div>
  </div>

  <div class="entry">
    <div class="when">2021 — 2024</div>
    <div>
      <h3>Freelance data consultant</h3>
      <p class="org">Dallas Data Science Academy</p>
      <p>Automated ETL across multi-source client databases, time-series
      forecasting and scenario modelling, and the dashboards that made the
      results usable.</p>
    </div>
  </div>

  <div class="entry">
    <div class="when">2020 — 2021</div>
    <div>
      <h3>Data science intern</h3>
      <p class="org">University of North Texas</p>
      <p>Built a cloud ingestion pipeline on Azure Data Factory, Blob Storage
      and Azure SQL that replaced manual collection, alongside an MS in Data
      Science.</p>
    </div>
  </div>

  <div class="entry">
    <div class="when">2014 — 2019</div>
    <div>
      <h3>Data analysis and engineering</h3>
      <p class="org">Qualcomm, Hyderabad</p>
      <p>Python tooling to parse high-volume hardware test telemetry, cutting
      manual verification cycles by a third. Where I learned that data arrives
      messy.</p>
    </div>
  </div>

  <hr class="rule">

  <h2>Selected work</h2>

  <div class="entry">
    <div class="when">AWS</div>
    <div>
      <h3><a href="#">Analytics pipeline on NYC taxi data</a></h3>
      <p>S3, Glue and Athena over trip records, partitioned to keep scanned
      bytes &mdash; and cost &mdash; down.</p>
    </div>
  </div>

  <div class="entry">
    <div class="when">Azure</div>
    <div>
      <h3><a href="#">Cloud telemetry ETL pipeline</a></h3>
      <p>Sensor events ingested, transformed and loaded into Azure SQL.</p>
    </div>
  </div>

  <div class="entry">
    <div class="when">Python</div>
    <div>
      <h3><a href="#">Retail demand forecasting</a></h3>
      <p>Regression time-series model with seasonal lag features and rolling
      averages.</p>
    </div>
  </div>

  <hr class="rule">

  <p style="color:#6d6459;font-size:1rem">Open to data engineering roles in
  Houston and remote. Authorised to work in the US.<br>
  <a href="#">somaraju.preethi164@gmail.com</a></p>

</div>
"""


# =====================================================================
# 13 — ATELIER. Newsreader, oatmeal, sage. Wide left margin for labels.
# =====================================================================
ATELIER_FONT = "https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300&display=swap"
ATELIER_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#faf8f4;color:#26241f;font-family:Newsreader,Georgia,serif;
     font-size:19.5px;line-height:1.78;-webkit-font-smoothing:antialiased;
     font-optical-sizing:auto;font-weight:300}
.sheet{max-width:52rem;margin:0 auto;padding:5.5rem 2.5rem 7rem}
a{color:#26241f;text-decoration:none;box-shadow:inset 0 -1px 0 #bdc3ae}
a:hover{box-shadow:inset 0 -2px 0 #7f8a6c}

.row{display:grid;grid-template-columns:9rem 1fr;gap:2.5rem}
.label{font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;
       color:#9a9484;font-weight:400;padding-top:.65rem}

h1{font-size:3.1rem;font-weight:300;letter-spacing:-.015em;line-height:1.08;
   margin-bottom:.5rem}
.sub{font-style:italic;color:#6f6a5e;font-size:1.16rem;margin-bottom:3rem}

p{margin-bottom:1.2rem}
p.lead{font-size:1.18rem;font-weight:300;line-height:1.72}

.block{margin-bottom:3.4rem}
h2{font-size:1.45rem;font-weight:400;margin-bottom:1rem;letter-spacing:-.01em}

.item{margin-bottom:1.7rem}
.item h3{font-size:1.1rem;font-weight:500;margin-bottom:.05rem}
.item .meta{font-style:italic;color:#8b8578;font-size:.98rem;margin-bottom:.25rem}
.item p{font-size:1rem;color:#4f4b43;margin-bottom:0}

.quiet{color:#6f6a5e;font-size:1rem}
hr{border:0;border-top:1px solid #e6e1d6;margin:0 0 3.4rem}

@media(max-width:44rem){
  body{font-size:18px}
  .sheet{padding:3rem 1.5rem 4.5rem}
  .row{grid-template-columns:1fr;gap:.5rem}
  .label{padding-top:0;margin-bottom:.3rem}
  h1{font-size:2.3rem}
}
"""

ATELIER_BODY = """
<div class="sheet">

  <h1>Preethi Somaraju</h1>
  <p class="sub">Data engineer &mdash; Houston, Texas</p>

  <div class="row block">
    <div class="label">Now</div>
    <div>
      <p class="lead">I build the pipelines and reporting layers that teams rely
      on to make decisions, and I am rebuilding that skill set on AWS in the
      open &mdash; one lab a week for a year.</p>
      <p>Each lab is infrastructure as code, tested with real command output,
      and written up including what went wrong. The first is
      <a href="#">account foundations</a>: why a budget alarm should exist
      before anything else in an account does.</p>
      <p class="quiet"><a href="#">Writing</a> &nbsp;·&nbsp;
      <a href="#">GitHub</a> &nbsp;·&nbsp; <a href="#">LinkedIn</a>
      &nbsp;·&nbsp; <a href="#">Résumé</a></p>
    </div>
  </div>

  <hr>

  <div class="row block">
    <div class="label">Work</div>
    <div>
      <div class="item">
        <h3>AWS data engineering labs</h3>
        <p class="meta">Self-directed, in public · 2026 —</p>
        <p>Fifty-two weeks from an empty AWS account to a capstone lakehouse.
        Terraform, positive and negative tests, a written record of each.</p>
      </div>
      <div class="item">
        <h3>Freelance data consultant</h3>
        <p class="meta">Dallas Data Science Academy · 2021 — 2024</p>
        <p>Automated ETL across multi-source client databases, forecasting and
        scenario modelling, and the reporting that made results usable.</p>
      </div>
      <div class="item">
        <h3>Data science intern</h3>
        <p class="meta">University of North Texas · 2020 — 2021</p>
        <p>A cloud ingestion pipeline on Azure Data Factory, Blob Storage and
        Azure SQL replacing manual collection, alongside an MS in Data Science.</p>
      </div>
      <div class="item">
        <h3>Data analysis and engineering</h3>
        <p class="meta">Qualcomm, Hyderabad · 2014 — 2019</p>
        <p>Python tooling parsing high-volume hardware test telemetry, cutting
        manual verification cycles by a third.</p>
      </div>
    </div>
  </div>

  <hr>

  <div class="row block">
    <div class="label">Projects</div>
    <div>
      <div class="item">
        <h3><a href="#">Analytics pipeline on NYC taxi data</a></h3>
        <p>S3, Glue and Athena over trip records, partitioned to keep scanned
        bytes &mdash; and cost &mdash; down.</p>
      </div>
      <div class="item">
        <h3><a href="#">Cloud telemetry ETL pipeline</a></h3>
        <p>Sensor events ingested, transformed and loaded into Azure SQL.</p>
      </div>
      <div class="item">
        <h3><a href="#">Retail demand forecasting</a></h3>
        <p>Regression time-series model with seasonal lag features and rolling
        averages over daily sales.</p>
      </div>
    </div>
  </div>

  <hr>

  <div class="row">
    <div class="label">Elsewhere</div>
    <div>
      <p class="quiet">Open to data engineering roles in Houston and remote.
      Authorised to work in the US.<br>
      <a href="#">somaraju.preethi164@gmail.com</a></p>
    </div>
  </div>

</div>
"""


# =====================================================================
# 14 — LETTER. One continuous piece of writing. Fraunces, clay.
# =====================================================================
LETTER_FONT = "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300&display=swap"
LETTER_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#f5f1ea;color:#312b26;font-family:Fraunces,Georgia,serif;
     font-size:20px;line-height:1.8;font-weight:300;font-optical-sizing:auto;
     -webkit-font-smoothing:antialiased}
.sheet{max-width:38rem;margin:0 auto;padding:7rem 2rem 8rem}
a{color:#312b26;text-decoration:none;border-bottom:1px solid #cbb6a4}
a:hover{border-bottom-color:#9c6f4f}

h1{font-size:1.5rem;font-weight:400;letter-spacing:.01em;margin-bottom:.1rem}
.place{color:#8a7c70;font-size:.95rem;font-style:italic;margin-bottom:3.2rem}

p{margin-bottom:1.45rem}
p.first::first-letter{font-size:3.2rem;float:left;line-height:.85;
  padding:.1rem .5rem .1rem 0;color:#9c6f4f;font-weight:400}

.aside{font-size:.92rem;color:#8a7c70;font-style:italic;
       border-left:1px solid #ddd0c2;padding-left:1.1rem;margin:2.2rem 0}

.sign{margin-top:3.2rem;padding-top:1.6rem;border-top:1px solid #e3dace;
      font-size:.95rem;color:#8a7c70}
.sign a{margin-right:.5rem}

@media(max-width:40rem){
  body{font-size:18.5px}
  .sheet{padding:4rem 1.5rem 5rem}
}
"""

LETTER_BODY = """
<div class="sheet">

  <h1>Preethi Somaraju</h1>
  <p class="place">Data engineer &mdash; Houston, Texas</p>

  <p class="first">For about ten years I have worked on the unglamorous half of
  data: getting it out of the systems that produce it, into a shape someone can
  actually use, reliably enough that nobody has to think about it. That started
  with hardware test telemetry at Qualcomm, where I learned that data arrives
  messy and on its own schedule.</p>

  <p>At the University of North Texas I built a cloud ingestion pipeline on
  Azure &mdash; Data Factory, Blob Storage, Azure SQL &mdash; that replaced a
  manual collection process, while finishing an MS in Data Science. After that
  came four years of consulting: ETL automation across client databases,
  forecasting work, and the reporting layers that made any of it useful to the
  people paying for it.</p>

  <p>Now I am rebuilding that skill set on AWS, in the open. One lab a week for
  a year &mdash; from an empty account through Glue, Athena, Iceberg, Kinesis,
  Redshift and Airflow, to a lakehouse at the end. Terraform for everything,
  torn down after each one.</p>

  <p class="aside">Every lab records the tests that passed <em>and</em> the ones
  meant to fail, with real command output. A successful <code>terraform
  apply</code> is not evidence that anything works.</p>

  <p>The first is <a href="#">account foundations</a> &mdash; on why a budget
  alarm should exist before any other resource does, and what happens when you
  ask S3 to make a bucket public while Block Public Access is switched on. The
  rest follow weekly, and the <a href="#">code is all public</a>.</p>

  <p>Older work sits alongside it: an <a href="#">analytics pipeline over NYC
  taxi data</a> using S3, Glue and Athena, a
  <a href="#">cloud telemetry ETL pipeline</a>, and
  <a href="#">demand forecasting</a> on daily retail sales.</p>

  <p>I am looking for data engineering work in Houston or remote, and I am
  authorised to work in the US.</p>

  <p class="sign"><a href="#">Email</a> <a href="#">GitHub</a>
  <a href="#">LinkedIn</a> <a href="#">Writing</a> <a href="#">Résumé</a></p>

</div>
"""

PAGES = [
    ("12-paper.html", "Paper — EB Garamond, marginal dates", PAPER_FONT, PAPER_CSS, PAPER_BODY),
    ("13-atelier.html", "Atelier — Newsreader, labelled columns", ATELIER_FONT, ATELIER_CSS, ATELIER_BODY),
    ("14-letter.html", "Letter — one continuous piece of writing", LETTER_FONT, LETTER_CSS, LETTER_BODY),
]

for fname, title, font, css, body in PAGES:
    (OUT / fname).write_text(
        HEAD.format(title=title, font=font, css=css, body=body), encoding="utf-8")
    print(f"wrote {fname}  ({title})")
