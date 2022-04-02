'''
Author: Clayton Branstetter
KUID: 3089206
Date: 03/28/2022
Lab: lab#05
Last modified: 04/01/2022
Purpose: Outbreak Returns
'''


def flu(day):
    """Calculation of infected for a given day"""
    if day==1: #On day 1, there was only 6 people had the flu
        return 6
    if day==2: #On day 2, it jumped to 20
        return 20
    if day==3: #On day 3, there were 75
        return 75
    return flu(day-1) + flu(day-2) + flu(day-3) #Every day > 3, the number of people who have the flu is equal to the last 3 days combined

def main():
    print("OUTBREAK!")
    try:
        day = int(input("What day do you want a sick count for?: "))
        if day<1: #the day must be 1 or larger
            raise RuntimeError
        print(f"Total people with flu: {day}")
    except:
        print("invalid day")


