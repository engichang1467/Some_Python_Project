###CMPT 120 Scantron Assignment###

#Created by
#   Michael Chang (Student ID 301 329 253)

print ("Welcome to Micheal's CMPT 120 Scantron Processing Program")
print ()

#----------DEFINITIONS----------#

#qans reads txt file given in folder, provides student answers
def qans(file):

    fileRef = open(file,"r")
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]

        localList.append(string)

    fileRef.close()
    print ("The student answers for this scantron are :")

    for element in localList:
        print (element)

    return localList

#poin gives the point value of each question for the scantron
def poin(file):

    fileRef = open(file,"r")
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]

        localList.append(string)

    fileRef.close()
    print ("The points for each question of the scantron are :")

    for element in localList:
        print (element)

    return localList

def loopsans(ans):
    test = 0
    repeat = 1
    var1 = 0
    while test == 0:
        if ans1[repeat].isdigit:
            test = 1
        else:
            repeat = repeat + 1
    var1 = ans1[repeat-1:repeat]

#rtf gives result, should be used last
def result(lres,file):

    fileRef = open(file,"w")
    for line in lres:
        fileRef.write(line)

    fileRef.close()
    return

#----------INPUTS----------#

ans1 = qans("IN_data_studs.txt")
print ()

loopsans(ans1)
print (var1)

ans2 = poin("IN_key+pts.txt")
print()

#Activate when program is done
#result("Out_result.csv","IN_data_studs.txt")
