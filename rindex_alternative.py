#define rindex_alt(string: str, value: str, start: int, end: int) -> int:
def rindex_alt(string: str, value: str, start: int = None, end: int = None) -> int:

    #initialize index_count, compare_val, pause_count, and start
    compare_val = ""

    #within function, create for loop to iterate from end to start according to parameters
    for i in string[end:start:-1]:

        #within for loop, create if statement to evaluate whether value ends with compare_val
        if value.endswith(i + compare_val):

            #if above statement is True, add i to compare_val
            compare_val = i + compare_val

            #if above statement is True, create another if statement to evaluate whether compare_val == value
            if compare_val == value:

                #if nested if statement is True, evaluate whether start and end are none types
                if start == None and end == None:
                    return string.rfind(value)
                
                elif start and end != None:
                    return (len(string[:end:1]) - string[end:start:-1].rfind(value))
            
            continue
    
        #outside initial if statement, continue to else, if True, reset compare_val, add i to compare_val if length of value is not 1
        else: 
            compare_val = ""

            #if length of value is not equal to 1, do not add past iterations to compare_val
            if len(value) != 1:
                compare_val = i + compare_val

            continue

#tester
user_string = input("input a string to evaluate: ")
user_val = input("input a value to evaluate string on: ")
user_start = int(input("input start value: "))
user_end = int(input("input end value: "))

print(rindex_alt(user_string, user_val, user_start, user_end))
print(user_string.rindex(user_val, user_start, user_end))