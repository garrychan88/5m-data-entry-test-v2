"""
Question 8 — Python: Find and Fix the Bug  [Short Answer — Write Code]

The function below is SUPPOSED to count how many even numbers are in a list.
It runs without crashing, but it returns the wrong answer.

    def count_evens(numbers):
        count = 0
        for n in numbers:
            if n % 2 == 1:      # <-- something here is wrong
                count = count + 1
        return count

    # Expected: 4  (the evens are 2, 4, 6, 8)
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))

------------------------------------------------------------------
Task
------------------------------------------------------------------

(a) What does the buggy version actually return for [1, 2, 3, 4, 5, 6, 8], and why?

    Answer: 3

(b) Fix the bug. Write the corrected function below.
    (A one-character change is enough, but you must understand why.)
n % 2 == 0, because even numbers leave a remainder of 0 when divided by 2.
"""

def count_evens(numbers):
    # your corrected code here
    pass
 

"""
(c) In one sentence, explain in plain English what `n % 2 == 0` checks.

    Answer: n % 2 == 0 checks whether n is evenly divisible by 2, which means n is an even number.
"""
