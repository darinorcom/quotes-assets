# @buildwithscars — launch queue (9 cards, 1/day) — QUEUED IN BUFFER 2026-08-29 (rev 3: images served from jsDelivr (darinorcom/quotes-assets))

All 9 queued on Buffer channel buildwithscars (id 6a92a7f5ccaf649a673c3504),
each with its card image attached (hosted on uguu.se, URLs in image_urls.json).

| Day | Date | Time (CET) | Buffer post id | Card |
|---|---|---|---|---|
| 1 | 2026-08-30 | 08:40 | 6a92aaa0aad1969d9e0b890c | launch/day001.png |
| 2 | 2026-08-31 | 12:30 | 6a92aaa3aad1969d9e0b895d | launch/day002.png |
| 3 | 2026-09-01 | 17:10 | 6a92aaa773b542df4dd6f453 | launch/day003.png |
| 4 | 2026-09-02 | 08:40 | 6a92aaaa73b542df4dd6f491 | launch/day004.png |
| 5 | 2026-09-03 | 12:30 | 6a92aaad946f458537431bd0 | launch/day005.png |
| 6 | 2026-09-04 | 17:10 | 6a92aab1463a5d78ec67ad29 | launch/day006.png |
| 7 | 2026-09-05 | 08:40 | 6a92aab5946f458537431c68 | launch/day007.png |
| 8 | 2026-09-06 | 12:30 | 6a92aab973b542df4dd6f5ae | launch/day008.png |
| 9 | 2026-09-07 | 17:10 | 6a92aabee959557ce55a379a | launch/day009.png |

NOTE: Buffer free plan limit = 10 scheduled posts per channel.

## Week-2 batch (queued 2026-08-29, 4 posts, quotes in quotation marks on image + caption)

|| Date | Time (CET) | Buffer post id | Card |
|---|---|---|---|
| 10 | 2026-09-06 | 12:30 | 6a92f5d119e5b3c30ea6c441 | launch/day011.png |
| 11 | 2026-09-07 | 17:10 | 6a92f5d573b542df4ddd39f1 | launch/day010.png |
| 12 | 2026-09-08 | 08:40 | 6a92f5d9463a5d78ec6e22d9 | launch/day012.png |
| 13 | 2026-09-09 | 12:30 | 6a92f5dd9e5f3621e72a1d8e | launch/day013.png |

Quotes on these cards are wrapped in double quotation marks (Ferdy's new style).
QUEUE FULL at 10/10 - drain before queueing more (earliest slot frees Sep 1).

## Posting rules
- Caption = the quote itself. No emojis.
- Hashtags: week 1 (launch batch) posts have none. Week 2 = A/B test: 1 niche builder tag per post (#BuildInPublic / #indiehacker / #solofounder), compare vs week 1 in the Sept 7 metrics pull. Keep only if materially positive.
- Time: rotate 08:40 / 12:30 / 17:10 CET so the grid covers different feed windows.
- First two weeks: reply to 5-10 builder/motivation accounts daily from @buildwithscars.
- Background rotation: rays → ember door → silk arc → horizon, no adjacent repeats.
- Image hosting: repo **darinorcom/quotes-assets** (public), served via jsDelivr:
  `https://cdn.jsdelivr.net/gh/darinorcom/quotes-assets@main/cards/launch/<file>`
  Never use expiring hosts (uguu = 3h). Buffer assets need a URL at publish time.
- Buffer free plan: max 10 scheduled posts/channel. Ping before batching a new week.

## Week-3 batch (queued 2026-08-30, 5 posts, quote-marks style on image + caption)

| # | Date | Time (CET) | Buffer post id | Card |
|---|---|---|---|---|
| 14 | 2026-08-31 | 08:40 | 6a943802e7e04684c6fd0a1b | batch2/day014.png |
| 15 | 2026-09-01 | 12:30 | 6a943804f7f5d8f78d1a637d | batch2/day015.png |
| 16 | 2026-09-02 | 17:10 | 6a943806e7e04684c6fd0a64 | batch2/day016.png |
| 17 | 2026-09-03 | 08:40 | 6a94380894904b3a23e95210 | batch2/day017.png |
| 18 | 2026-09-04 | 12:30 | 6a943809d076c0e5835c9784 | batch2/day018.png |

Images: cdn.jsdelivr.net/gh/darinorcom/quotes-assets@main/cards/batch2/<file>
Cards + source quotes in ~/projects/quotes-x/batch2/. All 5 vision-checked; handle verified @buildwithscars.
Queue now 5/10 after this batch (launch queue drained during week 1).

## Batch 3 (created 2026-09-03, 4 posts as DRAFTS — awaiting Ferdy's approval, not scheduled)

|| # | Buffer post id | Status | Card |
|---|---|---|---|---|
| 19 | 6a997d4a37b8e68715cbbdfc | draft | batch3/day020.png |
| 20 | 6a998300ed3a2df69e0b77ee | draft | batch3/day021.png |
| 21 | 6a998302f61beac67602dd68 | draft | batch3/day022.png |
| 22 | 6a998303784ae840132ae79b | draft | batch3/day023.png |

Quotes (all vision-checked word-for-word, curly-quote style, render_card.py over palettes/ backgrounds):
- day020 (ember door): "Motivation is weather. The builders are the ones who work in it."
- day021 (horizon): "Start before you feel ready. Ready is a rumor told by finished people."
- day022 (silk arc): "The niche you are waiting to find is on the far side of shipping."
- day023 (gold): "Consistency is not intensity. It is showing up on the days that should not count."

When approved: schedule to the rotating slots (next free after day018 ends Sep 4 → Sep 5 08:40 onward).
Note: day019 draft card (discipline quote) was NOT queued — same quote already published Sep 1.

