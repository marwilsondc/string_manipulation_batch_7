#define index_alt(string: str, val: str, start: int = 0, end: int = 999999) -> int:
def index_alt(string: str, val: str, start: int = 0, end: int = 999999) -> int:

    #initialize index_count, pause_count, compare_val
    index_count = 0
    pause_count = 0
    compare_val = ""

    #under function, create for loop to iterate through string according to parameters
    for i in string[start:end:1]:

        #within for loop, create if statement to evaluate whether i is in val
        if i in val:
            
            #if above statement is True, pass through another if statement that evaluates whether val starts with compare_val
            if val.startswith(compare_val + i):

                #if nested if statement is True, another if statement that evaluates whether compare_val == val
                if compare_val == val:

                    #if above nested statement is True, return index_count
                    return index_count
                
                #outside nested statement, continue to else, add 1 to pause_count
                else:
                    pause_count += 1
                
                continue
            
            #else, reset compare_val
            else:
                compare_val = ""

            #if above statement is True, add i to compare_val
            compare_val += i 
            

        #outside initial if statement, continue to else, reset compare_val and add pause_count to index_count, reset pause_count, and add 1 to index_count
        else:
            compare_val = ""
            index_count += pause_count
            pause_count = 0
            index_count += 1
            continue
    
#tester
user_string = input("input a string: ")
user_val = input("input a value to evaluate string with: ")

print(index_alt(user_string, user_val))
print(user_string.index(input("input a value to evaluate string with: ")))