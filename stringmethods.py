a="apple"
print(a)
print(len(a))
print(a.upper())
print(a.lower())

# b.rstrip() removes trailing character from the end but not from beginning
b="!!banana!!!!!!"
print(b.rstrip("!"))

# .replace(...... , ......)
print(b.replace("!","&"))

# .capitalize()
print(a.capitalize())

# .center() centers the string in the given space area
print(a.center(100))

# .count(....)
print(b.count("!"))

# .endswith(....)
print(b.endswith("!"))

# .find(....)
print(b.find("n"))

# .isalnum()
print(b.isalnum())