def move(x, y):
    print(f"move {x} {y}")

def mine(x, y):
    print(f"mine {x} {y}")

def build(x, y):
    print(f"build {x} {y}")

def convert(c_diamont, c_mineral, e_diamont, e_mineral, xp_diamond, xp_mineral):
    print(f"conv {c_diamont} diamond {c_mineral} mineral to coins, {e_diamont} diamond {e_mineral} mineral to energy, {xp_diamond} diamond {xp_mineral} mineral to xp")

def rest():
    print("rest")

def shop(item):
    print(f"shop {item}")

def attack(x, y):
    print(f"attack {x} {y}")

def put_refinement(x, y, mineral, diamond): #x, y - coordinates of fabric
    print(f"refinement-put {x} {y} mineral {mineral} diamond {diamond}")

def take_refinement(x, y, mineral, diamond): #x, y - coordinates of fabric
    print(f"refinement-take {x} {y} mineral {mineral} diamond {diamond}")