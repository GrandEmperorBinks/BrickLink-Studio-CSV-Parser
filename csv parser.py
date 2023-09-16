import csv

#define function for opening a csv and translating the contents into a single variable, as a list of dictionaries
def openCSV(fileName):
    try:
        fileContents = []
        file = open(fileName)
        reader = csv.DictReader(file)
        for row in reader:
            fileContents.append(row)
        file.close()
    #if there is an error in reading file, eg file is empty, handle the error
    except:
        fileContents = []
        print('Error in reading file. Please ensure the file exists, and contains valid data')
    return fileContents

#create variables for each of the two files and use the openCSV function - to be replaced by allowing the user to choose any two csv files and saving those to the variables
file1Contents = openCSV('3.csv')
file2Contents = openCSV('4.csv')

#search file1Contents for a specific piece number
#if file was empty, show error message
if file1Contents == [] or file2Contents == []:
    print('No data in one or more files')
else:
    piecesNeeded = []
    piecesNeededShort = []

    #for each dictionary in the 1st list, compare each dictionary in the second list
    for dict1 in file1Contents:
        foundMatch = False
        temp = {}
        for dict2 in file2Contents:
            if (
                dict1['BLItemNo'] == dict2['BLItemNo']
                and dict1['PartName'] == dict2['PartName']
                and dict1['BLColorId'] == dict2['BLColorId']
                ):
                #calculate quantities - if quantity is negative, eg we have more than we need, skip to next dictionary in the second list
                initialQty = dict1['Qty']
                finalQty = dict2['Qty']
                remainingQty = int(initialQty) - int(finalQty)
                if remainingQty <= 0:
                    foundMatch = True
                    break
                else:
                    dict1['Qty'] = remainingQty
        #if no match was found, save data of piece we need into a new list(s)
        if not foundMatch:
            piecesNeeded.append(dict1)
            temp['BLItemNo'] = dict1['BLItemNo']
            temp['BLColourId'] = dict1['BLColorId']
            temp['Qty'] = dict1['Qty']
            piecesNeededShort.append(temp)

#print results - to be replaced with saving results in a 3rd csv file
print(piecesNeededShort)
print(' ')
print(' ')
print(piecesNeeded)

