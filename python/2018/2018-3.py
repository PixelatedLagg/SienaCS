word = str(input())
words_found = []
def is_palindrome(w):
    for i in range(len(w)):
        if i >= len(w) - i - 1:
            return True
        if w[i].lower() != w[len(w) - i - 1].lower(): #case insensitive
            return False

for i in range(len(word)):
    j = 0
    continue_i_loop = False
    while len(word) - j != i:
        if is_palindrome(word[i:len(word) - j]):
            words_found.append(word[i:len(word) - j])
            continue_i_loop = True
            break
        j += 1
    if continue_i_loop == True:
        continue

if len(words_found) == 1:
    print(words_found[0])
    exit()
max_length = len(max(words_found, key=len))
new_words_found = []

for w in words_found:
    if len(w) == max_length:
        new_words_found.append(w)

new_words_found.sort()
print(new_words_found[0])