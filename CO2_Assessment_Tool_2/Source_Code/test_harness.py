"""Automated test harness for corrected and optimised SentinelOps functions."""
import math
from corrected import sort_alerts as c_sort, is_blocked as c_block, find_signature as c_find, closest_logins as c_close
from optimized import sort_alerts as o_sort, is_blocked as o_block, find_signature as o_find, closest_logins as o_close

def run():
    alerts = [("A1", 3), ("A2", 9), ("A3", 5), ("A4", 9), ("A5", 1)]
    expected_alerts = [("A2", 9), ("A4", 9), ("A3", 5), ("A1", 3), ("A5", 1)]
    assert c_sort(alerts.copy()) == expected_alerts
    assert o_sort(alerts.copy()) == expected_alerts

    blocklist = ["10.0.0.5", "10.0.0.9", "172.16.4.2"]
    for ip, expected in [("10.0.0.9", True), ("10.0.0.5", True), ("8.8.8.8", False)]:
        assert c_block(blocklist, ip) is expected
        assert o_block(set(blocklist), ip) is expected
    assert c_block([], "1.2.3.4") is False
    assert o_block(set(), "1.2.3.4") is False

    assert c_find("FAILFAIXFAIL", "FAIL") == [0, 8]
    assert o_find("FAILFAIXFAIL", "FAIL") == [0, 8]
    assert c_find("abcXYZ", "XYZ") == [3]       # final legal alignment
    assert o_find("abcXYZ", "XYZ") == [3]
    assert c_find("abc", "longer") == []
    assert o_find("abc", "longer") == []
    assert c_find("aaaa", "aa") == [0, 1, 2]     # overlaps
    assert o_find("aaaa", "aa") == [0, 1, 2]
    assert c_find("", "") == [0]
    assert o_find("", "") == [0]

    events = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    cp, cd = c_close(events)
    op, od = o_close(events)
    assert cp == (0, 5) and math.isclose(cd, math.sqrt(2))
    assert op == cp and math.isclose(od, cd)
    assert c_close([]) == (None, math.inf)
    assert o_close([]) == (None, math.inf)
    assert c_close([(1, 2)]) == (None, math.inf)
    assert o_close([(1, 2)]) == (None, math.inf)

    print("PASS: sorting (including stable equal severities)")
    print("PASS: sequential/set blocklist search and empty blocklist")
    print("PASS: string matching, final alignment, longer pattern, overlaps, empty pattern")
    print("PASS: closest pair, distinct indices, empty and single-event boundaries")
    print("ALL TESTS PASSED")

if __name__ == "__main__":
    run()
