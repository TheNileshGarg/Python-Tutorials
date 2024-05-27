# We are writing a function to transform a string written in simple english language to some secret 
# language 

##  Coding

#  change a to e, e to i and so on ... 
# leave consonants unchnged 
# add 4 char both to left and right of it 
# revrse the string 

## Decoding 
# Reverse string 
# remove 4 char on each side 
# bring vowels back to norm 


def vowel_code(ch):
    vowels = "aeioua"
    if ch in vowels:
        return vowels[vowels.index(ch) + 1]
    # if a comes it will go to e only here , and so for others 
def vowel_decode(ch):
    vowels = "aeiou"
    if ch in vowels:
        return vowels[vowels.index(ch) - 1]
    # others are normally doing job, in case of it gives -1 which again gives u 

def coder(text):
    text1 = ""
    for a in text:
        if a in "aeiou":
            text1 += str(vowel_code(a))
        else:
            text1 += str(a)

    # adding random char
    import random
    import string

    letters = string.ascii_lowercase  
    forward = ''.join(random.choice(letters) for _ in range(4))
    backward = ''.join(random.choice(letters) for _ in range(4))
    text1 = forward + text1 + backward
    
    text2 = list(text1)
    text2.reverse()
    text1 = ''.join(text2)

    return text1

def decoder(text):
    text1 = list(text)
    text1.reverse()
    text = ''.join(text1)

    text = text[4:-4]

    text1 = ""
    for a in text:
        if a in "aeiou":
            text1 += str(vowel_decode(a))
        else:
            text1 += str(a)
    return text1

s1 = coder("iamgoodboy")
print(s1)

s2 = decoder(s1)
print(s2)