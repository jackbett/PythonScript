import csv
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import pandas as pd
import json
import msvcrt

boolUser = True

def csvConverter(booly):

    fileExt = [('CSV File', '*.csv')]
    filenameIn = askopenfilename(filetypes = fileExt)
    filenameOut = asksaveasfilename(filetypes = fileExt, defaultextension = fileExt)
    fields = ['TAGS', 'Tags']

    df = pd.DataFrame()
    df2 = pd.read_csv(filenameIn, skiprows=[0], sep = ',')
    df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]

    detectedField = ""

    for col in df2.columns: 

        if col in fields:

            df = pd.read_csv('Azureresources.csv', skiprows=[0], sep = ',',  usecols = [col])
            detectedField = col

    newDF = pd.DataFrame()

    for i, row in df.iterrows():

        x = (row[detectedField])
        y = json.loads(x)
        # keyList = list(y.keys())
        dfDictionary = pd.DataFrame(y, index = [i])
        newDF = newDF.append(dfDictionary, sort=True)

    finalDF = pd.concat([df2, newDF], axis=1)

    finalDF.to_csv (filenameOut, index = False, header=True, mode = 'w+')

    print("Enter any input key into program to continue.  If you are done, close out of the program.")
    msvcrt.getch()
    booly = True

while boolUser == True:
    csvConverter(boolUser)