'''
Fix the regular expression used in the rearrange_name function
so that it can match middle names, middle initials, as well as double surnames.
'''

import re
def rearrange_name(name):
  #result = re.search(r"^(\w*), (\w*\s\w*.)$", name)
  '''
  Oops! We made a small error. Un-escaped, the dot in this expression will match any character.
  In this case it makes the code work, but it is incorrect! Since we wanted to match the dot character specifically,
  we should have escaped the dot in the regular expression. The correct regular expression should be:
  "^([\w \.-]*), ([\w \.-]*)$"
  '''
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)