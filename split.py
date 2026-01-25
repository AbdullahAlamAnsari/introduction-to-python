s = "one,two,three"
words = s.split(',')
print(words) #return a list of the strings mini ones


word = 'geeks, for, geeks, hello'

print(word.split(', ', 0)) 
print(word.split(', ', 4))  
print(word.split(', ', 1)) # will only split geeks from the main string and will return

text = "Hello geek, Welcome to GeeksforGeeks."

result = text.split()
print(result)