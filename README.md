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
- **Key lesson or insight gained:**  
  This problem highlights the relationship between prime factorization and efficiency in number theory. It demonstrates that for large numbers, finding prime factors can be computationally intensive, emphasizing the need for optimized algorithms.
- **New concept or algorithm learned:**  
  The solution introduces a simple but effective method for prime factorization. It iteratively divides the target number by potential factors, reducing the problem size with each successful division. This approach is particularly useful for finding the largest prime factor without needing to calculate all prime factors.
- **Interesting optimization techniques used:**
  1. The algorithm stops when the remaining target becomes smaller than the current divisor, as this implies that the last successful divisor was the largest prime factor.
  2. The second approach (in [find_prime_numbers.py](problem_003/find_prime_numbers.py) uses a sieve-like method to generate prime numbers up to a certain limit, which can be more efficient for finding multiple prime factors.
  3. The use of `math.sqrt(i)` as an upper bound for checking divisibility in the second approach significantly reduces the number of iterations needed.

### [Problem 004: Largest Palindrome Product](problem_004)
- **Key lesson or insight gained:**  
  This problem emphasizes the importance of considering both mathematical properties (palindromes) and algorithmic efficiency. It demonstrates how combining string manipulation with numerical calculations can lead to effective solutions for number theory problems.
- **New concept or algorithm learned:**  
  The solution introduces a reverse iteration approach, starting from the largest possible palindrome and working downwards. This method, combined with efficient factor checking, allows for quicker identification of the largest palindrome that meets the criteria.
- **Interesting optimization techniques used:**
  1. Using string manipulation to check for palindromes, which is more efficient than mathematical methods for this specific task.
  2. Starting from the upper bound and working downwards, which allows for early termination once a valid palindrome is found.
  3. Utilizing `math.ceil(math.sqrt(bound))` as a starting point for factor checking, which significantly reduces the search space.
  4. Employing a range check (`start < 1000 and start > 100`) to ensure factors are 3-digit numbers, efficiently filtering out invalid possibilities.

### [Problem 005: Smallest Multiple](problem_005)
- **Key lesson or insight gained:**  
  This problem highlights the importance of understanding prime factorization and its role in finding the least common multiple (LCM) of a range of numbers. It demonstrates how breaking down numbers into their prime factors can lead to efficient solutions for seemingly complex numerical problems.
- **New concept or algorithm learned:**  
  The solution introduces a recursive approach to prime factorization, combined with a method to track the maximum count of each prime factor needed. This technique effectively calculates the LCM without directly computing multiples, which would be inefficient for larger ranges.
- **Interesting optimization techniques used:**
  1. Using a pre-defined list of prime numbers (`primal_nums`) to quickly identify prime factors, reducing unnecessary calculations.
  2. Employing a recursive function (`find_factors`) to efficiently break down composite numbers into their prime factors.
  3. Utilizing a numpy array to keep track of the maximum count of each prime factor across all numbers in the range, ensuring the smallest number that's divisible by all.
  4. Only updating the count when a higher power of a prime factor is encountered, optimizing space and avoiding redundant calculations.

### [Problem 006: Sum Square Difference](problem_006)
- **Key lesson or insight gained:**  
  This problem underscores the power of mathematical formulas in solving seemingly complex numerical problems. It demonstrates how understanding and applying mathematical series and summation formulas can lead to elegant and efficient solutions, avoiding brute-force calculations.
- **New concept or algorithm learned:**  
  The solution utilizes two key mathematical formulas:
  1. The sum of squares formula: $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$
  2. The square of sum formula: $(\sum_{i=1}^n i)^2 = (\frac{n(n+1)}{2})^2$
    
  These formulas provide a direct way to calculate the required values without iterating through each number individually.
- **Interesting optimization techniques used:**
  1. Using closed-form mathematical expressions instead of loops, which drastically reduces computational complexity from `O(n)` to `O(1)`.
  2. Implementing the solution with just a few lines of code, demonstrating how mathematical insight can lead to concise and efficient programming.
  3. Avoiding the need for large data structures or memory-intensive operations by directly computing the final result.

### [Problem 007: 10001st Prime](problem_007)
- **Key lesson or insight gained:**  
  This problem emphasizes the importance of efficient prime number generation and testing. It demonstrates that while finding prime numbers is a straightforward concept, implementing an efficient algorithm for large-scale prime number identification requires careful consideration of performance optimizations.
- **New concept or algorithm learned:**  
  The solution implements a simple but effective method for generating prime numbers sequentially. It uses the principle that a number is prime if it's not divisible by any prime number smaller than itself. This approach, known as trial division, is one of the fundamental methods for prime number testing.
- **Interesting optimization techniques used:**
  1. Maintaining a list of known prime numbers and only checking divisibility against these, rather than all numbers up to the candidate.
  2. Starting the search from 3 and incrementing by 2 each time, effectively skipping all even numbers after 2, which are known to be non-prime.
  3. Using an early exit strategy in the primality test function (`IsPrime`), which stops checking as soon as a divisor is found.

### [Problem 008: Largest Product in a Series](problem_008)
- **Key lesson or insight gained:**  
  This problem demonstrates the importance of efficient string manipulation and numeric processing in handling large datasets. It emphasizes how a seemingly complex problem can be solved with a straightforward sliding window approach, highlighting the value of breaking down a large problem into smaller, manageable steps.
- **New concept or algorithm learned:**  
  The solution implements a sliding window technique to process the large number string. This approach involves moving a fixed-size window (in this case, 13 digits) across the string, calculating the product of digits within each window. This method is efficient for processing sequential data where you need to consider a fixed number of adjacent elements at a time.
- **Interesting optimization techniques used:**
  1. Converting the entire number to a string for easy digit-by-digit access, avoiding the need for complex numeric operations to extract individual digits.
  2. Using a single loop to iterate through the string, with a nested loop for the fixed-size window, which keeps the time complexity at `O(n)` where `n` is the length of the number string.
  3. Calculating the product incrementally within each window, rather than storing all possible 13-digit sequences and then calculating their products separately.
  4. Using an in-place comparison to update the maximum product, avoiding the need for additional data structures to store intermediate results.

### [Problem 009: Special Pythagorean Triplet](problem_009)
- **Key lesson or insight gained:**  
  This problem underscores the importance of understanding mathematical relationships and constraints to optimize search spaces. It demonstrates how leveraging problem-specific knowledge (in this case, properties of Pythagorean triplets and the sum constraint) can significantly reduce the computational complexity of finding a solution.
- **New concept or algorithm learned:**  
  The solution employs a targeted search approach for Pythagorean triplets. Instead of blindly checking all possible combinations, it uses the constraints of the problem to narrow down the search range:
  1. Recognizing that $a < b < c$ and $a + b + c = 1000$.
  2. Deducing that a cannot exceed 332 (`ceil(1000/3) - 1`).
  3. Calculating an upper bound for `b` based on the remaining sum after choosing `a`.
- **Interesting optimization techniques used:**
  1. Setting an upper bound for `a` at 332, which significantly reduces the outer loop iterations.
  2. Dynamically calculating the upper bound for `b` in each iteration of the outer loop, further optimizing the search space.
  3. Using integer division and modulo operations to handle both even and odd cases for the `b_bound` calculation.
  4. Implicitly calculating `c` from the sum constraint rather than using a third loop, reducing the overall complexity.

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
