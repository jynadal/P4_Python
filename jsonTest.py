import json

myfile = '''
{
  "_default": {
    "1": {
      "1": {
        "fname": "Sarah",
        "lname": "Johnson",
        "DBirth": "01/06/2001",
        "gender": "female",
        "rang": "1",
        "points": 1
      }
    },
    "2": {
      "2": {
        "fname": "Smith",
        "lname": "nathan",
        "DBirth": "2000",
        "gender": "male",
        "rang": "2",
        "points": 0.5
      }
    },
    "3": {
      "3": {
        "fname": "John",
        "lname": "Smithas",
        "DBirth": "01/02/2000",
        "gender": "male",
        "rang": "3",
        "points": 0
      }
    },
    "4": {
      "4": {
        "fname": "Sean",
        "lname": "Spinoza",
        "DBirth": "01/02/2000",
        "gender": "male",
        "rang": "4",
        "points": 1
      }
    }
  }
}
'''
open ()

data = json.load(myfile)

print(data['_default'])

