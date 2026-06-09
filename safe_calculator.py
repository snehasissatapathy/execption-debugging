"""
## 1. Safe Calculator with try / except  *(Easy)*

=================================================
SAFE CALCULATOR
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_divide`
that takes two values from the user and
performs a division, but never crashes the
program.

Handle the following error cases gracefully:
   - non-numeric input        -> ValueError
   - division by zero         -> ZeroDivisionError
   - any other unexpected bug -> generic Exception

The function must always return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the result on success,
                         or an error string on
                         failure.

-------------------------------------------------
Debugging Skills to Practice:
- Read the FULL traceback. The last line of a
  traceback names the exception class — match
  it to your `except`.
- Use a temporary print(type(a), type(b))
  before the division to confirm the inputs.
- Insert breakpoint() and step through with
  the Python debugger (pdb) commands:
       n  -> next line
       s  -> step into
       p  -> print a variable
       q  -> quit

-------------------------------------------------
Input Example 1:
safe_divide("10", "2")

Output Example 1:
('ok', 5.0)
Calculation finished

-------------------------------------------------
Input Example 2:
safe_divide("10", "0")

Output Example 2:
('error', 'Cannot divide by zero')
Calculation finished

-------------------------------------------------
Input Example 3:
safe_divide("ten", "2")

Output Example 3:
('error', 'Inputs must be numbers')
Calculation finished
=================================================

"""
def safe_divide():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2
        return ("ok", result)

    except ValueError:
        return ("error", "Non-numeric input entered")

    except ZeroDivisionError:
        return ("error", "Division by zero is not allowed")

    except Exception as e:
        return ("error", f"Unexpected error: {e}")
status, value_or_message = safe_divide()
print((status, value_or_message))