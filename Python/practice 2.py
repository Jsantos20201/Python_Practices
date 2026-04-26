def countMultiples(n):
    nums = []

    for i in range(1, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            nums.append("EvenThree")
        elif i % 2 == 0:
            nums.append("Even")
        elif i % 3 == 0:
            nums.append("Three")
        else:
            nums.append(i)
    return nums

print(countMultiples(6))

''''''

def countWords(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

words = ["apple", "banana", "apple", "orange", "banana", "apple"
]

print(countWords(words))

''''''

def findMissing(nums):
    s = set(nums)
    for i in range(1, len(nums) + 2):
        if i not in s:
            return i
        
print(findMissing([1, 2, 4, 5]))

''''''

def longestWord(sentence):
    words = sentence.split()
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longestWord("I love programming in Python"))

''''''
def filterNumbers(nums):
    results = []

    for num in nums:
        if num > 10 and num % 2 == 0:
            results.append(num)
    
    return results

print(filterNumbers([1, 2, 5, 13, 20, 100]))

""""""
def isPalindrome(s):
    s = s.lower().replace(" ", "")
    reserved_str = ""

    for char in s:
        reserved_str = char + reserved_str

    return s == reserved_str

print(isPalindrome("Race car"))
print(isPalindrome("never odd or even"))
print(isPalindrome("No lemon no melon"))
print(isPalindrome("A man, a plan, a canal: Panama"))

""""""
def firstUniqueChar(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    for char in s:
        if counts[char] == 1:
            return char
        
    return None

print(firstUniqueChar("leetcode"))
""""""

""""""
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i

print(twoSum([2,7,11,15], 9))
""""""

def maxDifference(nums):
    min_num = nums[0]
    max_diff = 0
    
    for num in nums:
        if num < min_num:
            min_num = num
        else:
            diff = num - min_num
            if diff > max_diff:
                max_diff = diff
    return max_diff

print(maxDifference([2, 3, 10, 6, 4, 8, 1]))
print(maxDifference([7, 1, 5, 3, 6, 4]))