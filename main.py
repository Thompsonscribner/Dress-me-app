import random

clothes = list()
tops = []
bottoms = []

class Clothing:
    global clothes
    def __init__(self, season, color):
        self.season = season
        self.color = color
        self.title = ("A", self.color, "item. Perfect for", self.season)
        clothes.append(self)
    def describe(self):
        print(" ".join(self.title))

class Top(Clothing):
    global tops
    def __init__(self, season, color, type):
        super().__init__(season, color)
        self.type = type
        self.title = ("A", self.color, self.type + ". Perfect for", self.season)   
        tops.append(self)

class T_shirt(Top):
    def __init__(self, season, color, type, sleeve):
        super().__init__(season, color, type)
        self.sleeve = sleeve + " sleeve"
        self.title = ("A", self.color, self.sleeve, self.type + ". Perfect for", self.season)

class Bottom(Clothing):
    def __init__(self, season, color, type):
        super().__init__(season, color)
        self.type = type
        self.title = (self.color, self.type + ". Perfect for", self.season)
        bottoms.append(self)


def rand3():
    print("here are three random items from your wardrobe: ")
    for clo in rand_3:
        clo.describe()

def rand_combo():
    print("here's a random outfit for the day: ")
    rand_top.describe()
    print("and".center(40))
    rand_bottom.describe()

def summer_combo():
    top for top in tops if top.season == "summer"
        rand_top.describe()
    else: print("not summer")
    # while True:
    #     if rand_top.season == "summer":
    #         rand_top.describe()
    #         break
    #     continue


handle = open("wardrobe.csv")

for line in handle: 

    chunkies = line.split(",")
    chunks= []
    for chunx in chunkies:
        chunk = chunx.strip()
        chunks.append(chunk)
    chunks = ",".join(chunks)
    chunks = line.split(",")
    if chunks[0] == "top":
        Top(chunks[2], chunks[3], chunks[1])
        #print(chunks)
    if chunks[0]=="bottom":
        Bottom(chunks[2], chunks[3], chunks[1])
#top[0], sweater[1], fall[2], brown striped[3], long[4]
#Top(season, color, type)
#Bottom(season, color, type)
top1 = Top("spring", "yellow", "long")
bottom1 = Bottom("spring", "black", "pants")

rand_3 = random.sample(clothes, 2)
rand_top = random.choice(tops)
rand_bottom = random.choice(bottoms)

# for x in tops: 

#     x.describe()
while True:
    inp = input("------what would you like to do? ")
    if inp == "random outfit":
        rand_combo()
    if inp == "summer outfit":
        summer_combo()
    if inp == "quit":
        quit()
    
