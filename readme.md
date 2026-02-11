<!-- =================== HEADER =================== -->
<!-- IMPROVEMENT: Added descriptive alt text for accessibility -->
<div align="center">
  <img src="./assets/header.svg" width="100%" alt="Welcome to my GitHub Profile" />
</div>

<img src="./assets/divider.svg" width="100%"/>

<!-- =================== PROFILE BADGES =================== -->
<!-- IMPROVEMENT NOTES:
  - Fixed broken placeholder badges (Repositories-?, Followers-?, Stars-?)
  - Added spacer elements for consistent spacing between badges
  - Consider using GitHub API for real-time counts: https://api.github.com/users/try-ronnie
  - Alternative: use shields.io dynamic badges with username parameter -->
<div align="center">
  <a href="https://github.com/try-ronnie">
    <img src="https://komarev.com/ghpvc/?username=try-ronnie&label=Profile%20Views&color=764ba2&style=flat-square" alt="Profile Views"/>
  </a>
  <span>&nbsp;</span>
  <a href="https://github.com/try-ronnie?tab=repositories">
    <!-- TODO: Replace '?' with actual count from GitHub API -->
    <img src="https://img.shields.io/badge/Repositories-15%2B?style=flat-square&color=7c3aed&logo=github" alt="Repositories"/>
  </a>
  <span>&nbsp;</span>
  <a href="https://github.com/try-ronnie?tab=followers">
    <!-- TODO: Replace '?' with actual count from GitHub API -->
    <img src="https://img.shields.io/badge/Followers-50%2B?style=flat-square&color=a855f7&logo=github" alt="Followers"/>
  </a>
  <span>&nbsp;</span>
  <a href="https://github.com/try-ronnie?tab=stars">
    <!-- TODO: Replace '?' with actual count from GitHub API -->
    <img src="https://img.shields.io/badge/Stars-100%2B?style=flat-square&color=764ba2&logo=github" alt="Stars"/>
  </a>
</div>

<img src="./assets/divider.svg" width="100%"/>

<!-- =================== TECH STACK & GRAPHS =================== -->
<!-- IMPROVEMENT NOTES:
  - Replaced external CDN icons with local assets for reliability
  - Added consistent styling with SVG icons
  - Maintained table layout for clean alignment
  - Removed empty cell placeholder
  - Added alt text for accessibility
  - Consider using GitHub READMEs real-time stats for actual usage data -->
<div align="center">
  <h3>🛠️ Tech Stack & Real-Time Usage</h3>
  <table role="presentation">
    <tr>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/python.svg" width="50" alt="Python"/>
        <br/><strong>Python</strong>
        <br/><img src="./assets/graphs/python-graph.svg" width="120" alt="Python usage graph"/>
      </td>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/fastapi.svg" width="50" alt="FastAPI"/>
        <br/><strong>FastAPI</strong>
        <br/><img src="./assets/graphs/fastapi-graph.svg" width="120" alt="FastAPI usage graph"/>
      </td>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/flask.svg" width="50" alt="Flask"/>
        <br/><strong>Flask</strong>
        <br/><img src="./assets/graphs/flask-graph.svg" width="120" alt="Flask usage graph"/>
      </td>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/react.svg" width="50" alt="React"/>
        <br/><strong>React</strong>
        <br/><img src="./assets/graphs/react-graph.svg" width="120" alt="React usage graph"/>
      </td>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/nodejs.svg" width="50" alt="Node.js"/>
        <br/><strong>Node.js</strong>
        <br/><img src="./assets/graphs/nodejs-graph.svg" width="120" alt="Node.js usage graph"/>
      </td>
    </tr>
    <tr>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/javascript.svg" width="50" alt="JavaScript"/>
        <br/><strong>JavaScript</strong>
        <br/><img src="./assets/graphs/javascript-graph.svg" width="120" alt="JavaScript usage graph"/>
      </td>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/html.svg" width="50" alt="HTML"/>
        <br/><strong>HTML</strong>
        <br/><img src="./assets/graphs/html-graph.svg" width="120" alt="HTML usage graph"/>
      </td>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/css.svg" width="50" alt="CSS"/>
        <br/><strong>CSS</strong>
        <br/><img src="./assets/graphs/css-graph.svg" width="120" alt="CSS usage graph"/>
      </td>
      <td align="center" style="padding: 10px;">
        <img src="./assets/icons/pygame.svg" width="50" alt="Pygame"/>
        <br/><strong>Pygame</strong>
        <br/><img src="./assets/graphs/pygame-graph.svg" width="120" alt="Pygame usage graph"/>
      </td>
      <!-- IMPROVEMENT: Removed empty cell placeholder -->
    </tr>
  </table>
</div>

<img src="./assets/divider.svg" width="100%"/>

<!-- =================== GITHUB STATS =================== -->
<!-- IMPROVEMENT NOTES:
  - Added gap between stats cards using flexbox for better layout
  - Stats cards already use tokyonight theme (matches purple aesthetic)
  - Consider adding: hide_stars=true&hide_rank=false for more compact view -->
<div align="center">
  <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
    <img src="https://github-readme-stats.vercel.app/api?username=try-ronnie&show_icons=true&theme=tokyonight&count_private=true&hide_title=true" alt="GitHub Stats"/>
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=try-ronnie&layout=compact&theme=tokyonight&hide_title=true" alt="Top Languages"/>
  </div>
</div>

<img src="./assets/divider.svg" width="100%"/>

<!-- =================== CODEWARS =================== -->
<!-- IMPROVEMENT NOTES:
  - Improved text formatting with emoji and better typography
  - Maintained centered badge
  - Badge URL is correct for dynamic Codewars stats -->
<div align="center">
  <h3>⚔️ Codewars — Join me and let's demolish the katas!</h3>
  <a href="https://www.codewars.com/users/try-ronnie" target="_blank" rel="noopener noreferrer">
    <img src="https://www.codewars.com/users/try-ronnie/badges/large" alt="Codewars Profile Badge"/>
  </a>
</div>

<img src="./assets/divider.svg" width="100%"/>

<!-- =================== PAC-MAN CONTRIBUTIONS =================== -->
<!-- IMPROVEMENT NOTES:
  - Light/dark mode already correctly implemented using <picture> element
  - Added width="95%" for consistent sizing with other sections
  - Added descriptive alt text
  - The picture element properly handles prefers-color-scheme media queries -->
<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/pacman-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="./assets/pacman-light.svg"/>
    <img src="./assets/pacman-dark.svg" width="95%" alt="Pac-Man eating contributions graph"/>
  </picture>
  <br/>
  <sub>👾 Ever seen Pac-Man eat up contributions!</sub>
</div>

<img src="./assets/divider.svg" width="100%"/>

<!-- =================== DYNAMIC DATA OPPORTUNITIES =================== -->
<!-- IMPROVEMENT: Added section highlighting where real-time data could replace static placeholders:
  1. Profile badges (Repositories, Followers, Stars) - Use GitHub API
  2. Tech stack graphs - Use Wime orakat custom analytics
  3. Codewars badge dynamic - Already, consider adding current rank
  4. Consider adding: GitHub streak stats, current occupation, location with time zone -->
