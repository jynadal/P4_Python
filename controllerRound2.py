import json
from tinydb import TinyDB, Query
#dbTournament = TinyDB('dbTournoisClassTest.json')

""" Récupérer le fichier Equipe A et clean  """
'''
dbjoueurNTestA.json
dbjoueurNTestB.json
'''
""" Add json file for name ..."""
with open ('dbjoueurNTestA.json','r') as myfileA:
    mydata=myfileA.read()
    objs = json.loads(mydata)
    last_T=(len(objs["_default"])) # the last tournament
    myObjs = objs["_default"]

player1 = myObjs['1']['1']
print(player1)
player2 = myObjs['2']['2']
player3 = myObjs['3']['3']
print(player3)
player4 = myObjs['4']['4']


# NE FONCTIONNE PAS
#playeurTeamA=['player1', 'player2','player3','player4']
# i=0
# for playeur in myObjs:
#     i+=1
#     playeurTeamA[0]= myObjs[str(i)][str(i)]
# #playeur1 = myObjs['1']['1']
# print('player1')
# #playeur2 = myObjs['1']['1']
# print('player2')
# #playeur1 = myObjs['1']['1']
# print('player3')
# #playeur2 = myObjs['1']['1']
# print('player4')


# for key, value in myObjs.items():
#     print(myObjs)
#     value=myObjs



# print(last_T)
#print(mydata[0][0])

""" END Add json file for name ..."""

# with open ('dbjoueurNTestA.json', 'r') as fileA:
#     data = json.loads(fileA)
#     data = data['_default']
# print(len(data))

# for index, Joueur in enumerate(data):
#     print(Joueur[0][0]['fname'])


""" Récupérer le fichier Equipe B et clean  """

with open ('dbjoueurNTestB.json','r') as myfileB:
    mydata=myfileB.read()
    objs = json.loads(mydata)
    last_T=(len(objs["_default"])) # the last tournament
    myObjs = objs["_default"]

player5 = myObjs['1']['1']
print(player1)
player6 = myObjs['2']['2']
player7 = myObjs['3']['3']
print(player3)
player8 = myObjs['4']['4']

""" Rassembler et ranger les joueurs """

#round2_players= []
'''
file.sort('points')
with open('dbfichierRound2.json', 'w') as newFile:
    for joueur in joueurs:
        newFile.write(joueur + '\n')
'''
