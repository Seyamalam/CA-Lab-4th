def pizza_cuts(cuts):
    if cuts == 0:
        return 1
    return pizza_cuts(cuts - 1) + cuts


cuts = int(input("Enter the number of cuts: "))
for i in range(cuts + 1):
    print(f"With {i} cuts, the pizza can be divided into {pizza_cuts(i)} pieces.")
