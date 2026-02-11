import requests
import os

# ===== CONFIG =====
USERNAME = "try-ronnie"
OUTPUT_DIR = "./assets/graphs/"
TECHS = ["Python", "FastAPI", "Flask", "React", "Node.js", "JavaScript", "HTML", "CSS", "Pygame"]
SVG_WIDTH = 120
SVG_HEIGHT = 20
BAR_COLOR = "#7c3aed"  # neon purple
BG_COLOR = "#1e1b2a"   # dark purple background

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== FETCH REPOS =====
repos = requests.get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100").json()

# ===== COUNT LANGUAGE STATS =====
lang_totals = {tech: 0 for tech in TECHS}

for repo in repos:
    langs_url = repo.get("languages_url")
    if not langs_url:
        continue
    langs = requests.get(langs_url).json()
    for lang, count in langs.items():
        key = lang.lower()
        if key == "python":
            lang_totals["Python"] += count
        elif key == "html":
            lang_totals["HTML"] += count
        elif key == "css":
            lang_totals["CSS"] += count
        elif key == "javascript":
            lang_totals["JavaScript"] += count
        elif key in ["typescript", "tsx", "jsx"]:
            lang_totals["React"] += count
        elif key == "pygame":
            lang_totals["Pygame"] += count
        elif key == "flask":
            lang_totals["Flask"] += count
        elif key == "fastapi":
            lang_totals["FastAPI"] += count
        elif key == "nodejs":
            lang_totals["Node.js"] += count

# ===== GENERATE NEON SVGS =====
max_count = max(lang_totals.values()) or 1

for tech, count in lang_totals.items():
    bar_length = int((count / max_count) * SVG_WIDTH)
    
    svg_content = f'''<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">
      <!-- Dark Background -->
      <rect width="{SVG_WIDTH}" height="{SVG_HEIGHT}" fill="{BG_COLOR}" rx="5" ry="5"/>
      
      <!-- Neon Bar with Glow -->
      <defs>
        <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="2.5" result="blur"/>
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>
      <rect width="{bar_length}" height="{SVG_HEIGHT}" fill="{BAR_COLOR}" rx="5" ry="5" filter="url(#glow)"/>
    </svg>'''
    
    file_name = tech.lower().replace(".", "") + "-graph.svg"
    svg_file = os.path.join(OUTPUT_DIR, file_name)
    with open(svg_file, "w") as f:
        f.write(svg_content)
