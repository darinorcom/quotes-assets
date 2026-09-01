#!/usr/bin/env python3
"""Typeset a quote card for the X quotes account into card PNGs.

Usage:
    uv run --with pillow python3 make_card.py --bg background.png \
        --text "The quote line." --out card_001.png

Template v1: 1080x1080, white Inter (semibold-ish), soft shadow,
small handle at bottom-left. One look, reused forever.
"""
import argparse
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONT = "/home/frn/.local/share/fonts/syncdefend/Inter-VF.ttf"
SIZE = 1080
MARGIN = 110
HANDLE = "@buildwithscars"  # confirmed account name (2026-08-29)


def wrap(text, font, max_width, draw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make(bg_path, text, out_path, handle=HANDLE):
    img = Image.open(bg_path).convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)

    # slight vertical darkening so white type holds contrast anywhere
    overlay = Image.new("L", (1, SIZE))
    for y in range(SIZE):
        # darken edges of the midband slightly, keep overall rich color
        overlay.putpixel((0, y), 28)
    overlay = overlay.resize((SIZE, SIZE))
    black = Image.new("RGB", (SIZE, SIZE), (10, 8, 20))
    img = Image.composite(black, img, overlay)

    draw = ImageDraw.Draw(img)
    # Heavier weight variant for longer quotes -> slightly smaller size
    variation = "SemiBold"
    body_size = 64
    while True:
        font = ImageFont.truetype(FONT, body_size)
        font.set_variation_by_name(variation)
        lines = wrap(text, font, SIZE - 2 * MARGIN, draw)
        if len(lines) <= 7:
            break
        body_size -= 3
        if body_size < 44:
            break

    line_h = int(body_size * 1.28)
    total_h = line_h * len(lines)
    y = (SIZE - total_h) // 2 - 30

    # soft shadow pass
    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    for i, ln in enumerate(lines):
        w = sdraw.textlength(ln, font=font)
        sdraw.text(((SIZE - w) / 2 + 4, y + i * line_h + 5), ln,
                   font=font, fill=(0, 0, 0, 170))
    shadow = shadow.filter(ImageFilter.GaussianBlur(7))
    img = Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB")

    draw = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        w = draw.textlength(ln, font=font)
        draw.text(((SIZE - w) / 2, y + i * line_h), ln, font=font,
                  fill=(255, 255, 255))

    hfont = ImageFont.truetype(FONT, 26)
    hfont.set_variation_by_name("Medium")
    draw.text((MARGIN, SIZE - 74), handle, font=hfont, fill=(255, 255, 255, 220))

    img.save(out_path, quality=95)
    print(f"saved {out_path} body_size={body_size} lines={len(lines)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--bg", required=True)
    ap.add_argument("--text", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--handle", default=HANDLE)
    a = ap.parse_args()
    make(a.bg, a.text, a.out, a.handle)