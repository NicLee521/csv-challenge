import pandas as pd
import os
import sys

"""
Used to get input from the user and remove script name from 
arguments then returns arguments to use in other functions
"""
def GetArgs():
    arguments = sys.argv
    arguments.remove(os.path.basename(__file__))
    return arguments
"""
Used to check if files exist at the given path then if they do
to check if the correct file extension is given if neither is 
true then it exits the script
"""
def CheckFiles(arguments):
    for arg in arguments:
        if (os.path.exists(arg) == False):
            print("File does not exist in " + arg + " location")
            sys.exit()
        else:
            if(arg.lower().endswith('.csv') == False):
                print("File exists but does not have correct extension please try again")
                sys.exit()

"""
After checking if the files exist this function is used to read 
the csv's given into a list and return that list the be used later
"""
def GetFiles(arguments): 
    csvList =[]
    for arg in arguments:
        tempCsv = pd.read_csv(arg)
        tempCsv["filename"] = os.path.basename(arg) 
        csvList.append(tempCsv) 
    return csvList

"""
Combines all csv's given into a single file then outputs to a new file 
names "combined.csv" and also outputs the new csv to the console using
stdout
"""
def CreateNewCsv(csvList):
    combinded_csv = pd.concat(csvList) 
    return combinded_csv
    

def PrintAndCreate(combinded_csv):
    combinded_csv.to_csv("combined.csv", index= False)
    combinded_csv.to_csv(sys.stdout, index = False) 

def main():
    arguments = GetArgs()
    CheckFiles(arguments)
    csvList = GetFiles(arguments)
    PrintAndCreate(CreateNewCsv(csvList))


if __name__== "__main__":
    main()