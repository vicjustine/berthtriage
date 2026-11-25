from berthtriage.queue import by_priority, total_teu, ordered


def test_total_teu():
    assert total_teu() == 7800


def test_by_priority():
    assert [r.ref for r in by_priority("blocker")] == ["R-1003"]
    assert by_priority("critical") == []


def test_ordered_puts_blockers_first():
    assert [r.ref for r in ordered()] == ["R-1003", "R-1001", "R-1002"]
