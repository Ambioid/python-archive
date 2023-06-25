raw_data = open("airports.txt", "r").read().split("\n")
data = []

for i in range(len(raw_data)):
    data.append(raw_data[i].split("|"))

codes = [item[0] for item in data][:len(data)-1]
aircrafts = [["medium narrow body", 8, 2650, 180, 8], ["large narrow body", 7, 5600, 220, 10], ["medium wide body", 5, 4050, 406, 14]]
craft_types = [item[0] for item in aircrafts]

uk_code = -1
airport_code = -1
aircraft_selection = -1
first_class_seats = -1



def airportDetails():

    global uk_code
    uk_code = str(input("Please Enter the Code for the UK Airport\n")).upper()
    if not (uk_code == "BOH" or uk_code == "LPL"):
        print("Error, Please Try Again.")
        uk_code = -1
        return True
    global airport_code

    airport_code = str(input("\nPlease Enter the overseas airport code\n")).upper()
    if airport_code in codes:
        print("Your airport is:", data[codes.index(airport_code)][1]) #Prints the name of the airport code

    else:
        print("Error, Please Try Again.")
        airport_code = -1
        return True
    print("Information Recorded, returning to main menu")
    return True

def flightDetails():
    global aircraft_selection
    aircraft_selection = str(input("Please Enter the Type of Aircraft\n")).lower()
    if aircraft_selection not in craft_types:
        print("Error, Please Try Again.")
        aircraft_selection = -1
        return True
    global craft
    craft = aircrafts[craft_types.index(aircraft_selection)]
    print(craft)
    #print(f'''Your aircraft Information: Type:{craft[0]}, Running Cost per seat per 100km:{craft[1]}, Minimum flight range(KM): {craft[2]}Capacity if all Seats are standard-Class:{craft[3]}, Minimum numbers of first-class seats (if there are any):{craft[4]}''' )  # Prints the Infor of the aircraft

    global first_class_seats
    first_class_seats = int(input("How many first-class Seats are there?\n"))

    if first_class_seats > 0:
        if first_class_seats < craft[4]: #If seats is not less than minimum
            print("Error, Selected number of seats is less than the minimum. Please Try Again.")
            first_class_seats = -1
            return True
        if first_class_seats > (craft[3]//2): # If selected seats is less than capacity if all seats are standard
            print("Error, selected seats is less than capacity if all seats are standard. Please Try Again.")
            first_class_seats = -1
            return True
    global standard_seats
    standard_seats = craft[3] - first_class_seats*2
    print("Amount of standard seats:", standard_seats)

    print("Information Recorded, returning to main menu")
    return True

    flight_details = str(input("Please Enter the Flight details"))

def calcPricePlan():
    if airport_code == -1 and uk_code == -1:
        print("You have not entered valid codes for UK and overseas airport yet!")
        return True
    if aircraft_selection == -1:
        print("You have not entered valid aircraft information yet!")
        return True
    if first_class_seats == -1:
        print("You have not entered valid seating information yet!")
        return True

    if uk_code == "LPL": # If airport is LPL, get distance data from there
        dist = int(data[codes.index(airport_code)][2])
    else:
        dist = int(data[codes.index(airport_code)][3])
    if craft[2] < dist: # If maximum flight distance is less than the airport distance
        print("The selected plan does not have enough range!")
        return True


    standard_cost = int(input("Please enter the cost of a standard claas seat!\n"))
    first_class_cost = int(input("Please enter the cost of a first clas seat! \n"))

    flight_cost_per_seat = craft[1]*dist/100
    flight_cost = flight_cost_per_seat*(first_class_seats + standard_seats)
    flight_income = first_class_seats * first_class_cost + standard_cost * standard_seats
    flight_profit = flight_income = flight_cost

    print(f'Flight Cost Per Seat: {flight_cost_per_seat}, Flight Cost: {flight_cost}, Flight Income: {flight_income}, Flight Profit: {flight_profit}')




    return True


print(data)
choice = 0

repeat = True
while repeat:
    while (choice >5 or choice < 1):
        choice = int(input("Please choose one of the three choices: \n 1: Enter Airport details\n 2: Enter Flight Details\n 3: Enter Price Plan\n 4: Clear Data\n 5: Quit\n"))


    if choice == 1:
        choice = 0
        repeat = airportDetails()
    elif choice == 2:
        choice = 0
        repeat = flightDetails()
    elif choice == 3:
        repeat = calcPricePlan()
        choice = 0
    elif choice == 4:
        uk_code = -1
        airport_code = -1
        aircraft_selection = -1
        first_class_seats = -1
    elif choice == 5:
        quit()
    print("")