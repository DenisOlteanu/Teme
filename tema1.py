my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list.sort()
print(my_list)

my_list2 = [-5, 0, 4, 2, 53, -1, 54, 2]
my_list2.sort()
print(my_list2)

my_list3 = [3,123,53,2,1,354,43,512]
my_list3.sort(reverse=True)
print(my_list3)

my_list4 = [10, 21, 4, 45, 66, 93]

pare = [numere for numere in my_list4 if numere % 2 == 0]
impare=[numere for numere in my_list4 if numere % 2 == 1]
print(pare)
print(impare)


my_list5= [3,13,2,4,51,2,424,123,444,9]
multiplu3=[x for x in my_list5 if x % 3 == 0]
print(multiplu3)




