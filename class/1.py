import re

def is_phone_number(text):
    if len(text)!=

message=""
for i in range(len(message)):
    chunk=message[i:i+12]
    if is_phone_number(chunk):
        print(""+chunk)
print("")

phone_number_regex=re.compiler(r'\d\d\d-\d\d\d-\d\d\d\d')
mo =phone_number_regex.serch(message)
print(""+mo.group())
