def cache_hit_rate(keys: list[int]) -> tuple[int, int, float]:
    """
    keys: a sequence of request keys in arrival order.

    A request is a hit iff its key has appeared earlier in the sequence
    (the first occurrence of any key is always a miss).

    Return (hits, misses, rate) where rate = hits / len(keys).
    """
    # TODO: track which keys have been seen so far, in order.
    if not keys:
        return 0,0,0.0

    seen = set()
    hits = 0
    misses = 0
    for key in keys:
        if key in seen:
            hits +=1
        else:
            misses +=1
            seen.add(key)
    rate = hits/len(keys)
    return hits, misses, rate
