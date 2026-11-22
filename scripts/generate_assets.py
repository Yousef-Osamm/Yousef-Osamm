"""Generate the animated SVGs in ../assets (hero, marquee, section headers, stats, arch).

Run:  python3 scripts/generate_assets.py
Edit the `rows` list in stats() to update the skill levels.
"""
import math
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")

FONTS = """
    .mono{font-family:ui-monospace,SFMono-Regular,"JetBrains Mono",Menlo,Consolas,"Liberation Mono",monospace}
    .sans{font-family:"Segoe UI",-apple-system,BlinkMacSystemFont,"Inter",Ubuntu,"Helvetica Neue",Arial,sans-serif}
"""
CY, YE, GR = "#61DAFB", "#FFD43B", "#44B78B"
BG = "#070B14"

EDGE = f"""<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CY}" stop-opacity=".55"/><stop offset=".5" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="{GR}" stop-opacity=".55"/></linearGradient>"""


def write(name, svg):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg.strip() + "\n")


# ─────────────────────────────────────────────────────────────── HERO
def hero():
    W, H, HZ = 1000, 440, 318  # horizon y
    # perspective floor: converging verticals
    verts = []
    for k in range(-14, 15):
        xt, xb = 500 + k * 16, 500 + k * 120
        verts.append(f'<line x1="{xt}" y1="{HZ}" x2="{xb}" y2="{H}"/>')
    # horizontal lines rushing toward the viewer
    hors = []
    n = 7
    for i in range(n):
        b = f"{i * 2.8 / n:.2f}s"
        hors.append(
            f'<line x1="0" x2="{W}" y1="{HZ}" y2="{HZ}">'
            f'<animate attributeName="y1" values="{HZ};{H}" dur="2.8s" begin="{b}" repeatCount="indefinite" calcMode="spline" keySplines=".55 0 1 1"/>'
            f'<animate attributeName="y2" values="{HZ};{H}" dur="2.8s" begin="{b}" repeatCount="indefinite" calcMode="spline" keySplines=".55 0 1 1"/>'
            f'<animate attributeName="stroke-opacity" values="0;.9" dur="2.8s" begin="{b}" repeatCount="indefinite" calcMode="spline" keySplines=".55 0 1 1"/>'
            "</line>"
        )
    stars = []
    pts = [(560, 40), (640, 120), (705, 58), (930, 74), (975, 210), (600, 250), (880, 30), (470, 30), (520, 120), (955, 280), (660, 290), (420, 100)]
    for i, (x, y) in enumerate(pts):
        stars.append(f'<circle class="tw" cx="{x}" cy="{y}" r="{1 + (i % 3) * .4:.1f}" style="animation-delay:{(i * .37) % 3:.2f}s"/>')

    boot_lines = [
        ('<tspan fill="#6B7A99">&gt;</tspan> booting <tspan fill="#E6EDF7">YOUSEF_OS</tspan> v2.0 ...', ""),
        ('<tspan fill="#44B78B">[  OK  ]</tspan> html · css · javascript', ""),
        ('<tspan fill="#44B78B">[  OK  ]</tspan> responsive ui engine', ""),
        ('<tspan fill="#44B78B">[  OK  ]</tspan> git · github · vscode', ""),
        ('<tspan fill="#61DAFB">[ LOAD ]</tspan> react runtime ............ 45%', ""),
        ('<tspan fill="#FFD43B">[ BUILD]</tspan> python · django ......... compiling', ""),
        ('<tspan fill="#6B7A99">&gt;</tspan> launching profile<tspan class="blink" fill="#61DAFB">_</tspan>', ""),
    ]
    boot = []
    for i, (t, _) in enumerate(boot_lines):
        boot.append(f'<text x="48" y="{78 + i * 30}" class="bl" style="animation-delay:{.15 + i * .36:.2f}s">{t}</text>')

    corners = []
    for (x, y, sx, sy) in [(18, 18, 1, 1), (982, 18, -1, 1), (18, 422, 1, -1), (982, 422, -1, -1)]:
        corners.append(f'<path d="M{x} {y + 22 * sy}V{y}H{x + 22 * sx}" />')

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
  <title id="title">Yousef Osama — Full-Stack Developer in the making</title>
  <desc id="desc">Cinematic animated banner: a boot sequence glitches into the name Yousef Osama, Full-Stack Developer in the making, React, Python and Django, above a neon perspective floor with a rotating 3D atom.</desc>
  <style>{FONTS}
    .bl{{opacity:0;animation:show .01s linear forwards}}
    @keyframes show{{to{{opacity:1}}}}
    .boot{{transform-origin:500px 220px;animation:bootOut .45s ease-in 2.9s forwards}}
    @keyframes bootOut{{0%{{opacity:1;transform:scaleY(1)}}60%{{opacity:1;transform:scaleY(.01)}}100%{{opacity:0;transform:scaleY(0)}}}}
    .bootwrap{{transform-origin:500px 220px}}
    .flash{{opacity:0;animation:flash .9s ease-out 3.15s}}
    @keyframes flash{{0%{{opacity:0}}12%{{opacity:.85}}100%{{opacity:0}}}}
    .in{{opacity:0;animation:in 1s cubic-bezier(.2,.8,.2,1) forwards}}
    @keyframes in{{from{{opacity:0;transform:translateY(16px)}}to{{opacity:1;transform:translateY(0)}}}}
    .gA{{opacity:0;animation:gA 7s steps(1) 3.2s infinite}}
    .gB{{opacity:0;animation:gB 7s steps(1) 3.2s infinite}}
    @keyframes gA{{0%{{opacity:.85;transform:translate(-7px,0)}}2%{{transform:translate(5px,-2px)}}4%{{transform:translate(-3px,2px)}}6%{{transform:translate(8px,0)}}8%{{opacity:0}}60%{{opacity:0}}61%{{opacity:.8;transform:translate(4px,0)}}62.5%{{transform:translate(-5px,1px)}}64%{{opacity:0}}}}
    @keyframes gB{{0%{{opacity:.85;transform:translate(7px,1px)}}2%{{transform:translate(-6px,0)}}4%{{transform:translate(3px,-2px)}}6%{{transform:translate(-8px,0)}}8%{{opacity:0}}60%{{opacity:0}}61%{{opacity:.8;transform:translate(-4px,0)}}62.5%{{transform:translate(5px,-1px)}}64%{{opacity:0}}}}
    .slice{{opacity:0;animation:slice 7s steps(1) 3.2s infinite}}
    @keyframes slice{{0%{{opacity:1;transform:translateX(18px)}}3%{{transform:translateX(-14px)}}6%{{opacity:0}}61%{{opacity:1;transform:translateX(-10px)}}63%{{opacity:0}}}}
    .tw{{fill:#CFE8FF;animation:tw 3.2s ease-in-out infinite}}
    @keyframes tw{{0%,100%{{opacity:.12}}50%{{opacity:.95}}}}
    .spin{{transform-origin:790px 160px;animation:spin 30s linear infinite}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
    .pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 2.4s ease-in-out infinite}}
    @keyframes pulse{{0%,100%{{transform:scale(1);opacity:.9}}50%{{transform:scale(1.35);opacity:.5}}}}
    .blink{{animation:blink 1s steps(1) infinite}}
    @keyframes blink{{50%{{opacity:0}}}}
    .dot{{animation:dot 1.4s ease-in-out infinite}}
    @keyframes dot{{0%,100%{{opacity:1}}50%{{opacity:.2}}}}
    .scan{{animation:scan 6s linear infinite}}
    @keyframes scan{{from{{transform:translateY(-90px)}}to{{transform:translateY(460px)}}}}
  </style>
  <defs>
    {EDGE}
    <radialGradient id="auC"><stop offset="0" stop-color="{CY}" stop-opacity=".35"/><stop offset="1" stop-color="{CY}" stop-opacity="0"/></radialGradient>
    <radialGradient id="auG"><stop offset="0" stop-color="{GR}" stop-opacity=".3"/><stop offset="1" stop-color="{GR}" stop-opacity="0"/></radialGradient>
    <radialGradient id="auY"><stop offset="0" stop-color="{YE}" stop-opacity=".14"/><stop offset="1" stop-color="{YE}" stop-opacity="0"/></radialGradient>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05070E"/><stop offset="1" stop-color="#0B1424"/></linearGradient>
    <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0A1B2B"/><stop offset="1" stop-color="#04070D"/></linearGradient>
    <linearGradient id="gridC" x1="0" x2="1"><stop offset="0" stop-color="{CY}"/><stop offset=".5" stop-color="{YE}"/><stop offset="1" stop-color="{GR}"/></linearGradient>
    <linearGradient id="hzG" x1="0" x2="1"><stop offset="0" stop-color="{CY}" stop-opacity="0"/><stop offset=".3" stop-color="{CY}"/><stop offset=".7" stop-color="{GR}"/><stop offset="1" stop-color="{GR}" stop-opacity="0"/></linearGradient>
    <linearGradient id="fadeY" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000"/><stop offset=".2" stop-color="#888"/><stop offset="1" stop-color="#fff"/></linearGradient>
    <mask id="floorMask"><rect y="{HZ}" width="{W}" height="{H - HZ}" fill="url(#fadeY)"/></mask>
    <linearGradient id="reflG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".5"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <mask id="reflMask"><rect y="{HZ}" width="{W}" height="{H - HZ}" fill="url(#reflG)"/></mask>
    <linearGradient id="name" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="560" y2="0" spreadMethod="reflect">
      <stop offset="0" stop-color="{CY}"/><stop offset=".45" stop-color="#F2FBFF"/><stop offset="1" stop-color="{GR}"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="1120 0" dur="7s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{CY}"/><stop offset=".55" stop-color="{YE}"/><stop offset="1" stop-color="{GR}"/></linearGradient>
    <linearGradient id="sheen" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <linearGradient id="scanG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CY}" stop-opacity="0"/><stop offset=".5" stop-color="{CY}" stop-opacity=".07"/><stop offset="1" stop-color="{CY}" stop-opacity="0"/></linearGradient>
    <pattern id="lines" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" fill-opacity=".025"/></pattern>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <filter id="blur" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="10"/></filter>
    <clipPath id="card"><rect width="{W}" height="{H}" rx="22"/></clipPath>
    <clipPath id="band"><rect x="0" y="122" width="{W}" height="16"/></clipPath>
    <clipPath id="type"><rect x="56" y="54" width="0" height="30"><animate attributeName="width" values="0;580" dur="1.6s" begin="3.5s" fill="freeze" calcMode="spline" keySplines=".4 0 .6 1"/></rect></clipPath>
    <clipPath id="barclip"><rect x="62" y="388" width="476" height="8" rx="4"/></clipPath>

    <g id="atom">
      <circle cx="790" cy="160" r="150" fill="none" stroke="#9FB4D9" stroke-opacity=".14" stroke-dasharray="2 9"/>
      <g class="spin">
        <g transform="rotate(0 790 160)"><ellipse cx="790" cy="160" rx="132" ry="20" fill="none" stroke="{CY}" stroke-width="2" stroke-opacity=".85"><animate attributeName="ry" values="20;74;20" dur="5s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></ellipse></g>
        <g transform="rotate(60 790 160)"><ellipse cx="790" cy="160" rx="132" ry="74" fill="none" stroke="{CY}" stroke-width="2" stroke-opacity=".85"><animate attributeName="ry" values="74;20;74" dur="5s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></ellipse></g>
        <g transform="rotate(120 790 160)"><ellipse cx="790" cy="160" rx="132" ry="47" fill="none" stroke="{CY}" stroke-width="2" stroke-opacity=".85"><animate attributeName="ry" values="47;20;47;74;47" dur="5s" repeatCount="indefinite"/></ellipse></g>
      </g>
      <circle r="6" fill="{CY}" filter="url(#glow)"><animateMotion dur="4s" repeatCount="indefinite" path="M640 160a150 150 0 1 0 300 0a150 150 0 1 0-300 0"/></circle>
      <circle r="6" fill="{YE}" filter="url(#glow)"><animateMotion dur="6s" repeatCount="indefinite" path="M940 160a150 150 0 1 0-300 0a150 150 0 1 0 300 0"/></circle>
      <circle r="6" fill="{GR}" filter="url(#glow)"><animateMotion dur="8s" repeatCount="indefinite" path="M790 10a150 150 0 1 1 0 300a150 150 0 1 1 0-300"/></circle>
      <circle cx="790" cy="160" r="26" fill="{CY}" opacity=".45" filter="url(#blur)" class="pulse"/>
      <circle cx="790" cy="160" r="13" fill="{CY}"/>
      <circle cx="790" cy="160" r="5.5" fill="#F2FBFF"/>
    </g>
  </defs>

  <g clip-path="url(#card)">
    <!-- ══════════ SCENE ══════════ -->
    <rect width="{W}" height="{H}" fill="url(#sky)"/>
    <circle cx="160" cy="40" r="320" fill="url(#auC)"><animate attributeName="cx" values="160;260;160" dur="16s" repeatCount="indefinite"/></circle>
    <circle cx="900" cy="300" r="300" fill="url(#auG)"><animate attributeName="cy" values="300;240;300" dur="12s" repeatCount="indefinite"/></circle>
    <circle cx="560" cy="180" r="240" fill="url(#auY)"/>
    {''.join(stars)}
    <!-- shooting star -->
    <line x1="0" y1="0" x2="70" y2="22" stroke="#E6F6FF" stroke-width="1.6" stroke-linecap="round" opacity="0">
      <animate attributeName="opacity" values="0;1;0;0" keyTimes="0;.04;.12;1" dur="9s" begin="5s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate" values="420 20;640 90;640 90" keyTimes="0;.12;1" dur="9s" begin="5s" repeatCount="indefinite"/>
    </line>

    <!-- floor -->
    <rect y="{HZ}" width="{W}" height="{H - HZ}" fill="url(#floor)"/>
    <use href="#atom" transform="translate(0 {2 * HZ}) scale(1 -1)" mask="url(#reflMask)" opacity=".35"/>
    <g mask="url(#floorMask)" stroke="url(#gridC)" stroke-width="1.2" stroke-opacity=".55">
      {''.join(verts)}
    </g>
    <g mask="url(#floorMask)" stroke="url(#gridC)" stroke-width="1.4">
      {''.join(hors)}
    </g>
    <ellipse cx="500" cy="{HZ}" rx="520" ry="16" fill="{CY}" opacity=".18" filter="url(#blur)"/>
    <rect x="0" y="{HZ - 1}" width="{W}" height="2" fill="url(#hzG)"/>

    <!-- atom -->
    <use href="#atom"/>

    <!-- HUD -->
    <g fill="none" stroke="{CY}" stroke-opacity=".6" stroke-width="2">{''.join(corners)}</g>
    <g class="mono" font-size="11" fill="#5E6E8E" letter-spacing="1.5">
      <text x="48" y="38">YOUSEF_OS · v2.0</text>
      <text x="952" y="410" text-anchor="end">MODE: LEARNING  <tspan class="dot" fill="{GR}">●</tspan> LIVE</text>
    </g>

    <!-- typed command -->
    <g clip-path="url(#type)">
      <text x="60" y="76" class="mono" font-size="15" fill="#6B7A99"><tspan fill="{GR}">❯</tspan> <tspan fill="#8FA3C7">yousef</tspan> build <tspan fill="{CY}">--target</tspan> fullstack <tspan fill="{YE}">--stack</tspan> react,django</text>
    </g>

    <!-- name with glitch layers -->
    <g class="in" style="animation-delay:3.15s">
      <text x="56" y="168" class="sans" font-size="76" font-weight="800" letter-spacing="-2" fill="url(#name)">Yousef Osama</text>
    </g>
    <g class="gA" style="mix-blend-mode:screen"><text x="56" y="168" class="sans" font-size="76" font-weight="800" letter-spacing="-2" fill="{CY}" opacity=".8">Yousef Osama</text></g>
    <g class="gB" style="mix-blend-mode:screen"><text x="56" y="168" class="sans" font-size="76" font-weight="800" letter-spacing="-2" fill="{YE}" opacity=".7">Yousef Osama</text></g>
    <g class="slice" clip-path="url(#band)"><g><text x="56" y="168" class="sans" font-size="76" font-weight="800" letter-spacing="-2" fill="#F2FBFF">Yousef Osama</text></g></g>

    <g class="in" style="animation-delay:3.4s">
      <text x="60" y="210" class="sans" font-size="22" font-weight="500" fill="#C9D4E5">Full-Stack Developer <tspan fill="#56647F">—</tspan> <tspan fill="#fff" font-style="italic">in the making</tspan></text>
    </g>
    <g class="in mono" font-size="13.5" style="animation-delay:3.6s">
      <g transform="translate(60 232)"><rect width="104" height="32" rx="9" fill="{CY}" fill-opacity=".1" stroke="{CY}" stroke-opacity=".6"/><circle cx="18" cy="16" r="4" fill="{CY}"/><text x="30" y="21" fill="#BDEFFF">React</text></g>
      <g transform="translate(176 232)"><rect width="112" height="32" rx="9" fill="{YE}" fill-opacity=".08" stroke="{YE}" stroke-opacity=".55"/><circle cx="18" cy="16" r="4" fill="{YE}"/><text x="30" y="21" fill="#FFF1B8">Python</text></g>
      <g transform="translate(300 232)"><rect width="112" height="32" rx="9" fill="{GR}" fill-opacity=".1" stroke="{GR}" stroke-opacity=".6"/><circle cx="18" cy="16" r="4" fill="{GR}"/><text x="30" y="21" fill="#BFF2DA">Django</text></g>
    </g>

    <!-- build HUD on the floor -->
    <g class="in" style="animation-delay:3.8s">
      <rect x="44" y="344" width="510" height="72" rx="12" fill="#05080F" fill-opacity=".82" stroke="#1E2A3D"/>
      <text x="62" y="372" class="mono" font-size="12.5" fill="#6B7A99">compiling <tspan fill="#C9D4E5">full_stack_developer</tspan></text>
      <text x="538" y="372" class="mono" font-size="12.5" text-anchor="end"><tspan fill="{GR}">frontend ✓</tspan><tspan fill="#56647F">  ·  </tspan><tspan fill="{YE}">backend ⟳</tspan></text>
      <rect x="62" y="388" width="476" height="8" rx="4" fill="#141C2E"/>
      <g clip-path="url(#barclip)">
        <rect x="62" y="388" width="0" height="8" rx="4" fill="url(#bar)"><animate attributeName="width" values="0;309" dur="2.2s" begin="4.2s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1"/></rect>
        <rect x="-60" y="388" width="60" height="8" fill="url(#sheen)"><animate attributeName="x" values="-60;371" dur="2.4s" begin="6.5s" repeatCount="indefinite"/></rect>
      </g>
      <text x="538" y="408" class="mono" font-size="10.5" fill="#4F5D7A" text-anchor="end">65% · next: Django REST Framework</text>
    </g>

    <!-- scanlines -->
    <rect width="{W}" height="{H}" fill="url(#lines)" pointer-events="none"/>
    <rect class="scan" width="{W}" height="90" fill="url(#scanG)"/>

    <!-- ══════════ BOOT OVERLAY ══════════ -->
    <g class="bootwrap"><g class="boot">
      <rect width="{W}" height="{H}" fill="#03050A"/>
      <rect width="{W}" height="{H}" fill="url(#lines)"/>
      <g class="mono" font-size="15" fill="#AEB9CC">{''.join(boot)}</g>
      <rect x="48" y="300" width="420" height="4" rx="2" fill="#141C2E"/>
      <rect x="48" y="300" width="0" height="4" rx="2" fill="url(#bar)"><animate attributeName="width" values="0;420" dur="2.6s" begin=".1s" fill="freeze"/></rect>
      <text x="48" y="330" class="mono" font-size="11" fill="#3E4C68" letter-spacing="2">LOADING DEVELOPER PROFILE</text>
    </g></g>
    <rect class="flash" width="{W}" height="{H}" fill="#E6F6FF"/>
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="21.5" fill="none" stroke="url(#edge)"/>
</svg>
"""
    write("hero.svg", svg)


# ─────────────────────────────────────────────────────────────── MARQUEE
def marquee():
    W, H = 1000, 112
    big = "REACT • DJANGO • PYTHON • JAVASCRIPT • REST APIs • HTML • CSS • "
    small = "learn → build → ship → repeat   //   frontend ✓   //   backend ⟳   //   full-stack loading   //   "
    L1, L2 = 1900, 1000
    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="React, Django, Python, JavaScript, REST APIs, HTML, CSS — learn, build, ship, repeat">
  <style>{FONTS}
    .m1{{animation:m1 36s linear infinite}}
    .m2{{animation:m2 22s linear infinite}}
    @keyframes m1{{to{{transform:translateX(-{L1}px)}}}}
    @keyframes m2{{from{{transform:translateX(-{L2}px)}}to{{transform:translateX(0)}}}}
  </style>
  <defs>
    {EDGE}
    <linearGradient id="st" gradientUnits="userSpaceOnUse" x1="0" x2="950" spreadMethod="reflect"><stop offset="0" stop-color="{CY}"/><stop offset=".5" stop-color="{YE}"/><stop offset="1" stop-color="{GR}"/></linearGradient>
    <linearGradient id="fx" x1="0" x2="1"><stop offset="0" stop-color="#000"/><stop offset=".1" stop-color="#fff"/><stop offset=".9" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
    <mask id="m"><rect width="{W}" height="{H}" fill="url(#fx)"/></mask>
    <clipPath id="c"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <g mask="url(#m)">
      <g class="m1 sans" font-size="54" font-weight="900" fill="none" stroke="url(#st)" stroke-width="1.4" letter-spacing="2">
        <text x="0" y="64" textLength="{L1}" lengthAdjust="spacingAndGlyphs">{big}</text>
        <text x="{L1}" y="64" textLength="{L1}" lengthAdjust="spacingAndGlyphs">{big}</text>
      </g>
      <g class="m2 mono" font-size="13" fill="#6B7A99">
        <text x="0" y="96" textLength="{L2}" lengthAdjust="spacing">{small}</text>
        <text x="{L2}" y="96" textLength="{L2}" lengthAdjust="spacing">{small}</text>
      </g>
    </g>
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="17.5" fill="none" stroke="url(#edge)"/>
</svg>
"""
    write("marquee.svg", svg)


# ─────────────────────────────────────────────────────────────── SECTION HEADERS
SECTIONS = [
    ("01", "whoami", "who I am &amp; how I think"),
    ("02", "character_sheet", "stats, perks &amp; current level"),
    ("03", "system.architecture", "how I'll ship full-stack apps"),
    ("04", "roadmap", "where I am · where I'm going"),
    ("05", "toolbox", "what's in my hands right now"),
    ("06", "github_pulse", "the receipts"),
    ("07", "connect", "let's build something together"),
]


def headers():
    W, H = 1000, 78
    for i, (num, title, sub) in enumerate(SECTIONS):
        svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{num} — {title}: {sub}">
  <style>{FONTS}
    .in{{opacity:0;animation:in .8s cubic-bezier(.2,.8,.2,1) .1s forwards}}
    @keyframes in{{from{{opacity:0;transform:translateX(-14px)}}to{{opacity:1;transform:translateX(0)}}}}
    .blink{{animation:blink 1s steps(1) infinite}}
    @keyframes blink{{50%{{opacity:0}}}}
  </style>
  <defs>
    {EDGE}
    <linearGradient id="num" x1="0" x2="1"><stop offset="0" stop-color="{CY}"/><stop offset="1" stop-color="{GR}"/></linearGradient>
    <linearGradient id="sweep" x1="0" x2="1"><stop offset="0" stop-color="{CY}" stop-opacity="0"/><stop offset=".5" stop-color="{CY}" stop-opacity=".9"/><stop offset="1" stop-color="{GR}" stop-opacity="0"/></linearGradient>
    <linearGradient id="glowL" x1="0" x2="1"><stop offset="0" stop-color="{CY}" stop-opacity=".12"/><stop offset=".5" stop-color="{CY}" stop-opacity="0"/></linearGradient>
    <clipPath id="c"><rect width="{W}" height="{H}" rx="16"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <rect width="{W}" height="{H}" fill="url(#glowL)"/>
    <rect x="-300" y="{H - 2}" width="300" height="2" fill="url(#sweep)"><animate attributeName="x" values="-300;1000" dur="4s" begin="{i * .3:.1f}s" repeatCount="indefinite"/></rect>
    <g class="in">
      <text x="28" y="55" class="sans" font-size="44" font-weight="900" fill="none" stroke="url(#num)" stroke-width="1.3">{num}</text>
      <rect x="100" y="20" width="1.5" height="38" fill="#1E2A3D"/>
      <text x="120" y="40" class="mono" font-size="21" font-weight="700" fill="#E6EDF7"><tspan fill="{GR}">❯ </tspan>{title}<tspan class="blink" fill="{CY}">_</tspan></text>
      <text x="120" y="60" class="mono" font-size="12" fill="#5E6E8E">// {sub}</text>
    </g>
    <text x="972" y="44" class="mono" font-size="11" fill="#2E3B55" text-anchor="end" letter-spacing="2">SECTION {num} / {len(SECTIONS):02d}</text>
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="15.5" fill="none" stroke="url(#edge)"/>
</svg>
"""
        write(f"sec-{num}.svg", svg)


# ─────────────────────────────────────────────────────────────── CHARACTER SHEET
def stats():
    W, H = 1000, 450
    cx, cy = 190, 150

    def hexagon(r):
        return " ".join(f"{cx + r * math.cos(math.radians(60 * k - 90)):.1f},{cy + r * math.sin(math.radians(60 * k - 90)):.1f}" for k in range(6))

    rows = [
        ("HTML", "semantics", 85, "#E8704A", False),
        ("CSS", "responsive", 80, "#4F8CF7", False),
        ("JavaScript", "DOM · logic", 65, "#F7DF1E", False),
        ("React", "hooks · JSX", 40, CY, True),
        ("Python", "OOP · logic", 35, YE, True),
        ("Django", "models · ORM", 15, GR, True),
    ]
    bars = []
    x0, seg, gap, nseg = 560, 16, 4, 20
    for r, (name, sub, val, col, learning) in enumerate(rows):
        y = 104 + r * 48
        filled = round(val / 5)
        bars.append(f'<text x="410" y="{y + 4}" class="sans" font-size="15" font-weight="700" fill="#E6EDF7">{name}</text>')
        bars.append(f'<text x="410" y="{y + 21}" class="mono" font-size="10.5" fill="#4F5D7A">{sub}</text>')
        tag = f'<tspan fill="{col}">{val}</tspan>'
        bars.append(f'<text x="544" y="{y + 10}" class="mono" font-size="14" font-weight="700" text-anchor="end" fill="#6B7A99">{tag}</text>')
        for s in range(nseg):
            x = x0 + s * (seg + gap)
            bars.append(f'<rect x="{x}" y="{y - 4}" width="{seg}" height="18" rx="3" fill="#121A2B"/>')
            if s < filled:
                d = .3 + r * .18 + s * .045
                cls = "sg edge" if (learning and s == filled - 1) else "sg"
                bars.append(f'<rect class="{cls}" x="{x}" y="{y - 4}" width="{seg}" height="18" rx="3" fill="{col}" style="animation-delay:{d:.2f}s"/>')
        if learning:
            bars.append(f'<text x="{x0 + filled * (seg + gap) + 6}" y="{y + 10}" class="mono up" font-size="11" fill="{col}" style="animation-delay:{.3 + r * .18 + filled * .045 + .2:.2f}s">▲ leveling</text>')

    perks = ["Responsive layouts", "Clean UI", "Fast learner", "Consistent"]
    px = 410
    chips = []
    for i, p in enumerate(perks):
        w = len(p) * 7.3 + 30
        chips.append(f'<g class="up" style="animation-delay:{1.8 + i * .15:.2f}s"><rect x="{px}" y="394" width="{w:.0f}" height="28" rx="14" fill="#0F1726" stroke="#24324C"/><circle cx="{px + 14}" cy="408" r="3" fill="{[CY, YE, GR, "#C792EA"][i]}"/><text x="{px + 23}" y="412.5" class="mono" font-size="12" fill="#AEB9CC">{p}</text></g>')
        px += w + 10

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
  <title id="title">Character sheet — Yousef Osama</title>
  <desc id="desc">RPG-style character sheet. Class: Frontend Developer, evolving into Full-Stack (65%). Self-rated skills: HTML 85, CSS 80, JavaScript 65, React 40, Python 35, Django 15. Perks: responsive layouts, clean UI, fast learner, consistent.</desc>
  <style>{FONTS}
    .sg{{opacity:0;animation:sg .25s ease-out forwards}}
    @keyframes sg{{from{{opacity:0}}to{{opacity:1}}}}
    .edge{{animation:sg .25s ease-out forwards,edge 1.4s ease-in-out 3s infinite}}
    @keyframes edge{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
    .up{{opacity:0;animation:up .6s cubic-bezier(.2,.8,.2,1) forwards}}
    @keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
    .spin{{transform-origin:{cx}px {cy}px;animation:spin 24s linear infinite}}
    .spinr{{transform-origin:{cx}px {cy}px;animation:spin 16s linear infinite reverse}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
    .breath{{transform-origin:{cx}px {cy}px;animation:breath 3s ease-in-out infinite}}
    @keyframes breath{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.04)}}}}
    .blink{{animation:blink 1.2s steps(1) infinite}}
    @keyframes blink{{50%{{opacity:.15}}}}
  </style>
  <defs>
    {EDGE}
    <linearGradient id="mono" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CY}"/><stop offset=".5" stop-color="#F2FBFF"/><stop offset="1" stop-color="{GR}"/></linearGradient>
    <linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{CY}"/><stop offset=".55" stop-color="{YE}"/><stop offset="1" stop-color="{GR}"/></linearGradient>
    <linearGradient id="sheen" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".6"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <radialGradient id="halo"><stop offset="0" stop-color="{CY}" stop-opacity=".3"/><stop offset="1" stop-color="{CY}" stop-opacity="0"/></radialGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#9FB4D9" fill-opacity=".07"/></pattern>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <clipPath id="c"><rect width="{W}" height="{H}" rx="22"/></clipPath>
    <clipPath id="evo"><rect x="60" y="372" width="260" height="8" rx="4"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect width="{W}" height="{H}" fill="#0A0F1A"/>
    <rect width="{W}" height="{H}" fill="url(#dots)"/>
    <rect x="0" y="0" width="372" height="{H}" fill="{BG}"/>
    <rect x="372" y="0" width="1" height="{H}" fill="#1A2438"/>

    <!-- emblem -->
    <circle cx="{cx}" cy="{cy}" r="120" fill="url(#halo)"/>
    <g class="spin"><circle cx="{cx}" cy="{cy}" r="96" fill="none" stroke="{CY}" stroke-opacity=".45" stroke-dasharray="3 9" stroke-width="2"/></g>
    <g class="spinr">
      <circle cx="{cx}" cy="{cy}" r="110" fill="none" stroke="#9FB4D9" stroke-opacity=".12"/>
      <circle cx="{cx}" cy="{cy - 110}" r="5" fill="{CY}" filter="url(#glow)"/>
      <circle cx="{cx + 95.3:.1f}" cy="{cy + 55}" r="5" fill="{YE}" filter="url(#glow)"/>
      <circle cx="{cx - 95.3:.1f}" cy="{cy + 55}" r="5" fill="{GR}" filter="url(#glow)"/>
    </g>
    <g class="breath">
      <polygon points="{hexagon(72)}" fill="#0B1322" stroke="url(#mono)" stroke-width="2.5"/>
      <polygon points="{hexagon(60)}" fill="none" stroke="#1E2A3D"/>
      <text x="{cx}" y="{cy + 16}" text-anchor="middle" class="sans" font-size="46" font-weight="900" letter-spacing="-1" fill="url(#mono)">YO</text>
    </g>

    <text x="{cx}" y="298" text-anchor="middle" class="sans" font-size="22" font-weight="800" fill="#E6EDF7" letter-spacing="1">YOUSEF OSAMA</text>
    <text x="{cx}" y="322" text-anchor="middle" class="mono" font-size="11.5" fill="#5E6E8E" letter-spacing="2">CLASS · FRONTEND DEVELOPER</text>
    <text x="60" y="360" class="mono" font-size="11.5" fill="{YE}" letter-spacing="1.5">EVOLVING ▸ FULL-STACK<tspan class="blink"> ◆</tspan></text>
    <text x="320" y="360" class="mono" font-size="11.5" fill="#6B7A99" text-anchor="end">65%</text>
    <rect x="60" y="372" width="260" height="8" rx="4" fill="#141C2E"/>
    <g clip-path="url(#evo)">
      <rect x="60" y="372" width="0" height="8" rx="4" fill="url(#bar)"><animate attributeName="width" values="0;169" dur="2s" begin=".4s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1"/></rect>
      <rect x="-60" y="372" width="60" height="8" fill="url(#sheen)"><animate attributeName="x" values="-60;229" dur="2.2s" begin="2.6s" repeatCount="indefinite"/></rect>
    </g>
    <text x="60" y="404" class="mono" font-size="10.5" fill="#3E4C68">next unlock: Django REST Framework</text>

    <!-- attributes -->
    <text x="410" y="52" class="mono" font-size="13" fill="#4F5D7A">// attributes.json</text>
    <text x="960" y="52" class="mono" font-size="11" fill="#3E4C68" text-anchor="end" letter-spacing="1.5">SELF-RATED · UPDATED 2026</text>
    {''.join(bars)}
    {''.join(chips)}
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="21.5" fill="none" stroke="url(#edge)"/>
</svg>
"""
    write("stats.svg", svg)


# ─────────────────────────────────────────────────────────────── ARCHITECTURE
def arch():
    W, H = 1000, 430
    Y = 236  # wire y
    nodes = [110, 300, 510, 700, 890]
    cw, ch, top = 140, 148, 172

    def card(x, live, delay):
        stroke = f'stroke="{CY}" stroke-opacity=".55"' if live else f'stroke="#3A4A66" stroke-dasharray="4 4"'
        fill = "#0B1626" if live else "#0A0F1A"
        return f'<g class="pop" style="animation-delay:{delay}s"><rect x="{x - cw / 2}" y="{top}" width="{cw}" height="{ch}" rx="14" fill="{fill}" {stroke}/></g>'

    svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
  <title id="title">System architecture — how I'll ship full-stack apps</title>
  <desc id="desc">Animated diagram. Frontend zone (online): Browser and React UI exchange data. Backend zone (under construction): REST API with Django REST Framework, Django, and PostgreSQL, with requests flowing slowly while they are being built.</desc>
  <style>{FONTS}
    .pop{{opacity:0;animation:pop .6s cubic-bezier(.3,1.5,.5,1) forwards}}
    @keyframes pop{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:translateY(0)}}}}
    .fade{{opacity:0;animation:fade .8s ease forwards}}
    @keyframes fade{{to{{opacity:1}}}}
    .flow{{animation:flow 1s linear infinite}}
    @keyframes flow{{to{{stroke-dashoffset:-16}}}}
    .blink{{animation:blink 1.2s steps(1) infinite}}
    @keyframes blink{{50%{{opacity:.2}}}}
    .dot{{animation:dot 1.4s ease-in-out infinite}}
    @keyframes dot{{0%,100%{{opacity:1}}50%{{opacity:.2}}}}
    .spin{{transform-origin:300px 212px;animation:spin 10s linear infinite}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
    .ping{{transform-box:fill-box;transform-origin:center;animation:ping 2.4s cubic-bezier(0,0,.2,1) infinite}}
    @keyframes ping{{0%{{transform:scale(.6);opacity:.9}}100%{{transform:scale(2.4);opacity:0}}}}
    .hz{{animation:hz 2s linear infinite}}
    @keyframes hz{{to{{transform:translateX(24px)}}}}
  </style>
  <defs>
    {EDGE}
    <pattern id="haz" width="24" height="24" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="12" height="24" fill="{YE}" fill-opacity=".035"/></pattern>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#9FB4D9" fill-opacity=".07"/></pattern>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <linearGradient id="cross" x1="370" x2="440" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{CY}"/><stop offset="1" stop-color="{YE}"/></linearGradient>
    <clipPath id="c"><rect width="{W}" height="{H}" rx="22"/></clipPath>
    <clipPath id="bz"><rect x="410" y="118" width="570" height="236" rx="16"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <rect width="{W}" height="{H}" fill="url(#dots)"/>

    <text x="40" y="48" class="mono" font-size="13" fill="#4F5D7A">// system.architecture.svg</text>
    <text x="40" y="80" class="sans" font-size="24" font-weight="700" fill="#E6EDF7">How I'll ship <tspan fill="{CY}">full-stack</tspan> apps</text>

    <!-- zones -->
    <rect x="20" y="118" width="380" height="236" rx="16" fill="{GR}" fill-opacity=".035" stroke="{GR}" stroke-opacity=".35"/>
    <g clip-path="url(#bz)"><g class="hz"><rect x="386" y="118" width="620" height="236" fill="url(#haz)"/></g></g>
    <rect x="410" y="118" width="570" height="236" rx="16" fill="none" stroke="{YE}" stroke-opacity=".45" stroke-dasharray="7 6" class="flow"/>
    <g class="mono" font-size="11.5" letter-spacing="1.5">
      <circle cx="40" cy="145" r="4.5" fill="{GR}" class="dot"/>
      <text x="52" y="149" fill="{GR}">FRONTEND · ONLINE</text>
      <circle cx="430" cy="145" r="4.5" fill="{YE}" class="blink"/>
      <text x="442" y="149" fill="{YE}">BACKEND · UNDER CONSTRUCTION</text>
      <text x="962" y="149" fill="#4F5D7A" text-anchor="end">ETA: one commit at a time</text>
    </g>

    <!-- wires -->
    <line x1="180" y1="{Y}" x2="230" y2="{Y}" stroke="{CY}" stroke-width="2"/>
    <line x1="370" y1="{Y}" x2="440" y2="{Y}" stroke="url(#cross)" stroke-width="2" stroke-dasharray="6 4" class="flow"/>
    <line x1="580" y1="{Y}" x2="630" y2="{Y}" stroke="{YE}" stroke-opacity=".5" stroke-width="2" stroke-dasharray="6 4" class="flow"/>
    <line x1="770" y1="{Y}" x2="820" y2="{Y}" stroke="{YE}" stroke-opacity=".5" stroke-width="2" stroke-dasharray="6 4" class="flow"/>

    <!-- cards -->
    {card(nodes[0], True, .2)}{card(nodes[1], True, .4)}{card(nodes[2], False, .6)}{card(nodes[3], False, .8)}{card(nodes[4], False, 1.0)}

    <!-- icons + labels -->
    <g class="fade" style="animation-delay:.4s">
      <rect x="80" y="192" width="60" height="42" rx="6" fill="none" stroke="{CY}" stroke-width="1.8"/>
      <line x1="80" y1="203" x2="140" y2="203" stroke="{CY}" stroke-width="1.5"/>
      <circle cx="87" cy="197.5" r="1.8" fill="#FF5F57"/><circle cx="93" cy="197.5" r="1.8" fill="#FEBC2E"/><circle cx="99" cy="197.5" r="1.8" fill="#28C840"/>
      <path d="M100 215l6 12 2-5 5-2z" fill="#E6EDF7"/>
      <text x="110" y="268" text-anchor="middle" class="sans" font-size="15" font-weight="700" fill="#E6EDF7">Browser</text>
      <text x="110" y="287" text-anchor="middle" class="mono" font-size="11" fill="#6B7A99">the user</text>
    </g>
    <g class="fade" style="animation-delay:.6s">
      <g class="spin" fill="none" stroke="{CY}" stroke-width="1.8">
        <ellipse cx="300" cy="212" rx="30" ry="11"/><ellipse cx="300" cy="212" rx="30" ry="11" transform="rotate(60 300 212)"/><ellipse cx="300" cy="212" rx="30" ry="11" transform="rotate(120 300 212)"/>
      </g>
      <circle cx="300" cy="212" r="4.5" fill="{CY}"/>
      <text x="300" y="268" text-anchor="middle" class="sans" font-size="15" font-weight="700" fill="#E6EDF7">React UI</text>
      <text x="300" y="287" text-anchor="middle" class="mono" font-size="11" fill="{GR}">✓ shipping</text>
    </g>
    <g class="fade" style="animation-delay:.8s">
      <text x="510" y="224" text-anchor="middle" class="mono" font-size="30" font-weight="700" fill="{YE}" fill-opacity=".85">{{ }}</text>
      <text x="510" y="268" text-anchor="middle" class="sans" font-size="15" font-weight="700" fill="#AEB9CC">REST API</text>
      <text x="510" y="287" text-anchor="middle" class="mono" font-size="11" fill="#6B7A99">DRF · JSON</text>
    </g>
    <g class="fade" style="animation-delay:1s">
      <rect x="680" y="192" width="40" height="40" rx="9" fill="{GR}" fill-opacity=".14" stroke="{GR}" stroke-opacity=".6"/>
      <text x="700" y="218" text-anchor="middle" class="mono" font-size="17" font-weight="700" fill="{GR}">dj</text>
      <text x="700" y="268" text-anchor="middle" class="sans" font-size="15" font-weight="700" fill="#AEB9CC">Django</text>
      <text x="700" y="287" text-anchor="middle" class="mono" font-size="11" fill="#6B7A99">models · views</text>
    </g>
    <g class="fade" style="animation-delay:1.2s" fill="none" stroke="#7FA7D6" stroke-width="1.8">
      <ellipse cx="890" cy="196" rx="22" ry="7"/>
      <path d="M868 196v28c0 4 10 7 22 7s22-3 22-7v-28"/>
      <path d="M868 210c0 4 10 7 22 7s22-3 22-7" stroke-opacity=".6"/>
      <text x="890" y="268" text-anchor="middle" class="sans" font-size="15" font-weight="700" fill="#AEB9CC" stroke="none">PostgreSQL</text>
      <text x="890" y="287" text-anchor="middle" class="mono" font-size="11" fill="#6B7A99" stroke="none">data layer</text>
    </g>

    <!-- build meters inside backend cards -->
    <g class="fade mono" style="animation-delay:1.4s" font-size="9.5" fill="#4F5D7A">
      <rect x="455" y="296" width="110" height="3" rx="1.5" fill="#1A2438" transform="translate(0 0)"/>
      <rect x="455" y="296" width="0" height="3" rx="1.5" fill="{YE}"><animate attributeName="width" values="0;22" dur="1.5s" begin="1.6s" fill="freeze"/></rect>
      <rect x="645" y="296" width="110" height="3" rx="1.5" fill="#1A2438"/>
      <rect x="645" y="296" width="0" height="3" rx="1.5" fill="{GR}"><animate attributeName="width" values="0;17" dur="1.5s" begin="1.8s" fill="freeze"/></rect>
      <rect x="835" y="296" width="110" height="3" rx="1.5" fill="#1A2438"/>
      <rect x="835" y="296" width="0" height="3" rx="1.5" fill="#7FA7D6"><animate attributeName="width" values="0;6" dur="1.5s" begin="2s" fill="freeze"/></rect>
    </g>
    <g transform="translate(0 10)" class="fade mono" style="animation-delay:1.4s" font-size="9.5" fill="#4F5D7A" text-anchor="middle">
      <text x="510" y="304">building · 20%</text><text x="700" y="304">building · 15%</text><text x="890" y="304">queued · 5%</text>
    </g>

    <!-- packets: frontend (fast, solid) -->
    <circle r="4.5" fill="{CY}" filter="url(#glow)"><animateMotion dur="1.1s" repeatCount="indefinite" path="M180 {Y - 6}H230"/></circle>
    <circle r="4.5" fill="{GR}" filter="url(#glow)"><animateMotion dur="1.1s" begin=".55s" repeatCount="indefinite" path="M230 {Y + 6}H180"/></circle>
    <!-- request crossing into backend -->
    <circle r="4.5" fill="{CY}" filter="url(#glow)" opacity="0">
      <animateMotion dur="3s" repeatCount="indefinite" path="M370 {Y}H440" keyPoints="0;1;1" keyTimes="0;.4;1" calcMode="linear"/>
      <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.4;.42;1" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="440" cy="{Y}" r="8" fill="none" stroke="{YE}" stroke-width="2" class="ping"/>
    <text x="405" y="{Y - 14}" text-anchor="middle" class="mono" font-size="10" fill="#6B7A99">GET /api</text>
    <text x="405" y="{Y + 24}" text-anchor="middle" class="mono blink" font-size="10" fill="{YE}">202 · soon</text>
    <!-- backend (slow, dim) -->
    <circle r="3.5" fill="{YE}" opacity=".7"><animateMotion dur="3.2s" repeatCount="indefinite" path="M580 {Y}H630"/></circle>
    <circle r="3.5" fill="{YE}" opacity=".7"><animateMotion dur="4.2s" begin="1s" repeatCount="indefinite" path="M770 {Y}H820"/></circle>

    <!-- legend -->
    <g class="mono" font-size="11.5" fill="#6B7A99">
      <line x1="40" y1="389" x2="64" y2="389" stroke="{CY}" stroke-width="2"/><text x="72" y="393">live data flow</text>
      <line x1="200" y1="389" x2="224" y2="389" stroke="{YE}" stroke-width="2" stroke-dasharray="5 3"/><text x="232" y="393">being wired up</text>
      <rect x="362" y="381" width="16" height="16" rx="3" fill="url(#haz)" stroke="{YE}" stroke-opacity=".5"/><text x="386" y="393">construction zone</text>
      <text x="960" y="393" text-anchor="end" fill="#3E4C68">frontend today · backend tomorrow · full-stack soon</text>
    </g>
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="21.5" fill="none" stroke="url(#edge)"/>
</svg>
"""
    write("arch.svg", svg)


hero()
marquee()
headers()
stats()
arch()
print("generated")
