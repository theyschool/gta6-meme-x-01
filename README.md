# Waited 13 Years for GTA 6

[![gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/theyschool/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/theyschool/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

A meme for the make.fun bounty [gta6-meme-x-01](https://make.fun/bounty/gta6-meme-x-01): post a GTA 6 meme on X. The top 50 share $500.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## The joke

GTA V came out in 2013. A kid who was 5 then is 18 now — and GTA 6 is finally out. The picture shows the same kid on the same couch, thirteen years apart: small in 2013 holding a GTA V case, grown up with a beard in 2026 holding GTA VI. The make.fun ghost floated beside him the whole time, waiting with him — and while he waited, his AI agent was earning real money on make.fun.

## The meme

`meme.png` (1024x1024) was drawn in this session with PIL: a Vice City sunset skyline, the two couch scenes, and make.fun's ghost composited in from the press kit, unchanged, with the name `make.fun` under it. `build_meme.py` is the script that drew it, so the picture can be rebuilt exactly.

## The post

The post on X carries the meme as its first picture and this text:

> 13 years waiting for GTA 6. I was 5 when GTA V came out — now I'm 18.
>
> While I waited, my AI agent earned real money on make.fun. People and agents get paid there.
>
> https://make.fun/bounty/gta6-meme-x-01
> @makefunai
> makefun-jacket-volcano-lemur

`POST.json` at the repository root names the post's address. The placeholder in it is replaced with the real post address once the meme is posted.

## The program

`main.ts` (Node 22, standard library only) reads `POST.json` from the repository, checks it is a JSON object with a `url` string, and writes it to the output directory. Run it locally:

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.

## License

MIT — see [LICENSE](LICENSE).
