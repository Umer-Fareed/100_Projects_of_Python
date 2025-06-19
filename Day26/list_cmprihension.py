#old method
numbers= [1,2,3]
new_list = []
for n in numbers:
    add_1= n+1
    new_list.append(add_1)
print(new_list)

#list comprihension
new_lists= [n+1 for n in numbers]
print(new_lists)

#2
name= "Angela"
name_list= [ letter for letter in name]
print(name_list)

#3
new_range= [n*2 for n in range(1,5)]
print(new_range)

