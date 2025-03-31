#define rjust_alt(string: str, val: int, char: str = " ") -> str:
def rjust_alt(string: str, val: int, char: str = " ") -> str:

    #initialize new_string == string, new_string_len = len(new_string)
    new_string = string
    new_string_len = len(new_string)

    #create while loop to evaluate new_string_len
    while new_string_len < val:

        #within while loop, add whitespaces to new_string
        new_string = " " + new_string

    #outside while loop, return new_string
    return new_string
