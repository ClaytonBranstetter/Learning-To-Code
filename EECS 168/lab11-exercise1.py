'''
Author: Clayton Branstetter
KUID: 3089206
Date: 11/30/2021
Lab: lab#10
Last modified: 11/30/2021
Purpose: Class & List for DMV
'''

"""with open("records.txt" ,"r") as file:
    f = file.read()
    for row in f.split("\n"):
        print(row.split('\t'))
"""


class DriversLicense:
    def __init__(self, data):
        _data = data.split("\t")
        self._l_number = int(_data[0])
        self._f_name = _data[1]
        self._l_name = _data[2]
        self._age = int(_data[3])
        self._registered = _data[4]

    def __eq__(self, other):
        return self._l_number == other._l_number

    def __ne__(self, other):
        return self._l_number != other._l_number

    def __str__(self):
        return f"{self._f_name}, {self._l_name} ({self._age }): {self._l_number}"


class DMV:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            data = file.read().split('\n')
            self.n_entries = data[0]
            self.dl = [DriversLicense(row) for row in data[1:]]

    def all_driver(self):
        for driver in self.dl:
            print(driver)

    def young_uv(self):
        for driver in self.dl:
            if (18 <= driver._age <= 24) and (driver._registered == 'N'):
                print(driver)

    def f_initial(self):
        letter = input("Enter a single character : ").upper()
        print()
        exist = False
        for driver in self.dl:
            if driver._f_name[0] == letter:
                print(driver)
                exist = True
        if not exist:
            print("No record found.")

    def by_id(self):
        id = int(input("Enter an id : "))
        print()
        exist = False
        for driver in self.dl:
            if driver._l_number == id:
                print(driver)
                exist = True
        if not exist:
            print("No record found.")

    def menu(self):
        print("\nSelect an option:")
        print("1) Print all Drivers Info")
        print("2) Print all young, unregistered voters")
        print("3) Print drivers by first initial")
        print("4) Print driver with id")
        print("5) Quit\n")
        choice = input("Enter your choice: ")
        print()
        if choice.isdigit() and "1" <= choice <= "5":
            return int(choice)
        return self.menu()

    def run(self):
        choice = self.menu()
        if choice == 5:
            return 0
        if choice == 1:
            self.all_driver()
        elif choice == 2:
            self.young_uv()
        elif choice == 3:
            self.f_initial()
        elif choice == 4:
            self.by_id()
        return self.run()


def main():

    #get the file name from user via terminal
    fileName = input("Enter the filename : ")
    #Hand control over to the DMV
    myDMV = DMV(fileName)
    myDMV.run()


if __name__ == "__main__":
    main()
