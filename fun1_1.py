def grams(grams):
    ounces = 28.3495231 * grams
    return ounces

recipe = float(input("Enter grams: "))
print("It's", grams(recipe), "ounces")