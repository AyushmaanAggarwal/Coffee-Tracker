import shelve as sh
import Ratings, RoastedCoffee, Roasters, Tracker


dictionary = shelve.open(filename, flag='c', protocol=None, writeback=False)

catagories = [
        "Brews",
        "Roasters",
        "Roasted Coffee",
        "Quit"]

options = [
        "New",
        "Edit",
        "Add",
        "Quit"
        ]

print("Welcome to the interactive coffee logger!")
print("_"*30 + "\n\n\n")

continue_input = True

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
    
    if input_catagory == "Brews":
        f
    elif input_cata

def print_list(lst):
    for i in range(1, len(lst)+1):
        print(f"({1}) {lst[i-1]})")


