#!/usr/bin/env python3

#*-------------------------------------------*#
#  Title       : SAC Rate Calculator v0.1     #
#  File        : SACcalc.py                   #
#  Author      : Yigit Suoglu                 #
#  License     : EUPL-1.2                     #
#  Last Edit   : 26/11/2022                   #
#*-------------------------------------------*#
#  Description :  Script for calculating      #
#                surface air consumption rate #
#*-------------------------------------------*#

import sys

def getInput(prompt, defValue):
  val = input(prompt)
  if val == "":
    val = defValue
    sys.stdout.write('\033[F' + str(prompt) + '\033[2m' + str(defValue) + '\033[0m\n')
  return val


if __name__ == '__main__':
  imperial = False
  askHour = False
  while len(sys.argv) > 1:
    current = sys.argv.pop(-1)
    current = current.strip()
    if current == '-h':
      askHour = True
    elif current == '-i':
      imperial = True
    elif current == "--help":
        print('Usage: SACcalc.py [arg]')
        print(' Possible arguments:')
        print('  -h: Ask for hour too')
        print('  -i: Use imperial units')
        sys.exit(0)
    else:
      print("Unknown argument: ", current)
  totalAir = 0
  numberOfTanks = int(getInput("Number of tanks: ", 1))
  for i in range(numberOfTanks):
    startPres = float(getInput("Start Pressure: ", 200))
    endPres   = float(getInput("End Pressure: ", 50))
    tankL     = float(getInput("Tank Size: ", 12))
    totalAir = (startPres-endPres)*tankL + totalAir
  print("Total gas consumed ", totalAir, " liters in 1 atm")
  avgDepth = float(getInput("Average depth: ", 18))
  if imperial:
    waterH = 33.8
  else:
    waterH = 10.3
  avgPres = 1.0 + avgDepth / waterH
  time = 0
  if askHour:
    time = int(getInput("Dive time hours: ", 0)) * 60 * 60
  time = time + int(getInput("Dive time minutes: ", 0)) * 60
  time = time + int(getInput("Dive time seconds: ", 0))
  sacRate = (totalAir * 60.0) / (time * avgPres)
  print("Calculated surface air consumption rate is ", sacRate, " volume per minute")

