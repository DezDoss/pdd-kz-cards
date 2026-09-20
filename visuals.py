# -*- coding: utf-8 -*-
"""Карточки с графикой: дорожные знаки и схемы перекрёстков.

Вся графика — инлайновый SVG: работает офлайн в PWA и рендерится в Anki.
Знаки нарисованы в своих настоящих цветах (белое поле остаётся белым и в тёмной теме —
это изображение физического объекта). Схемы перекрёстков имеют собственную светлую
подложку, поэтому одинаково читаются на любом фоне.
"""

RED = "#d32011"; BLUE = "#0d4a9e"; YELLOW = "#f5c400"; WHITE = "#ffffff"; BLACK = "#1a1a1a"

# ---------------------------------------------------------------- оболочки знаков
def _svg(inner, box="0 0 100 100", w=124):
    return ('<svg viewBox="%s" width="%d" xmlns="http://www.w3.org/2000/svg" '
            'style="display:block;margin:2px auto 12px;max-width:100%%;height:auto" '
            'role="img">%s</svg>') % (box, w, inner)

def warn(sym):      # предупреждающий: белый треугольник, красная кайма
    return _svg('<path d="M50 9 L95 87 H5 Z" fill="%s" stroke="%s" stroke-width="8" '
                'stroke-linejoin="round"/>%s' % (WHITE, RED, sym))

def ban(sym, field=WHITE):   # запрещающий: круг с красной каймой
    return _svg('<circle cx="50" cy="50" r="43" fill="%s" stroke="%s" stroke-width="10"/>%s'
                % (field, RED, sym))

def must(sym):      # предписывающий: синий круг
    return _svg('<circle cx="50" cy="50" r="46" fill="%s"/>%s' % (BLUE, sym))

def info(sym):      # особых предписаний / информационный: синий квадрат
    return _svg('<rect x="4" y="4" width="92" height="92" rx="5" fill="%s"/>%s' % (BLUE, sym))

# ---------------------------------------------------------------- символы
CAR_SIDE = ('<path d="M18 62 L27 45 H56 L70 62 V70 H18 Z" fill="%s"/>'
            '<circle cx="31" cy="71" r="6" fill="%s"/><circle cx="61" cy="71" r="6" fill="%s"/>')
def car_side(color, x=0, y=0, s=1.0):
    return '<g transform="translate(%g,%g) scale(%g)">%s</g>' % (x, y, s, CAR_SIDE % (color, color, color))

def car_front(color):
    return ('<path d="M28 68 V50 q0-5 4-9 l4-9 h28 l4 9 q4 4 4 9 v18 z" fill="%s"/>'
            '<path d="M37 41 h26 l3 8 h-32 z" fill="%s" opacity=".55"/>'
            '<rect x="24" y="60" width="8" height="7" rx="2" fill="%s"/>'
            '<rect x="68" y="60" width="8" height="7" rx="2" fill="%s"/>') % (color, BLUE, color, color)

def person(cx, cy, s, color):
    return ('<g transform="translate(%g,%g) scale(%g)" fill="%s">'
            '<circle cx="0" cy="-15" r="4.6"/>'
            '<path d="M-4.5 -10 h9 l2 13 h-4 l-1 -6 -1 6 h-4 l-1 -6 -1 6 h-4 z"/>'
            '<path d="M-3 2 l-3 12 h3.4 l2.6 -9 2.6 9 h3.4 l-3 -12 z"/>'
            '</g>') % (cx, cy, s, color)

ZEBRA = ''.join('<rect x="%d" y="70" width="5" height="12" fill="%s"/>' % (x, BLACK)
                for x in (24, 34, 44, 54, 64))

SIGNS = {}

SIGNS["2.1"] = _svg('<path d="M50 5 L95 50 L50 95 L5 50 Z" fill="%s" stroke="#c8ccd2" stroke-width="2" '
                    'stroke-linejoin="round"/><path d="M50 6 L94 50 L50 94 L6 50 Z" fill="none" '
                    'stroke="%s" stroke-width="1"/>'
                    '<path d="M50 20 L80 50 L50 80 L20 50 Z" fill="%s"/>' % (WHITE, WHITE, YELLOW))
SIGNS["2.4"] = _svg('<path d="M50 91 L5 13 H95 Z" fill="%s" stroke="%s" stroke-width="9" '
                    'stroke-linejoin="round"/>' % (WHITE, RED))
SIGNS["2.5"] = _svg('<path d="M31 5 H69 L95 31 V69 L69 95 H31 L5 69 V31 Z" fill="%s"/>'
                    '<text x="50" y="59" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" '
                    'font-weight="900" font-size="25" fill="%s">STOP</text>' % (RED, WHITE))
SIGNS["3.1"] = _svg('<circle cx="50" cy="50" r="46" fill="%s"/>'
                    '<rect x="20" y="43" width="60" height="14" rx="2" fill="%s"/>' % (RED, WHITE))
SIGNS["3.2"] = ban('')
SIGNS["3.19"] = ban('<path d="M32 72 V46 a18 18 0 0 1 36 0 V60" fill="none" stroke="%s" '
                    'stroke-width="8"/><path d="M58 58 L68 74 L78 58 Z" fill="%s"/>'
                    '<path d="M20 20 L80 80" stroke="%s" stroke-width="9" stroke-linecap="round"/>'
                    % (BLACK, BLACK, RED))
SIGNS["3.20"] = ban(car_side(BLACK, 6, -4, .62) + car_side(RED, 36, 10, .62))
SIGNS["3.24"] = ban('<text x="50" y="66" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" '
                    'font-weight="700" font-size="46" fill="%s">60</text>' % BLACK)
SIGNS["3.27"] = ban('<path d="M26 26 L74 74 M74 26 L26 74" stroke="%s" stroke-width="9" '
                    'stroke-linecap="round"/>' % RED, field=BLUE)
SIGNS["3.28"] = ban('<path d="M28 72 L72 28" stroke="%s" stroke-width="9" '
                    'stroke-linecap="round"/>' % RED, field=BLUE)
SIGNS["4.1.1"] = must('<path d="M50 24 L68 48 H58 V76 H42 V48 H32 Z" fill="%s"/>' % WHITE)
SIGNS["4.3"] = must('<g fill="none" stroke="%s" stroke-width="7">'
                    '<path d="M38 66 a17 17 0 0 1 8 -28"/><path d="M66 52 a17 17 0 0 1 -18 16"/>'
                    '<path d="M50 30 a17 17 0 0 1 16 12"/></g>'
                    '<path d="M40 30 L52 34 L43 43 Z" fill="%s"/>'
                    '<path d="M70 62 L60 70 L58 58 Z" fill="%s"/>'
                    '<path d="M35 74 L34 62 L46 68 Z" fill="%s"/>' % (WHITE, WHITE, WHITE, WHITE))
SIGNS["5.3"] = info(car_front(WHITE))
SIGNS["5.5"] = info('<rect x="14" y="44" width="72" height="12" fill="%s"/>'
                    '<path d="M66 30 L92 50 L66 70 Z" fill="%s"/>' % (WHITE, WHITE))
SIGNS["5.19"] = info('<path d="M50 14 L86 50 L50 86 L14 50 Z" fill="%s"/>' % WHITE
                     + "".join('<rect x="%d" y="62" width="4" height="10" fill="%s"/>' % (x, BLACK)
                               for x in (34, 41, 48, 55, 62))
                     + person(50, 50, 1.25, BLACK))
SIGNS["6.4"] = info('<text x="50" y="72" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" '
                    'font-weight="700" font-size="60" fill="%s">P</text>' % WHITE)
SIGNS["1.22"] = warn(''.join('<rect x="%d" y="66" width="4" height="11" fill="%s"/>' % (x, BLACK)
                             for x in (34, 41, 48, 55, 62)) + person(50, 56, 1.15, BLACK))
SIGNS["1.23"] = warn(person(42, 70, 1.05, BLACK) + person(58, 66, 1.25, BLACK))
SIGNS["1.1"] = warn('<rect x="20" y="47" width="9" height="26" fill="%s"/>' % BLACK
                    + '<rect x="29" y="56" width="52" height="8" rx="2" fill="%s"/>' % BLACK
                    + "".join('<rect x="%d" y="56" width="8" height="8" fill="%s"/>' % (x, RED)
                              for x in (36, 52, 68)))
SIGNS["1.2"] = warn('<rect x="30" y="52" width="34" height="18" rx="3" fill="%s"/>'
                    '<rect x="44" y="44" width="9" height="9" fill="%s"/>'
                    '<rect x="64" y="60" width="10" height="10" fill="%s"/>'
                    '<circle cx="39" cy="73" r="5" fill="%s"/><circle cx="57" cy="73" r="5" fill="%s"/>'
                    % (BLACK, BLACK, BLACK, BLACK, BLACK))

# ---------------------------------------------------------------- схемы перекрёстков
ROAD = "#8d959e"; DIRT = "#b4966e"; GROUND = "#e7eaee"
A_COL = "#1b5cb8"; B_COL = "#e09b12"; C_COL = "#2f8f5b"; TRAM_COL = "#7a4bbd"
INK = "#10141a"

def car(cx, cy, rot, label, color):
    """Машина 22x38. rot: 0 — едет вверх, 90 — вправо, 180 — вниз, 270 — влево."""
    return ('<g transform="translate(%g,%g) rotate(%g)">'
            '<rect x="-11" y="-19" width="22" height="38" rx="5" fill="%s"/></g>'
            '<text x="%g" y="%g" text-anchor="middle" font-family="Arial,sans-serif" '
            'font-size="15" font-weight="700" fill="#fff">%s</text>') % (cx, cy, rot, color, cx, cy + 9, label)

def tram(cx, cy, rot, label="Т"):
    return ('<g transform="translate(%g,%g) rotate(%g)">'
            '<rect x="-13" y="-25" width="26" height="50" rx="4" fill="%s"/></g>'
            '<text x="%g" y="%g" text-anchor="middle" font-family="Arial,sans-serif" '
            'font-size="15" font-weight="700" fill="#fff">%s</text>') % (cx, cy, rot, TRAM_COL, cx, cy + 10, label)

def arrow(d):
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="3.5" stroke-dasharray="8 6" '
            'stroke-linecap="round" marker-end="url(#ah)"/>') % (d, INK)

def sign_yield(cx, cy):
    return ('<g transform="translate(%g,%g)"><path d="M0 12 L-12 -9 H12 Z" fill="#fff" '
            'stroke="%s" stroke-width="4" stroke-linejoin="round"/></g>') % (cx, cy, RED)

def sign_main(cx, cy):
    return ('<g transform="translate(%g,%g)"><path d="M0 -13 L13 0 L0 13 L-13 0 Z" fill="#fff"/>'
            '<path d="M0 -8 L8 0 L0 8 L-8 0 Z" fill="%s"/></g>') % (cx, cy, YELLOW)

def light(cx, cy, top="red", arrow_right=False):
    """Светофор: основной сигнал + при необходимости зелёная стрелка направо."""
    on = {"red": (RED, "#3b3f44", "#3b3f44"), "green": ("#3b3f44", "#3b3f44", "#2f8f5b")}[top]
    g = ('<g transform="translate(%g,%g)"><rect x="-9" y="-24" width="18" height="48" rx="4" fill="#23282e"/>'
         '<circle cx="0" cy="-14" r="6" fill="%s"/><circle cx="0" cy="0" r="6" fill="%s"/>'
         '<circle cx="0" cy="14" r="6" fill="%s"/>') % (cx, cy, on[0], on[1], on[2])
    if arrow_right:
        g += ('<rect x="9" y="6" width="17" height="17" rx="3" fill="#23282e"/>'
              '<path d="M14 14.5 h7 M18 11 l4 3.5 -4 3.5" stroke="#4fd48a" stroke-width="2.4" '
              'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    return g + '</g>'

def zebra(x, y, horiz=True, n=5, span=34):
    out = []
    for i in range(n):
        if horiz: out.append('<rect x="%g" y="%g" width="5" height="%g" fill="#fff" opacity=".95"/>'
                             % (x + i * 7, y, span))
        else:     out.append('<rect x="%g" y="%g" width="%g" height="5" fill="#fff" opacity=".95"/>'
                             % (x, y + i * 7, span))
    return "".join(out)

def walker(cx, cy, color=INK):
    return person(cx, cy, 1.0, color)

def scene(inner, vfill=ROAD, hfill=ROAD, marks=True, w=236):
    """Перекрёсток 200x200. Вертикальная дорога x 66..134, горизонтальная y 66..134."""
    p = ['<rect width="200" height="200" rx="8" fill="%s"/>' % GROUND,
         '<rect x="0" y="66" width="200" height="68" fill="%s"/>' % hfill,
         '<rect x="66" y="0" width="68" height="200" fill="%s"/>' % vfill]
    if marks:
        dash = 'stroke="#fff" stroke-width="2.5" stroke-dasharray="10 9" opacity=".9"'
        if hfill == ROAD:
            p.append('<path d="M0 100 H60 M140 100 H200" %s/>' % dash)
        if vfill == ROAD:
            p.append('<path d="M100 0 V60 M100 140 V200" %s/>' % dash)
    defs = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
            'markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="%s"/></marker></defs>') % INK
    return ('<svg viewBox="0 0 200 200" width="%d" xmlns="http://www.w3.org/2000/svg" '
            'style="display:block;margin:4px auto 12px;max-width:100%%;height:auto" role="img">'
            '%s%s%s</svg>') % (w, defs, "".join(p), inner)

def legend(*items):
    return ('<div style="font-size:13.5px;line-height:1.8;opacity:.8">%s</div>'
            % "".join('<span style="display:inline-block;margin-right:14px;white-space:nowrap">'
                      '<i style="width:11px;height:11px;border-radius:3px;background:%s;'
                      'display:inline-block;vertical-align:-1px;margin-right:5px"></i>%s</span>'
                      % (c, t) for c, t in items))

# позиции по сторонам (правостороннее движение)
S = (117, 168, 0)     # снизу, едет вверх
N = (83, 32, 180)     # сверху, едет вниз
E = (168, 83, 270)    # справа, едет влево
W = (32, 117, 90)     # слева, едет вправо
