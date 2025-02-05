def function_with_uncommon_error_solution(x):
    try:
        if isinstance(x, (int, float)): #Explicitly check data type before operations
          if x == 0:
              return 0
          else:
              return 1 / x
        else:
          return "Invalid Input"
    except TypeError as e:
        return f'Error: {e}' #Handle TypeError gracefully
    except Exception as e: 
        return f'An unexpected error occurred: {e}' #Handle unexpected exception

# This improved version explicitly checks the type of the input and handles the potential exception 
# using a try-except block. This makes the function more robust and less prone to unexpected errors.