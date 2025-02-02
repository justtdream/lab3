def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    reversed_snt = ' '.join(words)
    return reversed_snt
users = input("Enter sentence: ")
print(reverse_words(users))
