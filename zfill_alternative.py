#define zfill_alt(string: str, len: int) -> str: 
def zfill_alt(string: str, length: int) -> str:

    #initialize new_string = string
    new_string = string

    #create while loop to compare len(new_string) with len
    while len(new_string) < length:

        #inside while loop, add "0" to new_string
        new_string = "0" + new_string

    #outside while loop, return new_string
    return new_string

#tester
user_string = input("input a string: ")
user_val = int(input("input the desired length of new string: "))

print(zfill_alt(user_string, user_val))