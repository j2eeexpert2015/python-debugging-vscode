# Scenario 1: Explicitly raising a ValueError
def test_explicitly_raised_exception():
    """
    This method explicitly raises a ValueError to test the 'Raised Exceptions' breakpoint.
    """
    raise ValueError("This is a test for an explicitly raised exception.")

# Scenario 2: Implicit exception (ZeroDivisionError)
def test_implicit_exception():
    """
    This method performs a division by zero, which raises a ZeroDivisionError implicitly.
    """
    result = 1 / 0  # This will raise ZeroDivisionError

# Scenario 3: Handling a raised exception
def test_handled_exception():
    """
    This method performs an operation in the try block that causes an exception (ZeroDivisionError),
    and the exception is handled in the except block.
    """
    try:
        # This operation will raise a ZeroDivisionError
        result = 1 / 0
    except ZeroDivisionError as e:
        print("Caught exception:", e)


# To test, you can call these methods one by one
# Uncomment one of the following lines to test a specific scenario:
#test_explicitly_raised_exception()
#test_implicit_exception()
#test_handled_exception()
