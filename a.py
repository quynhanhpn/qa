#bai 1
thisdict ={
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS":30,
}
# print(thisdict["MACBOOK"])
# a = input("nhập hãng máy: ")
# print(thisdict[a])
#bài 2
# thisdict["TOSHIBA"] = 10
# print(thisdict)

# b = input("nhập hãng máy: ")
# c = input("số lượng: ")
# thisdict[b] = c
# print(thisdict)

# thisdict.update({"DELL": 60})
# print(thisdict)
#bai 3
cost ={
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 1200,
    "ASUS":400,
}
# print(cost["ASUS"])
# a = input("nhập hãng máy: ")
# print(cost[a])

#bai 4 
# a = cost["DELL"] * 5 
# print(a)

# b = input("nhập hãng máy: ")
# c = int(input("số lượng: "))
# a = cost[b] * c 
# print(a)

# b = input("nhập hãng máy xuất kho: ")
# c = int(input("số lượng máy xuất kho: "))
# a = cost[b] * c 
# print("tông giá trị máy xuất kho: " , a)
# d = thisdict[b] - c
# print(d)
# thisdict.update({b: d})
# print(thisdict)



#bai 6
# thisdict = {
#   "Name": "Light",
#   "Age": 17,
#   "Strength": 8,
#   "Defense": 10,
#   "HP": 100,
#   "Backpack": ["Shield"," Bread Loaf"],
#   "Gold": 100,
#   "Level": 2,
# }
# thisdict["Gold"] = 150
# print(thisdict["Gold"])
# thisdict["Pocket "] = "MonsterDex "," Flashlight"
# print(thisdict)

#bai 7
thislist ={
    "Skill_1" :{
     "Name":"Tackle",
     "Minimum level":1,
     "Damage":5,
     "Hit rate":0.3,
     },
    "Skill_2" :{
     "Name":"Quick Attack",
     "Minimum level":2,
     "Damage":3,
     "Hit rate":0.5,
     },
    "Skill_3" :{
     "Name":" Strong Kick",
     "Minimum level":4,
     "Damage":9,
     "Hit rate":0.2,
     },
}
print(thislist)
