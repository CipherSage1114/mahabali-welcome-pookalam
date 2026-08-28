from PIL import Image, ImageDraw
import math
import os

# MAHABALI'S WELCOME — Code-a-Pookalam
# Purely procedural Python/Pillow render.
# Run: python pookalam.py
# Output: output/pookalam.png

SIZE = 2048
C = SIZE // 2
TAU = math.tau

# Palette inspired by Kerala flowers, foliage and the warm gold of a harvest festival.
BG = "#100B12"
BG2 = "#21101A"
MAROON = "#58152C"
RED = "#A92547"
CHESTNUT = "#7E2038"
PINK = "#D95678"
ORANGE = "#F07820"
MARIGOLD = "#F5A51B"
GOLD = "#FFD04A"
CREAM = "#FFF0B5"
WHITE = "#FFF9E5"
GREEN = "#3D874E"
DEEP_GREEN = "#175238"
TEAL = "#2C8171"

img = Image.new("RGB", (SIZE, SIZE), BG)
d = ImageDraw.Draw(img)

def polar(r, a):
    return C + math.cos(a)*r, C + math.sin(a)*r

def circle(r, fill, outline=None, width=1, xy=None):
    x, y = (C, C) if xy is None else xy
    d.ellipse((x-r, y-r, x+r, y+r), fill=fill, outline=outline, width=width)

def ring(r, width, fill):
    d.ellipse((C-r, C-r, C+r, C+r), outline=fill, width=width)

def petal(r, length, width, angle, fill, outline=None, stroke=3, lean=0.0):
    # Smooth sampled petal profile; radial geometry keeps every ring exact.
    pts = []
    for i in range(29):
        t = i / 28
        x = length*t + lean*length*t*t
        y = -width * (math.sin(math.pi*t)**0.74) * (1 - .08*t)
        pts.append((C+(r+x)*math.cos(angle)-y*math.sin(angle),
                    C+(r+x)*math.sin(angle)+y*math.cos(angle)))
    for i in range(28, -1, -1):
        t = i / 28
        x = length*t + lean*length*t*t
        y = width * (math.sin(math.pi*t)**0.74) * (1 - .08*t)
        pts.append((C+(r+x)*math.cos(angle)-y*math.sin(angle),
                    C+(r+x)*math.sin(angle)+y*math.cos(angle)))
    d.polygon(pts, fill=fill)
    if outline:
        d.line(pts + [pts[0]], fill=outline, width=stroke, joint="curve")

def leaf(r, length, width, angle, fill):
    petal(r, length, width, angle, fill, DEEP_GREEN, 3, -0.12)

def rosette(r, count, radius, fill, inner=None):
    for i in range(count):
        a = i*TAU/count
        x, y = polar(radius, a)
        circle(r, fill, xy=(x,y))
    if inner:
        circle(r*.58, inner)

# ------------------------------------------------------------
# BACKGROUND
# ------------------------------------------------------------
for r in range(1000, 0, -8):
    t = 1 - r/1000
    a = (16,11,18)
    b = (33,16,26)
    col = tuple(int(a[k]*(1-t)+b[k]*t) for k in range(3))
    d.ellipse((C-r,C-r,C+r,C+r), fill=col)

# Quiet concentric frame: the flower remains the hero.
ring(980, 12, MAROON)
ring(958, 5, GOLD)
ring(936, 3, CREAM)

# ------------------------------------------------------------
# THE TEN RINGS OF ONAM
#
# The ten main layers are a visual reference to the ten-day
# Onam festival. Their flower choices tell one continuous story:
# welcome -> purity -> auspiciousness -> joy -> nature -> abundance
# -> celebration -> community -> renewal -> radiant welcome.
# ------------------------------------------------------------

# 1. THUMBA-INSPIRED WHITE RING — purity / a clear welcome
for i in range(36):
    a = i*TAU/36
    petal(700, 175, 43, a, WHITE, CREAM, 3, -0.02)

# 2. CHECHI / CHEthi-INSPIRED RED PETALS — vitality / auspicious energy
for i in range(36):
    a = (i+.5)*TAU/36
    petal(610, 145, 40, a, RED, MAROON, 3, -0.04)

# 3. MARIGOLD GOLD — celebration / warmth
for i in range(30):
    a = i*TAU/30
    petal(510, 150, 48, a, ORANGE if i%2==0 else MARIGOLD, MAROON, 3, 0.02)

# 4. GREEN LEAF GARLAND — land, harvest and living nature
for i in range(30):
    a = (i+.5)*TAU/30
    leaf(435, 120, 34, a, GREEN if i%2==0 else TEAL)

# 5. GOLD GRAIN BEADS — abundance / the harvest
for i in range(60):
    a = i*TAU/60
    r = 380 + 7*math.sin(i*1.9)
    x,y = polar(r,a)
    circle(8 if i%3 else 11, GOLD, xy=(x,y))

# 6. JASMINE-INSPIRED WHITE RING — hospitality / softness
for i in range(24):
    a = i*TAU/24
    petal(320, 145, 43, a, WHITE, GOLD, 3, -0.03)

# Tiny red separators make the ring read as flowers, not a generic mandala.
for i in range(24):
    x,y = polar(300,(i+.5)*TAU/24)
    circle(7, RED, xy=(x,y))

# 7. CHRYSANTHEMUM-LIKE SAFFRON ROSETTES — joy / fullness
for i in range(20):
    a = i*TAU/20
    x,y = polar(245,a)
    # 5-petal micro-flower at each station
    for j in range(5):
        q = a + j*TAU/5
        xx = x + math.cos(q)*25
        yy = y + math.sin(q)*25
        circle(14, MARIGOLD, xy=(xx,yy))
    circle(10, CREAM, xy=(x,y))

# 8. GEOMETRIC CHUKKI RING — order / community / every part fitting together
for i in range(32):
    a = i*TAU/32
    x,y = polar(205,a)
    pts=[]
    for off,rr in [(0,25),(math.pi/2,13),(math.pi,25),(3*math.pi/2,13)]:
        q=a+off
        pts.append((x+math.cos(q)*rr,y+math.sin(q)*rr))
    d.polygon(pts, fill=PINK if i%2==0 else CHESTNUT)
    d.line(pts+[pts[0]], fill=CREAM, width=2, joint="curve")

# 9. LOTUS PETALS — renewal / harmony / the heart of the welcome
for i in range(12):
    a = i*TAU/12
    petal(110, 112, 34, a, PINK if i%2==0 else RED, MAROON, 3, -0.10)

# Inner golden lotus
for i in range(8):
    a = i*TAU/8 + math.pi/8
    petal(55, 86, 27, a, ORANGE if i%2==0 else GOLD, MAROON, 2, -0.12)

# 10. CENTRAL "WELCOME" SEED — a warm shared centre, not a logo or text
circle(48, MAROON, CREAM, 4)
circle(35, GOLD)
circle(22, RED)
circle(11, CREAM)

# ------------------------------------------------------------
# SUBTLE "MAHABALI WELCOME" MOTIF
# ------------------------------------------------------------
# Eight small white dots form an open circular gesture around the heart.
for i in range(8):
    a = i*TAU/8
    x,y = polar(75,a)
    circle(5, WHITE, xy=(x,y))

# Four small leaf-pairs at the cardinal points:
# they make the centre feel rooted in Kerala's greenery.
# Four tiny directional leaf pairs, placed around the lotus.
for a in (0, math.pi/2, math.pi, 3*math.pi/2):
    for side in (-1, 1):
        q = a + side*0.20
        x,y = polar(145,q)
        # small local leaf polygon
        ux,uy = math.cos(q), math.sin(q)
        vx,vy = -uy,ux
        L,W = 34,10
        pts = [
            (x, y),
            (x+ux*L*.45+vx*W, y+uy*L*.45+vy*W),
            (x+ux*L, y+uy*L),
            (x+ux*L*.45-vx*W, y+uy*L*.45-vy*W)
        ]
        d.polygon(pts, fill=DEEP_GREEN)
        d.line(pts+[pts[0]], fill=GREEN, width=2)

# ------------------------------------------------------------
# FINAL MICRO-FLOWER STITCHING
# ------------------------------------------------------------
# Sparse ivory dots at ring boundaries give the composition a hand-made
# floral texture without destroying the large-scale rhythm.
for i in range(72):
    a = i*TAU/72
    r = 565 + 10*math.sin(i*1.31)
    x,y = polar(r,a)
    circle(4, CREAM, xy=(x,y))

for i in range(48):
    a = (i+.5)*TAU/48
    x,y = polar(745,a)
    circle(4, GOLD, xy=(x,y))

# Clean final edge.
ring(987, 5, CREAM)

# The competition wants a square render. Render large, then downsample.
os.makedirs("output", exist_ok=True)
img.resize((1024,1024), Image.Resampling.LANCZOS).save(
    "output/pookalam.png", optimize=True
)
print("Created output/pookalam.png — 1024 x 1024")
