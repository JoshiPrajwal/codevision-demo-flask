# codevision-demo-flask

A tiny Flask notes app made by CodeVision.ai for trying out a scan.

**The bugs in this project are deliberate.** Do not deploy it. It exists so you can see findings, explanations and
suggested fixes on code you own.

| File | Deliberate bug |
|---|---|
| `app.py` | SQL built from user input (SQL injection) |
| `app.py` | A hardcoded secret key |
| `app.py` | Flask debug mode turned on |
| `app.py` | `eval()` on a query parameter |
| `pagination.py` | A logic bug: every page drops its last item |

`manifest.json` lists what CodeVision's deterministic rules are expected to find. The logic bug is there for the review
engine; no rule looks for it.
