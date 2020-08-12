import re
def convert_phone_number(phone):
  #pattern = r"([\w ]+)([\d{3}]-[\d{3}]-[d{4}])"
  #pattern = r"([\w ]+)([\d-]+)"
  if not re.search("( [\d]{3}-[\d]{3}-[\d]{4})",phone):
    return phone

  #i = re.search("( [\d]{3}-[\d]{3}-[\d]{4})",phone).span()[0]
  #np = "(" + phone[i+1:i+4] + ") " + phone[i+5:i+13]
  #print('i value is {}, np value is {}'.format(i, np))
  #print("abc value and type is {} {}".format(abc, type(abc)))
  #pattern = r"([a-zA-Z ]+)([+ \d-]+)"
  pattern = r"([a-zA-Z ]+)([\d]{3})([\d -]+)"
  result = re.sub(pattern,r"\1 (\2) \3",phone)
  #print("result to list = {}".format(result.split('-')[0]))
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300