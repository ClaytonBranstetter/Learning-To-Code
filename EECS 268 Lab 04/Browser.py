from LinkedList import LinkedList
class Browser:
    def __init__(self):
        """Initialize Browser"""
        self.navigation = LinkedList()
        self.index = -1

    def navigate_to(self, url):
        """The browser navigate to the given url"""
        n = self.navigation.length
        for _ in range (self.index, n-1):
            self.navigation.remove(self.index + 1)
        self.index += 1
        self.navigation.insert(self.index, url)

    def forward(self):
        """If possible, the browser navigates forward in the history otherwise it keeps focus"""
        if self.index < self.navigation.length-1:
            self.index += 1

    def back(self):
        """If possible, the browser navigates forward in the history otherwise it keeps focus"""
        if self.index > 0:
            self.index -= 1

    def history(self):
        """Returns a well formatted string (see below) with the current history."""
        print("Oldest\n===========")
        navigation = self.navigation
        n = navigation.length
        for i in range(n):
            if i == self.index:
                print(navigation.get_entry(i) + "  <==current")
            else:
                print(navigation.get_entry(i))
        print("===========\nNewest")
