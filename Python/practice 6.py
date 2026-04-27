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