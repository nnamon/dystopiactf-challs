from pymongo import MongoClient

client = MongoClient()
db = client.pico

teams = db.teams.find()
for i in teams:
    print("Team %s (%s)" % (i["team_name"], i["school"]))
    members = db.users.find({"tid":i["tid"]})
    count = 0
    for j in members:
        count += 1
        print("%d. %s - %s %s (%s)" % (count, j['username'], j['firstname'], j['lastname'], j['email']))
    print("\n")

          
          

