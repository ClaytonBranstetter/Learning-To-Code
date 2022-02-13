class BoardGame:
    def __init__(self,name,year,GR,PR,MP,MT):
        self.name = name #name of the game
        self.year = year #year published
        self.GR = GR #gibbons-rating
        self.PR = PR #people's rating
        self.MP = MP #min players
        self.MT = MT #min playtime
    
    def __str__(self):
        return f"{self.name} ({self.year}) [GR={self.GR}, PR={self.PR}, MP={self.MP}, MT={self.MT}]"