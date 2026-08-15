<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Application Calendar — Eidee Tan · Fall 2027 Entry</title>
<style>
  :root{
    --ink:#1d232a; --ink2:#4a545e; --ink3:#7a828a; --line:#dde3e8; --bg:#f6f8fa;
    --stanford:#8C1515; --princeton:#E77500; --harvard:#A51C30; --yale:#00356B;
    --mit:#750014; --uchicago:#800000; --cmu:#C41230; --upenn:#011F5B;
    --cornell:#B31B1B; --berkeley:#003262; --uiuc:#13294B; --uw:#4B2E83;
  }
  *{box-sizing:border-box}
  html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  body{font-family:Carlito,Calibri,'Segoe UI',system-ui,sans-serif;color:var(--ink);
       margin:0;background:#fff;font-size:10.2pt;line-height:1.45}
  .page{max-width:8.1in;margin:0 auto;padding:20pt 8pt}

  .hero{background:linear-gradient(120deg,#1d2a3a 0%,#0e1620 100%);color:#fff;
        border-radius:8pt;padding:20pt 22pt;margin-bottom:14pt}
  .hero .eyebrow{font-size:8pt;letter-spacing:2.4pt;text-transform:uppercase;opacity:.8;margin-bottom:6pt}
  .hero h1{margin:0 0 4pt;font-size:20pt;line-height:1.15}
  .hero p{margin:4pt 0 0;font-size:9.6pt;opacity:.9;max-width:52em}
  .stats{display:flex;gap:10pt;margin-top:12pt;flex-wrap:wrap}
  .stat{background:rgba(255,255,255,.09);border:.6pt solid rgba(255,255,255,.22);
        border-radius:6pt;padding:8pt 12pt;min-width:104pt}
  .stat b{display:block;font-size:15pt;line-height:1.1}
  .stat span{font-size:8.2pt;opacity:.85}

  h2{font-size:13.5pt;margin:18pt 0 4pt;color:var(--ink)}
  h2 .n{display:inline-block;background:var(--ink);color:#fff;border-radius:50%;
        width:15pt;height:15pt;line-height:15pt;text-align:center;font-size:9pt;margin-right:5pt}
  .sub{color:var(--ink2);font-size:9.2pt;margin:0 0 10pt}

  /* Season band */
  .band{display:flex;border-radius:6pt;overflow:hidden;margin:8pt 0 4pt;border:.7pt solid var(--line)}
  .band .seg{padding:8pt 9pt;font-size:8.6pt;border-right:.7pt solid var(--line)}
  .band .seg:last-child{border-right:none}
  .band .seg b{display:block;font-size:9.4pt;margin-bottom:2pt}
  .band .seg small{color:var(--ink2);display:block;line-height:1.35}
  .s1{background:#eef4fb;flex:1.1}.s2{background:#fdf3e7;flex:1.5}.s3{background:#fbecec;flex:1.3}
  .s4{background:#eef9f1;flex:1.2}.s5{background:#f3eefb;flex:1.2}

  /* Month agenda */
  .months{display:grid;grid-template-columns:repeat(3,1fr);gap:9pt;margin-top:8pt}
  .month{border:.8pt solid var(--line);border-radius:6pt;overflow:hidden;
         break-inside:avoid;page-break-inside:avoid}
  .month h3{margin:0;background:var(--bg);padding:5pt 9pt;font-size:10pt;
            border-bottom:.8pt solid var(--line)}
  .month ul{list-style:none;margin:0;padding:5pt 7pt 7pt}
  .month li{display:flex;gap:5pt;align-items:baseline;padding:2.4pt 0;font-size:8.5pt;line-height:1.3}
  .d{flex:0 0 34pt;font-weight:700;color:var(--ink2);font-size:8pt}
  .chip{flex:1;border-left:2.6pt solid var(--c,#888);padding-left:5pt}
  .chip b{color:var(--ink)}
  .chip .tag{display:inline-block;font-size:6.8pt;font-weight:700;letter-spacing:.4pt;
             text-transform:uppercase;color:#fff;background:var(--c,#888);
             border-radius:2pt;padding:.4pt 3pt;margin-left:3pt;vertical-align:middle}
  .music .tag.music{background:#8a6d1a}
  li.music .chip{background:#fdfaf0;border-radius:0 3pt 3pt 0}
  li.aid .d::after{content:""}

  /* School cards */
  .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9pt}
  .card{border:.8pt solid var(--line);border-top:3pt solid var(--c,#888);border-radius:6pt;
        padding:7pt 9pt 8pt;break-inside:avoid;page-break-inside:avoid}
  .card h3{margin:0 0 1pt;font-size:9.8pt;color:var(--c,#333)}
  .card .plan{font-size:7.4pt;color:var(--ink3);margin-bottom:5pt;text-transform:uppercase;letter-spacing:.5pt}
  .card table{width:100%;border-collapse:collapse;font-size:8.2pt}
  .card td{padding:1.8pt 0;vertical-align:top;border-bottom:.5pt dotted #e7ebef}
  .card tr:last-child td{border-bottom:none}
  .card td:first-child{color:var(--ink2);width:47%;padding-right:4pt}
  .card td:last-child{font-weight:700}
  .card .warn{font-weight:400;font-size:7.6pt;color:#8a4b00}

  .legendrow{display:flex;gap:12pt;flex-wrap:wrap;font-size:8.2pt;color:var(--ink2);margin:6pt 0 2pt}
  .legendrow span{display:inline-flex;align-items:center;gap:4pt}
  .sw{width:9pt;height:9pt;border-radius:2pt;display:inline-block}

  .note{background:#fdf6e9;border:.8pt solid #ecd9ae;border-radius:6pt;padding:9pt 12pt;
        font-size:8.8pt;margin-top:14pt}
  .note b{color:#7a5200}
  footer{margin-top:14pt;color:var(--ink3);font-size:7.8pt;border-top:.7pt solid var(--line);padding-top:6pt}
  @media print{ .page{max-width:none;padding:0} .months{grid-template-columns:repeat(3,1fr)} }
  @media (max-width:700px){ .months,.cards{grid-template-columns:1fr 1fr} }
  @media (max-width:480px){ .months,.cards{grid-template-columns:1fr} }
</style>
</head>
<body>
<div class="page">

<div class="hero">
  <div class="eyebrow">Application Calendar · Prepared for Eidee Tan &amp; Family</div>
  <h1>Every date that matters — Fall 2027 entry</h1>
  <p>All deadlines for the twelve universities under consideration, consolidated from the program dossiers
     (researched against official sources Aug 15, 2026). Dates are the published cycle's — re-verify each when
     applications open in fall 2026.</p>
  <div class="stats">
    <div class="stat"><b>Oct 15</b><span>earliest hard date (Stanford REA + arts portfolio)</span></div>
    <div class="stat"><b>Nov 1–2</b><span>nine early deadlines land together</span></div>
    <div class="stat"><b>Dec 1</b><span>NEC dual-degree + CMU Music (both with violin prescreen)</span></div>
    <div class="stat"><b>May 1</b><span>Decision Day — one choice</span></div>
  </div>
</div>

<h2><span class="n">1</span> The shape of the year</h2>
<p class="sub">Five seasons, in order. The heavy lifting is September–December; spring is auditions and decisions.</p>
<div class="band">
  <div class="seg s1"><b>Aug – Sep 2026</b><small>UW &amp; UIUC apps open · UC app drafting · optional SAT EBRW retake (Aug/Sep sittings) · essays</small></div>
  <div class="seg s2"><b>Oct – Nov</b><small>Stanford arts REA Oct 15 · UC files Oct 1–Nov 30 · <b>Nov 1–2 early wave</b> · UW Nov 15 · UC Nov 30</small></div>
  <div class="seg s3"><b>Dec</b><small><b>Dec 1: NEC + CMU Music prescreens</b> · early decisions mid-Dec · RD essays finalized</small></div>
  <div class="seg s4"><b>Jan – Feb</b><small>RD wave Jan 1–5 · NEC recs Jan 15 · <b>Feb: NEC live audition (Boston)</b> · aid forms</small></div>
  <div class="seg s5"><b>Mar – May</b><small>Decisions Feb–Apr · aid offers · <b>May 1: commit</b></small></div>
</div>

<h2><span class="n">2</span> Month-by-month master checklist</h2>
<p class="sub">Every dated obligation, in the order it arrives. Music-related items are shaded gold. Color bar = school (named on every line).</p>

<div class="months">
  <div class="month"><h3>September 2026</h3><ul>
    <li><span class="d">Sep 1</span><div class="chip" style="--c:var(--uiuc)"><b>UIUC</b> application opens</div></li>
    <li><span class="d">Sep&nbsp;(mid)</span><div class="chip" style="--c:#666"><b>All schools</b> — confirm 2026–27 dates as sites update</div></li>
    <li class="music"><span class="d">Sep</span><div class="chip" style="--c:#8a6d1a"><b>Violin</b> — record prescreen/arts-supplement footage early<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
  </ul></div>

  <div class="month"><h3>October 2026</h3><ul>
    <li><span class="d">Oct 1</span><div class="chip" style="--c:var(--berkeley)"><b>UC Berkeley</b> filing window opens (through Nov 30)</div></li>
    <li><span class="d">Oct 1</span><div class="chip" style="--c:#666"><b>Aid</b> — CSS Profile &amp; FAFSA open</div></li>
    <li class="music"><span class="d">Oct 15</span><div class="chip" style="--c:var(--stanford)"><b>Stanford</b> REA <i>with arts portfolio</i>: application due<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li class="music"><span class="d">Oct 20</span><div class="chip" style="--c:var(--stanford)"><b>Stanford</b> REA portfolio materials due<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li><span class="d">Oct 31</span><div class="chip" style="--c:var(--stanford)"><b>Stanford</b> REA: last SAT sitting (ACT: end of Sep)</div></li>
  </ul></div>

  <div class="month"><h3>November 2026</h3><ul>
    <li><span class="d">Nov 1</span><div class="chip" style="--c:var(--harvard)"><b>Harvard</b> REA + aid forms (CSS/FAFSA/IDOC)</div></li>
    <li><span class="d">Nov 1</span><div class="chip" style="--c:var(--yale)"><b>Yale</b> SCEA</div></li>
    <li><span class="d">Nov 1</span><div class="chip" style="--c:var(--princeton)"><b>Princeton</b> SCEA</div></li>
    <li><span class="d">Nov 1</span><div class="chip" style="--c:var(--stanford)"><b>Stanford</b> REA (no-portfolio track)</div></li>
    <li><span class="d">Nov 1</span><div class="chip" style="--c:var(--mit)"><b>MIT</b> EA (own portal)</div></li>
    <li><span class="d">Nov 1</span><div class="chip" style="--c:var(--upenn)"><b>UPenn</b> ED (binding)</div></li>
    <li><span class="d">Nov 1</span><div class="chip" style="--c:var(--cornell)"><b>Cornell</b> ED (binding; materials Nov 13)</div></li>
    <li><span class="d">Nov 1</span><div class="chip" style="--c:var(--uiuc)"><b>UIUC</b> Early Action (materials Nov 7)</div></li>
    <li><span class="d">Nov 2</span><div class="chip" style="--c:var(--uchicago)"><b>UChicago</b> EA / ED I</div></li>
    <li class="music"><span class="d">Nov 6</span><div class="chip" style="--c:var(--princeton)"><b>Princeton</b> SCEA arts supplement<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li class="music"><span class="d">Nov 8</span><div class="chip" style="--c:var(--yale)"><b>Yale</b> SCEA music supplement<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li><span class="d">Nov 15</span><div class="chip" style="--c:var(--uw)"><b>UW</b> single application deadline</div></li>
    <li class="aid"><span class="d">Nov 15</span><div class="chip" style="--c:#666"><b>Aid</b> — Stanford REA · UChicago EA/ED I · CMU ED · Cornell ED forms</div></li>
    <li><span class="d">Nov 30</span><div class="chip" style="--c:var(--berkeley)"><b>UC Berkeley</b> application closes</div></li>
    <li><span class="d">Nov 30</span><div class="chip" style="--c:var(--mit)"><b>MIT</b> EA: last SAT/ACT date · aid forms due</div></li>
  </ul></div>

  <div class="month"><h3>December 2026</h3><ul>
    <li class="music"><span class="d">Dec 1</span><div class="chip" style="--c:var(--harvard)"><b>Harvard–NEC</b> dual degree: NEC application + prescreen video<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li class="music"><span class="d">Dec 1</span><div class="chip" style="--c:var(--cmu)"><b>CMU School of Music</b> application + violin prescreen (Acceptd); no ED for Music<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li class="music"><span class="d">Dec 5</span><div class="chip" style="--c:var(--stanford)"><b>Stanford</b> RD <i>with arts portfolio</i>: application due (materials Dec 10)<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li><span class="d">Mid-Dec</span><div class="chip" style="--c:#666"><b>Early decisions</b> — Harvard, Yale, Princeton, Stanford, MIT, UPenn, Cornell, UChicago</div></li>
    <li><span class="d">Dec 31</span><div class="chip" style="--c:var(--mit)"><b>MIT</b> RA: last SAT/ACT date (scores by Feb 15)</div></li>
  </ul></div>

  <div class="month"><h3>January 2027</h3><ul>
    <li><span class="d">Jan 1</span><div class="chip" style="--c:var(--harvard)"><b>Harvard</b> RD</div></li>
    <li><span class="d">Jan 1</span><div class="chip" style="--c:var(--princeton)"><b>Princeton</b> RD</div></li>
    <li><span class="d">Jan 2</span><div class="chip" style="--c:var(--yale)"><b>Yale</b> RD</div></li>
    <li><span class="d">Jan 2</span><div class="chip" style="--c:var(--cornell)"><b>Cornell</b> RD (materials Jan 19)</div></li>
    <li><span class="d">Jan 4</span><div class="chip" style="--c:var(--mit)"><b>MIT</b> Regular Action</div></li>
    <li><span class="d">Jan 4</span><div class="chip" style="--c:var(--uchicago)"><b>UChicago</b> ED II / RD</div></li>
    <li><span class="d">Jan 4</span><div class="chip" style="--c:var(--cmu)"><b>CMU</b> RD (non-Music colleges)</div></li>
    <li><span class="d">Jan 5</span><div class="chip" style="--c:var(--stanford)"><b>Stanford</b> RD</div></li>
    <li><span class="d">Jan 5</span><div class="chip" style="--c:var(--upenn)"><b>UPenn</b> RD</div></li>
    <li><span class="d">Jan 5</span><div class="chip" style="--c:var(--uiuc)"><b>UIUC</b> regular deadline (materials Jan 11)</div></li>
    <li class="music"><span class="d">Jan 8</span><div class="chip" style="--c:var(--princeton)"><b>Princeton</b> RD arts supplement<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li class="music"><span class="d">Jan 9</span><div class="chip" style="--c:var(--yale)"><b>Yale</b> RD music supplement<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li><span class="d">Jan 10</span><div class="chip" style="--c:var(--berkeley)"><b>UC Berkeley</b> optional invited letters due</div></li>
    <li class="music"><span class="d">Jan 15</span><div class="chip" style="--c:var(--harvard)"><b>NEC</b> recommendations &amp; transcripts<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li class="aid"><span class="d">Jan 15</span><div class="chip" style="--c:var(--uchicago)"><b>UChicago</b> ED II aid forms</div></li>
    <li><span class="d">~Jan 30</span><div class="chip" style="--c:var(--uiuc)"><b>UIUC</b> EA decisions (CS+X may defer to March)</div></li>
  </ul></div>

  <div class="month"><h3>February 2027</h3><ul>
    <li class="aid"><span class="d">Feb 1</span><div class="chip" style="--c:#666"><b>Aid</b> — Harvard &amp; UPenn RD forms · UW priority date</div></li>
    <li class="music"><span class="d">Feb</span><div class="chip" style="--c:var(--harvard)"><b>NEC live audition, Boston</b> (prescreen passers; higher-than-B.M. standard)<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li class="music"><span class="d">Feb</span><div class="chip" style="--c:var(--cmu)"><b>CMU Music</b> live audition (dates TBA; Pittsburgh + NYC regionals)<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li><span class="d">Feb 15</span><div class="chip" style="--c:#666"><b>Aid</b> — Stanford, MIT, CMU, Cornell, UChicago RD forms · NEC aid priority</div></li>
    <li><span class="d">Mid-Feb</span><div class="chip" style="--c:var(--uchicago)"><b>UChicago</b> ED II decisions</div></li>
    <li><span class="d">Feb 28</span><div class="chip" style="--c:var(--uw)"><b>UW</b> Husky Promise FAFSA/WASFA date (WA residents)</div></li>
  </ul></div>

  <div class="month"><h3>March 2027</h3><ul>
    <li><span class="d">Mar 1–15</span><div class="chip" style="--c:var(--uw)"><b>UW</b> decisions</div></li>
    <li class="aid"><span class="d">Mar 2</span><div class="chip" style="--c:var(--berkeley)"><b>UC Berkeley</b> FAFSA/CADAA deadline</div></li>
    <li><span class="d">~Mar 6</span><div class="chip" style="--c:var(--uiuc)"><b>UIUC</b> regular decisions</div></li>
    <li><span class="d">Mid-Mar</span><div class="chip" style="--c:var(--mit)"><b>MIT</b> RA decisions</div></li>
    <li><span class="d">Late Mar</span><div class="chip" style="--c:#666"><b>RD decisions</b> — Harvard, Yale, Princeton, Cornell, UChicago, Berkeley</div></li>
    <li class="music"><span class="d">Late Mar</span><div class="chip" style="--c:var(--harvard)"><b>NEC</b> dual-degree decision<span class="tag music" style="--c:#8a6d1a">music</span></div></li>
    <li class="aid"><span class="d">~Mar 15</span><div class="chip" style="--c:var(--uiuc)"><b>UIUC</b> FAFSA priority date</div></li>
  </ul></div>

  <div class="month"><h3>April 2027</h3><ul>
    <li><span class="d">Early Apr</span><div class="chip" style="--c:var(--stanford)"><b>Stanford</b> RD decisions</div></li>
    <li><span class="d">Apr</span><div class="chip" style="--c:var(--upenn)"><b>UPenn</b> RD decisions</div></li>
    <li><span class="d">By Apr 1</span><div class="chip" style="--c:var(--cmu)"><b>CMU</b> decisions (incl. School of Music)</div></li>
    <li><span class="d">Apr</span><div class="chip" style="--c:#666"><b>Compare aid offers</b> — appeal windows are short</div></li>
  </ul></div>

  <div class="month"><h3>May 2027</h3><ul>
    <li><span class="d">May 1</span><div class="chip" style="--c:#666"><b>National Decision Day</b> — deposit at ONE school (UC SIR also due May 1)</div></li>
  </ul></div>
</div>

<h2><span class="n">3</span> School-by-school card file</h2>
<p class="sub">The same dates, filed per school — for pinning next to each application.</p>
<div class="cards">
  <div class="card" style="--c:var(--stanford)"><h3>Stanford</h3><div class="plan">Common App · $100 · SAT/ACT required</div>
    <table><tr><td>REA (arts track)</td><td>Oct 15 / Oct 20</td></tr>
    <tr><td>REA standard</td><td>Nov 1</td></tr>
    <tr><td>RD (arts track)</td><td>Dec 5 / Dec 10</td></tr>
    <tr><td>RD standard</td><td>Jan 5</td></tr>
    <tr><td>Aid (REA / RD)</td><td>Nov 15 / Feb 15</td></tr>
    <tr><td>Decisions</td><td>mid-Dec / early Apr</td></tr></table></div>

  <div class="card" style="--c:var(--princeton)"><h3>Princeton</h3><div class="plan">Common App · test-optional (final year)</div>
    <table><tr><td>SCEA</td><td>Nov 1</td></tr>
    <tr><td>Arts supp (SCEA/RD)</td><td>Nov 6 / Jan 8</td></tr>
    <tr><td>RD</td><td>Jan 1</td></tr>
    <tr><td>Decisions</td><td>mid-Dec / late Mar</td></tr></table></div>

  <div class="card" style="--c:var(--harvard)"><h3>Harvard (+ NEC)</h3><div class="plan">Common App · $90 · SAT/ACT required</div>
    <table><tr><td>REA + aid forms</td><td>Nov 1</td></tr>
    <tr><td>NEC app + prescreen</td><td>Dec 1</td></tr>
    <tr><td>RD</td><td>Jan 1</td></tr>
    <tr><td>NEC recs</td><td>Jan 15</td></tr>
    <tr><td>NEC live audition</td><td>February</td></tr>
    <tr><td>Decisions (both)</td><td>mid-Dec / late Mar</td></tr></table></div>

  <div class="card" style="--c:var(--yale)"><h3>Yale</h3><div class="plan">Common App · SAT/ACT required</div>
    <table><tr><td>SCEA</td><td>Nov 1</td></tr>
    <tr><td>Music supp (SCEA/RD)</td><td>Nov 8 / Jan 9</td></tr>
    <tr><td>RD</td><td>Jan 2</td></tr>
    <tr><td>Decisions</td><td>mid-Dec / late Mar</td></tr>
    <tr><td>B.A./M.M. audition</td><td class="warn">pre-matriculation or 3rd year — not this cycle</td></tr></table></div>

  <div class="card" style="--c:var(--mit)"><h3>MIT</h3><div class="plan">MIT portal · $75 · SAT/ACT required</div>
    <table><tr><td>EA</td><td>Nov 1</td></tr>
    <tr><td>Last test (EA / RA)</td><td>Nov 30 / Dec 31</td></tr>
    <tr><td>Aid (EA / RA)</td><td>Nov 30 / Feb 15</td></tr>
    <tr><td>RA</td><td>Jan 4</td></tr>
    <tr><td>Decisions</td><td>mid-Dec / mid-Mar</td></tr></table></div>

  <div class="card" style="--c:var(--uchicago)"><h3>UChicago</h3><div class="plan">Common App · test-optional · no CSS</div>
    <table><tr><td>EA / ED I</td><td>Nov 2</td></tr>
    <tr><td>ED II / RD</td><td>Jan 4</td></tr>
    <tr><td>Aid (EA / EDII / RD)</td><td>Nov 15 / Jan 15 / Feb 15</td></tr>
    <tr><td>Decisions</td><td>mid-Dec / mid-Feb / late Mar</td></tr></table></div>

  <div class="card" style="--c:var(--cmu)"><h3>CMU</h3><div class="plan">Common App · $75 · CFA test-optional</div>
    <table><tr><td>Music app + prescreen</td><td>Dec 1</td></tr>
    <tr><td>ED (non-Music)</td><td>Nov 2</td></tr>
    <tr><td>RD (non-Music)</td><td>Jan 4</td></tr>
    <tr><td>Live audition</td><td>Feb (TBA)</td></tr>
    <tr><td>Decisions</td><td>by Apr 1</td></tr></table></div>

  <div class="card" style="--c:var(--upenn)"><h3>UPenn</h3><div class="plan">Common App · $75 · SAT/ACT required</div>
    <table><tr><td>ED (binding)</td><td>Nov 1</td></tr>
    <tr><td>Last SAT (ED / RD)</td><td>Nov 7 / Dec 5</td></tr>
    <tr><td>Aid (ED / RD)</td><td>Nov 6 / Feb 1</td></tr>
    <tr><td>RD</td><td>Jan 5</td></tr>
    <tr><td>Decisions</td><td>Dec / Apr</td></tr></table></div>

  <div class="card" style="--c:var(--cornell)"><h3>Cornell</h3><div class="plan">Common App · $85 · SAT/ACT required</div>
    <table><tr><td>ED (binding)</td><td>Nov 1 <span class="warn">(materials Nov 13)</span></td></tr>
    <tr><td>RD</td><td>Jan 2 <span class="warn">(materials Jan 19)</span></td></tr>
    <tr><td>Aid (ED / RD)</td><td>~Nov 15 / ~Feb 15</td></tr>
    <tr><td>Decisions</td><td>mid-Dec / late Mar</td></tr></table></div>

  <div class="card" style="--c:var(--berkeley)"><h3>UC Berkeley</h3><div class="plan">UC App only · $80 · test-blind</div>
    <table><tr><td>Filing window</td><td>Oct 1 – Nov 30</td></tr>
    <tr><td>Invited letters</td><td>Jan 10</td></tr>
    <tr><td>Aid (FAFSA/CADAA)</td><td>Mar 2</td></tr>
    <tr><td>Decisions / SIR</td><td>end Mar / May 1</td></tr></table></div>

  <div class="card" style="--c:var(--uiuc)"><h3>UIUC</h3><div class="plan">myIllinois or Common App · test-optional</div>
    <table><tr><td>App opens</td><td>Sep 1</td></tr>
    <tr><td>EA</td><td>Nov 1 <span class="warn">(materials Nov 7)</span></td></tr>
    <tr><td>Regular</td><td>Jan 5 <span class="warn">(materials Jan 11)</span></td></tr>
    <tr><td>Decisions (EA / RD)</td><td>~Jan 30 / ~Mar 6</td></tr>
    <tr><td>FAFSA priority</td><td>~Mar 15</td></tr></table></div>

  <div class="card" style="--c:var(--uw)"><h3>UW–Seattle</h3><div class="plan">Common App · $85 · test-free</div>
    <table><tr><td>Opens / closes</td><td>Aug 15 / Nov 15</td></tr>
    <tr><td>Aid priority</td><td>Feb 1 <span class="warn">(Husky Promise Feb 28)</span></td></tr>
    <tr><td>Decisions</td><td>Mar 1–15</td></tr>
    <tr><td>Music</td><td class="warn">no audition at admission; ensembles audition Sep after enrolling</td></tr></table></div>
</div>

<h2><span class="n">4</span> Violin — portfolio &amp; audition repertoire, stage by stage</h2>
<p class="sub">Every program that can receive Eidee's playing, what each stage requires, and when it's due. Verified against the official audition/portfolio pages Aug 15, 2026.</p>

<div class="cards" style="grid-template-columns:1fr 1fr">
  <div class="card" style="--c:var(--harvard)">
    <h3>NEC — Harvard dual degree</h3>
    <div class="plan">Required · judged above B.M. standard · necmusic.edu/auditions/violin</div>
    <table>
      <tr><td><b>Prescreen video</b><br>due <b>Dec 1</b></td><td style="font-weight:400">① Exposition (or first 5 min) of the 1st mvt of a <b>major concerto, 1800–1945</b> (Shostakovich No. 1: 4th mvt/cadenza allowed) · ② <b>Two contrasting movements</b> of an unaccompanied <b>Bach</b> sonata/partita. Single unedited takes, one file per piece.</td></tr>
      <tr><td><b>Live audition</b><br><b>February, Boston</b> (memorized)</td><td style="font-weight:400">① Concerto 1st mvt (1800–1945) · ② two contrasting Bach mvts (may reuse prescreen) · ③ <b>étude/caprice</b> from Rode Op. 22, Dont Op. 35, Wieniawski Op. 10/18, or Paganini Op. 1 · ④ sonata 1st mvt with piano in a contrasting style — or Mozart concerto exposition (Mozart <i>required</i> if unaccompanied) · ⑤ <b>one personally meaningful piece</b> of her choosing.</td></tr>
      <tr><td>Recorded alternative</td><td style="font-weight:400">15-minute <b>single continuous unedited take</b>, memorized; ≥3 selections incl. concerto exposition + one Bach mvt + own choice.</td></tr>
    </table>
  </div>

  <div class="card" style="--c:var(--cmu)">
    <h3>CMU School of Music (BXA)</h3>
    <div class="plan">Required · all repertoire from memory · via Acceptd</div>
    <table>
      <tr><td><b>Prescreen video</b><br>due <b>Dec 1</b></td><td style="font-weight:400">① One <b>étude</b> (Kreutzer, Fiorillo, Rode, Dont, Gaviniès) <i>or</i> a <b>caprice</b> (Wieniawski, Paganini) · ② <b>Allegro movement of a non-Baroque concerto</b> · ③ one movement of a <b>Bach solo sonata/partita</b>.</td></tr>
      <tr><td><b>Live audition</b><br><b>Feb (TBA)</b>; Pittsburgh or NYC</td><td style="font-weight:400"><b>Same repertoire as the prescreen; unaccompanied.</b></td></tr>
    </table>
  </div>

  <div class="card" style="--c:var(--stanford)">
    <h3>Stanford — Arts Portfolio (Music)</h3>
    <div class="plan">Optional · video only · moves the whole app earlier</div>
    <table>
      <tr><td>Due (REA)</td><td>app Oct 15 · media Oct 20</td></tr>
      <tr><td>Due (RD)</td><td>app Dec 5 · media Dec 10</td></tr>
      <tr><td>Content</td><td style="font-weight:400"><b>2–3 short contrasting pieces, ~10 min total</b>; videos no older than one year; accompaniment optional (no disadvantage without). Music résumé; a teacher recommendation encouraged.</td></tr>
    </table>
  </div>

  <div class="card" style="--c:var(--princeton)">
    <h3>Princeton — Arts Supplement (Music)</h3>
    <div class="plan">Optional · reviewed by Music faculty</div>
    <table>
      <tr><td>Due (SCEA / RD)</td><td>Nov 6 / Jan 8</td></tr>
      <tr><td>Content</td><td style="font-weight:400"><b>10–15 min of advanced solo work</b> showing <b>contrasting expression and technique</b> (no ensemble unless prominently soloed). Audio or video (or YouTube/Vimeo/SoundCloud). Plus music résumé and a <b>250-word statement</b> on integrating music at Princeton.</td></tr>
    </table>
  </div>

  <div class="card" style="--c:var(--mit)">
    <h3>MIT — Creative Portfolio (Music)</h3>
    <div class="plan">Optional · SlideRoom · $10 (waivable ≥3 days pre-deadline)</div>
    <table>
      <tr><td>Due</td><td>with the application (Nov 1 EA / Jan 4 RA)</td></tr>
      <tr><td>Content</td><td style="font-weight:400"><b>Two recordings of contrasting styles/periods, 10 min combined</b>; unedited solo performances, accompaniment as feasible. Performing-arts résumé + one music-teacher recommendation requested through SlideRoom. Reviewed by Music &amp; Theater Arts faculty.</td></tr>
    </table>
  </div>

  <div class="card" style="--c:var(--yale)">
    <h3>Yale — Music Supplement &nbsp;·&nbsp; Cornell — Recording</h3>
    <div class="plan">Optional at both · no fixed repertoire published</div>
    <table>
      <tr><td>Yale (SCEA / RD)</td><td style="font-weight:400"><b>Nov 8 / Jan 9</b> via the status portal; audio or video. Yale's own advice: submit <b>only if it shows "a high level of ability"</b>; consult the Music Dept guidelines for specifics.</td></tr>
      <tr><td>Cornell (ED / RD)</td><td style="font-weight:400">Arts &amp; Sciences accepts a <b>musical recording as its only supplemental material</b> — submit with the Nov 1 / Jan 2 application per A&amp;S instructions.</td></tr>
      <tr><td>No music at admission</td><td style="font-weight:400">UChicago (2-min video is general, not musical), UPenn, UC Berkeley, UIUC, UW — ensembles audition <i>after</i> enrollment.</td></tr>
    </table>
  </div>
</div>

<div class="note" style="background:#f0f6ee;border-color:#c4dcbc">
  <b style="color:#33611f">One recording session can feed almost everything.</b>
  A single well-produced October session covering ① a movement of solo Bach, ② the first movement (or exposition) of a Romantic-era concerto, and ③ a short contrasting piece satisfies Stanford, Princeton, MIT, Yale, and Cornell outright and supplies both required prescreens (NEC needs a <i>second</i> contrasting Bach movement; CMU needs the memorized étude/caprice — the only item on no other list). Record in one block, then trim per school. The live-audition-only additions (NEC's piano sonata/Mozart + meaningful piece) can be prepared over winter break for February.
</div>

<div class="note">
  <b>Three planning notes.</b>&nbsp; ① <b>Only one early card can be played</b> among Harvard REA, Yale SCEA, Princeton SCEA, Stanford REA, UPenn ED, Cornell ED, and UChicago ED I — the restrictive/binding programs exclude each other (MIT EA is non-restrictive but is barred <i>by the other schools'</i> REA/SCEA rules; UIUC EA, UW, and the UCs are public/non-binding and combine freely with any of them). ② An <b>SAT EBRW retake</b> aimed at 750+ must land by the October sitting for REA/SCEA schools — August or September is safer. ③ <b>Dec 1 is the quiet killer</b>: the NEC prescreen video and CMU violin prescreen both come due four weeks after the Nov 1 wave — the recording should exist by October, not be scheduled for Thanksgiving.
</div>

<footer>
  Repertoire verified Aug 15, 2026 against NEC's violin audition page, CMU's violin requirements page, Stanford Music's recorded-arts-portfolio page, Princeton's optional-arts-supplement page, MIT's creative-portfolios page, and Yale's supplementary-materials page. NEC dual-degree candidates are auditioned to a higher standard than regular B.M. applicants; the published B.M. repertoire is the base requirement. Dates consolidated from the twelve program dossiers (ai-kitchen-inc/university-admission-research · brochures/), each researched against official admissions, program, and aid pages on August 15, 2026. Where a school had not yet posted its 2026–27 calendar, the current published cycle's dates are shown — re-verify each on the official page when applications open. UChicago's Nov 2 early deadline reflects its published page (Nov 1, 2026 is a Sunday); confirm in-cycle. Decision months marked "~" are the school's typical release window, not a guaranteed date.
</footer>

</div>
</body>
</html>
