import random

# function to choose dress type
def choose_wear():
    print("Select Dress Type: ")
    print("1.Casual")
    print("2.Party Wear")


# getting user input until its a valid one
    while True:
        # getting user input
        choice = input("Enter choice(1/2): ")
        if choice in ('1', '2'):
            if choice == '1':
                dress = "Casual"
                return dress
            else:
                dress = "Party Wear"
                return dress
            break
        else:
            print("Invalid Input")
            print("Select Season: ")
            print("1.Spring")
            print("2.Summer")
            print("3.Fall")
            print("4.Winter")

# randome number generator
random = random.randrange(1, 2)

# loop
while True:
    # getting user input
    choice = input("Enter choice(1/2/3/4): ")
    # list
    choice_list = ['1', '2', '3', '4']
    # if-elif-else
    if choice in choice_list:
        if choice == '1':
            season = "Spring"
            dress = choose_wear()
            if dress == "Casual":
                if random == 1:
                    # f string
                    print(f"For {season} Try Shorts with T-shirt")
                elif random == 2:
                    print(f"For {season} Try Trousers with pack shirt")
            elif dress == "Party Wear":
                if random == 1:
                    print(f"For {season} Try Patterned full sleeves")
                elif random == 2:
                    print(f"For {season} Try Patterned short sleeves")