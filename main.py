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
    def __init__(self, season, color, sleeve):
        super().__init__(season, color)
        self.sleeve = sleeve + " sleeve"
        self.title = ("A", self.color + ",", self.sleeve, "top. Perfect for", self.season)      
        tops.append(self)

class Bottom(Clothing):
    def __init__(self, season, color, length):
        super().__init__(season, color)
        self.length = length
        self.title = ("A", self.color, self.length + ". Perfect for", self.season)
        bottoms.append(self)


def rand3():
    print("here are three random items from your wardrobe: ")
    for clo in rand_3:
        clo.describe()

def rand_combo():
    print("here's a random outfit for the day: ")
    rand_top.describe()
    rand_bottom.describe()

handle = open("wardrobe.csv")

for line in handle: 
    chunks = line.split(",")
    if chunks[0] == "top":
        Top(chunks[2], chunks[3], chunks[4])
    if chunks[0]=="bottom":
        Bottom(chunks[2], chunks[3], chunks[1])

top1 = Top("spring", "yellow", "long")
bottom1 = Bottom("spring", "black", "pant")

rand_3 = random.sample(clothes, 2)
rand_top = random.choice(tops)
rand_bottom = random.choice(bottoms)

# for x in tops: 
#     x.describe()
rand_combo()
