menu = ['eggs', 'bacon', 'spam', 'spam']
print(menu)
print(menu.count('spam'))
print(menu.count('eggs'))
print(menu.index('eggs'))
print(menu.reverse())
print(menu)
print(menu.append('lobster thermidor'))
print(menu)
print(menu.sort())
print(menu)
print(menu.pop())

# Challenge
crew = ["Jean-Luc", "Wesley", "Warf", "Deanna", "William", "Data", "Geordie", "Tasha"]
print(crew)
crew.pop()
print(crew)
crew.append("Beverly")
print(crew)
crew.extend(["Miles", "Guinan"])
print(crew)
crew.sort(key=len, reverse=True)
print(crew)