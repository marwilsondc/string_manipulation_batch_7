#define rstrip_alt(str)
def rstrip_alt(string):

    #initialize string_len and new_string
    str_len = len(string)
    left_whitespace = ""

    #create a for loop to iterate through string from start to end
    for i in string:

        #within for loop, create an if statement to evaluate whether i is a whitespace
        if i.isspace():

            #if above statement is True, add i to left_whitespace
            left_whitespace += i

        #elif i is an alphabet or any other symbol, break loop
        else:
            break

    #strip the string and combine with left_whitespace
    string = string.strip()
    string = left_whitespace + string

    #outside for loop, return str
    return string

#bug: removes all spaces instead of one
user_string = input("input a string with several spaces after text: ")
print(rstrip_alt(user_string))