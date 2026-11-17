"""Production-oriented stable algorithms for the SentinelOps SOC module."""
from bisect import bisect_left, bisect_right, insort
import math

def sort_alerts(alerts):
    """Stable descending-severity sort. Python's Timsort is efficient on nearly sorted data."""
    return sorted(alerts, key=lambda alert: alert[1], reverse=True)

def is_blocked(blocklist, ip):
    """Membership lookup. Build a set once and reuse it for repeated queries."""
    return ip in blocklist if isinstance(blocklist, (set, frozenset)) else ip in set(blocklist)

def find_signature(log, pattern):
    """Brute-force all-occurrences scan; each alignment is tested once, including final one."""
    if pattern == "":
        return list(range(len(log) + 1))
    n, m = len(log), len(pattern)
    hits = []
    for start in range(n - m + 1):
        for offset in range(m):
            if log[start + offset] != pattern[offset]:
                break
        else:
            hits.append(start)
    return hits

def closest_logins(events):
    """Sweep-line closest pair in 2D; returns ((i, j), distance), or (None, inf).

    Events are (x, y) coordinates in km. The active set is ordered by y.
    Points whose x-distance is >= the current best distance cannot improve it.
    """
    n = len(events)
    if n < 2:
        return None, math.inf
    points = sorted((x, y, idx) for idx, (x, y) in enumerate(events))
    active = []  # sorted tuples (y, x, original_index)
    left = 0
    best_sq = math.inf
    best_pair = None
    for x, y, idx in points:
        # Expire points outside the current best-distance vertical strip.
        while left < len(points) and (x - points[left][0]) ** 2 >= best_sq:
            old_x, old_y, old_idx = points[left]
            item = (old_y, old_x, old_idx)
            pos = bisect_left(active, item)
            if pos < len(active) and active[pos] == item:
                active.pop(pos)
            left += 1
        radius = math.sqrt(best_sq) if math.isfinite(best_sq) else math.inf
        low = bisect_left(active, (y - radius, -math.inf, -1))
        high = bisect_right(active, (y + radius, math.inf, math.inf))
        for ay, ax, aidx in active[low:high]:
            dx, dy = x - ax, y - ay
            d_sq = dx * dx + dy * dy
            if d_sq < best_sq:
                best_sq = d_sq
                best_pair = (min(idx, aidx), max(idx, aidx))
        insort(active, (y, x, idx))
    return best_pair, math.sqrt(best_sq) if best_pair is not None else math.inf
