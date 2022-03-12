from BoardGame import BoardGame

class Executive:
    def __init__(self,file_name):
        with open(file_name) as f:#read the file
            rows = f.read().split('\n')
            rows_data = [row.split('\t') for row in rows]
            l = []
            for row in rows_data:
                l.append(BoardGame(name=row[0], year=row[1], GR = row[2], PR=row[3], MP=row[4], MT=row[5])) #create broadgame objects and add them to a list
            self.list_bg = l #list of all broadgame objects

    def all_g(self):
        for game in self.list_bg:
            print(game) #show all broadgames

    def all_g_y(self):
        year = input('Enter the year : ')
        i = 0
        for game in self.list_bg:
            if game.year == year:
                i+=1
                print(game)  #show all games from a year
        if i==0:
            print('No games found')

    def ranking(self):
        start = int(input('Enter the start value : ')) #starting range
        stop = int(input('Enter the stop value : '))
        for game in self.list_bg:
            GR = float(game.GR)
            if start<=GR<=stop:
                print(game)

    def differ(self):
        rating = float(input('Enter a rating : ')) #getting a rating difference
        for game in self.list_bg:
            PR = float(game.PR)
            GR = float(game.GR)
            if abs(GR-PR)>=rating:
                print(game)

    def play_time(self):
        time = int(input('Enter a play time : ')) # getting a play time
        for game in self.list_bg:
            if int(game.MT)<=time: #Print all games that have a min play time of that value or lower
                print(game)

    def menu(self):
        print('\n1-Print all games (same order as from file)')
        print('2-Print all games from a year')
        print('3-Print a ranking range')
        print('4-The People VS Dr. Gibbons')
        print('5-Print based on play time')
        print('6-Exit the program\n')

    def run(self):
        self.menu()
        choice = int(input('Choose an option : '))
        while choice != 6:
            if choice == 1:
                self.all_g()
            elif choice == 2:
                self.all_g_y()
            elif choice == 3:
                self.ranking()
            elif choice == 4:
                self.differ()
            elif choice == 5:
                self.play_time()
            self.menu()
            choice = int(input('Choose an option : '))
