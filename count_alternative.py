#define count_alt(string: str, value: str, start: int, end: int) -> int:
#initialize final_count, compare_value
#create a for loop to iterate through string according to parameters
#within for loop, create if statement that evaluates whether i is in value
#if above statement is True, add i to compare_value and set another if statement that evaluates whether compare_value == value
#if nested if statement is True, add 1 to final_count
#outside nested if statement, continue iteration
#outside initial if, continue else (for characters not included in value), if True, reset compare_value and continue iteration