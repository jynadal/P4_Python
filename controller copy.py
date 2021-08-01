import model

"""Test model"""
class Player:
    
    def __init__(self, fname, lname, rang):
        self.fname = fname
        self.lname = lname
        self.rang = rang

# class Tournament():

#     def __init__(self, T_name, T_begin, T_end, T_contender):
#         self.T_name = T_name
#         self.T_begin = T_begin
#         self.T_end = T_end
#         self.T_contender = T_contender

"""End Test model"""


tournament = {}
players = {}
continuer = "o"


# while continuer == "o":

#     continuer = input('Voulez-vous ajouter un autre client')

"""Créer le tournoi Round 0 """
# def ajouter_info(info):
#     input(info)
#     return info

# T_name = input("Nom du tournois:")
# T_begin = input("Date du début")
# T_end = input("Date de fin")
T_contender = input("Nombre de particitant: ")

# tournament[T_name] = Tournament()
# tournament[T_name].T_name = T_name
# tournament[T_name].T_begin = T_begin
# tournament[T_name].T_end = T_end
# tournament[T_name].T_contender = T_contender

# print(tournament)


#print("Welcome to the {0} Tournament. It begin {1} to {2} in the afternoon. There will be {3} players".format(T_name, T_begin, T_end, T_contender))

for i in range(int(T_contender)):
    
    fname = input("Saisissez le prénom du joueur: ")
    lname = input("Saisissez le nom du joueur: ")
    rang = i+1

    players[fname] = Player()
    players[fname].fname = fname
    players[fname].lname = lname 
    players[fname].rang = rang
    print("")

print("")

"""Fin Round 0 """


for player in players.values():
    print("Joueur {0} {1} et le numéro {2} du classement".format(player.fname, player.lname, player.rang))

