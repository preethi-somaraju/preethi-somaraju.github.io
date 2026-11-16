"""Second batch of homepage aesthetic variants. Reuses the content from build.py.

    python previews/build2.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import BODY, SHARED, PAGE  # noqa: E402

OUT = pathlib.Path(__file__).parent

THEMES = {
# ---------------------------------------------------------------- 5
"05-swiss": dict(
  name="Swiss — grid, bold type",
  badge='<span class="badge">Open to data engineering roles / Houston TX</span>',
  role='Data Engineer / <em>AWS</em>',
  css="""
body{font-family:"Helvetica Neue",Inter,Arial,sans-serif;font-size:16.5px;line-height:1.55;
     color:#111;background:#fff;-webkit-font-smoothing:antialiased}
.hero{padding:3.2rem 0 2.4rem;border-bottom:3px solid #111}
.badge{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.14em;
       text-transform:uppercase;color:#e8341c;margin-bottom:1.4rem}
h1{font-size:4.6rem;font-weight:800;letter-spacing:-.045em;line-height:.92;margin-bottom:.7rem}
.role{font-size:1.5rem;font-weight:700;letter-spacing:-.02em;margin-bottom:1rem}
.role em{color:#e8341c;font-style:normal}
.lede{font-size:1.02rem;color:#444;max-width:34rem;margin-bottom:1.7rem}
.btn{border-radius:0;font-size:.82rem;letter-spacing:.06em;text-transform:uppercase}
.btn-main{background:#111;color:#fff}
.btn-ghost{border:2px solid #111;color:#111}
.stats{border-top:2px solid #111;gap:0;display:grid;grid-template-columns:repeat(4,1fr)}
.stat{border-right:1px solid #ddd;padding-right:1rem}
.stat:last-child{border-right:0}
.stat b{font-size:1.9rem;letter-spacing:-.03em}
.stat span{color:#666;font-size:.76rem;text-transform:uppercase;letter-spacing:.07em}
.eyebrow{color:#e8341c;letter-spacing:.14em}
h2{font-size:2.4rem;font-weight:800;letter-spacing:-.035em;margin-bottom:.5rem}
.sec-lede{color:#555}
section+section{border-top:1px solid #ddd}
.feature{background:#111;color:#fff;padding:2.4rem 2.2rem}
.feature h3{font-size:1.7rem;font-weight:800;letter-spacing:-.025em;margin-bottom:.6rem}
.feature p{color:#aaa;max-width:40rem}
.chip{border:1px solid #444;color:#ddd;border-radius:0;text-transform:uppercase;
      font-size:.7rem;letter-spacing:.06em}
.progress{background:#333;border-radius:0}.progress i{background:#e8341c}
.progress-label{color:#888;text-transform:uppercase;letter-spacing:.06em;font-size:.72rem}
.card{border:1px solid #ddd;border-radius:0}
.card h3{font-size:1.05rem;font-weight:800;letter-spacing:-.015em}
.card p{color:#555}
.tag{border:1px solid #ddd;border-radius:0;color:#666;text-transform:uppercase;
     font-size:.68rem;letter-spacing:.05em}
"""),
# ---------------------------------------------------------------- 6
"06-blueprint": dict(
  name="Blueprint — technical drawing",
  badge='<span class="badge">◆ Open to data engineering roles · Houston, TX</span>',
  role='Data Engineer &mdash; <em>AWS data platforms</em>',
  css="""
body{font-family:"IBM Plex Sans",Inter,system-ui,sans-serif;font-size:16.5px;line-height:1.6;
     color:#0f2231;background:#f4f8fb;
     background-image:linear-gradient(#dce7ef 1px,transparent 1px),
                      linear-gradient(90deg,#dce7ef 1px,transparent 1px);
     background-size:28px 28px}
.hero{padding:3.6rem 0 2.6rem;border-bottom:1px solid #bcd0dd}
.badge{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.76rem;
       color:#0a6e8a;border:1px solid #9cc4d4;background:#e8f4f9;padding:.28rem .75rem;
       margin-bottom:1.2rem}
h1{font-size:3rem;font-weight:700;letter-spacing:-.03em;color:#0f2231;margin-bottom:.4rem}
.role{font-family:"IBM Plex Mono",monospace;font-size:1rem;color:#0a6e8a;margin-bottom:1rem}
.role em{color:#0f2231;font-style:normal;font-weight:600}
.lede{color:#41606f;max-width:40rem;margin-bottom:1.7rem}
.btn{border-radius:2px;font-size:.88rem}
.btn-main{background:#0a6e8a;color:#fff}
.btn-ghost{border:1px solid #9cc4d4;color:#0f2231;background:rgba(255,255,255,.7)}
.stats{border-top:1px dashed #9cc4d4}
.stat b{color:#0f2231;font-family:"IBM Plex Mono",monospace}
.stat span{color:#5d7f8f;font-size:.78rem}
.eyebrow{color:#0a6e8a;font-family:"IBM Plex Mono",monospace;letter-spacing:.08em}
h2{font-size:1.75rem;color:#0f2231;font-weight:700;letter-spacing:-.02em;margin-bottom:.5rem}
.sec-lede{color:#41606f}
section+section{border-top:1px solid #bcd0dd}
.feature{background:rgba(255,255,255,.85);border:1px solid #9cc4d4;border-left:4px solid #0a6e8a;
         padding:2rem;backdrop-filter:blur(2px)}
.feature h3{font-size:1.3rem;color:#0f2231;margin-bottom:.5rem}
.feature p{color:#41606f;max-width:40rem}
.chip{background:#e8f4f9;border:1px solid #9cc4d4;color:#0a6e8a;border-radius:2px;
      font-family:"IBM Plex Mono",monospace;font-size:.74rem}
.progress{background:#d4e4ed}.progress i{background:#0a6e8a}
.progress-label{color:#5d7f8f;font-family:"IBM Plex Mono",monospace;font-size:.76rem}
.card{background:rgba(255,255,255,.85);border:1px solid #bcd0dd;border-radius:2px}
.card h3{color:#0f2231}.card p{color:#41606f}
.tag{background:#eef5f9;border:1px solid #bcd0dd;border-radius:2px;color:#5d7f8f;
     font-family:"IBM Plex Mono",monospace;font-size:.72rem}
"""),
# ---------------------------------------------------------------- 7
"07-warm": dict(
  name="Warm — approachable, soft",
  badge='<span class="badge"><span class="dot"></span> Open to data engineering roles · Houston, TX</span>',
  role='Data Engineer, <em>building on AWS</em>',
  css="""
body{font-family:"Inter",system-ui,-apple-system,sans-serif;font-size:17px;line-height:1.68;
     color:#2e2a26;background:#fdfaf6}
.hero{padding:4rem 0 3rem}
.badge{display:inline-flex;align-items:center;gap:.5rem;background:#fff;color:#8a5a28;
       border:1px solid #ecd9c0;border-radius:999px;padding:.35rem .95rem;font-size:.82rem;
       font-weight:600;margin-bottom:1.3rem;box-shadow:0 1px 3px rgba(120,90,50,.06)}
.dot{width:7px;height:7px;border-radius:50%;background:#d98a3d}
h1{font-size:3rem;font-weight:700;letter-spacing:-.03em;color:#241f1a;margin-bottom:.45rem}
.role{font-size:1.2rem;color:#5c5349;margin-bottom:1rem}
.role em{color:#c2741f;font-style:normal;font-weight:600}
.lede{color:#6b6157;max-width:40rem;margin-bottom:1.8rem}
.btn{border-radius:10px;font-size:.93rem}
.btn-main{background:#241f1a;color:#fdfaf6}
.btn-ghost{border:1px solid #e4d7c6;color:#241f1a;background:#fff}
.stats{border-top:1px solid #ecdfd0}
.stat b{color:#241f1a}.stat span{color:#8a7e70}
.eyebrow{color:#c2741f}
h2{font-size:1.8rem;color:#241f1a;font-weight:700;letter-spacing:-.02em;margin-bottom:.5rem}
.sec-lede{color:#6b6157}
section+section{border-top:1px solid #ecdfd0}
.feature{background:#fff;border:1px solid #ecdfd0;border-radius:16px;padding:2.1rem;
         box-shadow:0 6px 22px -12px rgba(120,90,50,.22)}
.feature h3{font-size:1.35rem;color:#241f1a;margin-bottom:.5rem}
.feature p{color:#6b6157;max-width:40rem}
.chip{background:#fdf6ed;border:1px solid #f0e2cf;color:#8a5a28;border-radius:999px}
.progress{background:#f1e6d8}.progress i{background:#d98a3d}
.progress-label{color:#8a7e70}
.card{background:#fff;border:1px solid #ecdfd0;border-radius:14px}
.card h3{color:#241f1a}.card p{color:#6b6157}
.tag{background:#fdf6ed;border:1px solid #f0e2cf;border-radius:999px;color:#8a5a28}
"""),
# ---------------------------------------------------------------- 8
"08-split": dict(
  name="Split — fixed sidebar",
  badge='<span class="badge"><span class="dot"></span> Open to roles · Houston, TX</span>',
  role='Data Engineer &mdash; <em>building on AWS</em>',
  css="""
body{font-family:"Inter",system-ui,sans-serif;font-size:16.5px;line-height:1.62;
     color:#17202a;background:#fff}
.wrap{max-width:38rem;margin:0;padding:0 2.5rem}
.hero{position:fixed;top:0;left:0;width:36%;height:100vh;background:#111820;color:#e8edf2;
      display:flex;align-items:center;padding:0;border-right:1px solid #1e2730}
.hero .wrap{max-width:none;padding:0 2.8rem}
.badge{display:inline-flex;align-items:center;gap:.5rem;background:rgba(255,255,255,.07);
       border:1px solid rgba(255,255,255,.16);border-radius:999px;padding:.28rem .8rem;
       font-size:.76rem;font-weight:600;margin-bottom:1.1rem;color:#b7c3cf}
.dot{width:7px;height:7px;border-radius:50%;background:#45c47f}
h1{font-size:2.35rem;font-weight:800;letter-spacing:-.03em;color:#fff;margin-bottom:.35rem}
.role{font-size:1rem;color:#9fb0bf;margin-bottom:.9rem}
.role em{color:#ffb547;font-style:normal}
.lede{color:#8d9dab;font-size:.93rem;margin-bottom:1.5rem}
.cta{flex-direction:column;align-items:flex-start;gap:.45rem}
.btn{border-radius:5px;font-size:.86rem;padding:.45rem 1rem}
.btn-main{background:#ffb547;color:#111820}
.btn-ghost{border:1px solid rgba(255,255,255,.2);color:#e8edf2}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:1.1rem;border-top:1px solid rgba(255,255,255,.14)}
.stat b{font-size:1.2rem;color:#fff}.stat span{color:#7d8c9a;font-size:.76rem}
section{padding:3.2rem 0;margin-left:36%}
.eyebrow{color:#c07f12}
h2{font-size:1.6rem;color:#17202a;font-weight:700;letter-spacing:-.02em;margin-bottom:.5rem}
.sec-lede{color:#5c6872}
section+section{border-top:1px solid #e8ecef}
.feature{background:#f7f9fb;border:1px solid #e3e8ec;border-left:4px solid #ffb547;
         border-radius:6px;padding:1.9rem}
.feature h3{font-size:1.25rem;color:#17202a;margin-bottom:.5rem}
.feature p{color:#5c6872}
.chip{background:#fff;border:1px solid #e3e8ec;color:#5c6872;border-radius:4px}
.progress{background:#e3e8ec}.progress i{background:#ffb547}
.progress-label{color:#7d8c9a}
.grid{grid-template-columns:1fr}
.card{border:1px solid #e8ecef;border-radius:6px}
.card h3{color:#17202a}.card p{color:#5c6872}
.tag{background:#f7f9fb;border:1px solid #e8ecef;border-radius:4px;color:#5c6872}
@media(max-width:60rem){
  .hero{position:static;width:auto;height:auto;padding:2.5rem 0}
  section{margin-left:0}
  .wrap{max-width:46rem;margin:0 auto;padding:0 1.5rem}
  .cta{flex-direction:row}
  .grid{grid-template-columns:repeat(auto-fit,minmax(16rem,1fr))}
}
"""),
}

for slug, t in THEMES.items():
    html = PAGE.format(name=t["name"], shared=SHARED, css=t["css"],
                       body=BODY.format(badge=t["badge"], role=t["role"]))
    (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
    print(f"wrote {slug}.html  ({t['name']})")
