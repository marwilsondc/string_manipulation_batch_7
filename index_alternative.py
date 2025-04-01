#define index_alt(string: str, val: str, start: int = 0, end: int = 999999) -> int:
def index_alt(string: str, val: str, start: int = 0, end: int = 999999) -> int:
    index_count = 0
    pause_count = 0
    compare_val = ""

    #inside function, create for loop to iterate through string according to parameters
    for i in string[start:end:1]:

        #inside for loop, create if statement that evaluates whether val starts with compare_val
        if val.startswith(compare_val + i):

            #if above statement is True, add i to compare_val
            compare_val += i

            #if above statement is True, pass through another if statement that evaluates whether compare_val is equal to val, if True, return index_count
            if compare_val == val:
                return index_count + start
            
            #outside nested if statement, continue to else, if True, add 1 to pause_count
            else:
                pause_count += 1
            
            continue
        
        #outside initial if statement, continue to else.
        else:
            
            #if else is True, pass through another if statement that evaluates whether pause_count has a value. If True, add pause_count - 1 to index_count
            if pause_count:
                index_count += pause_count - 1

            #if else is True, reset compare_val, add new iteration to it, reset pause_count, and add 1 to index_count
            compare_val = ""
            compare_val += i
            pause_count = 0
            index_count += 1
            continue
    
#tester
user_string = input("input a string: ")
user_val = input("input a value to evaluate string with: ")

print(index_alt(user_string, user_val, 3))
print(user_string.index(input("input a value to evaluate string with: "), 3))