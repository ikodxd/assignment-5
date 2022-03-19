#task 1
s = input("Enter your string: ")
b = s.find("a")
if b == -1:
    print("False")
else: 
    print("True")


#task 2
import re

stroka = input("enter the string: ")
poisk = 'abb|abbb'
if re.search(poisk, stroka):
    print("True")
else:
    print("False")
    
    
#task 3
import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))


#task 4
import re
def text_match(text):
        patterns = '^[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("Python"))
print(text_match("python"))


#task 5
import re
def text_match(text):
        patterns = '^a.*b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aa"))
print(text_match("ab"))
print(text_match("afkdjdnwfk"))
print(text_match("afkdjdnwfkb"))


#task 6
import re
text = 'Hello, my name is Danil.'
print(re.sub("[ ,.]", ":", text))


#task 7
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('hello_world!'))


#task 8
s = input("Enter your string: ")
i = 0
while i < len(s):
    if s[i] == ' ':
        i += 1
        print(s[i].upper(), end="")
    else:
        print(s[i], end="")
    i+=1
    
    
#task 9
s = input("Enter your string: ")
for i in range(len(s)):
    if s[i].isupper():
        print(' ' + s[i], end="")
    else:
        print(s[i], end="")


#task 10
import re

string = 'HelloWorld!'
string = re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
print(string)   
