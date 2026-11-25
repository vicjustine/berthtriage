"""Berth request queue — the thing issues are filed against."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    ref: str
    vessel: str
    teu: int
    priority: str


QUEUE = [
    Request("R-1001", "MSC Aurora", 3800, "major"),
    Request("R-1002", "Ever Lyric", 1600, "minor"),
    Request("R-1003", "Nordic Dawn", 2400, "blocker"),
]


def by_priority(level: str) -> list:
    return [r for r in QUEUE if r.priority == level]


def total_teu() -> int:
    return sum(r.teu for r in QUEUE)


def ordered() -> list:
    """Queue in service order: blockers first, then major, then minor."""
    rank = {"blocker": 0, "major": 1, "minor": 2}
    return sorted(QUEUE, key=lambda r: (rank[r.priority], r.ref))
