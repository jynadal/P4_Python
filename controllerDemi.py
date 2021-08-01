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
with open ('dbRoundDemi_P_list.json','r') as myfile:
    mydata=myfile.read()
    objs = json.loads(mydata)
    myObjs = objs

    print(myObjs)

    for player in myObjs:
        print(player)


# print(last_T)
#print(mydata[0][0])

""" END Add json file for name ..."""

# with open ('dbTournEquipeA.json', 'r') as fileA:
#     data = json.loads(fileA)
#     data = data['_default']
# print(len(data))

# for index, Joueur in enumerate(data):
#     print(Joueur[0][0]['fname'])


""" Récupérer le fichier Equipe B et clean  """

# with open ('dbTournEquipeB.json','r') as myfileA:
#     mydata=myfileA.read()
#     objs = json.loads(mydata)
#     last_T=(len(objs["_default"])) # the last tournament
#     myObjsB = objs["_default"]['1']['equipe_B']

    #print(myObjsB)

    # for player in myObjsB:
    #     print(player)

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
roundDemi_ListS_points = sorted(myObjs, key = lambda i: i['points'], reverse=True)

# Création de fonction FONCTIONNE PAS
# def sortedList( ListIn,key,reverse):
#     sorted(ListIn, key = lambda i: i[key], reverse=reverse)

# round2_ListS_points = sortedList(round2_List,'points',True)

print(roundDemi_ListS_points)

jsonList = json.dumps(roundDemi_ListS_points)
jsonFile = open("dbRoundDemi_P_list.json", "w")
jsonFile.write(jsonList)
jsonFile.close()