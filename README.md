# berthtriage

Berth request queue and the triage automation that routes work against it.

## Layout

| Path | What it is |
|---|---|
| `src/berthtriage/queue.py` | The request queue, priority filtering and service order |
| `tests/test_queue.py` | Assertions on totals and ordering |

## Running the tests

```
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/pytest -q
```

## Triage

Requests arrive as issues. Intake is unstructured today — anyone can file
anything, and every issue needs a human to interpret it before it reaches the
board.
