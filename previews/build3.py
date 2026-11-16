"""Concept variants — different ideas, not different palettes.

    python previews/build3.py

Each page is structured around a metaphor from her actual work rather than a
generic hero-and-cards layout.
"""
import pathlib

OUT = pathlib.Path(__file__).parent

HEAD = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>{css}</style></head><body>{body}</body></html>"""


# =====================================================================
# A — PIPELINE: the page is a data pipeline. Career = stages.
# =====================================================================
PIPELINE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,system-ui,sans-serif;background:#0b1020;color:#e6ebf4;
     font-size:16.5px;line-height:1.62;overflow-x:hidden}
.wrap{max-width:66rem;margin:0 auto;padding:0 1.5rem}
a{color:#6ee7b7;text-decoration:none}a:hover{text-decoration:underline}

.top{padding:3.4rem 0 1.5rem;text-align:center}
.top h1{font-size:2.8rem;font-weight:800;letter-spacing:-.03em;color:#fff}
.top .role{color:#8fa3c0;font-size:1.05rem;margin-top:.3rem}
.top .role b{color:#fbbf24;font-weight:600}
.top .lede{max-width:38rem;margin:1rem auto 0;color:#93a4bd;font-size:1rem}

/* the pipeline itself */
.pipe{padding:2.5rem 0 3.5rem;position:relative}
.rail{display:grid;grid-template-columns:repeat(4,1fr);gap:0;position:relative}
.rail::before{content:"";position:absolute;top:34px;left:12%;right:12%;height:2px;
  background:linear-gradient(90deg,#1e3a5f,#2563eb,#7c3aed,#fbbf24)}
.flow{position:absolute;top:30px;left:12%;width:10px;height:10px;border-radius:50%;
  background:#fbbf24;box-shadow:0 0 12px #fbbf24;animation:run 4.5s linear infinite}
.flow:nth-of-type(2){animation-delay:1.5s}
.flow:nth-of-type(3){animation-delay:3s}
@keyframes run{from{left:12%}to{left:88%}}
.node{text-align:center;position:relative;z-index:2}
.dot{width:70px;height:70px;border-radius:16px;margin:0 auto .8rem;display:grid;
  place-items:center;background:#111a2e;border:2px solid #24324d;font-size:1.5rem}
.node.on .dot{border-color:#fbbf24;background:#1a1630;box-shadow:0 0 0 6px rgba(251,191,36,.12)}
.node h3{font-size:.95rem;color:#fff;font-weight:600}
.node .yr{font-family:"JetBrains Mono",monospace;font-size:.76rem;color:#6b7f9e;margin-bottom:.3rem}
.node p{font-size:.84rem;color:#8fa3c0;max-width:13rem;margin:0 auto}
.stage{font-family:"JetBrains Mono",monospace;font-size:.68rem;letter-spacing:.14em;
  text-transform:uppercase;color:#4a5f82;margin-bottom:.5rem}

.cta{display:flex;justify-content:center;gap:.6rem;flex-wrap:wrap;margin-top:2.5rem}
.btn{padding:.6rem 1.3rem;border-radius:7px;font-size:.92rem;font-weight:600}
.b1{background:#fbbf24;color:#0b1020}
.b2{border:1px solid #2b3b58;color:#e6ebf4}

section{padding:3rem 0;border-top:1px solid #16203a}
h2{font-size:1.55rem;color:#fff;font-weight:700;letter-spacing:-.02em;margin-bottom:.4rem}
.sub{color:#8fa3c0;margin-bottom:1.6rem;max-width:42rem}
.eyebrow{font-family:"JetBrains Mono",monospace;font-size:.72rem;letter-spacing:.14em;
  text-transform:uppercase;color:#fbbf24;margin-bottom:.4rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:1rem}
.card{background:#101829;border:1px solid #1d2941;border-radius:10px;padding:1.2rem 1.3rem}
.card h3{font-size:1rem;color:#fff;margin-bottom:.3rem}
.card p{font-size:.9rem;color:#8fa3c0}
@media(max-width:46rem){
  .rail{grid-template-columns:1fr;gap:1.6rem}
  .rail::before,.flow{display:none}
}
"""

PIPELINE_BODY = """
<div class="wrap top">
  <h1>Preethi Somaraju</h1>
  <p class="role">Data Engineer &mdash; <b>building on AWS</b></p>
  <p class="lede">Ten years moving data from where it is produced to where
  decisions get made. Here is the pipeline that got me here.</p>
</div>

<div class="wrap pipe">
  <div class="rail">
    <span class="flow"></span><span class="flow"></span><span class="flow"></span>
    <div class="node">
      <div class="stage">Source</div>
      <div class="dot">⚙</div>
      <div class="yr">2014 &ndash; 2019</div>
      <h3>Qualcomm</h3>
      <p>Parsing hardware test telemetry at volume. Where I learned that data
      arrives messy.</p>
    </div>
    <div class="node">
      <div class="stage">Transform</div>
      <div class="dot">☁</div>
      <div class="yr">2020 &ndash; 2021</div>
      <h3>UNT &mdash; Azure</h3>
      <p>Built a cloud ingestion pipeline on Data Factory while finishing an MS
      in Data Science.</p>
    </div>
    <div class="node">
      <div class="stage">Load</div>
      <div class="dot">▦</div>
      <div class="yr">2021 &ndash; 2024</div>
      <h3>Consulting</h3>
      <p>ETL automation, forecasting and reporting layers for client
      businesses.</p>
    </div>
    <div class="node on">
      <div class="stage">Now</div>
      <div class="dot">▲</div>
      <div class="yr">2026 &ndash;</div>
      <h3>AWS, in public</h3>
      <p>52 weeks of data engineering labs. Terraform, tested, written up.</p>
    </div>
  </div>
  <div class="cta">
    <a class="btn b1" href="#">See the AWS labs</a>
    <a class="btn b2" href="#">GitHub</a>
    <a class="btn b2" href="#">LinkedIn</a>
    <a class="btn b2" href="#">R&eacute;sum&eacute;</a>
  </div>
</div>

<section><div class="wrap">
  <p class="eyebrow">Currently</p>
  <h2>52 weeks of AWS data engineering labs</h2>
  <p class="sub">One lab a week, from an empty account to a capstone lakehouse.
  Each one records positive and negative tests with real output.</p>
  <div class="grid">
    <div class="card"><h3>Week 1 &mdash; Account foundations</h3>
      <p>Budget alarm, versioned state, locking. Eight tests, two negative.</p></div>
    <div class="card"><h3>Week 2 &mdash; IAM for data access</h3>
      <p>Analyst and engineer reach different prefixes, provably.</p></div>
    <div class="card"><h3>Week 3 &mdash; S3 as a data lake</h3>
      <p>Zone layout that survives contact with real queries.</p></div>
  </div>
</div></section>
"""

# =====================================================================
# B — QUERY: the page is a SQL client. Content is the result set.
# =====================================================================
QUERY_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,system-ui,sans-serif;background:#f6f7f9;color:#1b2330;
     font-size:16px;line-height:1.6}
.app{max-width:70rem;margin:0 auto;background:#fff;min-height:100vh;
     border-left:1px solid #e2e6ec;border-right:1px solid #e2e6ec}
.bar{display:flex;align-items:center;gap:.6rem;padding:.7rem 1.2rem;
     background:#1b2330;color:#cdd6e3;font-family:"JetBrains Mono",monospace;font-size:.82rem}
.bar .d{width:11px;height:11px;border-radius:50%}
.tabs{display:flex;border-bottom:1px solid #e2e6ec;font-size:.85rem;
      font-family:"JetBrains Mono",monospace}
.tab{padding:.6rem 1.1rem;color:#6b7788;border-right:1px solid #eef1f5;cursor:default}
.tab.on{color:#1b2330;font-weight:600;border-bottom:2px solid #f59e0b;background:#fffdf7}
.editor{padding:1.3rem 1.4rem;background:#fbfcfd;border-bottom:1px solid #e2e6ec;
        font-family:"JetBrains Mono",monospace;font-size:.92rem;line-height:1.75}
.kw{color:#b91c6b;font-weight:500}.fn{color:#0b7285}.str{color:#1a7f37}.cm{color:#8b95a4}
.run{display:inline-block;margin-top:.9rem;background:#1b2330;color:#fff;
     font-family:Inter,sans-serif;font-size:.82rem;font-weight:600;
     padding:.35rem .9rem;border-radius:4px}
.meta{padding:.5rem 1.4rem;font-family:"JetBrains Mono",monospace;font-size:.76rem;
      color:#6b7788;background:#f3f5f8;border-bottom:1px solid #e2e6ec}
table{width:100%;border-collapse:collapse;font-size:.9rem}
th{background:#f3f5f8;text-align:left;font-family:"JetBrains Mono",monospace;
   font-size:.74rem;text-transform:uppercase;letter-spacing:.07em;color:#6b7788;
   padding:.55rem 1.4rem;border-bottom:1px solid #e2e6ec}
td{padding:.75rem 1.4rem;border-bottom:1px solid #eef1f5;vertical-align:top}
td.n{font-family:"JetBrains Mono",monospace;color:#6b7788;font-size:.84rem;white-space:nowrap}
td b{display:block;color:#1b2330;font-size:.97rem}
td span{color:#6b7788;font-size:.88rem}
.pill{display:inline-block;background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;
      border-radius:3px;padding:.1rem .45rem;font-size:.74rem;
      font-family:"JetBrains Mono",monospace;margin-right:.25rem}
.hdr{padding:1.6rem 1.4rem 1.2rem;border-bottom:1px solid #e2e6ec}
.hdr h1{font-size:1.9rem;font-weight:800;letter-spacing:-.025em}
.hdr p{color:#6b7788;margin-top:.2rem}
.hdr .av{display:inline-block;background:#ecfdf3;border:1px solid #abefc6;color:#067647;
         border-radius:999px;padding:.2rem .7rem;font-size:.78rem;font-weight:600;
         margin-top:.7rem}
.foot{padding:1.2rem 1.4rem;font-family:"JetBrains Mono",monospace;font-size:.8rem;
      color:#6b7788}
.foot a{color:#0b7285}
"""

QUERY_BODY = """
<div class="app">
  <div class="bar">
    <span class="d" style="background:#ff5f57"></span>
    <span class="d" style="background:#febc2e"></span>
    <span class="d" style="background:#28c840"></span>
    <span style="margin-left:.6rem">preethi@portfolio — athena</span>
  </div>

  <div class="hdr">
    <h1>Preethi Somaraju</h1>
    <p>Data Engineer · Houston, TX · building on AWS</p>
    <span class="av">● Open to data engineering roles</span>
  </div>

  <div class="tabs">
    <div class="tab on">experience.sql</div>
    <div class="tab">projects.sql</div>
    <div class="tab">labs.sql</div>
    <div class="tab">contact.sql</div>
  </div>

  <div class="editor">
<span class="cm">-- a decade of moving data to where decisions get made</span><br>
<span class="kw">SELECT</span> org, role, years, what_i_built<br>
<span class="kw">FROM</span> preethi.experience<br>
<span class="kw">WHERE</span> domain <span class="kw">IN</span> (<span class="str">'data engineering'</span>, <span class="str">'cloud'</span>)<br>
<span class="kw">ORDER BY</span> started <span class="kw">DESC</span>;
    <div class="run">▶ Run</div>
  </div>

  <div class="meta">4 rows returned · 0.42s · scanned 2.1 MB</div>

  <table>
    <tr><th>Years</th><th>Role</th><th>What I built</th></tr>
    <tr>
      <td class="n">2026 –</td>
      <td><b>AWS data engineering labs</b><span>Self-directed, in public</span></td>
      <td>52 weeks, one lab a week. Terraform, positive and negative tests,
        written up.
        <div style="margin-top:.4rem"><span class="pill">Terraform</span><span class="pill">S3</span><span class="pill">Glue</span><span class="pill">Athena</span></div></td>
    </tr>
    <tr>
      <td class="n">2021 – 2024</td>
      <td><b>Freelance Data Consultant</b><span>Dallas Data Science Academy</span></td>
      <td>Automated ETL for multi-source client data, forecasting, Tableau and
        Power BI reporting.
        <div style="margin-top:.4rem"><span class="pill">Python</span><span class="pill">SQL</span><span class="pill">Tableau</span></div></td>
    </tr>
    <tr>
      <td class="n">2020 – 2021</td>
      <td><b>Data Science Intern</b><span>University of North Texas</span></td>
      <td>Cloud ingestion pipeline on Azure Data Factory, Blob Storage and Azure
        SQL replacing manual collection.
        <div style="margin-top:.4rem"><span class="pill">Azure</span><span class="pill">XGBoost</span></div></td>
    </tr>
    <tr>
      <td class="n">2014 – 2019</td>
      <td><b>Data Analysis &amp; Engineering</b><span>Qualcomm, Hyderabad</span></td>
      <td>Python tooling parsing high-volume hardware test telemetry, cutting
        manual verification cycles 30%.
        <div style="margin-top:.4rem"><span class="pill">Python</span><span class="pill">SQL</span></div></td>
    </tr>
  </table>

  <div class="foot">
    <a href="#">github</a> · <a href="#">linkedin</a> · <a href="#">résumé</a> ·
    <a href="#">writing</a>
  </div>
</div>
"""

# =====================================================================
# C — 52 GRID: the lab series is the hero. Progress is the visual.
# =====================================================================
GRID_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,system-ui,sans-serif;background:#fcfcfd;color:#16181d;
     font-size:16.5px;line-height:1.62}
.wrap{max-width:58rem;margin:0 auto;padding:0 1.5rem}
a{color:#0d5bd4;text-decoration:none}a:hover{text-decoration:underline}
.hero{padding:3.6rem 0 2.2rem}
.av{display:inline-flex;align-items:center;gap:.45rem;background:#ecfdf3;color:#067647;
    border:1px solid #abefc6;border-radius:999px;padding:.28rem .85rem;font-size:.8rem;
    font-weight:600;margin-bottom:1.1rem}
.av i{width:7px;height:7px;border-radius:50%;background:#17b26a;display:block}
h1{font-size:2.7rem;font-weight:800;letter-spacing:-.03em;margin-bottom:.35rem}
.role{font-size:1.1rem;color:#5b6472;margin-bottom:1rem}
.role b{color:#e8820c}
.lede{color:#5b6472;max-width:40rem;margin-bottom:2rem}

.counter{display:flex;align-items:baseline;gap:.7rem;margin-bottom:.9rem}
.counter .big{font-size:3.4rem;font-weight:800;letter-spacing:-.04em;line-height:1}
.counter .of{font-size:1.1rem;color:#8b94a3}
.counter .lbl{font-size:.9rem;color:#5b6472;margin-left:auto}

.weeks{display:grid;grid-template-columns:repeat(26,1fr);gap:5px;margin-bottom:.8rem}
.wk{aspect-ratio:1;border-radius:3px;background:#eceff3;border:1px solid #e1e5eb}
.wk.done{background:#e8820c;border-color:#d4760a}
.wk.next{background:#fff;border:1.5px dashed #e8820c}
.legend{display:flex;gap:1.2rem;font-size:.8rem;color:#8b94a3;margin-bottom:2rem}
.legend i{width:11px;height:11px;border-radius:2px;display:inline-block;
  vertical-align:-1px;margin-right:.35rem}

.cta{display:flex;flex-wrap:wrap;gap:.6rem}
.btn{padding:.6rem 1.25rem;border-radius:6px;font-size:.93rem;font-weight:600}
.b1{background:#16181d;color:#fff}
.b2{border:1px solid #dde1e7;color:#16181d}

section{padding:2.8rem 0;border-top:1px solid #eceff3}
.eyebrow{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  color:#e8820c;margin-bottom:.35rem}
h2{font-size:1.5rem;font-weight:700;letter-spacing:-.02em;margin-bottom:.4rem}
.sub{color:#5b6472;margin-bottom:1.4rem;max-width:42rem}
.phase{display:grid;grid-template-columns:3.2rem 1fr;gap:1rem;padding:.7rem 0;
  border-bottom:1px solid #f1f3f6;align-items:start}
.phase:last-child{border-bottom:0}
.phase .n{font-family:"JetBrains Mono",monospace;font-size:.8rem;color:#8b94a3;
  padding-top:.15rem}
.phase b{display:block;font-size:.98rem}
.phase span{font-size:.89rem;color:#5b6472}
@media(max-width:42rem){
  .weeks{grid-template-columns:repeat(13,1fr)}
  h1{font-size:2.1rem}
}
"""


def week_cells():
    out = []
    for i in range(1, 53):
        cls = "wk done" if i == 1 else "wk next" if i == 2 else "wk"
        out.append(f'<div class="{cls}" title="Week {i}"></div>')
    return "\n".join(out)


GRID_BODY = """
<div class="wrap hero">
  <span class="av"><i></i> Open to data engineering roles · Houston, TX</span>
  <h1>Preethi Somaraju</h1>
  <p class="role">Data Engineer &mdash; <b>building on AWS, in public</b></p>
  <p class="lede">A decade moving data from where it is produced to where
  decisions get made. Right now I am rebuilding that skill set on AWS &mdash;
  one lab a week, every week, for a year.</p>

  <div class="counter">
    <span class="big">01</span><span class="of">/ 52</span>
    <span class="lbl">labs shipped &mdash; Terraform, tested, written up</span>
  </div>

  <div class="weeks">
%%WEEKS%%
  </div>
  <div class="legend">
    <span><i style="background:#e8820c"></i>shipped</span>
    <span><i style="background:#fff;border:1.5px dashed #e8820c"></i>in progress</span>
    <span><i style="background:#eceff3;border:1px solid #e1e5eb"></i>planned</span>
  </div>

  <div class="cta">
    <a class="btn b1" href="#">Read Lab 01</a>
    <a class="btn b2" href="#">GitHub</a>
    <a class="btn b2" href="#">LinkedIn</a>
    <a class="btn b2" href="#">R&eacute;sum&eacute;</a>
  </div>
</div>

<section><div class="wrap">
  <p class="eyebrow">The plan</p>
  <h2>Eight phases, 52 labs</h2>
  <p class="sub">From an empty AWS account to a capstone lakehouse. Every lab
  states its cost before the first command and is torn down after.</p>
  <div class="phase"><div class="n">01–06</div><div><b>Identity &amp; security</b>
    <span>IAM, permissions boundaries, CloudTrail, KMS, VPC for data services</span></div></div>
  <div class="phase"><div class="n">07–14</div><div><b>Lake &amp; catalog</b>
    <span>Partitioning, Parquet, Glue Catalog, Athena tuning, Iceberg, Lake Formation</span></div></div>
  <div class="phase"><div class="n">15–22</div><div><b>Batch ETL</b>
    <span>Glue PySpark, bookmarks, schema drift, EMR Serverless, dbt on Fargate</span></div></div>
  <div class="phase"><div class="n">23–30</div><div><b>Streaming</b>
    <span>Kinesis, Firehose, Managed Flink, MSK, CDC with DMS, streaming Iceberg</span></div></div>
  <div class="phase"><div class="n">31–38</div><div><b>Warehousing</b>
    <span>Redshift Serverless, dist/sort keys, Spectrum, DynamoDB, SCD Type 2</span></div></div>
  <div class="phase"><div class="n">39–44</div><div><b>Orchestration</b>
    <span>Step Functions, MWAA, event-driven pipelines, backfills and late data</span></div></div>
  <div class="phase"><div class="n">45–50</div><div><b>Governance &amp; ML</b>
    <span>QuickSight, lineage, PII masking with Macie, Feature Store, Bedrock</span></div></div>
  <div class="phase"><div class="n">51–52</div><div><b>Operations &amp; capstone</b>
    <span>Pipeline observability, cost, and a full lakehouse end to end</span></div></div>
</div></section>
"""

PAGES = [
    ("09-pipeline.html", "Pipeline — career as a data flow", PIPELINE_CSS, PIPELINE_BODY),
    ("10-query.html", "Query — portfolio as a SQL client", QUERY_CSS, QUERY_BODY),
    ("11-grid.html", "52-week grid — progress is the hero",
     GRID_CSS, GRID_BODY.replace("%%WEEKS%%", week_cells())),
]

for fname, title, css, body in PAGES:
    (OUT / fname).write_text(HEAD.format(title=title, css=css, body=body), encoding="utf-8")
    print(f"wrote {fname}  ({title})")
