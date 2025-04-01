#define rindex_alt(string: str, value: str, start: int, end: int) -> int:
#initialize index_count, compare_val, pause_count
#within function, create for loop to iterate from end to start according to parameters
#within for loop, create if statement to evaluate whether value ends with compare_val
#if above statement is True, add i to compare_val
#if above statement is True, create another if statement to evaluate whether compare_val == value
#if nested if statement is True, return (len(string) - 1) - (index_count + 1)
#else, add 1 to pause_count
#outside initial if statement, continue to else, if True, reset compare_val, add i to compare_val, if pause_count: add pause_count to index_count, reset pause_count, and add 1 to index_count