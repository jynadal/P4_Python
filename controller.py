import model
import collections

"""Test model"""


"""End Test model"""


tournament = {}
players = collections.OrderedDict()
continuer = "o"


"""Créer le tournoi Round 0 """
# def ajouter_info(info):
#     input(info)
#     return info

T_name = input("Nom du tournois:")
T_begin = input("Date du début")
T_end = input("Date de fin")
T_contender = input("Nombre de particitant: ")

tournament[T_name] = model.Tournament()
tournament[T_name].T_name = T_name
tournament[T_name].T_begin = T_begin
tournament[T_name].T_end = T_end
tournament[T_name].T_contender = T_contender

print(tournament)


print("Welcome to the {0} Tournament. It begin {1} to {2} in the afternoon. There will be {3} players".format(T_name, T_begin, T_end, T_contender))

for i in range(int(T_contender)):
#while continuer == "o":
    fname = input("Saisissez le prénom du joueur: ")
    lname = input("Saisissez le nom du joueur: ")
    # dBirth = input("La date de naissance: ")
    # sexe = input("C'est un joueur ou une joueuse? M/F")
    rang = i+1

    players[fname] = model.Player(fname,lname,rang)
  
    # players[fname].dBirth = dBirth
    # players[fname].sexe = sexe  
   
    print("")
print("")



"""Fin Round 0 """


for player in players.values():
    print("Joueur {0} {1} et le numéro {2} du classement".format(player.fname, player.lname, player.rang))

"""Begin Round 1 """

""" Défini des classes joueur."""

# class Player:

#     def __init__(self,name,rang, point):
#         """ Initialise les joueurs."""
#         self.name = name
#         self.rang = rang
#         self.point = point

#         """ Pour representer le classe objet comme un string."""
#     def __repr__(self):
#         return repr((self.name, self.rang, self.point))

""" La liste des joueurs du 1er round."""

for i in players.items():
    print(i)

""" Diviser la liste en 2 groupe."""
# dico1 = dict(players.items()[len(players)//2:])
# dico2 = dict(players.items()[:len(players)//2])

middle_index = (len(players.items())//2)
round1_A = list(players.items())[:middle_index]
round1_B = list(players.items())[middle_index:]
    
""" Classement des joueurs par leur classement."""
# round1_ready = sorted(players.items(), key=lambda p: p[0][1])
    
# print(round1_ready)

# """ Diviser la liste en 2 groupe."""
# middle_index = (len(round1_ready)//2)
# round1_A = round1_ready[:middle_index]
# round1_B = round1_ready[middle_index:]

# print(dico1)
# print(dico2)

print(round1_A)
print(round1_B)

""" Afficher les matches."""
print("For the {0} Tournament. It begin {1} to {2} in the afternoon. With {3} players.\n And the match are: ".format(T_name, T_begin, T_end, T_contender))
for indice_objet, valeur_objet in enumerate(round1_A):
    pass
    print("Le match opposera {} N°{} au classement VS {} N°{} au classement"
    .format(valeur_objet[1].fname, valeur_objet[1].rang,round1_B[indice_objet][1].fname, round1_B[indice_objet][1].rang))
"""Fin Round 1 """
