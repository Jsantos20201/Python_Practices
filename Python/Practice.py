generated_words = ["AI", "ML", "AI","ML", "Data"]

def count_ai(words):
    seen = set()
    count = set()
    for word in words:
        if word in seen:
            count.add(word)
        seen.add(word)
    return count, len(count)

dupes, count = count_ai(generated_words)
print(f"Duplicate Found: {dupes}")
print(f"Count: {count}")


numbers_list = [1,2,3,4,5,6,7,8,9,10]
evens = []

def get_evens(nums):
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(get_evens(numbers_list))

def revrse_string(s):
    reversed_str = ""

    for char in s:
        reversed_str = char + reversed_str

    return reversed_str

def reverse_string(s):
    reversed_str = ""
    
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    
    return reversed_str

word = revrse_string("Hello")
print(word)


def first_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

print(first_duplicate([3, 1, 4, 2, 1]))

def word_count(sentence):
    words = sentence.split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else: 
            counts[word] = 1
    return counts

print(word_count("AI is the future and AI is powerful"))

"""Another way"""
def word_count_2(sentence):
    counts = {}
    
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
        
    return counts