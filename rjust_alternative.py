#define rjust_alt(string: str, val: int, char: str = " ") -> str:
def rjust_alt(string: str, val: int, char: str = " ") -> str:

    #initialize new_string == string, new_string_len = len(new_string)
    new_string = string
    new_string_len = len(new_string)

    #create while loop to evaluate 
    #bug: endless loop
    while new_string_len < val:

        #within while loop, add whitespaces to new_string
        new_string = char + new_string

    #outside while loop, return new_string
    return new_string

#tester
user_string = input("input a string to use rjust on: ")
user_val = int(input("input a value for padding: "))

print(rjust_alt(user_string, user_val))
print(rjust_alt(user_string, user_val, "0"))
