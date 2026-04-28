def countBetween(nums, low, high):
    count = 0
    for num in nums:
        if num >= low and num <= high:
            count += 1
    return count

print(countBetween([1, 5, 10, 15, 20], 5, 15))
''''''
def doubleEvens(nums):
    store = []

    for num in nums:
        if num % 2 == 0:
            store.append(num * 2)
        else:
            store.append(num)
    return store
print(doubleEvens([1, 2, 3, 4]))
''''''
def countWords(sentence):
    word_count = {}

    for word in sentence.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(countWords("cat dog cat"))
''''''

def lastUnique(s):
    char_dic = {}

    for char in s:
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1

    for char in reversed(s):
        if char_dic[char] == 1:
            return char
    return None
print(lastUnique("aabbcde"))
''''''
def inventoryTracker(transactions):
    stock = {}

    for transaction in transactions:
        action, item, quantity = transaction.split()
        quantity = int(quantity)
        if quantity < 0:
            return [-1]
    
        if action == "remove":
            if item not in stock or stock[item] < quantity:
                return [-1]
            stock[item] -= quantity
        elif action == "add":
            stock[item] = stock.get(item, 0) + quantity
    result = []
    for item in sorted(stock):
        result.append(stock[item])
    return result