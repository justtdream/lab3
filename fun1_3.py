def pazzle(heads, legs):
    rabs = int((legs - (heads * 2))/2)
    chks = int(heads - rabs)
    print("It's", rabs, "rabbits", "and", chks, "chickens")

hd = int(input("Heads: "))
lg = int(input("Legs: "))
pazzle(hd, lg)