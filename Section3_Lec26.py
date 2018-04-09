import re

string = "'I AM YELLING',she said 'we know it'"
print(string)
new = re.sub('','',string)
print(new)
new = re.sub('[A-Z]','',string)
print(new)
new = re.sub('[a-z]','',string)
print(new)
new = re.sub('[''"",]','',string)
print(new)
new = re.sub('[" "]','',string)
print(new)
string = string + "92654"
new = re.sub('[A-Za-z]','',string)
print(new)