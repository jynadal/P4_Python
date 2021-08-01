class Player:
    
    def __init__(self,fname, lname, rang, point=0):
        self.fname = fname
        self.lname = lname
        # self.dBirth = ""
        # self.sexe = ""
        self.rang = rang
        self.point = point

    """ Pour representer le classe objet comme un string."""
    def __repr__(self):
        return repr((self.fname, self.rang, self.point))



class Tournament:

    def __init__(self):
        # self.T_name = ""
        # self.T_begin = ""
        # self.T_end = ""
        self.T_contender = 0

    

