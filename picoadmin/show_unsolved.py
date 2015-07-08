from pymongo import MongoClient

client = MongoClient()
db = client.pico

problems = db.problems.find()
for i in problems:
    count = 1
    if db.submissions.find({"pid": i["pid"], "correct": True}).count() == 0:
        print("%d. %s" % (count, i["name"]))


