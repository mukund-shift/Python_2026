# Performance Evaluation of Cache Memory using LRU Replacement Policy

cache_size = int(input("Enter Cache Size: "))

reference_string = list(map(int, input("Enter Memory Reference String (space separated): ").split()))

hit_time = float(input("Enter Cache Hit Time (ns): "))
miss_penalty = float(input("Enter Miss Penalty (ns): "))

cache = []

hits = 0
misses = 0

print("\nMemory Access Simulation")
print("-" * 60)

for page in reference_string:

    if page in cache:
        hits += 1

        # Move page to most recently used position
        cache.remove(page)
        cache.append(page)

        print(f"{page} -> HIT\tCache = {cache}")

    else:
        misses += 1

        if len(cache) == cache_size:
            cache.pop(0)

        cache.append(page)

        print(f"{page} -> MISS\tCache = {cache}")

total_accesses = len(reference_string)

hit_ratio = hits / total_accesses
miss_ratio = misses / total_accesses

amat = hit_time + (miss_ratio * miss_penalty)

print("\n------------- RESULT -------------")
print("Total Memory Accesses :", total_accesses)
print("Cache Hits            :", hits)
print("Cache Misses          :", misses)
print("Hit Ratio             :", round(hit_ratio, 4))
print("Miss Ratio            :", round(miss_ratio, 4))
print("Average Memory Access Time (AMAT):", round(amat, 4), "ns")
