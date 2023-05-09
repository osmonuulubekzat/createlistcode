class Main:
    def __init__(self, name) -> None:
        self.name = name
        self.number = 0
        self.status = True

    def Show(self):
        pass

    def Write(self, name, lastname, n):
        with open("test.txt", "a") as file:
            file.write(str(n) + ")" + name.capitalize() + " " + lastname.capitalize() + "\n")

    def Delete(self):
        pass

    def Update(self):
        pass

    def Exit(self):
        pass

    def Current_position(self):
        with open("test.txt", "r") as test:
            t = test.readlines()
            if len(t) == 0:
                return 0
            else:
                number = t[-1].split(")")
                return number[0]

MainOne = Main("Asiya")
number = int(MainOne.Current_position())
while MainOne.status:
    number += 1
    name = input("enter name: ")
    lastname = input("enter lastname: ")
    MainOne.Write(name, lastname, number)
    enter = input("if you want to exit enter Y or to continue N: ")
    if enter == "y":
        MainOne.status = False




