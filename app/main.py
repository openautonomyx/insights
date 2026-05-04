from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.insight_engine import InsightEngine

app = FastAPI(title="Autonomyx Insights")
engine = InsightEngine()


HOMEPAGE_HTML = """
<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Autonomyx Insights</title>
  <style>
    :root { --bg: #070b14; --card: #101827; --muted: #9aa4b2; --text: #ecf2ff; --accent: #6ea8fe; --accent2: #86efac; }
    * { box-sizing: border-box; }
    body { margin: 0; font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background: radial-gradient(circle at top right, #12213b, var(--bg)); color: var(--text); }
    .container { max-width: 1120px; margin: 0 auto; padding: 28px 20px 72px; }
    .nav { display:flex; justify-content:space-between; align-items:center; margin-bottom: 40px; }
    .brand { font-weight:700; letter-spacing:.3px; }
    .btn { border: 1px solid #2d3d57; border-radius: 10px; padding: 10px 14px; color: var(--text); text-decoration: none; display:inline-block; }
    .btn.primary { background: linear-gradient(90deg,#3b82f6,#60a5fa); border: none; font-weight: 600; }
    .hero { display:grid; grid-template-columns: 1.1fr .9fr; gap:24px; align-items:center; margin-bottom: 56px; }
    h1 { font-size: 46px; line-height:1.1; margin:0 0 10px; }
    h2 { font-size: 34px; margin: 0 0 14px; }
    h3 { margin:0 0 6px; }
    p { color: var(--muted); line-height:1.6; }
    .card { background: rgba(16,24,39,.86); border: 1px solid #263448; border-radius: 14px; padding: 18px; }
    .grid3 { display:grid; grid-template-columns: repeat(3,1fr); gap: 14px; }
    .section { margin: 56px 0; }
    .pipeline { text-align:center; padding:16px; font-weight:600; }
    .demo input { width:100%; padding:12px; border-radius:10px; border:1px solid #334155; background:#0b1220; color:var(--text); }
    ul { margin:8px 0 0 20px; color: var(--muted); }
    .chips { display:flex; gap:8px; flex-wrap: wrap; }
    .chip { padding:8px 12px; border-radius:999px; border:1px solid #2d3d57; color:#c6d3e6; }
    .pricing { display:grid; grid-template-columns: repeat(3,1fr); gap:14px; }
    .price { font-size:28px; font-weight:700; color:#dbeafe; }
    footer { margin-top:48px; color:#8aa0bd; display:flex; gap:18px; flex-wrap:wrap; }
    @media (max-width: 900px){ .hero,.grid3,.pricing{grid-template-columns:1fr;} h1{font-size:36px;} }
  </style>
</head>
<body>
  <div class=\"container\">
    <div class=\"nav\"><div class=\"brand\">Autonomyx Insights</div><a class=\"btn\" href=\"#pricing\">Pricing</a></div>

    <section class=\"hero\">
      <div>
        <h1>Decision Intelligence for a Faster World</h1>
        <p>Autonomyx Insights turns live web signals into structured, actionable decisions—before trends become obvious.</p>
        <a class=\"btn primary\" href=\"#demo\">Generate First Insight</a>
        <a class=\"btn\" href=\"#solution\" style=\"margin-left:8px\">View Sample Report</a>
      </div>
      <div class=\"card\">
        <h3>🧠 Emerging Trend Detected</h3>
        <p><strong>Topic:</strong> AI Agent Infrastructure<br><strong>Confidence:</strong> 87%</p>
        <p><strong>Insight</strong></p>
        <ul><li>Tool-based agents are replacing monolithic LLM workflows</li><li>Open-source frameworks are accelerating adoption</li><li>Enterprise pilots increasing rapidly</li></ul>
        <p><strong>Recommendation:</strong> → Invest in agent orchestration layer now</p>
      </div>
    </section>

    <section class=\"section\">
      <h2>Traditional Intelligence Is Too Slow</h2>
      <div class=\"grid3\">
        <div class=\"card\"><h3>Consulting Firms</h3><ul><li>Expensive</li><li>Slow cycles</li><li>Static reports</li></ul></div>
        <div class=\"card\"><h3>News & Blogs</h3><ul><li>No synthesis</li><li>No prioritization</li><li>No context</li></ul></div>
        <div class=\"card\"><h3>Internal Teams</h3><ul><li>Limited visibility</li><li>Biased signals</li><li>Reactive decisions</li></ul></div>
      </div>
      <p>By the time insights arrive, the opportunity is already gone.</p>
    </section>

    <section id=\"solution\" class=\"section\">
      <h2>We Turn the Web Into Decision Intelligence</h2>
      <div class=\"card pipeline\">Web Signals → Agentic Analysis → Pattern Detection → Insight Engine → Decision Output</div>
      <ul><li>Scans real-time digital signals</li><li>Detects emerging market patterns</li><li>Synthesizes cross-domain intelligence</li><li>Generates decision-ready outputs</li></ul>
      <p><strong>Not summaries. Not dashboards. Actual decisions.</strong></p>
    </section>

    <section id=\"demo\" class=\"section demo\">
      <h2>See Intelligence in Action</h2>
      <input value=\"AI agents in SaaS?\" aria-label=\"Ask a question\" />
      <div class=\"card\" style=\"margin-top:10px\"><p><strong>Insight Generated in 3.2s</strong><br>📊 Market Direction: Strong Uptrend</p></div>
    </section>

    <section class=\"section\">
      <h2>Insights Tailored to Your Context</h2>
      <p>Every business sees different signals. We adapt to industry, stage, geography, and strategy focus.</p>
      <div class=\"chips\"><span class=\"chip\">SaaS</span><span class=\"chip\">AI</span><span class=\"chip\">Fintech</span><span class=\"chip\">Automation</span><span class=\"chip\">DevTools</span></div>
    </section>

    <section id=\"pricing\" class=\"section\">
      <h2>Simple Pricing. No Complexity.</h2>
      <div class=\"pricing\">
        <div class=\"card\"><h3>Starter</h3><div class=\"price\">$19/mo</div><ul><li>Weekly insights</li><li>Trend summaries</li></ul></div>
        <div class=\"card\"><h3>Pro (Recommended)</h3><div class=\"price\">$99/mo</div><ul><li>Real-time insights</li><li>Custom focus areas</li><li>Decision recommendations</li></ul></div>
        <div class=\"card\"><h3>Enterprise</h3><div class=\"price\">Custom</div><ul><li>API access</li><li>Team workflows</li><li>Private streams</li></ul></div>
      </div>
      <p><strong>Start with your first insight free</strong></p>
    </section>

    <section class=\"section\"><h2>Stop Waiting for Reports. Start Acting on Intelligence.</h2><p>The best decisions are made before the market agrees with them.</p><a class=\"btn primary\" href=\"#demo\">Generate Your First Insight</a></section>
    <footer><span>Product</span><span>API</span><span>Docs</span><span>Pricing</span><span>Contact</span></footer>
  </div>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def homepage() -> str:
    return HOMEPAGE_HTML


@app.post("/decide")
def decide(payload: dict):
    return engine.analyze(
        agent_output=payload.get("input", ""),
        context=payload.get("context", {}),
    )


@app.get("/health")
def health():
    return {"status": "ok"}
