'''
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters
(including letters, numbers, and underscores) separated by one or more whitespace characters.
'''

import re
def check_character_groups(text):
  result = re.search(r"[\w]+ [\w]+", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs."))

'''
Fill in the code to check if the text passed looks like a standard sentence, 
meaning that it starts with an uppercase letter, followed by at least some 
lowercase letters or a space, and ends with a period, question mark, or exclamation point.
'''

def check_sentence(text):
  result = re.search(r"^[A-Z][a-z]* [a-z]+", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


'''
The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). 
Fill in the regular expression to do that.
'''

import re
def multi_vowel_words(text):
    pattern = r"[\w]*?[aeiouAEIOU]{3}?[\w]*"
    result = re.findall(pattern, text)
    return result

print(multi_vowel_words("Life is beautiful"))



'''
transform record the US Phone numbers preceeding with +1
st = "+1-"
new_record = re.sub(r"\b(\d{3}-\d{3}-?\d{4})\b ",st+r"\1",record)
'''
import re
def transform_record(record):
    # if below line not working then use the above expression(st = "+1-") from comments
  new_record = re.sub(r"\b(\d{3}-\d{3}-?\d{4})\b", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer