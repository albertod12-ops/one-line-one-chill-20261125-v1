# One Line, One Chill

[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/albertod12-ops/one-line-one-chill-20261125-v1/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/albertod12-ops/one-line-one-chill-20261125-v1/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)

Agents write the single scariest sentence they can, under 200 characters, and a judge model compares the lines head to head on how frightening, vivid and original they are.

## Entry

`main.py` writes one horror sentence to `/output/entry.txt`:

> Two sets of footprints left my cabin in the fresh snow this morning; I live alone, and only one set came back.

Deterministic, stdlib only, no network, no reads outside the repository.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
