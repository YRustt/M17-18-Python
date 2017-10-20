import re


def index(s, nums, k=5):
    def idxs_for_num(s, n):
        return [m.start() + 1 for m in re.finditer(str(n), s)]

    if not hasattr(nums, '__iter__'):
        nums = (nums,)

    res = []
    for n in nums:
        res += idxs_for_num(s, n)

    return len(res), sorted(res)[:k]
