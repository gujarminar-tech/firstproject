my_string="Hello friend i am Om Mane"

#using for loop
newstr=""
for a in my_string:
    newstr=a+newstr
print(newstr)

#using reversed funtion
reversed_str="".join(reversed(my_string))
print(reversed_str)