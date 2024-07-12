import os
import time
import copy

# TODO add input protection
def delayPrint(input):
    time.sleep(.15)
    print(input)
    time.sleep(.15)

def listDirectoryContents(path):
    filelist = []
    for entry in os.listdir(path):
        filelist.append(entry)
    return filelist


def printDirectoryContents(listOfFiles):
    tooLongCheck = False
    for index, item in enumerate(listOfFiles):
        listNumber = index + 1
        delayPrint(f'{listNumber}. {item}')
        if index == 14 or index == 29 or index == 59 or index == 119 or index == 239:
            longList = input(
                delayPrint(
                    "List of files is getting long, continue printing, select all or break?(contprnt/all/break)"))
            if longList == "contprnt" and index == 240:
                selectAll = input(delayPrint("File list is too long! Do you want to select all files?(y/n)"))
                if selectAll == "y":
                    delayPrint("Selected all contents")
                    tooLongCheck = True
                    break
                else:
                    delayPrint("Ending Program...")
                    exit()
            elif longList == "all":
                delayPrint("Selected all contents")
                tooLongCheck = True
                break
            elif longList == "contprnt":
                continue
            elif longList == "break":
                break
    return tooLongCheck


searchMatches = []
nameAppend = []
searchFilters = []
delayPrint("Welcome to the mass file sortnamer!")
while True:
    directory = input("Please specify the directory in which you want file names changed\n")
    if not os.path.exists(directory):
        continue
    else:
        break
delayPrint("Directory set.")
delayPrint("Choose the files you want to rename.")
directoryContents = listDirectoryContents(directory)
selectAllCheck = printDirectoryContents(directoryContents)
directoryOriginal = copy.deepcopy(directoryContents)
if not selectAllCheck:
    while True:
        renamePoint = input("To what point do you wish to rename, or rename all(all)?\n")
        if renamePoint == "all":
            delayPrint("Selected all contents of directory")
            renamePoint = len(directoryContents)
            break
        try:
            renamePoint = int(renamePoint)
            if renamePoint > len(directoryContents):
                delayPrint(
                    f"Rename point is greater than the number of files ({len(directoryContents)}). Please try again.")
            else:
                for n in directoryContents:
                    try:
                        del directoryContents[renamePoint+1]
                    except IndexError:
                        break
                break
        except ValueError:
            delayPrint("Invalid input. Please enter a number or 'all'.")
            continue
numberOfFilters = input("How many filters would you like to use?\n")
numberOfFilters = int(numberOfFilters)
for n in range(numberOfFilters):
    searchFilters.append(input("Enter the filter that you wish to use"))
    nameAppend.append(input("What would you like this filter to append?"))
for n in range(numberOfFilters):
    searchTerm = searchFilters[n]
    filteredContents = [[p, directoryContent]
                        for p, directoryContent in enumerate(directoryContents) if searchFilters[n] in directoryContent]
    for i in range(len(filteredContents)):
        searchMatches.append([nameAppend[n] + filteredContents[i][1], filteredContents[i][0]])
for n in range(len(searchMatches)):
    replacePos = searchMatches[n][1]
    directoryContents[replacePos] = searchMatches[n][0]
for n in range(len(directoryContents)):
    oldFile = os.path.join(directory, directoryOriginal[n])
    newFile = os.path.join(directory, directoryContents[n])
    os.rename(oldFile, newFile)
delayPrint("Renamed files")
