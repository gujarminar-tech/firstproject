#if
# age=18
# if age > 18:
#     print("Adult")
# elif age==18:
#     print("Becoming Adult")
# else:
#     print("Minor")

# num1=17
# status=False
# if num1>18:
#     status=True


#for loop
# my_list=["a","b","c"]
# for i in range(len(my_list)):
#     print(i) 

# for i in my_list:
#     print(i)

# for i,v in enumerate(my_list):
#     print(i,v)

# my_dist={
#     "name":"Om",
#     "age":21,
#     "gender":"male"
# }

# for i in my_dist.keys():
#     print(my_dist.values())

# for i in range(10):
#     if i ==5:
#         print("Hello")
#         break
#     print(i)

for i in range(10):
    if i ==5:
        continue
    print(i)