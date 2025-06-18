text = "Hello world from Python"
words = text.split() # splits on space by default
words.reverse()
result = ' '.join(words)
print(result)  

#stack
text = "Hello world from Python"
stack = []
word = ""
result = ""

# Step 1: Extract words manually and push to stack
for ch in text:
    if ch != ' ':
        word += ch
    else:
        if word:
            stack.append(word)
            word = ""
if word:
    stack.append(word)

result = []
while stack:
    result.append(stack.pop())

print(' '.join(result)) 

#Optimal without stack
text = "Hello world from Python"
i = len(text) - 1
result = ""
while i >= 0:
    if text[i] == ' ':
        i -= 1
        continue
    word = ""
    while i >= 0 and text[i] != ' ':
        word = text[i] + word
        i -= 1
    if result == "":
        result = word
    else:
        result += " " + word
print(result)
