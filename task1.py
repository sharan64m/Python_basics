# a_list = [1,"333",2,3.44,3+4j]
# for i in a_list:
#     print(i)
# print(a_list[0])
# for i in range(0,2,1):
#     print(i)

# Write a Python program to multiply all the items in a list.


# def list_multiply(items):
#     sum=1
#     for i in items:
#         sum*=i
#     print(sum)
#     return sum
# list_multiply([1,2,2.2,4])

# Write a Python program to get the largest number from a list.

# def list_largest(items):
#      sum=items[0]
#      for i in items:
#         if sum < i:
#          sum=i
#      print(sum)
#      return sum
     
# list_largest([52,5,36,100])








def list_second_largest(items):

    min=items[0]
    lar=items[1]
    # len=items.length
    if min > lar:
        c=lar
        lar=min
        min=c
    print(min)
    print(lar)
    # print(len)
    for i in items:
       if i < lar:
           min=lar
           lar=i
       elif i > min :
           min=i
       
       print(min)
    return min

list_second_largest([52,45,58,455])