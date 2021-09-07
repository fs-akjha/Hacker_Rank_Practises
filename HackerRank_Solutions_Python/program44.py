import re

string_input=input()
k_string=input()

pattern = re.compile(k_string)
r = pattern.search(string_input)
if not r: 
    print ("(-1, -1)")
while r:
    print ("({}, {})".format(r.start(), r.end() - 1))
    r = pattern.search(string_input,r.start() + 1)