import sys
import re

try:
    from bs4 import BeautifulSoup, NavigableString
except ImportError:
    print("BeautifulSoup not installed. Please install 'beautifulsoup4'")
    sys.exit(1)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

body = soup.body

# find the photo base64
photo_img = soup.find('img', class_='photo')
# copy the element
import copy
new_photo = copy.copy(photo_img)

# Find sections
about_sec = soup.find('section', id='about')
skills_sec = soup.find('section', id='skills')
projects_sec = soup.find('section', id='projects')
achv_sec = soup.find('section', id='achievements')
contact_sec = soup.find('section', id='contact')

# Grab texts from hero
hero_sec = soup.find('section', id='hero')
hero_name = hero_sec.find('h1', class_='hero-name')
hero_role = hero_sec.find('div', class_='hero-role')
hero_badge = hero_sec.find('div', class_='spidey-badge')

slinks = contact_sec.find('div', class_='slinks')

new_body_html = f"""
<body>
<div id="cur"></div>
<div id="cur2"></div>
<canvas id="webCanvas"></canvas>

<!-- Top Left: Origin Story -->
<div class="quadrant q-top-left" id="q-about">
  <div class="q-title">Origin Story</div>
  <div class="q-content">
    {str(about_sec)}
  </div>
</div>

<!-- Top Right: Skills -->
<div class="quadrant q-top-right" id="q-skills">
  <div class="q-title">Web of Knowledge</div>
  <div class="q-content">
    {str(skills_sec)}
  </div>
</div>

<!-- Bottom Left: Projects -->
<div class="quadrant q-bottom-left" id="q-projects">
  <div class="q-title">Spider Builds</div>
  <div class="q-content">
    {str(projects_sec)}
  </div>
</div>

<!-- Bottom Right: Achievements & Contact -->
<div class="quadrant q-bottom-right" id="q-achievements">
  <div class="q-title">Hall of Fame</div>
  <div class="q-content">
    {str(achv_sec)}
    {str(contact_sec)}
  </div>
</div>

<!-- Center Hero -->
<div class="center-hero" id="centerHero">
  <div class="hero-visual">
    <div class="frame">
      <div class="ring ring3"></div>
      <div class="ring ring2"></div>
      <div class="ring ring1"></div>
      <div class="pglow"></div>
      {str(new_photo)}
      {str(hero_badge)}
    </div>
  </div>
  <div class="hero-text-center">
    {str(hero_name)}
    {str(hero_role)}
    {str(slinks)}
  </div>
</div>

<!-- Close button -->
<button class="btn-close" id="btnClose"><i class="fas fa-times"></i></button>

<footer>
  © 2025 Snehal Marteen Garikamukkala &nbsp;·&nbsp; Built with 🕷 Spider-Man Energy &nbsp;·&nbsp; AIML Undergraduate
</footer>

<script>
// Keep original JS logic
const cur = document.getElementById('cur');
const cur2 = document.getElementById('cur2');
document.addEventListener('mousemove', e => {{
  cur.style.left = e.clientX + 'px';
  cur.style.top = e.clientY + 'px';
  cur2.style.left = e.clientX + 'px';
  cur2.style.top = e.clientY + 'px';
}});
document.querySelectorAll('a,button,.pc,.ach,.sc,.stag,.exc,.quadrant').forEach(el => {{
  el.addEventListener('mouseenter', () => {{ cur.style.transform = 'translate(-50%,-50%) scale(2)'; cur.style.background = 'rgba(227,28,35,.15)'; }});
  el.addEventListener('mouseleave', () => {{ cur.style.transform = 'translate(-50%,-50%) scale(1)'; cur.style.background = 'transparent'; }});
}});

// Canvas
const canvas = document.getElementById('webCanvas');
const ctx = canvas.getContext('2d');
function resizeCanvas() {{ canvas.width = window.innerWidth; canvas.height = window.innerHeight; drawWeb(); }}
function drawWeb() {{
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const centers = [[0, 0], [canvas.width, 0], [0, canvas.height], [canvas.width, canvas.height]];
  centers.forEach(([cx, cy]) => {{
    for (let a = 0; a < 360; a += 22) {{
      const rad = a * Math.PI / 180;
      const len = Math.max(canvas.width, canvas.height) * 1.5;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + Math.cos(rad) * len, cy + Math.sin(rad) * len);
      const g = ctx.createLinearGradient(cx, cy, cx + Math.cos(rad) * len, cy + Math.sin(rad) * len);
      g.addColorStop(0, '#E31C23');
      g.addColorStop(1, '#003B8E');
      ctx.strokeStyle = g;
      ctx.lineWidth = 0.7;
      ctx.stroke();
    }}
    for (let r = 80; r < Math.max(canvas.width, canvas.height) * 1.5; r += 90) {{
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(227,28,35,0.5)';
      ctx.lineWidth = 0.4;
      ctx.stroke();
    }}
  }});
}}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// Particles
const colors = ['#E31C23','#FFD700','#00d4ff','#ff006e','#00ff88','#7c3aed'];
for (let i = 0; i < 35; i++) {{
  const p = document.createElement('div');
  p.className = 'pt';
  p.style.cssText = `
    left:${{Math.random()*100}}vw;
    width:${{2+Math.random()*4}}px;
    height:${{2+Math.random()*4}}px;
    background:${{colors[Math.floor(Math.random()*colors.length)]}};
    animation-duration:${{8+Math.random()*15}}s;
    animation-delay:${{-Math.random()*20}}s;
    box-shadow:0 0 ${{4+Math.random()*8}}px currentColor;
  `;
  document.body.appendChild(p);
}}

// Scroll Reveal
const revEls = document.querySelectorAll('.rev,.revL,.revR');
const revObs = new IntersectionObserver((entries) => {{
  entries.forEach((e, i) => {{
    if (e.isIntersecting) {{
      setTimeout(() => e.target.classList.add('in'), 80 * (e.target.dataset.delay || 0));
      revObs.unobserve(e.target);
    }}
  }});
}}, {{ threshold: 0.12 }});

// Staggered cards
document.querySelectorAll('.pg .pc, .ag .ach, .stats .sc').forEach((el, i) => {{
  el.style.transitionDelay = (i * 0.1) + 's';
}});
document.querySelectorAll('.stag').forEach(t => {{
  t.addEventListener('mouseenter', () => {{ t.style.color = '#fff'; }});
}});

// Counters
function animateCount(el, target, suffix = '') {{
  let count = 0;
  const step = target / 60;
  const interval = setInterval(() => {{
    count = Math.min(count + step, target);
    el.textContent = (Number.isInteger(target) ? Math.round(count) : count.toFixed(1)) + suffix;
    if (count >= target) clearInterval(interval);
  }}, 25);
}}
const statsObs = new IntersectionObserver(entries => {{
  entries.forEach(e => {{
    if (e.isIntersecting) {{
      e.target.querySelectorAll('.snum').forEach(n => {{
        const txt = n.textContent.trim();
        if (txt === '3+') {{ n.textContent = '0'; animateCount(n, 3, '+'); }}
        else if (txt === '400+') {{ n.textContent = '0'; animateCount(n, 400, '+'); }}
      }});
      statsObs.unobserve(e.target);
    }}
  }});
}}, {{ threshold: 0.3 }});
document.querySelectorAll('.stats').forEach(s => statsObs.observe(s));

// Quadrants Logic
const quads = document.querySelectorAll('.quadrant');
const btnClose = document.getElementById('btnClose');

quads.forEach(q => {{
  q.addEventListener('click', (e) => {{
    if (!q.classList.contains('expanded')) {{
      // Expand quadrant
      quads.forEach(other => other.classList.remove('expanded'));
      q.classList.add('expanded');
      document.body.classList.add('quadrant-active');
      
      // Observe reveals inside expanded quadrant
      setTimeout(() => {{
          q.querySelectorAll('.rev,.revL,.revR').forEach(el => {{
             el.classList.remove('in');
             revObs.observe(el);
          }});
          q.querySelectorAll('.stats').forEach(s => statsObs.observe(s));
          q.scrollTop = 0;
      }}, 600);
    }}
  }});
}});

btnClose.addEventListener('click', (e) => {{
  e.stopPropagation();
  quads.forEach(q => {{
    q.classList.remove('expanded');
  }});
  document.body.classList.remove('quadrant-active');
}});
</script>
</body>
"""

# Now handle the CSS
style_tag = soup.head.find('style')
old_css = style_tag.text

new_css_rules = """
/* ── NEW QUADRANT LAYOUT ── */
body {
  overflow: hidden; /* Stop page scrolling */
}

/* Hide original sections as they are now in .q-content */
section {
  padding: 4rem 3rem;
  background: transparent !important; /* override old inline backgrounds */
  max-width: 1200px;
  margin: 0 auto;
}
.sl, .st { text-align: center; } /* Optional: center titles in quadrant */

.quadrant {
  position: absolute;
  width: 50vw;
  height: 50vh;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.7s cubic-bezier(0.8, 0, 0.2, 1);
  z-index: 10;
  display: flex;
  justify-content: center;
  align-items: center;
}

.q-title {
  font-family: 'Bangers', cursive;
  font-size: clamp(2rem, 5vw, 4rem);
  letter-spacing: 4px;
  color: var(--text);
  opacity: 0.7;
  transition: all 0.5s ease;
  z-index: 5;
  text-shadow: 0 5px 20px rgba(0,0,0,0.8);
  text-transform: uppercase;
  pointer-events: none;
}

.quadrant:hover .q-title {
  transform: scale(1.15);
  color: var(--gold);
  opacity: 1;
}

/* Backgrounds for corners */
.q-top-left { top: 0; left: 0; background: radial-gradient(circle at top left, rgba(0,59,142,0.5) 0%, rgba(7,7,15,0.8) 70%); }
.q-top-right { top: 0; right: 0; background: radial-gradient(circle at top right, rgba(227,28,35,0.4) 0%, rgba(7,7,15,0.8) 70%); }
.q-bottom-left { bottom: 0; left: 0; background: radial-gradient(circle at bottom left, rgba(124,58,237,0.4) 0%, rgba(7,7,15,0.8) 70%); }
.q-bottom-right { bottom: 0; right: 0; background: radial-gradient(circle at bottom right, rgba(255,215,0,0.3) 0%, rgba(7,7,15,0.8) 70%); }

/* Quadrant Expansion */
.quadrant.expanded {
  width: 100vw;
  height: 100vh;
  z-index: 100;
  cursor: default;
  background: var(--dark) !important;
  overflow-y: auto;
  align-items: flex-start;
  top: 0 !important;
  left: 0 !important;
  right: auto !important;
  bottom: auto !important;
}

.quadrant.expanded .q-title {
  display: none;
}

.q-content {
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s ease;
  width: 100%;
}
.quadrant.expanded .q-content {
  opacity: 1;
  pointer-events: auto;
  transition-delay: 0.5s;
}

/* Center Hero */
.center-hero {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 20;
  pointer-events: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: all 0.6s cubic-bezier(0.8, 0, 0.2, 1);
}

.hero-text-center {
  margin-top: 2rem;
  background: rgba(7,7,15,0.7);
  padding: 1.5rem 3rem;
  border-radius: 20px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(227,28,35,0.2);
}

body.quadrant-active .center-hero {
  opacity: 0;
  transform: translate(-50%, -50%) scale(0.5);
  pointer-events: none;
}

/* Close Button */
.btn-close {
  position: fixed;
  top: 2rem;
  right: 2rem;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: rgba(7,7,15,0.8);
  border: 2px solid var(--red);
  color: var(--red);
  font-size: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  z-index: 110;
  transition: all 0.3s;
  backdrop-filter: blur(10px);
}
body.quadrant-active .btn-close {
  opacity: 1;
  pointer-events: auto;
}
.btn-close:hover {
  background: var(--red);
  color: #fff;
  transform: rotate(90deg) scale(1.1);
}

/* Slinks adjust */
.slinks { pointer-events: auto; margin-top: 1rem; }
.hero-visual { pointer-events: auto; }

/* Hide old unused parts */
nav { display: none !important; }
.div { display: none !important; }
"""

style_tag.string = old_css + new_css_rules

# re-render body
body_new = BeautifulSoup(new_body_html, 'html.parser')
soup.body.replace_with(body_new)

with open('index_new.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully generated index_new.html")
