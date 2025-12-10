# Optimization Explanation – Problem 2

I optimized Problem 2 by replacing multiple loops with a single comprehension.

Before:
- Reverse string
- Loop to remove 3rd chars
- Loop to shift ASCII
- Loop to count vowels

After:
- Combined operations into fewer passes
- Reduced time complexity from ~4n to ~2n

This makes the solution faster and uses less memory.