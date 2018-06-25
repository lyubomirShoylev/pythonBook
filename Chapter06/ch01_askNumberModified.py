# Ask Number Modified
# 
# Modifies the function so that it can be called with a step value
# Original in ex-05

# ORIGINAL FUNCTION
# def askNumber(question, low, high):
#     """Ask for a number within a range."""
#     response = None
#     while response not in range(low, high):
#         response = int(input(question))
#     return response

def askNumber(question, low, high, step = 1):
    """
    askNumber(question, low, high[, step])\n
    Ask for a number within a range. Optional step is available, and the default
    value is 1.
    """
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response