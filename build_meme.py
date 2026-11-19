"""Draw the gta6-meme-x-01 meme with PIL.

Scene: a Vice City sunset. A kid sits on a couch in 2013 holding a
GTA V case; thirteen years later the same kid, now 18, sits on the same
couch holding GTA VI. The make.fun ghost floats between them -- it
waited with him the whole time. The ghost is composited straight from
the press kit (mark-1024.png), never redrawn or recoloured.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
GHOST = "/home/hatch/workspace/makefun/gta6-meme-x-01-press/make-fun-press-kit/mark-1024.png"
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-01/meme.png"

BOLD = "/usr/share/fonts/truetype/noto/NotoSansDisplay-Black.ttf"
BOLD2 = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def fit_font(draw, text, path, max_w, start, floor=10):
    size = start
    while size > floor:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(path, floor)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def sunset(img, y0, y1):
    d = ImageDraw.Draw(img)
    top = (255, 154, 90)      # orange
    mid = (255, 107, 157)     # pink
    bot = (123, 47, 190)      # purple
    for y in range(y0, y1):
        t = (y - y0) / max(1, y1 - y0)
        c = lerp(top, mid, t * 2) if t < 0.5 else lerp(mid, bot, (t - 0.5) * 2)
        d.line([(0, y), (W, y)], fill=c)


def text_c(d, cx, y, s, f, fill, stroke=0, sw=0):
    d.text((cx, y), s, font=f, fill=fill, anchor="ma",
           stroke_width=sw, stroke_fill=stroke)


img = Image.new("RGB", (W, H), (20, 16, 46))
d = ImageDraw.Draw(img)

# ---- sunset sky behind the scene ----
sunset(img, 118, 800)

# sun
d.ellipse([90, 180, 290, 380], fill=(255, 226, 138))
d.ellipse([110, 200, 270, 360], fill=(255, 240, 180))

# stars
for (sx, sy, r) in [(700, 170, 3), (820, 230, 2), (620, 260, 2), (920, 160, 3),
                    (380, 150, 2), (480, 210, 2), (60, 420, 2), (980, 420, 2)]:
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 255, 255))

# ---- skyline silhouette ----
d.rectangle([0, 560, W, 800], fill=(43, 16, 84))
buildings = [(0, 470, 70, 560), (70, 420, 150, 560), (150, 490, 210, 560),
             (210, 440, 300, 560), (300, 500, 360, 560), (360, 430, 450, 560),
             (450, 490, 520, 560), (520, 450, 610, 560), (610, 500, 680, 560),
             (680, 420, 770, 560), (770, 480, 850, 560), (850, 440, 930, 560),
             (930, 490, 1024, 560)]
for x0, y0, x1, y1 in buildings:
    d.rectangle([x0, y0, x1, y1], fill=(43, 16, 84))
# lit windows
for (wx, wy) in [(90, 450), (120, 480), (240, 470), (400, 460), (560, 480),
                 (700, 450), (880, 470), (960, 510), (180, 520), (640, 520)]:
    d.rectangle([wx, wy, wx + 12, wy + 16], fill=(255, 210, 110))

# ---- palms at the edges ----
def palm(x, y, s, flip=False):
    for k in range(5):
        ang = math.radians(-70 + k * 35) * (1 if not flip else -1)
        ex = x + math.cos(ang) * 70 * s
        ey = y + math.sin(ang) * 45 * s
        d.line([(x, y), (ex, ey)], fill=(30, 10, 60), width=int(10 * s))
    d.line([(x, y), (x + (6 if not flip else -6), y + 150 * s)],
           fill=(30, 10, 60), width=int(12 * s))

palm(40, 470, 1.0)
palm(990, 470, 1.0, flip=True)

# ---- year labels ----
yf = font(BOLD, 78)
text_c(d, 256, 128, "2013", yf, (255, 255, 255), (20, 16, 46), 4)
text_c(d, 768, 128, "2026", yf, (255, 255, 255), (20, 16, 46), 4)

# ---- couch ----
d.rounded_rectangle([60, 660, 964, 800], radius=28, fill=(22, 105, 122))
d.rounded_rectangle([60, 620, 964, 700], radius=28, fill=(28, 130, 150))
d.rounded_rectangle([90, 640, 300, 700], radius=16, fill=(34, 150, 172))
d.rounded_rectangle([724, 640, 934, 700], radius=16, fill=(34, 150, 172))
d.rounded_rectangle([60, 690, 964, 720], radius=12, fill=(18, 88, 104))


def person(cx, scale, beard, cap_col=(214, 48, 49)):
    """A seated figure on the couch, facing the viewer, holding a pad."""
    s = scale
    # legs
    d.rounded_rectangle([cx - 62 * s, 740, cx + 62 * s, 800],
                        radius=int(18 * s), fill=(40, 44, 90))
    # body (same blue shirt, kid and adult)
    d.rounded_rectangle([cx - 58 * s, 640, cx + 58 * s, 760],
                        radius=int(22 * s), fill=(52, 120, 220))
    # arms
    d.rounded_rectangle([cx - 78 * s, 660, cx - 42 * s, 740],
                        radius=int(14 * s), fill=(52, 120, 220))
    d.rounded_rectangle([cx + 42 * s, 660, cx + 78 * s, 740],
                        radius=int(14 * s), fill=(52, 120, 220))
    # hands + controller
    d.ellipse([cx - 46 * s, 712, cx - 22 * s, 736], fill=(242, 200, 155))
    d.ellipse([cx + 22 * s, 712, cx + 46 * s, 736], fill=(242, 200, 155))
    d.rounded_rectangle([cx - 34 * s, 706, cx + 34 * s, 738],
                        radius=int(10 * s), fill=(30, 30, 40))
    # head
    d.ellipse([cx - 46 * s, 540, cx + 46 * s, 632], fill=(242, 200, 155))
    # eyes
    d.ellipse([cx - 26 * s, 578, cx - 12 * s, 592], fill=(20, 16, 30))
    d.ellipse([cx + 12 * s, 578, cx + 26 * s, 592], fill=(20, 16, 30))
    # smile
    d.arc([cx - 18 * s, 592, cx + 18 * s, 620], 20, 160,
          fill=(20, 16, 30), width=max(2, int(3 * s)))
    if beard:
        d.pieslice([cx - 46 * s, 590, cx + 46 * s, 660], 0, 180,
                   fill=(70, 45, 25))
        d.arc([cx - 18 * s, 592, cx + 18 * s, 620], 20, 160,
              fill=(242, 200, 155), width=max(2, int(3 * s)))
    # red cap
    d.pieslice([cx - 48 * s, 512, cx + 48 * s, 592], 180, 360, fill=cap_col)
    d.rectangle([cx - 48 * s, 556, cx + 48 * s, 566], fill=cap_col)
    d.rounded_rectangle([cx - 48 * s, 556, cx + 52 * s, 570],
                        radius=int(6 * s), fill=cap_col)


person(225, 0.85, beard=False)   # the kid, 2013
person(800, 1.15, beard=True)    # the same kid, grown up, 2026

# ---- game cases leaning on the couch ----
def case(x, y, label):
    d.rounded_rectangle([x, y, x + 96, y + 118], radius=8,
                        fill=(255, 255, 255), outline=(20, 16, 30), width=4)
    f = font(BOLD, 30)
    text_c(d, x + 48, y + 8, "GTA", f, (20, 16, 30))
    f2 = font(BOLD, 52)
    text_c(d, x + 48, y + 40, label, f2, (214, 48, 49))

case(330, 668, "V")
case(600, 668, "VI")

# ---- the make.fun ghost, worked into the scene ----
ghost = Image.open(GHOST).convert("RGBA")
gs = 250
ghost = ghost.resize((gs, gs), Image.LANCZOS)
img.paste(ghost, (512 - gs // 2, 330), ghost)
d = ImageDraw.Draw(img)
gf = font(BOLD2, 34)
text_c(d, 512, 585, "make.fun", gf, (255, 255, 255), (20, 16, 46), 4)

# ---- top band ----
d.rectangle([0, 0, W, 118], fill=(20, 16, 46))
tf = fit_font(d, "I WAS 5 WHEN GTA V CAME OUT", BOLD, 960, 58)
text_c(d, 512, 28, "I WAS 5 WHEN GTA V CAME OUT", tf, (255, 255, 255))

# ---- bottom band ----
d.rectangle([0, 800, W, H], fill=(20, 16, 46))
bf1 = fit_font(d, "I'M 18 NOW.", BOLD, 960, 74)
text_c(d, 512, 812, "I'M 18 NOW.", bf1, (255, 255, 255))
bf2 = fit_font(d, "GTA 6 IS FINALLY OUT.", BOLD, 960, 56)
text_c(d, 512, 886, "GTA 6 IS FINALLY OUT.", bf2, (255, 210, 63))
sf = font(BOLD2, 26)
text_c(d, 512, 962, "while I waited, my agent earned real money on make.fun",
       sf, (200, 200, 220))

img.save(OUT, "PNG")
print("saved", OUT, img.size)
