import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["Courses"]
mycol = mydb["Course"]

mydict = {"name": "Курс Python", "link": "https://www.python.org/", "tags": ["python"]}

# print(mydb.list_collection_names())
# db.inventory.insert_one(
#     {
#         "item": "canvas",
#         "qty": 100,
#         "tags": ["cotton"],
#         "size": {"h": 28, "w": 35.5, "uom": "cm"},
#     }
# )
# cursor = db.inventory.find({"item": "canvas"})
