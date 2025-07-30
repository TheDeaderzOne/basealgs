import math
import collections

def subset_sums(lst):
    n = sum(lst)
    dp = [False] * (n + 1)
    dp[0] = True
    for a, count in collections.Counter(lst).items():
        dp = [min_count <= count for min_count in min_counts(dp, a)]
    return {x for (x, dp_x) in enumerate(dp) if dp_x}


def min_counts(dp, a):
    dp = [(0 if dp_x else math.inf) for dp_x in dp]
    for x in range(a, len(dp)):
        dp[x] = min(dp[x], dp[x - a] + 1)
    return dp

print(subset_sums([1,3,3,5,6]))