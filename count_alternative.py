#define count_alt(string: str, value: str, start: int, end: int) -> int:
def count_alt(string: str, value: str, start: int = 0, end: int = 999999) -> int:

    #initialize final_count, compare_value
    final_count = 0
    compare_value = ""

    #create a for loop to iterate through string according to parameters
    for i in string[start:end:1]:

        #within for loop, create if statement that evaluates whether i is in value
        if i in value:

            #if above statement is True, add i to compare_value and set another if statement that evaluates whether compare_value == value
            compare_value += i

            if compare_value == value:

                #if nested if statement is True, add 1 to final_count
                compare_value = ""
                final_count += 1

            #outside nested if statement, continue iteration
            continue
        
    #outside initial if, continue else (for characters not included in value), if True, reset compare_value and continue iteration
        else:
            compare_value = ""
            continue
    
    return final_count

#tester
user_string = input("input a string: ")
user_value = input("input value to count: ")

print(count_alt(user_string, user_value))