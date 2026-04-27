def countsOdds(nums):
    counts = 0

    for num in nums:
        if num % 2 != 0:
            counts += 1
    
    return counts

print(countsOdds([1, 2, 3, 4, 5]))

''''''
def sumPositive(nums):
    total = 0 

    for num in nums:
        if num > 0:
            total += num
        
    return total

print(sumPositive([-5, 0, 2, 4, -3]))
''''''
def findMax(nums):
    return max(nums)

'''Manual'''
def findMax2(nums):
    max_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num
    
    return max_num

print(findMax([-2, 0, -30, 50, 20]))
print(findMax2([-2, 0, -30, 50, 20]))
''''''

def longWords(words):
    word_list = []

    for word in words:
        if len(word) > 5:
            word_list.append(word)
    
    return word_list
print(longWords(["cat", "dog", "elephant"]))
""""""

def removeNegatives(nums):
    num_list = []

    for num in nums:
        if num > 0:
            num_list.append(num)
    
    return num_list

print(removeNegatives([-3, 5, -1, 7, 0]))
''''''
def countNums(nums):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return count

def countNums2(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    return count

print(countNums([1,2,2,4]))
''''''
def firstDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    
    return None
print(firstDuplicate([1, 2, 3, 2, 4]))