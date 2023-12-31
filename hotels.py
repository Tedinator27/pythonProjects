def bookRoom(): 
    print("Select Room Type: \n")
    print("1. Couples Room")
    print("2. Family Room")
    print("3. Group Travel Room")
    print("4. Luxury Suite")
    print("5. VIP Luxury Suite\n")
    roomChoice = int(input("Enter your choice: "))
    if roomChoice == 1: 
        name = input("Please enter your name: ")
        address = input("Please enter your address: ")
        phoneNum = int(input("Please enter your phone number: "))
        print("")
        print("Name: " + name + "\n" + "phone number: " + str(phoneNum) + "\n" + "Address: " + address + "\n" + "Room Type: Couples Room")
    elif roomChoice == 2: 
        name = input("Please enter your name: ")
        address = input("Please enter your address: ")
        phoneNum = int(input("Please enter your phone number: "))
        print("")
        print("Name: " + name + "\n" + "phone number: " + str(phoneNum) + "\n" + "Address: " + address + "\n" + "Room Type: Family Room")
    elif roomChoice == 3: 
        name = input("Please enter your name: ")
        address = input("Please enter your address: ")
        phoneNum = int(input("Please enter your phone number: "))
        print("")
        print("Name: " + name + "\n" + "phone number: " + str(phoneNum) + "\n" + "Address: " + address + "\n" + "Room Type: Group Travel Room")
    elif roomChoice == 4: 
        name = input("Please enter your name: ")
        address = input("Please enter your address: ")
        phoneNum = int(input("Please enter your phone number: "))
        print("")
        print("Name: " + name + "\n" + "phone number: " + str(phoneNum) + "\n" + "Address: " + address + "\n" + "Room Type: Luxury Suite")
    elif roomChoice == 5: 
        name = input("Please enter your name: ")
        address = input("Please enter your address: ")
        phoneNum = int(input("Please enter your phone number: "))
        print("")
        print("Name: " + name + "\n" + "phone number: " + str(phoneNum) + "\n" + "Address: " + address + "\n" + "Room Type: VIP Luxury Suite")
    else: 
        print("Please enter a number 1 - 5")
    

def checkout(): 
    print("Your checkout time is 11 am. Please make sure not to leave any items behind.\n")
    reviewChoice = input("Would you like to leave a review? y/n: ")
    if reviewChoice != 'y' and reviewChoice != 'n': 
        print("")
        print("Please enter either y or n")
    elif reviewChoice == 'y': 
        review = input("Please enter the amount of stars you would rate us out of 5: ")
    else: 
        print("")
        print("You have checked out successfully. Thank you for staying at Ted's Hotel!")


def roomService(): 
    print("Please select what kind of service you need: \n")
    print("1. Cleaning")
    print("2. Food")
    print("3. Breakfast and Dinner hours\n")
    roomServiceChoice = int(input("Enter your choice: "))
    if roomServiceChoice == 1: 
        print("")
        roomNum = int(input("Please enter your room number: "))
        print("")
        print("We'll send a cleaning employee to room " + str(roomNum) + " as soon as possible.")
    elif roomServiceChoice == 2: 
        print("")
        print("Please enter a number to select what you would like to eat: ")
        print("")
        print("1. Lobster")
        print("2. Steak")
        print("3. Spagheti Pesto")
        print("4. Pepperoni/Cheese/Magarita/Hawaiian/Sausage Pizza")
        print("5. Chicken Casear Salad\n")
        foodChoice = int(input("Enter your choice: "))
        if foodChoice == 1: 
            print("We'll send lobster to room " + str(roomNum) + " as soon as possible.")
        elif foodChoice == 2:
            print("How would you like your steak?")
            print("")
            print("1. Rare")
            print("2. Medium Rare")
            print("3. Medium")
            print("4. Medium Well")
            print("5. Well Done\n")
            steakChoice = int(input("Enter your choice: "))
            print("")
            roomNum = int(input("Please enter your room number: "))
            print("")
            if steakChoice == 1:  
                print("We'll send rare steak to room " + str(roomNum) + " as soon as possible.")
            elif steakChoice == 2:                 
                print("We'll send medium rare steak to room " + str(roomNum) + " as soon as possible.")
            elif steakChoice == 3:                 
                print("We'll send medium steak to room " + str(roomNum) + " as soon as possible.")
            elif steakChoice == 4: 
                print("We'll send medium well steak to room " + str(roomNum) + " as soon as possible.")
            elif steakChoice == 5:                 
                print("We'll send well done steak to room " + str(roomNum) + " as soon as possible.")
            else:
                print("Please enter a choice 1 - 5.")
        elif foodChoice == 3: 
            print("")
            roomNum = int(input("Please enter your room number: "))
            print("")
            print("We'll send Spagheti Pesto to room " + str(roomNum) + " as soon as possible.")
        elif foodChoice == 4: 
            print("")
            pizzaChoice = input("Which kind of pizza do you want specifically: ")
            if pizzaChoice == "Pepperoni" or pizzaChoice == "pepperoni":            
                roomNum = int(input("Please enter your room number: "))
                print("")
                print("We'll send pepperoni pizza to room " + str(roomNum) + " as soon as possible.")
            elif pizzaChoice == "Cheese" or pizzaChoice == "cheese": 
                roomNum = int(input("Please enter your room number: "))
                print("")
                print("We'll send cheese pizza to room " + str(roomNum) + " as soon as possible.")
            elif pizzaChoice == "Magarita" or pizzaChoice == "magarita": 
                roomNum = int(input("Please enter your room number: "))
                print("")
                print("We'll send magarita pizza to room " + str(roomNum) + " as soon as possible.")
            elif pizzaChoice == "Hawaiian" or pizzaChoice == "hawaiian": 
                roomNum = int(input("Please enter your room number: "))
                print("")
                print("We'll send hawaiian pizza to room " + str(roomNum) + " as soon as possible.")
            elif pizzaChoice == "Sausage" or pizzaChoice == "sausage": 
                roomNum = int(input("Please enter your room number: "))
                print("")
                print("We'll send sausage pizza to room " + str(roomNum) + " as soon as possible.")
            else: 
                print("")
                print("Please enter a choice that follows the given ones in the menu.")
        elif foodChoice == 5: 
            print("")
            roomNum = int(input("Please enter your room number: "))
            print("")
            print("We'll send chicken casear salad to room " + str(roomNum) + " as soon as possible.")
        else: 
            print("")
            print("Please enter a number 1 - 5.")
                       
    elif roomServiceChoice == 3: 
        print("")
        print("Breakfast hours are 6:00 AM to 10:30 AM")
        print("Dinner hours are 6:30 PM to 9:30 PM")
    else:
        print("") 
        print("Please enter a number 1 - 3")


def readReviews(): 
    oneStar = ["The location of Ted's Hotel is convenient, but that's the only positive. The rooms are outdated, and the breakfast was below average. The Wi-Fi was also spotty, which made it difficult to work during my stay.", 
    "This was my worst hotel experience. The room was small and musty, the air conditioning didn't work, and the bathroom was unclean. I had to request clean towels multiple times. Never staying here again.",
    "My room at Ted's Hotel was right next to a noisy street, making it impossible to sleep. The linens were stained, and the room had a foul odor. Health and safety seem to be of no concern here.",
    "From check-in to check-out, my stay at Ted's Hotel was a nightmare. The staff lost my reservation, the room was dirty, with trash from previous guests still present. The bathroom had mold. A total disaster."]

    twoStar = ["Ted's Hotel has a great location, but that's about it. The rooms are cramped and outdated. The air conditioning barely worked, and the noise from other rooms was very disturbing. Needs serious improvements.",
    "Expected more from Ted's Hotel. The staff seemed disinterested and unhelpful. The room service was slow, and the food quality was mediocre at best. The overall cleanliness was also lacking.",
    "Stayed at Ted's Hotel for a weekend. The beds were uncomfortable, and the pillows were too hard. The bathroom amenities were insufficient and the towels were worn out. Only the central location was a plus.",
    "The potential is there, but Ted's Hotel desperately needs a renovation. The decor is dated, the carpets are stained, and there's a musty smell in the corridors. Only the free Wi-Fi was reliable."]

    threeStar = ["Ted's Hotel is average at best. The rooms were clean but quite basic. The staff were polite, though not overly friendly. It's a decent place if you're not looking for anything fancy.",
    "The best thing about Ted's Hotel is its location, right in the city center. However, the service was just average and the amenities were limited. It's fine for a short stay but lacks the charm of other hotels in the area.",
    "The room at Ted's Hotel was comfortable and clean, but nothing stood out. The hotel lacks distinctive features or services. It's a standard place for a night or two but doesn't offer a memorable experience.",
    "Ted's Hotel is satisfactory for a budget stay. The room size was okay, but the décor felt outdated. The staff were helpful enough, but the overall experience didn't leave a lasting impression. Good for travelers watching their expenses."]

    fourStar = ["I was pleasantly surprised by Ted's Hotel. The room was spacious and well-decorated. The staff was friendly and attentive. The only downside was the limited menu in the restaurant, but overall a very good experience.",
    "Ted's Hotel offers a comfortable stay in a prime location. The beds were cozy, and the room had all the necessary amenities. The staff was helpful, though the check-in process could be quicker. Would recommend for city travelers.",
    "Had a great stay at Ted's Hotel. The rooms are modern and clean. The service was excellent, always prompt and courteous. It's great value for money, although the Wi-Fi could be faster. Would stay here again.",
    "Ted's Hotel impressed me with its exceptional service. The rooms are beautifully furnished and comfortable. The breakfast variety was good, and the location is perfect for exploring the city. Just a bit more attention to detail needed in room maintenance."]

    fiveStar = ["Ted's Hotel is a gem! From the luxurious rooms to the impeccable service, every aspect of my stay was outstanding. The staff made us feel like royalty, and the facilities were top-notch. Absolutely worth every penny!",
    "Our experience at Ted's Hotel was nothing short of perfect. The attention to detail in the rooms, the gourmet dining options, and the friendly, professional staff made our stay memorable. This is the epitome of luxury and comfort.",
    "Ted's Hotel exceeded all my expectations. The room was stunning with breathtaking views. The staff provided exceptional service, going above and beyond to accommodate our needs. The spa and dining experiences were phenomenal.",
    "I've stayed in many hotels, but Ted's Hotel tops them all. The ambiance is fantastic, and the rooms are incredibly comfortable and stylish. The staff is friendly and efficient, and the location is unbeatable. Can't wait to return!"]

    increment = 1
    print("What kind of reviews would you like to see?\n")
    print("1. One star")
    print("2. Two star")
    print("3. Three star")
    print("4. Four star")
    print("5. Five star\n")
    starChoice = int(input("Enter your choice: "))
    if starChoice == 1: 
        for x in oneStar: 
            print(str(increment) + ". " + x)
            print("")
            increment += 1
    elif starChoice == 2: 
        for x in twoStar: 
            print(str(increment) + ". " + x)
            print("")
            increment += 1
    elif starChoice == 3: 
        for x in threeStar: 
            print(str(increment) + ". " + x)
            print("")
            increment += 1
    elif starChoice == 4: 
        for x in fourStar: 
            print(str(increment) + ". " + x)
            print("")
            increment += 1
    elif starChoice == 5: 
        for x in fiveStar: 
            print(str(increment) + ". " + x)
            print("")
            increment += 1
    else: 
        print("")
        print("Please enter a number 1 - 5.")

print("Welcome to Ted's Hotel!")
print("Please select which of the following options you would like to do\n")
print("1. Book a room")
print("2. Checkout")
print("3. Room service")
print("4. Read reviews") 
print("5. Exit\n")
choice = int(input("Enter your choice: "))
if choice == 1: 
    bookRoom() 
elif choice == 2: 
    checkout()
elif choice == 3: 
    roomService() 
elif choice == 4: 
    readReviews() 
elif choice == 5: 
    print("Thank you for coming to Ted's Hotel! We were honored to have you stay here")
else: 
    print("Please enter a number 1 - 5")
