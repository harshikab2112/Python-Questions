# Python Error Handling

---

This repository contains **50 practice questions** focused on **error handling** in Python, covering concepts like:

---

- **try-except blocks**
- **Multiple exception handling**
- **Custom exceptions**
- **Raising exceptions**

---

The questions are divided into **Beginner**, **Intermediate**, and **Advanced** levels.

## Beginner Level (1–15: Basic Try-Except Handling)

### Basic Error Handling with Try-Except
1. Write a program that catches and prints a `ZeroDivisionError` when dividing a number by zero.
2. Write a program that catches a `ValueError` when trying to convert a non-numeric string to an integer.
3. Use a `try-except` block to catch a `TypeError` when trying to add a string and an integer.
4. Write a program that catches an `IndexError` when trying to access an element outside the bounds of a list.
5. Write a program that catches a `KeyError` when trying to access a key that doesn't exist in a dictionary.
6. Write a program that catches a `FileNotFoundError` when trying to open a file that doesn't exist.
7. Use `try-except` to catch any exception and print the error message.
8. Write a program that catches and prints an error if the user inputs a value that’s not an integer.
9. Write a function that tries to divide two numbers, and catches any exception that might occur.
10. Handle an exception that occurs when trying to access a negative index in a list.
11. Write a program that catches and prints a `TypeError` when trying to multiply a string by a non-integer value.
12. Create a program that catches a `ValueError` when a user inputs invalid data, such as a string for a number input.
13. Write a program that handles a `FileNotFoundError` and provides a message when the file is not found.
14. Handle a `NameError` when referencing a variable that has not been defined.
15. Write a program that catches and handles an `ImportError` when trying to import a module that doesn't exist.

## Intermediate Level (16–35: Multiple Except Clauses, Else, and Finally)

### Handling Multiple Exceptions
16. Write a program that uses multiple `except` clauses to handle different errors when reading and processing a file.
17. Write a program that tries to convert a string to an integer and handles both `ValueError` and `TypeError` separately.
18. Use `try-except` to handle a `KeyError` and a `ValueError` in a dictionary operation.
19. Write a program that catches both `IndexError` and `ValueError` while manipulating a list and handles them separately.
20. Use `try-except-else` to handle errors when opening a file, and use `else` to print a success message when no error occurs.
21. Write a program that handles both `TypeError` and `ZeroDivisionError` and prints an appropriate message for each.
22. Write a function that catches both `FileNotFoundError` and `PermissionError` when opening a file.
23. Use a `try-except-finally` block to ensure that a file is always closed after it’s opened, regardless of whether an exception occurs.
24. Write a program that handles multiple errors (e.g., `ValueError`, `ZeroDivisionError`) when performing arithmetic operations.
25. Handle multiple exceptions (e.g., `FileNotFoundError`, `PermissionError`) when attempting to read a file.
26. Use a `try-except-else` block to handle `ValueError` and perform a calculation only if no error occurs.
27. Write a program that attempts to access a dictionary key and catches both `KeyError` and `TypeError`.
28. Handle both `ValueError` and `IndexError` while processing user input for a list operation.
29. Use `try-except-finally` to manage a database connection, ensuring it’s closed whether an error occurs or not.
30. Write a program that handles both `AttributeError` and `TypeError` while working with objects and methods.

## Advanced Level (36–50: Custom Exceptions, Raising Exceptions)

### Custom Exceptions
36. Write a custom exception called `NegativeValueError` that is raised when a negative number is entered.
37. Create a custom exception `InvalidAgeError` that raises an exception when the age input is less than 0 or greater than 120.
38. Write a program that uses a custom exception `TooSmallValueError` to raise an exception when a value is smaller than a given threshold.
39. Define a custom exception `OutOfRangeError` that is raised when a user input is out of a defined range.
40. Create a custom exception `InvalidInputError` to raise an exception when invalid data is entered into a function.
41. Write a custom exception `NegativeBalanceError` for situations where a bank account balance goes negative.
42. Define a custom exception `InsufficientFundsError` and use it in a program that simulates a withdrawal from a bank account.
43. Create a custom exception `NotFoundError` that raises an exception when an item is not found in a list.
44. Write a program that raises a custom exception `DivideByZeroError` when a division by zero occurs.
45. Create a custom exception `DuplicateItemError` to raise when an item being added to a list already exists.

### Raising Exceptions
46. Write a function that raises an exception `ValueTooHighError` when a number exceeds a specified limit.
47. Write a program that raises a custom `FileMissingError` if the file cannot be found in the directory.
48. Write a function that raises an exception when the user inputs a number greater than 100, using a custom exception `ValueTooLargeError`.
49. Define a function `check_age` that raises a `CustomAgeError` if the provided age is less than 18.
50. Write a program that raises an exception if a user attempts to input an invalid date format, using a custom exception `InvalidDateError`.
