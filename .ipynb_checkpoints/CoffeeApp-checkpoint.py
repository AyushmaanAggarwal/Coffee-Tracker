import pickle, time
import Ratings, RoastedCoffee, Roasters, Tracker

catagories = [
        "Brews",
        "Roasters",
        "Coffee Beans",
        "Quit"]

options = [
        "New",
        "Edit",
        "View",
        "Quit"
        ]

# load previous data
try:
    filename = "coffeeData"
    dictionary = pickle.load(filename)
    loaded = True
except:
    # Default file format
    dictionary = {"Brews":[], "Roasters":[], "Coffee Beans":[]}
    loaded = False

print("Welcome to the interactive coffee logger!")
print("_"*30 + "\n\n\n")

continue_input = True
changes = False
while(continue_input):

    print("What would you like to work on: ")
    print_list(catagories)
    
    input_catagory = catagories[input("Enter number here: ")]

    if input_catagory == "Quit":
        break

    print("\n\nWould you like to: ")
    print_list(options)
    
    input_option = options[input("Enter number here: ")] 

    if input_option == "Quit":
        break
    
    # DECISION TREE
    if input_catagory == "Brews":
        if input_option == "New":
            assert dictionary["Coffee Beans"], "Must have Coffee Beans first"
            print("Creating a new brew log")
            date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
            if input(f"Is {date} the correct time and date?[T/F]: "=="F"):
                date = input("Enter Correct Date and Time here: ")
            coffee_dose = input("Enter Coffee Dose: ")
            total_water = input("Enter Brew Water : ")
            brew_temp   = input("Enter Brew Temp  :")
            grind_size  = input("Enter Grind Level: ")
            time_weight = input("Enter Total Brew Time: ")
            print("")
            print_list(dictionary["Coffee Beans"])
            coffee = dictionary["Coffee Beans"][int(input("Select Coffee Beans"))]
            
            dictionary["Brews"].append(Tracker(date, coffee, coffee_dose, total_water, grind_size, time_weight, brew_temp))


        elif input_option == "Edit":
            lst = ["date", "coffee", "coffee_dose", "total_water", "grind_size", "time_weight", "brew_temp"]
            print_list(lst)
            modify = input("What would you like to modify?")
        else:
            assert False, "Invalid Input Option"
            
    elif input_catagory == "Roasters":
        if input_option == "New":
            #f
        elif input_option == "Edit":
            #f
        else:
            assert False, "Invalid Input Option"
            
    elif input_catagory == "Coffee Beans":
        if input_option == "New":
            #f
        elif input_option == "Edit":
            #f
        else:
            assert False, "Invalid Input Option"
            
    else:
        assert False, "Invalid Input Catagory"
    
    if changes:
        # update dictionary and save using pickle

def print_list(lst):
    for i in range(1, len(lst)+1):
        print(f"({1}) {lst[i-1]})")


