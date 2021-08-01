from tinydb import TinyDB, Query
db = TinyDB('dbTest.json')

User = Query()

def insert():
    db.insert({'name': 'John', 'age' : 28, 'contender':'Sarah'})
    db.insert({'name': 'Max', 'age' : 27, 'contender':'John'})
    db.insert({'name': 'Sarah', 'age' : 26, 'contender':['Max','Bill']})

def search():
    results= db.search(User.name == "Sarah")
    contenders = results[0]['contender']
    print(contenders[0])

def search():
    results= db.search(User.name == "Sarah")
    print(results[0]['age'])
   

def update():
    db.update({'age': 24}, User.name == 'John')

    # results = db.search(User.name == 'Max')
    # for res in results:
    #     res['name'] = "Maxime"
    #     res['age'] = 28
    #     res['contender'] = "Sarah"
    # db.write_back(results) # Ne fonctionne pas et il n'y a pas de remplacement
    # db.update

def delete(user):
    db.remove(User.name == user)

''' Pour tous effacer truncate() au lieu de purge()'''
#db.truncate()

''' Pour tous insérer '''
#insert()

''' control '''
#print(db.all())

''' Recherche '''
search()

""" Modifier """
#update()

""" Supprimer """
#delete('John')

''' control '''
#print(db.all())

''' control '''
#print(db.all())