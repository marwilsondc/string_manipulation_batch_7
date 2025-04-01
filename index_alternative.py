#define index_alt(string: str, val: str, start: int = 0, end: int = 999999) -> int:
#initialize index_count, pause_count, compare_val
#under function, create for loop to iterate through string according to parameters
#within for loop, create if statement to evaluate whether i is in val
#if above statement is True, pass through another if statement to evaluate whether compare_val == val
#if nested statement is True, return index_count
#outside nested statement, continue to else, add 1 to pause_count
#outside initial if statement, continue to else, add pause_count to index_count, reset pause_count, and add 1 to index_count