# Terra Beyond

A collection of rules-light tabletop roleplaying settings spanning the three ages of human expansion into the cosmos, written by Roberto Bisceglie and powered by the 24XX engine.

Built as a multi-format Quarto website with automatic PDF, EPUB, Word, OpenDocument, and GFM compilation, and published automatically to GitHub Pages.

## Setting & Eras

1. **Sol: Beyond Earth (The Age of Settlement, 1957–2090)**
   - *Inspiration:* NASA 1970s retrofuturism.
   - *Overview:* Humanity's first steps into the solar system, from lunar settlements and Mars footholds to asteroid mining.
2. **Frontier: Beyond Sol (The Age of Expansion, 2090–2400)**
   - *Inspiration:* Terran Trade Authority.
   - *Overview:* Humanity spreads to nearby star systems (Alpha Centauri, Sirius, Tau Ceti) via stargate portals.
3. **Orion: Beyond the Frontier (The Age of Orion, 2400–4000)**
   - *Inspiration:* Classic Alliance/Union.
   - *Overview:* Fragmented galactic polities, transhumanist mind-uploading, psionic Resonants, ancient Precursor ruins, and contacts with enigmatic alien civilizations like the Zynthari.

There is also a unified **Terra Beyond Timeline** mapping the events of the universe from 1957 to 4000 AD, and the **Sol Union Standard Calendar**, the in-universe civil calendar ratified under the Federated Autonomy Treaty.

## Website & Multi-Format Exports

This repository is built using [Quarto](https://quarto.org/). Each page compiles from a single source file to several formats:
- **HTML Website:** Clean, responsive, supports light and dark themes.
- **PDF Booklets:** Professionally typeset using **Typst**.
- **EPUB E-books**
- **Word Document (.docx)**
- **OpenDocument (.odt)**
- **GitHub Flavored Markdown (.md)**

Download links for alternate formats are automatically generated and placed at the top of the sidebar.

## Structure

```
├── .github/workflows/
│   └── publish.yml          # GitHub Actions auto-publish workflow
├── _extensions/             # Custom Typst and GFM extensions
├── assets/                  # Custom SCSS and web assets
├── docs/
│   ├── assets/              # Logo
│   ├── sol-beyond-earth.md  # Sol: Beyond Earth rules & setting
│   ├── frontier-beyond-sol.md # Frontier: Beyond Sol rules & setting
│   ├── orion-beyond-the-frontier.md # Orion: Beyond the Frontier rules & setting
│   ├── terra_beyond_timeline.md # Universal timeline
│   ├── sol_union_calendar.md # Sol Union Standard Calendar reference
│   └── about.qmd            # About page
├── sol_beyond_earth/        # Raw source modules for Sol: Beyond Earth
├── frontier_beyond_sol/     # Raw source modules for Frontier: Beyond Sol
├── orion_beyond_the_frontier/ # Raw source modules for Orion: Beyond the Frontier
├── index.qmd                # Landing page
├── _brand.yml               # Branding options
├── _quarto.yml              # Main configuration
└── README.md                # This file
```

## Local Development

Ensure you have [Quarto](https://quarto.org/docs/get-started/) installed.

### Preview the Website
To start a local preview server with live reload:
```bash
quarto preview
```

### Render the Website
To render all pages and formats to the `_site/` directory:
```bash
quarto render
```

## License

- Rules and settings © 2023-2026 Roberto Bisceglie.
- Powered by the **24XX SRD** by Jason Tocci, licensed under CC BY 4.0.
- Cover and internal illustrations are released in the public domain by NASA.
- This work is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.
