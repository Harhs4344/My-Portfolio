"""Harshikesh Bhondave - portfolio (Streamlit app).

Run locally:
    pip install -r requirements.txt
    streamlit run app.py
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Harshikesh Bhondave | Portfolio",
    page_icon="\U0001F4CA",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own chrome so only the portfolio shows.
st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

PORTFOLIO_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="color-scheme" content="light">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Harshikesh Bhondave | AI & Data Science</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--bg:#f4f9ff;--ink:#0f2327;--mute:#47646a;--line:#d4e3f5;--accent:#0f766e;--accent2:#d97706;--card:rgba(255,255,255,.85);--chip:#e3eefb;--b1:rgba(147,197,253,.35);--b2:rgba(186,230,253,.45);--base:linear-gradient(180deg,#ffffff 0%,#eef6ff 55%,#e3f0ff 100%);
box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(800px 500px at 90% 0%,var(--b2),transparent 70%),radial-gradient(700px 500px at 0% 100%,var(--b1),transparent 70%),var(--base);background-attachment:fixed;color:var(--ink);font:400 17px/1.65 "DM Sans",system-ui,sans-serif}
main{max-width:860px;margin:0 auto;padding:56px 22px 72px}
h1,h2,h3{font-family:"Bricolage Grotesque",system-ui,sans-serif;line-height:1.15;margin:0}
h1{font-size:clamp(2.6rem,8vw,4.8rem);font-weight:800;letter-spacing:-.035em}
h2{font-size:1.7rem;margin-bottom:22px}
h3{font-size:1.25rem}
.role{font-size:1.15rem;color:var(--accent);font-weight:600;letter-spacing:.01em;margin:14px 0 18px}
.lead{max-width:62ch;color:var(--mute);margin:0 0 26px}
.btns{display:flex;flex-wrap:wrap;gap:12px}
a.btn{display:inline-block;padding:11px 20px;border-radius:8px;text-decoration:none;font-weight:600;border:1.5px solid var(--accent);color:var(--accent)}
a.btn.p{background:var(--accent);color:var(--bg)}
a:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
section{margin-top:64px;padding-top:28px;border-top:1px solid var(--line)}
.proj{background:var(--card);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1px solid var(--line);border-radius:10px;padding:24px;margin-bottom:18px}
.proj p{margin:10px 0;color:var(--mute)}
.proj ul{margin:10px 0 0;padding-left:20px;color:var(--mute)}
.proj li{margin-bottom:6px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.chips span{background:var(--chip);border-radius:6px;padding:3px 10px;font-size:.85rem;font-weight:500}
dl{margin:0;display:grid;grid-template-columns:150px 1fr;gap:14px 20px}
dt{font-weight:600}dd{margin:0;color:var(--mute)}
.job{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
.job span{color:var(--mute)}
footer{margin-top:64px;color:var(--mute);font-size:.9rem}
@media(max-width:600px){dl{grid-template-columns:1fr;gap:2px}dd{margin-bottom:12px}}
@media(prefers-reduced-motion:no-preference){h1{animation:rise .7s ease both}@keyframes rise{from{opacity:0;transform:translateY(14px)}}}
.hero{display:flex;align-items:center;gap:32px;flex-wrap:wrap}.hero>div{flex:1 1 380px}.hero svg{flex:0 1 280px;width:100%;max-width:300px;height:auto}
.art{display:block;width:100%;height:auto;border-radius:8px;background:var(--chip);margin-bottom:16px}
.s{stroke:var(--accent);fill:none;stroke-width:2}.f{fill:var(--accent)}.f2{fill:var(--accent2)}.s2{stroke:var(--accent2);fill:none;stroke-width:3;stroke-linecap:round}.t{fill:var(--ink);font:600 12px "DM Sans",sans-serif}
figure.fig{flex:0 1 320px;width:100%;max-width:320px;margin:0;text-align:center}canvas.h3{width:100%;aspect-ratio:300/260;display:block}figcaption{color:var(--mute);font-weight:600;font-size:.95rem;min-height:1.6em}canvas.art{height:200px}
section{perspective:1100px}
.pj{display:grid;grid-template-columns:1fr 1.2fr;gap:26px;align-items:center;padding:22px;transform-style:preserve-3d;transition:transform .15s ease-out;backdrop-filter:none;-webkit-backdrop-filter:none;box-shadow:0 1px 0 #fff inset,0 24px 44px -20px rgba(30,64,130,.4),0 6px 0 var(--line)}
.pj-viz{transform:translateZ(40px)}
.pj canvas.art{height:260px;margin:0;border-radius:12px;box-shadow:0 14px 28px -14px rgba(30,64,130,.45)}
.pj-body{transform:translateZ(18px)}
.pj-body p{margin:8px 0}
.blurb{color:var(--ink)!important}
.meta{font-size:.9rem}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:16px 0}
.st{background:var(--chip);border-radius:10px;padding:10px 6px;text-align:center;box-shadow:0 4px 0 var(--line)}
.st b{display:block;font:800 1.7rem/1.1 "Bricolage Grotesque",sans-serif;color:var(--accent)}
.st span{display:block;font-size:.78rem;line-height:1.25;color:var(--mute);margin-top:2px}
.flow{list-style:none;padding:0;margin:18px 0 14px;display:flex;flex-wrap:wrap;gap:12px 20px}
.flow li,.blk li{position:relative;background:#fff;color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:6px 12px;font-size:.86rem;font-weight:600;box-shadow:1px 1px 0 var(--accent),2px 2px 0 var(--accent),3px 3px 0 var(--accent),4px 4px 0 var(--accent)}
.flow li:not(:last-child)::after{content:"\203A";position:absolute;right:-15px;top:50%;transform:translateY(-52%);color:var(--accent);font-weight:800}
@media(max-width:720px){.pj{grid-template-columns:1fr}.pj canvas.art{height:230px}}
.pgrid{display:grid;grid-template-columns:1fr 1fr;gap:22px;align-items:stretch}
.pgrid .pj{grid-template-columns:1fr;align-items:start;margin:0;gap:18px}
.pgrid .pj canvas.art{height:220px}
.sgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px}
.sk,.one{display:block;margin:0;padding:20px}
.one{margin-bottom:0}
.skh{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.skh .st{min-width:66px;padding:8px 10px}
.blk{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:12px 14px}
.blk li{font-size:.84rem}
.st.w b{font-size:1.15rem;padding:5px 0}
.one .stats{margin:14px 0}
@media(max-width:820px){.pgrid{grid-template-columns:1fr}}
.tabs{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:20px}
.tabs button{font:600 .95rem "DM Sans",sans-serif;padding:9px 18px;border-radius:999px;border:1.5px solid var(--accent);background:transparent;color:var(--accent);cursor:pointer}
.tabs button[aria-selected="true"]{background:var(--accent);color:#fff}
.tabs button:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.pj[hidden]{display:none}
.pgrid{display:block}
.pgrid .pj{grid-template-columns:1fr 1.2fr;align-items:center}
.pgrid .pj canvas.art{height:260px}
@media(max-width:820px){.pgrid .pj{grid-template-columns:1fr}}
.sgrid{display:block;border-top:1px solid var(--line)}
.row{display:grid;grid-template-columns:200px 1fr;gap:10px 24px;padding:16px 0;border-bottom:1px solid var(--line);align-items:start}
.row h3{font-size:1.05rem}.row small{color:var(--mute);font:500 .8rem "DM Sans",sans-serif;margin-left:4px}
.pills{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px}
.pills li{background:var(--chip);border-radius:999px;padding:4px 13px;font-size:.88rem;font-weight:500}
@media(max-width:600px){.row{grid-template-columns:1fr}}
.tl{border-left:2px solid var(--accent);margin-left:7px;padding-left:26px}
.ti{position:relative}
.ti::before{content:"";position:absolute;left:-34px;top:4px;width:14px;height:14px;border-radius:50%;background:var(--bg);border:3px solid var(--accent)}
.when{display:inline-block;background:var(--chip);color:var(--accent);border-radius:6px;padding:2px 10px;font-weight:600;font-size:.85rem;margin-bottom:8px}
.org{margin:4px 0 12px;color:var(--mute)}
.bul{margin:0 0 14px;padding-left:20px;color:var(--mute)}.bul li{margin-bottom:6px}
</style>
</head>
<body>
<main>
<header class="hero"><div>
<h1>Harshikesh Bhondave</h1>
<p class="role">AI &amp; Data Science graduate, junior data scientist</p>
<p class="lead">I build machine learning workflows and ship them as working apps, from data preparation and feature engineering to model evaluation and deployment. I'm looking for entry-level AI/ML, data science, or analytics roles.</p>
<div class="btns">
<a class="btn p" href="https://mail.google.com/mail/?view=cm&fs=1&to=bhondweharshikesh@gmail.com&su=Hello%20Harshikesh" target="_blank" rel="noopener">Email me</a>
<a class="btn" href="#projects">See projects</a>
</div>
<p style="margin-top:16px;color:var(--mute);font-size:.95rem">Or write to <a href="mailto:bhondweharshikesh@gmail.com" style="color:var(--accent)">bhondweharshikesh@gmail.com</a></p>
</div>
<figure class="fig"><canvas id="c1" class="h3" role="img" aria-label="Rotating 3D models: neural network, k-means clustering, decision tree"></canvas><figcaption id="cap1"></figcaption></figure>
</header>

<section id="projects">
<h2>Projects</h2>
<div class="tabs" role="tablist"><button role="tab" aria-selected="true">Customer Churn Prediction</button><button role="tab" aria-selected="false">Document Q&amp;A</button></div>
<div class="pgrid">
<article class="proj pj" data-tilt>
<div class="pj-viz"><canvas id="c2" class="art" role="img" aria-label="3D bar chart comparing model results"></canvas></div>
<div class="pj-body">
<h3>Customer Churn Prediction</h3>
<p class="blurb">An end-to-end workflow that predicts which customers are likely to leave, with a Streamlit app for real-time predictions and TensorBoard to monitor training.</p>
<div class="stats"><div class="st"><b>3</b><span>models compared</span></div><div class="st"><b>5</b><span>evaluation metrics</span></div><div class="st"><b>2</b><span>fixes for class imbalance</span></div></div>
<ol class="flow"><li>Prepare data</li><li>Engineer features</li><li>Train</li><li>Evaluate</li><li>Deploy app</li></ol>
<p class="meta">Logistic Regression, Decision Tree and Neural Network, scored on accuracy, precision, recall, F1 and ROC-AUC. Imbalance handled with SMOTE and class weighting.</p>
<div class="chips"><span>Python</span><span>Pandas</span><span>scikit-learn</span><span>TensorFlow/Keras</span><span>Streamlit</span></div>
</div>
</article>
<article class="proj pj" data-tilt hidden>
<div class="pj-viz"><canvas id="c3" class="art" role="img" aria-label="3D pipeline: document, chunks, vectors, answer"></canvas></div>
<div class="pj-body">
<h3>AI Document Intelligence &amp; Q&amp;A</h3>
<p class="blurb">A question-answering app for documents: upload a file, ask a question, and get an answer built from the most relevant passages.</p>
<div class="stats"><div class="st"><b>5</b><span>pipeline steps</span></div><div class="st"><b>1</b><span>FastAPI service</span></div><div class="st"><b>RAG</b><span>retrieval + LLM</span></div></div>
<ol class="flow"><li>Parse upload</li><li>Chunk text</li><li>Embed</li><li>Retrieve</li><li>Answer with LLM</li></ol>
<p class="meta">Passages are found with vector similarity search, then passed to an LLM API for context-aware answers.</p>
<div class="chips"><span>Python</span><span>FastAPI</span><span>RAG</span><span>ChromaDB</span><span>Sentence Transformers</span></div>
</div>
</article>
</div>
</section>

<section>
<h2>Experience</h2>
<div class="tl"><div class="ti">
<span class="when">May &ndash; Aug 2026</span>
<h3>Technical Support Engineer</h3>
<p class="org">CARE Software</p>
<ul class="bul"><li>Troubleshot business management software, database and system issues reported by users.</li><li>Resolved application and data issues using SQL, DBF and Visual FoxPro, and guided users through operational problems to resolution.</li></ul>
<ul class="pills"><li>SQL</li><li>DBF</li><li>Visual FoxPro</li></ul>
</div></div>
</section>

<section>
<h2>Skills</h2>
<div class="sgrid">
<div class="row"><h3>Programming <small>3</small></h3><ul class="pills"><li>Python</li><li>Excel</li><li>SQL</li><li>R</li></ul></div>
<div class="row"><h3>Machine learning <small>7</small></h3><ul class="pills"><li>scikit-learn</li><li>TensorFlow</li><li>Keras</li><li>Model evaluation</li><li>Feature engineering</li><li>Cross-validation</li><li>Hyperparameter tuning</li></ul></div>
<div class="row"><h3>Data <small>6</small></h3><ul class="pills"><li>Pandas</li><li>NumPy</li><li>Matplotlib</li><li>Seaborn</li><li>EDA</li><li>Statistical analysis</li></ul></div>
<div class="row"><h3>Databases <small>3</small></h3><ul class="pills"><li>MySQL</li><li>Oracle SQL</li><li>PL/SQL</li></ul></div>
<div class="row"><h3>Deployment &amp; APIs <small>4</small></h3><ul class="pills"><li>Streamlit</li><li>FastAPI</li><li>Flask</li><li>REST APIs</li></ul></div>
<div class="row"><h3>Tools <small>8</small></h3><ul class="pills"><li>Git</li><li>GitHub</li><li>VS Code</li><li>Jupyter</li><li>TensorBoard</li><li>Postman</li><li>Power BI</li><li>Excel</li></ul></div>
</div>
</section>

<section>
<h2>Education</h2>
<div class="tl"><div class="ti">
<span class="when">2022 &ndash; 2026</span>
<h3>B.Tech, Artificial Intelligence and Data Science</h3>
<p class="org">TPCT's College of Engineering, Dharashiv &middot; CGPA 6.5/10</p>
<ul class="pills"><li>AI &amp; Machine Learning (Techobytes with ITC, IIT Bombay)</li><li>Data Science &amp; Analytics (HP LIFE)</li><li>Data Science (Fullstack Guru, Pune)</li></ul>
</div></div>
</section>

<footer>
<p>Pune, Maharashtra · <a href="mailto:bhondweharshikesh@gmail.com" style="color:var(--accent)">bhondweharshikesh@gmail.com</a></p>
</footer>
</main>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function(){var T=window.THREE;if(!T)return;var mats=[];
function col(k){if(k=='c')return '#3b82f6';return getComputedStyle(document.documentElement).getPropertyValue(k=='a'?'--accent':'--accent2').trim()||'#0f766e'}
function M(k){var m=new T.MeshLambertMaterial({color:col(k)});m.userData.k=k;mats.push(m);return m}
function L(k){var m=new T.LineBasicMaterial({color:col(k)});m.userData.k=k;mats.push(m);return m}
function V(x,y,z){return new T.Vector3(x,y,z)}
function line(a,b,k){return new T.Line(new T.BufferGeometry().setFromPoints([a,b]),L(k))}
var still=matchMedia('(prefers-reduced-motion:reduce)').matches;
function scene(id,z,sway,build){var c=document.getElementById(id);if(!c)return;var r;
try{r=new T.WebGLRenderer({canvas:c,alpha:true,antialias:true})}catch(e){return}
r.setPixelRatio(Math.min(devicePixelRatio||1,2));
var s=new T.Scene(),cam=new T.PerspectiveCamera(40,1,.1,100);cam.position.set(0,1.6,z);cam.lookAt(0,0,0);
s.add(new T.AmbientLight(0xffffff,.75));var d=new T.DirectionalLight(0xffffff,.8);d.position.set(3,5,4);s.add(d);
var g=new T.Group();s.add(g);build(g);var t=0;
function draw(){g.rotation.y=sway?Math.sin(t)*.6:t;r.render(s,cam)}
function size(){var w=c.clientWidth,h=c.clientHeight;if(!w||!h)return;r.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix();draw()}
new ResizeObserver(size).observe(c);size();
if(!still){(function f(){t+=.008;draw();requestAnimationFrame(f)})()}}
matchMedia('(prefers-color-scheme:dark)').addEventListener('change',function(){setTimeout(function(){mats.forEach(function(m){m.color.set(col(m.userData.k))})},60)});
var names=['Neural network','K-means clustering','Decision tree'];
scene('c1',6.5,false,function(g){var sd=7,i,j;function rnd(){sd=sd*16807%2147483647;return sd/2147483647}
var sg=new T.SphereGeometry(.09,14,14);
function node(p,k,gr,r){var m=new T.Mesh(sg,M(k));m.position.copy(p);m.scale.setScalar(r||1);gr.add(m)}
function link(a,b,gr){var l=line(a,b,'a');l.material.transparent=true;l.material.opacity=.4;gr.add(l)}
var nn=new T.Group(),cnt=[3,5,5,2],xs=[-2,-.7,.7,2],P=[];
for(i=0;i<4;i++){P[i]=[];for(j=0;j<cnt[i];j++){var p=V(xs[i],(j-(cnt[i]-1)/2)*.7,(rnd()-.5)*1.2);P[i].push(p);node(p,i==3?'b':'a',nn,i==3?1.6:1)}}
for(i=0;i<3;i++)P[i].forEach(function(a){P[i+1].forEach(function(b){link(a,b,nn)})});
var km=new T.Group(),cs=[V(-1.3,.7,.3),V(1.2,.5,-.6),V(0,-1,.5)],ks=['a','b','c'];
cs.forEach(function(c,ci){for(var q=0;q<26;q++)node(V(c.x+(rnd()-.5)*1.3,c.y+(rnd()-.5)*1.3,c.z+(rnd()-.5)*1.3),ks[ci],km,.8);var o=new T.Mesh(new T.OctahedronGeometry(.22),M(ks[ci]));o.position.copy(c);km.add(o)});
var tr=new T.Group(),lv=[[V(0,1.5,0)],[V(-1.1,.5,.4),V(1.1,.5,-.4)],[V(-1.7,-.5,-.3),V(-.5,-.5,.5),V(.5,-.5,-.5),V(1.7,-.5,.3)],[V(-2,-1.5,0),V(-1.4,-1.5,-.5),V(-.8,-1.5,.4),V(-.2,-1.5,-.3),V(.2,-1.5,.4),V(.8,-1.5,-.4),V(1.4,-1.5,.3),V(2,-1.5,-.2)]];
lv.forEach(function(l,li){l.forEach(function(p,pi){node(p,li<3?'a':(pi%2?'b':'c'),tr,li<3?1.2:.9);if(li<3){link(p,lv[li+1][2*pi],tr);link(p,lv[li+1][2*pi+1],tr)}})});
var hg=[nn,km,tr],cap=document.getElementById('cap1'),cur=0;
hg.forEach(function(x,n){x.visible=n==0;g.add(x)});if(cap)cap.textContent=names[0];
if(!still)setInterval(function(){hg[cur].visible=false;cur=(cur+1)%3;hg[cur].visible=true;if(cap)cap.textContent=names[cur]},5000)});
scene('c2',6.5,false,function(g){var h=[.6,1.1,.8,1.6,1,1.9,.7,1.3,1.5,.9,1.2,.5,.8,1.7,1];
for(var i=0;i<15;i++){var m=new T.Mesh(new T.BoxGeometry(.5,h[i],.5),M(i==5?'b':'a'));m.position.set((i%5-2)*.75,h[i]/2-.9,((i/5|0)-1)*.75);g.add(m)}});
scene('c3',7.5,true,function(g){var xs=[-2.6,-.9,.8,2.5];
var dc=new T.Mesh(new T.BoxGeometry(.7,1,.08),M('a'));dc.position.x=xs[0];g.add(dc);
for(var i=0;i<3;i++){var c=new T.Mesh(new T.BoxGeometry(.7,.22,.12),M('a'));c.position.set(xs[1],(1-i)*.35,0);g.add(c)}
var sg=new T.SphereGeometry(.09,12,12);
for(var j=0;j<14;j++){var p=new T.Mesh(sg,M(j==4?'b':'a'));p.position.set(xs[2]+Math.cos(j*2.4)*.45,Math.sin(j*1.7)*.5,Math.sin(j*2.4)*.45);g.add(p)}
var a=new T.Mesh(new T.OctahedronGeometry(.42),M('b'));a.position.x=xs[3];g.add(a);
for(var k=0;k<3;k++)g.add(line(V(xs[k]+.55,0,0),V(xs[k+1]-.55,0,0),'a'))});
scene('c4',6,false,function(g){var i;
for(i=0;i<3;i++){var c=new T.Mesh(new T.CylinderGeometry(1,1,.45,32),M(i==2?'b':'a'));c.position.y=(i-1)*.7;g.add(c)}
var bg=new T.BoxGeometry(.35,.25,.05);
for(i=0;i<5;i++){var b=new T.Mesh(bg,M('c')),an=i*1.26;b.position.set(Math.cos(an)*1.9,Math.sin(i*2)*.9,Math.sin(an)*1.9);b.rotation.y=-an;g.add(b)}});
})();
</script>
<script>
(function(){if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;
document.querySelectorAll('[data-tilt]').forEach(function(c){
c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform='rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg)'});
c.addEventListener('pointerleave',function(){c.style.transform=''})})})();
</script>
<script>
(function(){var tb=document.querySelectorAll('.tabs button'),ps=document.querySelectorAll('.pgrid .pj');
tb.forEach(function(b,i){b.addEventListener('click',function(){tb.forEach(function(x,j){x.setAttribute('aria-selected',j==i?'true':'false')});ps.forEach(function(p,j){p.hidden=j!=i})})})})();
</script>
</body>
</html>
"""

components.html(PORTFOLIO_HTML, height=2600, scrolling=True)
