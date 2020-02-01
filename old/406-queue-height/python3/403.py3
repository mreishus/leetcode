#!/usr/bin/env python3
from typing import List
from operator import itemgetter
import pprint

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by Height, tallest first.  Break ties with K, lowest first.
        people = sorted(people, key=itemgetter(1))
        people = sorted(people, key=itemgetter(0), reverse=True)

        q = [people.pop(0)]
        for person in people:
            q.insert(person[1], person)
        return q

expected_result = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
this_input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
s = Solution()
actual_result = s.reconstructQueue(this_input)
print("Expect to see")
print(expected_result)
print("Actual Result")
print(actual_result)
print("Are same?")
print(actual_result == expected_result)
