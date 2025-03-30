#define rstrip_alt(str)
def rstrip_alt(string):

    #initialize string_len
    str_len = len(string)

    #create a for loop to iterate through string from end to start
    for i in string[str_len::-1]:

        #within for loop, create an if statement to evaluate whether i is a whitespace
        if i.isspace():

            #if above statement is True, replace i with none
            string = string.replace(i, "", -1)

        #elif i is an alphabet or any other symbol, break loop
        else:
            break

    #outside for loop, return str
    return string

user_string = input("input a string with several spaces after text: ")
print(rstrip_alt(user_string))