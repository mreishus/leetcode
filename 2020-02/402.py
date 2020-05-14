#!/usr/bin/env python

"""
Given a non-negative integer num represented as a string, remove k digits from
the number so that the new number is the smallest possible.

Note:

    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output
must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing
which is 0.
"""

"""
Answer: Remove a digit when the next digit is smaller.
If all digits are ascending, remove last.

1234 -> Remove 4.

15234 -> Remove 5, because 5->2 is descending.

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return self.remove_leading_zeros(num)
        i = 0
        delete_i = None
        while i < len(num):
            if i + 1 >= len(num) or int(num[i + 1]) < int(num[i]):
                delete_i = i
                break
            i += 1
        new_num = self.remove_leading_zeros(num[:delete_i] + num[delete_i + 1 :])
        return self.removeKdigits(new_num, k - 1)

    def remove_leading_zeros(self, num: str) -> str:
        if len(num) == 0:
            return "0"
        begin = 0
        while num[begin] == "0" and begin + 1 < len(num):
            begin += 1
        return num[begin:]


if __name__ == "__main__":
    print("402 Remove digits")
    cases = [
        ("1234", "1234"),
        ("01234", "1234"),
        ("001234", "1234"),
        ("001", "1"),
        ("000", "0"),
    ]
    for (num, want) in cases:
        got = Solution().remove_leading_zeros(num)
        print(f"Pass? {want == got} | got {got} | want {want} | num {num}")

    cases = [
        ("1432219", 3, "1219"),
        ("10200", 1, "200"),
        ("10", 2, "0"),
    ]
    for (num, k, want) in cases:
        got = Solution().removeKdigits(num, k)
        print(f"Pass? {want == got} | got {got} | want {want} | num {num} | k {k}")
