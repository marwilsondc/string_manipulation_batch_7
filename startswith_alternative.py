#define startswith_alt(string: str, val: str, start: int = 0, end: int = len(string)) -> str:
def startswith_alt(string: str, val: str, start: int = 0, end: int = len):

    #initialize index_count, comparator, value_len
    index_count = 0
    comparator = ""
    value_len = len(val)

    #create for loop to iterate through string according to parameters
    for i in string[start:end:1]:

        #within for loop, create if statement to evaluate whether index_count is equal to value_len and comparator is equal to value
        if index_count == value_len and comparator == val:

            #if above statement is True, return True
            return True
        
        #elif, evaluate if index_count is <= value_len and i is in value
        elif index_count <= value_len and i in val:

            #if above statement is True, add i to comparator, add 1 to index_count, and continue
            comparator += i
            index_count += 1

        #else, return False
        else:
            return False
