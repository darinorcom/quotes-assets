# quotes-assets

Public social media assets for **@buildwithscars** (X).

Structure:
- `cards/launch/` — launch batch, day 001-013 (1080x1080 quote cards)
- `cards/batch2/` — week-2 batch, day 014-018 + day019 drafts
- `brand/` — profile image (gold B monogram) and header banner (1500x500)
- `pipeline/` — card factory: make_card.py (PIL typesetter), strategy.md (locked
  brand spec), palettes/ (5 approved gold backgrounds), quotes + Buffer queue logs

Served via jsDelivr:
`https://cdn.jsdelivr.net/gh/darinorcom/quotes-assets@main/<path>`

## Card pipeline (restored 2026-09-01 from ~/marketing/backup)

1. Write quotes (original phrasings only, builder/lifestyle voice, <25 words)
2. Typeset: `python3 pipeline/make_card.py --bg pipeline/palettes/<palette>.png --text "..." --out cards/batchN/dayNNN.png`
   (requires Inter VF at ~/.local/share/fonts/syncdefend/Inter-VF.ttf)
3. Vision-check the card for garbled text before queueing
4. Commit + push (jsDelivr picks up @main), then queue via Buffer CLI with the
   jsDelivr URL as the image asset
5. Log the Buffer post id in pipeline/buffer_created.json
