var1 = 'Hello World!'
var2 = "Python Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])
print('a' in var1, 'P' in var2)
print(r'\n', R'\t')

print("My name is %s and weight is %d kg!" % ('Zara', 21))

var3 = '''Hello,
I'm 
triple 
quotes'''

print(var3)

var4 = "The index is: " + str(5)
var5 = "The index is: {index}".format(index=5)
print(var4, var5)
