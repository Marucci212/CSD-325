# Justin Marucci
# Assignment 1.3
# 03/22/2025

# While loop
def beer_countdown(bottles):
  while bottles > 1:
      print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
      bottles -= 1
      print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.\n")
# If statement equals 1 
  if bottles == 1:
      print("1 bottle of beer on the wall, 1 bottle of beer.")
      print("Take it down, pass it around, no more bottles of beer on the wall.\n")

  print("Time to buy more beer!")

# Main program
num_bottles = int(input("How many bottles of beer are on the wall? "))
beer_countdown(num_bottles)