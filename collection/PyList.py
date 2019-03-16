
#列表的数据项不要求有相同的类型
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print(list1[-2:-1])
list1[1:3] = ("math", 1000)
print(list1)

#动态追加内容
list_dy1 = []
for i in range(5):
    list_dy1.append("i{index}".format(index=i))

print(list_dy1)

#list_dy1.remove('i2')
del list_dy1[2]
print(list_dy1)

