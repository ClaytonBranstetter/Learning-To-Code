from Browser import Browser

class Executive:
    def __init__(self, file):
        """read the file"""
        with open(file) as f:
            self.commands = f.read().split('\n')
    
    def run(self):
        """run file commands"""
        browser = Browser()
        for line in self.commands:
            l = line.split()
            command = l[0].upper()
            if  command== 'NAVIGATE':
                browser.navigate_to(l[1])
            elif command == 'BACK':
                browser.back()
            elif command == 'FORWARD':
                browser.forward()
            elif command == 'HISTORY':
                browser.history()
                print()

file = input('Enter the file : ')
Executive(file).run()