with open("story.txt", "r") as f: #opening text file
    story = f.read()

words = set() #word is set because we don't want duplicates
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story): #allows to locate positions of brackets 
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ") #asking for user input
    answers[word] = answer
for word in words:
    story = story.replace(word, answers[word]) #finding the brackets and

print(story)