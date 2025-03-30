#define removesuffix_alt(string: str, suffix: str) -> str:
#initialize suffix_len, compare_suffix, new_string, index_count, and done_flag
#create a for loop to iterate through string from end to start
#within for loop, create if statement that evaluates whether i is alpha
#if above statement is True, add i to compare suffix
#within initial if statement, create another if statement that evaluates if index_count is greater than len(suffix) and compares compare_suffix and suffix
#if above statement is True, add all remaining characters to new_string
#outside initial if statement, continue to elif: to evaluate whether i is a space or symbol AND whether done_flag false
#return new_string
