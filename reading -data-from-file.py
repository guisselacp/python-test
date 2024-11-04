f = open('data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)

# Runnable Example
import re
import collections

text = open('book.txt', 'r').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))

# Challenge
def get_content(file):
    f = open(file, 'r')
    read = f.read()
    f.close()
    return(read)
lyrics = get_content("lyrics.txt")    
print(lyrics)
