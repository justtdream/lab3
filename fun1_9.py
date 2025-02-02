import math  
def volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = float(input("Enter the radius: ")) 
volume = volume(radius) 
print(f"The volume with radius {radius} is {volume}")  
