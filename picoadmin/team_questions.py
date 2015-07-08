from pymongo import MongoClient

client = MongoClient()
db = client.pico

teams = db.teams.find()
results_teams = {}
for i in teams:
    results_teams[i["team_name"]] = []
    subs = db.submissions.find({"tid":i["tid"], "correct": True})
    for j in subs:
        problem = [pr for pr in db.problems.find({"pid":j["pid"]})][0]
        results_teams[i["team_name"]].append(problem["name"])

sorted_teams = sorted(results_teams.items(), key=lambda k: len(k[1]), reverse=True)
for i in sorted_teams:
    print("%s solved (%d):" % (i[0], len(i[1])))
    for j in range(len(i[1])):
        print("%d. %s" % (j, i[1][j]))
    print("\n")

          
          

