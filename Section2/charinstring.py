my_string="This is DYPIEMR ENTC"

#using count
print(my_string.count("E"))

#using for loop
count=0
for i in my_string:
    if i=="E":
        count+=1

print(count)

#Using counter
from collections import Counter
char_to_search="E"
count=Counter(my_string)
print(count[char_to_search])