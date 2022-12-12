# import re
#
# class PhoneMatched:
#
#     def __init__(self, phone):
#         self.exception = re.finditer(r"\+359([ |-])[1-9]\1[1-9]{3}\1[1-9]{4}\b", phone)
#         self.the_gsm = []
#
#         for phone in self.exception:
#             self.the_gsm.append(phone.group())
#
#
#     def __repr__(self):
#         return ", ".join(self.the_gsm)
#
#
# phones = input()
# phone = PhoneMatched(phones)
#
# print(phone)

import re

pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
phone = input()
exception = re.findall(pattern, phone)

print(", ".join(exception))


