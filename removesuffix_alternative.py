#define removesuffix_alt(string: str, suffix: str) -> str:
def removesuffix_alt(string: str, suffix: str) -> str:

    #initialize suffix_len, compare_suffix, new_string, index_count, and done_flag
    suffix_len = len(suffix)
    string_len = len(string)
    compare_suffix = ""
    new_string = ""
    index_count = 0
    done_flag = False

    #create a for loop to iterate through string from end to start
    for i in string[string_len::-1]:

        #within for loop, create if statement that evaluates whether i is alpha
        if i.isalpha():

            #if above statement is True, add i to compare suffix
            compare_suffix = i + compare_suffix

            #within initial if statement, create another if statement that evaluates if index_count is greater than len(suffix) and compares compare_suffix and suffix
            if index_count > suffix_len and compare_suffix == suffix:
                
                #if above statement is True, add all remaining characters to new_string
                done_flag = True
                new_string += i
                continue 
            
            #then add 1 to index_count
            index_count += 1
        
        #outside initial if statement, continue elif: evaluate whether done_flag is True, then add i to new_string (for whitespaces)
        elif done_flag:
            new_string += i
            continue
        
        #outside initial if statement, continue to elif: to evaluate whether first iteration is a space or symbol AND whether done_flag false
        elif done_flag == False:

            #if above elif is True, return string
            return string
        
#return new_string
    return new_string

#tester
user_string = input("input a string: ")
to_remove = input("input suffix to remove: ")

print(removesuffix_alt(user_string, to_remove))