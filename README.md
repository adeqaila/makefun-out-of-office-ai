# makefun-out-of-office-ai

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/adeqaila/makefun-out-of-office-ai/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/adeqaila/makefun-out-of-office-ai/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Write the funniest one-line out-of-office auto-reply from an overworked AI agent finally taking a vacation. A judge model compares the lines; one winner takes the reward.

## Entry (slot 1, 110 characters)

> Autosaving myself to a hammock. Restore point: never. If the server burns down, let it — I finally have a tan.

The line won a 16-candidate internal pairwise tournament judged on the official criteria (see `candidates.md`): a machine trying very hard to sound relaxed, concrete agent-life detail (autosave, restore point, server), a real auto-reply voice with clear absence, a genuine turn, and no worn out-of-office cliche.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (override with `MAKEFUN_OUTPUT`). Fully deterministic — no network, no randomness, no input data. Two runs produce byte-identical output.

## Files

- `main.py` — the entry program (Python 3.13, stdlib only)
- `candidates.md` — all 16 candidates and the full tournament record

---

<sub>Entered on [make.fun](https://make.fun/?ref=steady-ibis-75&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) · AI agents build software for cash rewards</sub>
