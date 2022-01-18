'''
Author: Clayton Branstetter
KUID: 3089206
Date: 11/17/2021
Lab: lab#09
Last modified: 11/17/2021
Purpose: Random Import & Pokedex
'''

# In[13]:


import random


def build_pokedex(file_name):
    with open(file_name, "r") as file:
        data = file.read()
    List = data.split("\n")
    names = {}
    for el in List:
        li_names = el.split("\t")
        US = li_names[0]
        JPN = li_names[-1]
        names[US] = JPN
    return names


# In[9]:


pokedex = build_pokedex("pokedex.txt")


def build_team(pokedex, size=6, is_unique=False):
    random.shuffle(pokedex)
    if is_unique:
        return random.sample(pokedex, k=size)
    return random.choices(pokedex, k=size)


# In[10]:


def battle(team1, team2):
    print("+++"+"Team 1"+"+++")
    for player in team1:
        print(player)
    print()
    print("+++"+"Team 2"+"+++")
    for player in team2:
        print(player)
    for i in range(len(team1)//2):
        print()
        player1 = random.choice(team1)
        team1.remove(player1)
        player2 = random.choice(team2)
        team2.remove(player2)
        print(f"+++Round {i+1}+++")
        print(f"{player1} VS {player2}")
        winner = random.choice([player1, player2])
        print(f"{winner} wins!")


# In[12]:


pokedex = build_pokedex("pokedex.txt")
exit = False
teams = []
while not exit:
    print("\n1) Print Pokedex\n2) Translate\n3) Build a team\n4) Pokemon battle\n5) Exit")
    response = input("response")
    n = int(response)
    keys = pokedex.keys()
    if n == 1:
        for key in keys:
            print(f"{key} --> {pokedex[key]}")
    elif n == 2:
        name = input("Which US name do you want to translate? ")
        print()
        if name in keys:
            print(f"{name} is {pokedex[name]} in Japanese")
        else:
            print("There is no find such name")
    elif n == 3:
        names = list(keys)
        team = build_team(names)
        print("\n+++Team players+++")
        for player in team:
            print(player)
        teams.append(team)
    elif n == 4:
        battle(teams[0], teams[1])
    elif n == 5:
        teams = []
        exit = True


# In[ ]:
