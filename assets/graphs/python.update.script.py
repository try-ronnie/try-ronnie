import requests
import os

# ===== CONFIG =====
USERNAME = "try-ronnie"  # your GitHub username
OUTPUT_DIR = "./assets/graphs/"
TECHS = ["Python", "FastAPI", "Flask", "React", "Node.js", "JavaScript", "HTML", "CSS", "Pygame"]
SVG_WIDTH = 120
SVG_HEIGHT = 20
BAR_COLOR = "#7c3aed"  # neon purple
BG_COLOR = "#1e1b2a"

# Make sure output directory exists
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
        # Map GitHub language names to your tech names
        if lang.lower() == "python":
            lang_totals["Python"] += count
        elif lang.lower() == "html":
            lang_totals["HTML"] += count
        elif lang.lower() == "css":
            lang_totals["CSS"] += count
        elif lang.lower() == "javascript":
            lang_totals["JavaScript"] += count
        elif lang.lower() == "typescript":
            lang_totals["React"] += count  # approximate React/TSX usage
        elif lang.lower() == "c++" or lang.lower() == "c":
            pass  # ignore for now
        elif lang.lower() == "pygame":
            lang_totals["Pygame"] += count
        elif lang.lower() == "flask":
            lang_totals["Flask"] += count
        elif lang.lower() == "fastapi":
            lang_totals["FastAPI"] += count
        elif lang.lower() == "nodejs":
            lang_totals["Node.js"] += count

# ===== GENERATE SVGS =====
max_count = max(lang_totals.values()) or 1  # avoid division by zero

for tech, count in lang_totals.items():
    bar_length = int((count / max_count) * SVG_WIDTH)
    svg_content = f'''<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">
      <rect width="{SVG_WIDTH}" height="{SVG_HEIGHT}" fill="{BG_COLOR}" rx="5" ry="5"/>
      <rect width="{bar_length}" height="{SVG_HEIGHT}" fill="{BAR_COLOR}" rx="5" ry="5"/>
    </svg>'''
    
    svg_file = os.path.join(OUTPUT_DIR, f"{tech.lower().replace('.', '')}-graph.svg")
    with open(svg_file, "w") as f:
        f.write(svg_content)
    print(f"[+] Generated {svg_file} ({count} bytes)")
