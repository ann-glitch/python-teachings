# Given a list of integers , return True if the sequence of numbers 1,2,3 appears in the list somewhere.

# for example

# array_check([1, 1, 2, 3, 1]) -> True
# array_check([1, 1, 2, 4, 1]) -> True
# array_check([1, 1, 2, 1, 2, 3]) -> True


def array_check(nums):
    for i in range(len(nums) -2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False                   

print(array_check([1, 1, 2, 3, 4, 5]))    


# Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo"

# for example

# stringBits("Hello") -> "Hlo"
# stringBits("Hi") -> "H"
# stringBits("Heeololeo") -> "Hello"

def stringBits(mystr):
    result = ""
    for i in range(len(mystr)):
        if i % 2 == 0:
            result = result + mystr[i]
    return result

print(stringBits("Hello"))   

# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring
# upper and lower case differences (in other words, the computation should not be "case sensitive")

# Note s.lower() returns the lowercase version of a string

# Examples

# end_other("Hiabc", "abc") - True
# end_other("AbC", "HiaBc") - True
# end_other("abc", "abXabc") - True

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    #first
    # return (a.endswith(b) or b.endswith(a))

    #second
    return a[-len(b):] == b or b[-len(a):] == a

print(end_other("AbC", "HiaBc"))    


# Given a string return a string where for every char in the original, there are two chars

# Examples

# double_char("The") -> "TThhee"
# double_char("AAbb") -> "AAAAbbbb"
# double_char("cup") -> "ccuupp"

def double_char(mychar):
    result = ""
    for char in mychar:
        result += char * 2

    return result;

print(double_char("The"))        


# Given 3 int values, a b c, return their sum. However, if any of the values is
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n): "that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent Level as the main no teen sum()
# Again you will have two functions for this problem 

# Examples

# no_teen_sum(1, 2, 3) -> 6
# no_teen_sum(1, 13, 3) -> 4
# no_teen_sum(1, 15, 1) -> 18

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if 13 <= n and n <= 19 and n != 15 and n != 16:
        return 0    
    return n


print(no_teen_sum(1, 15, 1))


# Return the number of even integers in the given array

# Examples

# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0

def count_evens(nums):
    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1
    return count    

print(count_evens([1,2,3,4]))        



    