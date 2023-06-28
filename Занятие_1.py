def check(word):
    if word[::-1] == word:
        return True
    else:
        return False

print(check("привет"))