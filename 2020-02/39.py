#!/usr/bin/env python


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answers = []
        for i in range(target + 1):
            answers.append([])
        answers[0] = [[0]]

        for score in candidates:
            for this_target in range(target + 1):
                without_this = this_target - score
                if without_this < 0:
                    continue

                sub_combos = answers[without_this]
                combos = []
                for sub in sub_combos:
                    combos.append(sub + [score])
                answers[this_target] += combos

        return [combo[1:] for combo in answers[target]]


if __name__ == "__main__":
    print("hi")
    A = [2, 3, 6, 7]
    target = 7
    S = Solution()

    got = S.combinationSum(A, target)
    want = [[7], [2, 2, 3]]
    got.sort()
    want.sort()

    print(f"Match? {got == want}")
    print(f"Want {want}")
    print(f"Got {got}")
    assert got == want
