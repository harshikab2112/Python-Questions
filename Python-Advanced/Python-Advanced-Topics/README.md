# Advanced Python Topics: Practice Questions

This repository contains **50 practice questions** focused on advanced Python topics, including **decorators**, **generators**, **context managers**, and **regular expressions**, organized into beginner, intermediate, and advanced levels.

## Beginner Level (1–15: Decorators, Generators, and Context Managers Basics)

### Decorators
1. Write a basic decorator that prints a message before and after a function is executed.
2. Create a decorator that logs the arguments passed to a function.
3. Write a decorator that times how long a function takes to execute.
4. Implement a decorator that accepts arguments and uses those arguments to modify the behavior of a function.
5. Write a decorator that prevents a function from being called more than once.
6. Create a decorator to cache the results of function calls.
7. Write a decorator to check whether a function argument is a valid integer.
8. Create a decorator that adds a custom message to the output of any function it decorates.
9. Implement a decorator that executes a function only if the user is authenticated (using a simple boolean check).
10. Write a decorator to memoize the results of a function, storing them in a dictionary.

### Generators
11. Write a generator function that yields numbers from 1 to 5.
12. Create a generator that generates the Fibonacci sequence.
13. Write a generator function that yields squares of numbers from 1 to N.
14. Implement a generator that yields words from a sentence one by one.
15. Write a generator that yields prime numbers indefinitely.

---

## Intermediate Level (16–35: Advanced Decorators, Generators, and Context Managers)

### Decorators
16. Write a decorator that logs the execution time of a function using the `time` module.
17. Create a decorator that retries a function up to 3 times if it raises an exception.
18. Write a decorator that limits the number of times a function can be called within a certain time window (rate-limiting).
19. Create a decorator that ensures the return value of a function is always of a specific type (e.g., string or integer).
20. Write a decorator that tracks the number of times a function has been called.
21. Implement a decorator that checks whether the function argument is even or odd before calling the function.
22. Create a decorator that enforces function arguments to be non-empty strings.
23. Write a decorator to log the output of a function to a file.
24. Implement a decorator that modifies the return value of a function.
25. Write a decorator that caches function results using an `lru_cache` mechanism.

### Generators
26. Create a generator function that yields values based on an external condition.
27. Write a generator that yields elements from a list, but skips even numbers.
28. Implement a generator that yields the first N elements of an infinite sequence (like Fibonacci).
29. Write a generator that takes a range of numbers and yields even numbers from the range.
30. Create a generator that pauses between yielding values, simulating a slow data stream.
31. Write a generator that reads a large file line-by-line instead of loading the entire file into memory.
32. Implement a generator that computes the factorial of a number.
33. Create a generator that yields pairs of items from two lists.
34. Write a generator that implements the `map()` function behavior for a given function and iterable.
35. Create a generator that implements the `filter()` function behavior for a given condition and iterable.

### Context Managers
36. Write a simple context manager using `__enter__` and `__exit__` methods.
37. Create a context manager that opens and automatically closes a file.
38. Write a context manager that measures the execution time of a code block.
39. Implement a context manager that ensures a database connection is always closed.
40. Create a context manager that logs the entry and exit of a block of code.
41. Write a context manager that checks for specific conditions before allowing the code block to execute (e.g., check if a file exists).
42. Implement a context manager that sets up and cleans up some resources for a unit test.
43. Write a context manager that temporarily changes the working directory.
44. Create a context manager that times a block of code and prints the execution time.
45. Implement a context manager that retries a block of code upon failure.

---

## Advanced Level (36–50: Advanced Regular Expressions, Complex Decorators and Generators)

### Regular Expressions
46. Write a regular expression to validate an email address.
47. Create a regular expression to match a valid phone number in various formats (e.g., (123) 456-7890, 123-456-7890).
48. Write a regular expression to extract all URLs from a given text.
49. Implement a regular expression to match a date in `YYYY-MM-DD` format.
50. Write a regular expression that finds all instances of words in a string that start with a specific letter (e.g., `s`).
51. Create a regular expression to match a valid IPv4 address.
52. Write a regular expression to replace all multiple spaces in a text with a single space.
53. Create a regular expression to extract hashtags (`#word`) from a text.
54. Implement a regular expression to validate a strong password (at least 8 characters, contains upper/lowercase letters, numbers, and special characters).
55. Write a regular expression to find all the words that are repeated consecutively in a sentence.

### Advanced Generators and Decorators
56. Write a generator that implements an infinite sequence of prime numbers using the `yield` keyword.
57. Create a decorator that logs each function call's arguments and return value to a log file.
58. Implement a decorator that caches function results but expires the cache after a specified time.
59. Write a decorator that checks whether the arguments of a function match certain conditions (e.g., not empty).
60. Create a generator that fetches data from a REST API and yields the results.
61. Implement a generator that paginates through a large collection of data (e.g., from a database or an API).
62. Create a decorator that adds authentication checks before allowing a function to execute.
63. Write a generator that processes a list of items in batches (e.g., processes 10 items at a time).
64. Create a decorator that prints a message before and after the function call, including arguments and return values.
65. Implement a context manager that acquires and releases locks in a multithreading environment.

---

This list covers a broad range of **advanced Python concepts**, including **decorators**, **generators**, **context managers**, and **regular expressions**. These topics will help you deepen your understanding of Python, especially when working with complex systems and optimizing performance.
