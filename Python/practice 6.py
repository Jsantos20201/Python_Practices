def countGreater(nums, k):
    count = 0

    for num in nums:
        if num > k:
            count += 1
    return count
    
print(countGreater([1,5,7,2,9], 5))

''''''
def reverseString(s):
    reversed_str = ""
    for letter in s.lower():
        reversed_str = letter + reversed_str
    return reversed_str

print(reverseString("hello"))
''''''
def evenIndexValues(nums):
    even_list = []

    for num in range(len(nums)):
        if num % 2 == 0:
            even_list.append(nums[num])
    return even_list

print(evenIndexValues([10, 20, 30, 40, 50]))
''''''
def removeDuplicates(nums):
    new_list = []

    for num in nums:
        if num not in new_list:
            new_list.append(num)

    return new_list
print(removeDuplicates([1,2,2,3,1]))
''''''
def mostFrequentChar(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    # Start by saying: we don't know the max yet
    max_char = None       # this will store the character with highest count
    max_count = 0         # this stores the highest count seen so far

    # Loop through each character in the dictionary
    for char in counts:
        # Check if this character's count is bigger than the current max
        if counts[char] > max_count:
            # If it is bigger, update the max count
            max_count = counts[char]
            # Also update which character has that max count
            max_char = char
    # After checking all characters, return the one with highest count
    return max_char
print(mostFrequentChar("banana"))