

a = 2
b = "sfsf"


def print_hello():
    import secondmodule
    print(secondmodule.c)
    pass

def modify_value():
    import secondmodule
    secondmodule.c = 15

str = []

for i in range(3):
    str.append("i: ")

print("\n".join(str))