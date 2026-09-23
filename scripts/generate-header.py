from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(exist_ok=True)

PALETTES = {
    "light": {
        "bg_top": "#FBFCFF",
        "bg_bottom": "#EEF3FF",
        "ink": "#171B2A",
        "muted": "#59647B",
        "line": "#D7E1F4",
        "card": "#FFFFFF",
        "blue": "#4C5EDB",
        "blue_soft": "#B9C8FF",
        "peach": "#F0AE92",
        "mint": "#B9E8D4",
        "shadow": "#344472",
    },
    "dark": {
        "bg_top": "#111729",
        "bg_bottom": "#19243B",
        "ink": "#F6F8FE",
        "muted": "#B2BED6",
        "line": "#394764",
        "card": "#202D47",
        "blue": "#9BA9FF",
        "blue_soft": "#6878D5",
        "peach": "#E9A88B",
        "mint": "#7BD8B6",
        "shadow": "#000000",
    },
}


def make_svg(c: dict[str, str]) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320">
  <title>From open loop to clear next step</title>
  <desc>An open task becomes a prepared draft and then a human-reviewed action.</desc>
  <defs>
    <linearGradient id="background" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0" stop-color="{c['bg_top']}"/>
      <stop offset="1" stop-color="{c['bg_bottom']}"/>
    </linearGradient>
    <linearGradient id="thread" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0" stop-color="{c['peach']}"/>
      <stop offset="0.53" stop-color="{c['blue']}"/>
      <stop offset="1" stop-color="{c['mint']}"/>
    </linearGradient>
    <filter id="soft-shadow" x="-25%" y="-35%" width="150%" height="190%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="{c['shadow']}" flood-opacity="0.13"/>
    </filter>
    <clipPath id="clip"><rect x="1" y="1" width="1198" height="318" rx="28"/></clipPath>
  </defs>

  <rect x="1" y="1" width="1198" height="318" rx="28" fill="url(#background)" stroke="{c['line']}" stroke-width="2"/>
  <g clip-path="url(#clip)">
    <circle cx="1120" cy="12" r="180" fill="{c['peach']}" opacity="0.18"/>
    <circle cx="731" cy="339" r="215" fill="{c['blue_soft']}" opacity="0.23"/>
    <circle cx="1051" cy="292" r="155" fill="{c['mint']}" opacity="0.18"/>
    <path d="M624 210 C694 186 696 113 767 119 S883 192 929 175 S1055 117 1110 190" fill="none" stroke="url(#thread)" stroke-width="5" stroke-linecap="round" opacity="0.8"/>
    <path d="M620 234 C710 204 708 142 769 152 S874 220 925 207 S1064 145 1128 216" fill="none" stroke="{c['blue']}" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="3 9" opacity="0.25"/>
  </g>

  <text x="64" y="70" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="700" letter-spacing="2.8" fill="{c['blue']}">STEPHAN MOERMAN  /  KOMMIT AI</text>
  <text x="62" y="151" font-family="Arial, Helvetica, sans-serif" font-size="55" font-weight="700" letter-spacing="-2" fill="{c['ink']}">The next step</text>
  <text x="62" y="212" font-family="Arial, Helvetica, sans-serif" font-size="55" font-weight="700" letter-spacing="-2" fill="{c['ink']}">should happen.</text>
  <rect x="64" y="244" width="35" height="5" rx="2.5" fill="{c['peach']}"/>
  <text x="111" y="252" font-family="Arial, Helvetica, sans-serif" font-size="19" fill="{c['muted']}">AI agents for the work that slips</text>

  <g filter="url(#soft-shadow)">
    <g transform="rotate(-5 741 121)">
      <rect x="638" y="65" width="205" height="113" rx="17" fill="{c['card']}" stroke="{c['line']}"/>
      <circle cx="667" cy="95" r="8" fill="{c['peach']}"/>
      <text x="686" y="100" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" letter-spacing="1.5" fill="{c['muted']}">01  NOTICE</text>
      <text x="661" y="140" font-family="Arial, Helvetica, sans-serif" font-size="19" font-weight="700" fill="{c['ink']}">Open loop</text>
      <rect x="661" y="152" width="111" height="4" rx="2" fill="{c['line']}"/>
    </g>
    <g transform="rotate(4 885 173)">
      <rect x="782" y="114" width="214" height="112" rx="17" fill="{c['card']}" stroke="{c['line']}"/>
      <circle cx="811" cy="144" r="8" fill="{c['blue']}"/>
      <text x="830" y="149" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" letter-spacing="1.5" fill="{c['muted']}">02  PREPARE</text>
      <text x="805" y="187" font-family="Arial, Helvetica, sans-serif" font-size="19" font-weight="700" fill="{c['ink']}">Next draft</text>
      <rect x="805" y="200" width="138" height="4" rx="2" fill="{c['line']}"/>
    </g>
    <g transform="rotate(-3 1046 216)">
      <rect x="941" y="164" width="207" height="113" rx="17" fill="{c['card']}" stroke="{c['line']}"/>
      <circle cx="970" cy="194" r="9" fill="{c['mint']}"/>
      <path d="M966 194 l3 3 5 -6" fill="none" stroke="{c['ink']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="988" y="199" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" letter-spacing="1.3" fill="{c['muted']}">03  REVIEW</text>
      <text x="964" y="237" font-family="Arial, Helvetica, sans-serif" font-size="19" font-weight="700" fill="{c['ink']}">Your call</text>
      <rect x="964" y="250" width="119" height="4" rx="2" fill="{c['line']}"/>
    </g>
  </g>
</svg>
'''


for name, palette in PALETTES.items():
    (OUT / f"header-{name}.svg").write_text(make_svg(palette), encoding="utf-8")
