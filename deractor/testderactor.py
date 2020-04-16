

def use(name):
    print("name: ", name)
    def one(func):
        print("func: ", func)
        def two(args):
            print("args: ", args)
            func(args)
        return two
    return one

def usetwo(func):
    def one(args):
        func(args)
    return one


@use("a")
def hello(a):
    print("a: " + a)

@usetwo
def helloxxx(a):
    pass
    #print("b: " + str(a))


if __name__ == '__main__':
    hello("haha")
