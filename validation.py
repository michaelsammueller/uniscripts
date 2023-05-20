# Function to validate integers
def validate_integer(variable):
    try:
        int(variable)
        return True
    except TypeError:
        return False

def are_you_sure(answer):
    if answer == "Yes" or answer == "Y" or answer == "yes" or answer == "y":
        return True
    elif answer == "No" or answer == "N" or answer == "no" or answer == "n":
        return False
    else:
        print("Invalid answer. Try again.")
        are_you_sure(answer)