

class Test:

    teller = 100


class Test2:

    def __init__(self):
        pass

    def method(self):
        print("Methode zonder parameters")

    def method(self, param):
        print(f"Methode met param : {param}")


if __name__ == "__main__":
    t2 = Test2()

    t2.method()
    t2.method("yow")
