#define islower_alt(string: str) -> bool:
def islower_alt(string: str) -> bool:

    #initialize str_comparator
    str_comparator = string.lower()

    #create if statement to evaluate whether string is the same as str_comparator
    if string == str_comparator:
        
        #if above statement is True, return True
        return True
    
    #else, return False
    else:
        return False
    

