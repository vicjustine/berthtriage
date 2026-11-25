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



There is no REST endpoint for any of this. Project vs is GrapQL-only so moving a card means resolving a project node ID, a field ID and an option ID, then issuing a type mutations. I will run the query from a workflow, because github retired the browser explorer last novemeber. 

##Delete later
PROJECT_ID:   PVT_kwHOAoJJBs4BtOxI
STATUS_FIELD: PVTSSF_lAHOAoJJBs4BtOxIzhrZNeQ

OPT_TRIAGE: f75ad846
OPT_ACCEPTED: 47fc9ee4
OPT_BLOCKED: 98236657
OPT_DONE: f7e0effe
