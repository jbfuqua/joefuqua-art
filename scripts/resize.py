#!/usr/bin/env python3
"""
Batch resize images for joefuqua.art
Usage: python3 scripts/resize.py /path/to/source/folder [collection]

collection = watercolor | digital | multimedia | ai
Output goes to public/images/[collection]/
"""

import sys
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Install Pillow first: pip install Pillow")
    sys.exit(1)

def slugify(name):
    return name.lower().replace(' ', '-').replace('_', '-')

def resize_images(source_dir, collection='watercolor', max_size=1200, quality=82):
    source = Path(source_dir)
    output = Path(__file__).parent.parent / 'public' / 'images' / collection
    output.mkdir(parents=True, exist_ok=True)

    extensions = {'.jpg', '.jpeg', '.png', '.heic', '.PNG', '.JPG', '.JPEG'}
    files = [f for f in source.iterdir() if f.suffix in extensions]

    if not files:
        print(f"No image files found in {source_dir}")
        return

    print(f"Processing {len(files)} images → public/images/{collection}/\n")

    for f in sorted(files):
        try:
            img = Image.open(f).convert('RGB')
            w, h = img.size
            if max(w, h) > max_size:
                ratio = max_size / max(w, h)
                img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)

            slug = slugify(f.stem)
            out_path = output / f"{slug}.jpg"
            img.save(out_path, 'JPEG', quality=quality, optimize=True)
            print(f"  ✓ {f.name} → {slug}.jpg {img.size}")
        except Exception as e:
            print(f"  ✗ {f.name}: {e}")

    print(f"\nDone. Add entries to src/data/catalog.ts for each new piece.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    source = sys.argv[1]
    collection = sys.argv[2] if len(sys.argv) > 2 else 'watercolor'
    resize_images(source, collection)
