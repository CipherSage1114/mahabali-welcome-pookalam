# Mahabali's Welcome — Code-a-Pookalam

A deterministic, procedural Pookalam created with Python and Pillow.

## Run

Requires Python 3.9+.

```bash
python -m pip install -r requirements.txt
python pookalam.py
```

The final competition render is created at:

```text
output/pookalam.png
```

It is **1024 × 1024**, square (1:1), and contains no text, name,
handle, watermark, signature, or logo.

## Design concept

**Mahabali's Welcome** is built as ten major floral layers, echoing the
ten-day Onam festival. The design moves from an outer radiance toward a
shared centre:

1. **White thumba-inspired petals** — purity and a sincere welcome.
2. **Red chethi-inspired petals** — vitality and auspicious energy.
3. **Orange/gold marigold** — celebration and warmth.
4. **Green leaf garland** — Kerala's living landscape and harvest.
5. **Gold grain beads** — abundance and gratitude for the harvest.
6. **White jasmine-inspired petals** — hospitality and gentleness.
7. **Saffron micro-rosettes** — joy and fullness.
8. **Geometric chukki ring** — many individual pieces forming one whole.
9. **Lotus** — renewal and harmony.
10. **Central seed** — a shared welcome at the heart of the festival.

The intention is that the viewer's eye travels inward: from the land and
harvest, through flowers and community, to a calm shared centre.

### Cultural note

Flower symbolism varies by family, region and tradition. The meanings above
are **artistic interpretations used for this competition concept**, not claims
that every flower has one universally fixed traditional meaning.

## Technical craft

The image is generated entirely from source code. Petals, leaves, rosettes,
beads and geometric marks are created from mathematical radial coordinates
and rotational symmetry. No photograph, external artwork, AI-generated image,
or downloaded visual asset is used.

The program renders at 2048 × 2048 and downsamples with Lanczos resampling
to produce the final 1024 × 1024 submission render.

## Reproducibility

There is no randomness and no external asset dependency. Running the script
again produces the same design.

## License

MIT License. See `LICENSE`.
