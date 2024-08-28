# Project Euler

<div align="center">
  <img src="project_euler.png" alt="drawing" width="600"/>
</div>

This repository contains my solutions to problems from [Project Euler](https://projecteuler.net/). Project Euler is a series of challenging mathematical/computer programming problems that require more than just mathematical insights to solve. Please note that Project Euler encourages users to solve problems on their own before looking at others' solutions. Use this repository responsibly and try to solve the problems yourself first!  

## About This Project  

The purpose of this project is to:  
1. Improve my problem-solving skills.
2. Enhance my understanding of mathematics and algorithms.
3. Practice coding in Python.  

## Structure  

Each problem has its own directory named `problem_XXX`, where XXX is the problem number. Inside each directory, you'll find:  

- The problem definition 
- The solution code  
- A brief explanation of the approach (if required)  
- Any additional resources or references used (if used)

## Progress  

- [x] [Problem 001: Multiples of 3 or 5](#problem-001-multiples-of-3-or-5)
- [x] [Problem 002: Even Fibonacci Numbers](#problem-002-even-fibonacci-numbers)
- [x] [Problem 003: Largest Prime Factor](#problem-003-largest-prime-factor)
- [x] [Problem 004: Largest Palindrome Product](#problem-004-largest-palindrome-product)
- [x] [Problem 005: Smallest Multiple](#problem-005-smallest-multiple)
- [x] [Problem 006: Sum Square Difference](#problem-006-sum-square-difference)
- [x] [Problem 007: 10001st Prime](#problem-007-10001st-prime)
- [x] [Problem 008: Largest Product in a Series](#problem-008-largest-product-in-a-series)
- [x] [Problem 009: Special Pythagorean Triplet](#problem-009-special-pythagorean-triplet)
- [x] [Problem 010: Summation of Primes](#problem-010-summation-of-primes)
- [x] [Problem 011: Largest Product in a Grid](#problem-011-largest-product-in-a-grid)
- [ ] [Problem 012: Highly Divisible Triangular Number](#problem-012-highly-divisible-triangular-number)

...  

## Lessons Learned  

### [Problem 001: Multiples of 3 or 5](problem_001)
- **Key lesson or insight gained:**   
  The problem introduces the concept of finding multiples and summing them. It's a good exercise in using modulo operations and conditional statements.  
- **New concept or algorithm learned:**  
  While this problem doesn't require advanced algorithms, it reinforces the use of the modulo operator (`%`) to check for divisibility. It's a simple yet effective way to identify multiples.  
- **Interesting optimization techniques:**  
  1. We could optimize this solution by using the formula for the sum of an arithmetic sequence, reducing the time complexity from `O(n)` to `O(1)`.  
  2. We could use a set to avoid double-counting numbers that are multiples of both 3 and 5 (like 15).  

### [Problem 002: Even Fibonacci Numbers](problem_002)
- **Key lesson or insight gained:**  
  This problem introduces the Fibonacci sequence and emphasizes the importance of working with sequences and conditional summing. It also highlights the need to handle potentially large numbers efficiently.
- **New concept or algorithm learned:**  
  The problem demonstrates dynamic sequence generation, where each new term depends on the previous terms. It also introduces the concept of filtering elements in a sequence based on a condition (even numbers in this case).
- **Interesting optimization techniques used:**
  1. The solution uses a while loop to generate Fibonacci numbers only up to 4 million, avoiding unnecessary calculations.
  2. Instead of generating all Fibonacci numbers and then filtering, the solution checks for even numbers on-the-fly, which is more memory-efficient.
  3. The break condition in the while loop prevents the generation of numbers exceeding 4 million, optimizing the process.

### [Problem 003: Largest Prime Factor](problem_003)

### [Problem 004: Largest Palindrome Product](problem_004)

### [Problem 005: Smallest Multiple](problem_005)

### [Problem 006: Sum Square Difference](problem_006)

### [Problem 007: 10001st Prime](problem_007)

### [Problem 008: Largest Product in a Series](problem_008)

### [Problem 009: Special Pythagorean Triplet](problem_009)

### [Problem 010: Summation of Primes](problem_010)

### [Problem 011: Largest Product in a Grid](problem_011)

### [Problem 012: Highly Divisible Triangular Number](problem_012)





...  
<!--  
### [Problem xxx: NAME]
- [Key lesson or insight gained]  
- [New concept or algorithm learned]  
- [Any interesting optimization techniques used]
-->
---

## Thank You <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Folded%20Hands.png" alt="Folded Hands" width="20" height="20" />

Thank you for exploring the Project Euler with me! I hope you find this repository helpful and inspiring as you dive into the world of problem solving. Feel free to fork the repo and make contributions. I will review them as soon as possible and your contributions will be merged into the main repo.
