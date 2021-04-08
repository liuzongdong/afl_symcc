from timeout import timeout

@timeout(5)
def test():
    while True:
        print("Hello")

test()
