'''
Author: Clayton Branstetter
KUID: 3089206
Date: 09/25/2021
Lab: lab#02
Last modified: 09/25/2021
Purpose: Finding windspeed over a scale/graph
'''

def category(windspeed):
  if int(windspeed) > 70:
    return "category 5"
  if int(windspeed) > 58:
    return "category 4"
  if int(windspeed) > 50:
    return "category 3"
  if int(windspeed) > 43:
    return "category 2"
  if int(windspeed) > 33:
    return "category 1"
  if int(windspeed) > 18:
    return "tropical storm"
  if int(windspeed) > 0:
    return "tropical depression"
  return "Sorry, that's invalid"
