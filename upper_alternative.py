#define upper_alt(string: str) -> str:
def upper_alt(string: str) -> str:

    #within function, initialize new_string
    new_string = ""

    #then, create a for loop to iterate through string
    for i in string:

        #within for loop, create an if statement to evaluate whether i is lowercase
        if i.islower():

            #if above statement is True, add i to new_string in uppercase through swapcase
            new_string += i.swapcase()

        #else (uppercase, symbol, or whitespace), add i to new_string
        else:
            new_string += i

    #outside for loop, return new_string
    return new_string

#tester
user_string = input("input a string to use upper on: ")

print(upper_alt(user_string))
