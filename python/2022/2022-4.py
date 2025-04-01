target = input()
num_guesses = int(input())
guesses = []

for i in range(num_guesses):
    guesses.append(input())

for word in guesses:
    output = ['D', 'D', 'D', 'D', 'D']
    yellow_letter_count = {c: target.count(c) for c in target}
    yellow_letter_placement = []

    for i in range(5):
        if word[i] == target[i]:
            output[i] = 'G'
            yellow_letter_count[word[i]] -= 1

    for i in range(5):
        if output[i] != 'G' and word[i] in target and yellow_letter_count[word[i]] > 0:
            output[i] = 'Y'
            yellow_letter_count[word[i]] -= 1

    print(''.join(output))