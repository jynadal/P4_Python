import json
from collections import defaultdict
from tinydb import TinyDB, Query
dbTourDemi = TinyDB('dbDemi_P_listTest.json')

""" Récupérer le fichier Equipe A et clean  """
'''
dbTournEquipeA.json
dbTournEquipeB.json
'''
""" Add json file for name ..."""
with open ('dbRoundFinal.json','r') as myfile:
    mydata=myfile.read()
    objs = json.loads(mydata)
    myObjs = objs

    #print(myObjs)

    for player in myObjs:
        #print(player)
        pass


# print(last_T)
#print(mydata[0][0])

""" END Add json file for name ..."""



""" Récupérer le fichier Equipe B et clean  """

""" Rassembler et ranger les joueurs / joint to list of dictionary """
#round2_List = [*myObjsA, *myObjsB]
#print(round2_List)
# D = defaultdict(dict)
# for lst in myObjsA, myObjsB:
#     for item in lst:
#         key = item['rang']


'''
file.sort('points')
with open('dbfichierRound2.json', 'w') as newFile:
    for joueur in joueurs:
        newFile.write(joueur + '\n')
'''
# Sorted list by "points"
#Final_ListS = sorted(myObjs['win'])
Points_listS=sorted(myObjs, key = lambda i:i['points'],reverse=True) # sorted by points reverse
Final_ListS = sorted(Points_listS, key = lambda i:i['win'], reverse=True) # sorted the result by "win"

# Création de fonction FONCTIONNE PAS
# def sortedList( ListIn,key,reverse):
#     sorted(ListIn, key = lambda i: i[key], reverse=reverse)

# round2_ListS_points = sortedList(round2_List,'points',True)


#print(Final_ListS)

jsonList = json.dumps(Final_ListS)
jsonFile = open("dbFinal_P_list.json", "w")
jsonFile.write(jsonList)
jsonFile.close()