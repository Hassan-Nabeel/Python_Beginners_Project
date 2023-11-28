####        Mad lib - Generators        ####

with open('story.txt','r') as f:
    story = f.read()

start = '<'
end = '>'
set = set()
start_of_word = -1

for i, char in enumerate(story):
    if char == start:
        start_of_word = i
    
    elif char == end and start_of_word != -1:
        word = story[start_of_word : i+1]
        set.add(word)
        start_of_word = -1

# print(set)
print()
d = {}
for j in set:
    x = input('Enter a word ' + j + ': ')
    d[j] = x

print()
for j in set:
    story = story.replace(j,d[j])
print(story)