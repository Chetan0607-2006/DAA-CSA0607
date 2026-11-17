"""Corrected reference implementations for the SentinelOps assignment."""
import math

def sort_alerts(alerts):
    """Stable insertion sort by descending severity; equal severities keep arrival order."""
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1
        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1
        alerts[j + 1] = key
    return alerts

def is_blocked(blocklist, ip):
    """Return True exactly when ip occurs in blocklist (sequential search)."""
    for item in blocklist:
        if item == ip:
            return True
    return False

def find_signature(log, pattern):
    """Return every starting index of pattern in log, including overlapping matches."""
    if pattern == "":
        return list(range(len(log) + 1))
    n, m = len(log), len(pattern)
    hits = []
    for i in range(n - m + 1):
        for j in range(m):
            if log[i + j] != pattern[j]:
                break
        else:
            hits.append(i)
    return hits

def closest_logins(events):
    """Return the closest distinct pair and Euclidean distance; None if fewer than two."""
    if len(events) < 2:
        return None, math.inf
    best_sq = math.inf
    pair = None
    for i in range(len(events) - 1):
        for j in range(i + 1, len(events)):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]
            d_sq = dx * dx + dy * dy
            if d_sq < best_sq:
                best_sq = d_sq
                pair = (i, j)
    return pair, math.sqrt(best_sq)
