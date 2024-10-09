#------------import statements
import sqlite3
import random


#initialize database:
conn = sqlite3.connect("dressme.sqlite")
cur = conn.cursor()


#------------function definitions
def generate_outfits():
    top1 = generate_rand("TOP")
    bottom1 = generate_rand("BOTTOM")
    print(top1)
    print("and")
    print(bottom1)
    return top1, bottom1

def generate_rand(type):
    cur.execute('''
    SELECT Description
    FROM Wardrobe
    WHERE Clean = 1 AND Type = ? 
                ''', (type, ))

    tops = cur.fetchall()
    return (random.choice(tops)[0])


def pick_new():
    pass

def wear(Description):
    cur.execute('''
    UPDATE Wardrobe
    SET Clean = 0
    WHERE Description = ?
                ''', (Description, ))
    conn.commit()

def wear_combo(top1, bottom1):
    wear(top1)
    wear(bottom1)
    print("worn")

def do_laundry():
    pass

def wash_1():
    pass

def wear_1():
    pass

def declutter_1():
    pass

def suggest_5():
    pass

def declutter_all():
    cur.executescript('''
    DROP TABLE IF EXISTS Wardrobe;
    
    CREATE TABLE Wardrobe (
        id  INTEGER PRIMARY KEY NOT NULL UNIQUE,
        Description    TEXT UNIQUE,
        Clean   BOOLEAN DEFAULT TRUE, 
        Type   TEXT,
        Fall    BOOLEAN DEFAULT FALSE,
        Winter    BOOLEAN DEFAULT FALSE,
        Spring    BOOLEAN DEFAULT FALSE,
        Summer    BOOLEAN DEFAULT FALSE,
        Dress    BOOLEAN DEFAULT FALSE,
        Onepiece    BOOLEAN DEFAULT FALSE
    );
    ''')

def add_item():
    d = input("describe item: ")
    t = input("item type (TOP or BOTTOM): ")
    f = bool(input("appropriate for fall? (y/n): "))
    w = bool(input("appropriate for winter? (y/n): "))
    sp = bool(input("appropriate for spring? (y/n): "))
    su = bool(input("appropriate for summer? (y/n): "))
    dr = bool(input("is dress? (y/n): "))
    o = bool(input("is onepiece? (y/n): "))

    
    cur.execute('''
    INSERT OR IGNORE INTO Wardrobe (Description, Clean, Type, Fall, Winter, Spring, Summer, Dress, Onepiece) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? ) ''', (d, True, t, f, w, sp, su, dr, o))
    conn.commit()

def bool(x):
    if x == "y": return True
    else: return False

def add_tag():
    pass

def edit_tags():
    pass

def retake_photo():
    pass

# add_item()
# add_item()

# add_item()

top1, bottom1 = generate_outfits()
wear_combo(top1, bottom1)