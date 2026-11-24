# INCREDIBLE INDIA - Terminal Version
# Run with:  python terminal_app.py

# ---------------- DATA ----------------
# For every state: capital, tourist places, food, culture and best time to visit.
state_info = {
    "Andaman and Nicobar Islands": {
        "capital": "Port Blair",
        "places": ["Cellular Jail", "Radhanagar Beach", "Ross Island"],
        "food": "Seafood, fish curry and coconut-based dishes",
        "culture": "Island culture, tribal heritage and coastal traditions",
        "best_time": "October to May"
    },
    "Andhra Pradesh": {
        "capital": "Amaravati",
        "places": ["Tirupati Temple", "Araku Valley", "Borra Caves"],
        "food": "Pulihora, gongura pachadi and Andhra meals",
        "culture": "Kuchipudi dance, Telugu literature and temple traditions",
        "best_time": "October to March"
    },
    "Arunachal Pradesh": {
        "capital": "Itanagar",
        "places": ["Tawang Monastery", "Sela Pass", "Ziro Valley"],
        "food": "Thukpa, momos and local rice dishes",
        "culture": "Many indigenous communities, festivals and crafts",
        "best_time": "October to April"
    },
    "Assam": {
        "capital": "Dispur",
        "places": ["Kaziranga National Park", "Kamakhya Temple", "Majuli Island"],
        "food": "Assamese thali, khar and tenga fish curry",
        "culture": "Bihu, Sattriya dance, silk weaving and tea heritage",
        "best_time": "November to April"
    },
    "Bihar": {
        "capital": "Patna",
        "places": ["Mahabodhi Temple", "Nalanda", "Rajgir"],
        "food": "Litti chokha, sattu paratha and thekua",
        "culture": "Buddhist and Jain heritage, Chhath Puja and Madhubani art",
        "best_time": "October to March"
    },
    "Chandigarh": {
        "capital": "Chandigarh",
        "places": ["Rock Garden", "Sukhna Lake", "Capitol Complex"],
        "food": "Chole bhature, parathas and Punjabi dishes",
        "culture": "Planned-city architecture, gardens and Punjabi culture",
        "best_time": "September to March"
    },
    "Chhattisgarh": {
        "capital": "Raipur",
        "places": ["Chitrakote Falls", "Bastar", "Barnawapara Wildlife Sanctuary"],
        "food": "Chila, fara and local rice dishes",
        "culture": "Tribal art, folk dances and Bastar Dussehra",
        "best_time": "October to March"
    },
    "Dadra and Nagar Haveli and Daman and Diu": {
        "capital": "Daman",
        "places": ["Diu Fort", "Nagoa Beach", "Dudhni Lake"],
        "food": "Gujarati dishes and coastal seafood",
        "culture": "Coastal traditions, Portuguese heritage and local festivals",
        "best_time": "October to March"
    },
    "Delhi": {
        "capital": "New Delhi",
        "places": ["Red Fort", "Qutub Minar", "Humayun's Tomb"],
        "food": "Chole bhature, parathas and chaat",
        "culture": "Mughal heritage, museums, festivals and food markets",
        "best_time": "October to March"
    },
    "Goa": {
        "capital": "Panaji",
        "places": ["Basilica of Bom Jesus", "Baga Beach", "Fort Aguada"],
        "food": "Goan fish curry, bebinca and coconut-based dishes",
        "culture": "Portuguese-influenced architecture, music and festivals",
        "best_time": "November to February"
    },
    "Gujarat": {
        "capital": "Gandhinagar",
        "places": ["Statue of Unity", "Rann of Kutch", "Somnath Temple"],
        "food": "Dhokla, thepla, khakhra and Gujarati thali",
        "culture": "Garba, Navratri, textiles and handicrafts",
        "best_time": "October to March"
    },
    "Haryana": {
        "capital": "Chandigarh",
        "places": ["Kurukshetra", "Sultanpur National Park", "Morni Hills"],
        "food": "Bajra khichdi, kadhi and roti with lassi",
        "culture": "Folk music, ragini, wrestling traditions and fairs",
        "best_time": "October to March"
    },
    "Himachal Pradesh": {
        "capital": "Shimla",
        "places": ["Shimla", "Manali", "Dharamshala"],
        "food": "Dham, siddu and madra",
        "culture": "Mountain festivals, traditional crafts and folk dances",
        "best_time": "March to June; December to February for snow"
    },
    "Jammu and Kashmir": {
        "capital": "Srinagar (summer), Jammu (winter)",
        "places": ["Dal Lake", "Gulmarg", "Pahalgam"],
        "food": "Kashmiri wazwan dishes, kahwa and rogan josh",
        "culture": "Kashmiri crafts, music, gardens and traditional festivals",
        "best_time": "March to October"
    },
    "Jharkhand": {
        "capital": "Ranchi",
        "places": ["Betla National Park", "Hundru Falls", "Deoghar"],
        "food": "Dhuska, thekua and litti",
        "culture": "Tribal music, dance, festivals and handicrafts",
        "best_time": "October to March"
    },
    "Karnataka": {
        "capital": "Bengaluru",
        "places": ["Hampi", "Mysore Palace", "Coorg"],
        "food": "Bisi bele bath, dosa, idli and Mysore pak",
        "culture": "Yakshagana, classical music, palaces and heritage sites",
        "best_time": "October to March"
    },
    "Kerala": {
        "capital": "Thiruvananthapuram",
        "places": ["Alleppey Backwaters", "Munnar", "Kochi"],
        "food": "Appam, puttu, avial and Kerala sadya",
        "culture": "Kathakali, boat races, Onam and Ayurveda traditions",
        "best_time": "September to March"
    },
    "Ladakh": {
        "capital": "Leh",
        "places": ["Pangong Lake", "Nubra Valley", "Thiksey Monastery"],
        "food": "Thukpa, skyu and butter tea",
        "culture": "Buddhist monasteries, mountain festivals and local crafts",
        "best_time": "May to September"
    },
    "Lakshadweep": {
        "capital": "Kavaratti",
        "places": ["Agatti Island", "Bangaram Island", "Kavaratti"],
        "food": "Tuna dishes, coconut rice and local seafood",
        "culture": "Island traditions, folk dances and maritime heritage",
        "best_time": "October to March"
    },
    "Madhya Pradesh": {
        "capital": "Bhopal",
        "places": ["Khajuraho Temples", "Sanchi Stupa", "Kanha National Park"],
        "food": "Poha-jalebi, dal bafla and bhutte ka kees",
        "culture": "Tribal art, classical dance and historic architecture",
        "best_time": "October to March"
    },
    "Maharashtra": {
        "capital": "Mumbai",
        "places": ["Gateway of India", "Ajanta Caves", "Ellora Caves"],
        "food": "Vada pav, misal pav and puran poli",
        "culture": "Ganesh Chaturthi, Lavani, forts and Marathi theatre",
        "best_time": "October to March"
    },
    "Manipur": {
        "capital": "Imphal",
        "places": ["Loktak Lake", "Kangla Fort", "Keibul Lamjao National Park"],
        "food": "Eromba, singju and local rice dishes",
        "culture": "Manipuri classical dance, handloom and Sangai Festival",
        "best_time": "October to March"
    },
    "Meghalaya": {
        "capital": "Shillong",
        "places": ["Living Root Bridges", "Cherrapunji", "Dawki"],
        "food": "Jadoh, dohneiiong and tungrymbai",
        "culture": "Khasi, Garo and Jaintia traditions, music and festivals",
        "best_time": "October to April"
    },
    "Mizoram": {
        "capital": "Aizawl",
        "places": ["Vantawng Falls", "Reiek", "Aizawl"],
        "food": "Bai, sawhchiar and local bamboo-shoot dishes",
        "culture": "Cheraw bamboo dance, handloom and Chapchar Kut",
        "best_time": "October to March"
    },
    "Nagaland": {
        "capital": "Kohima",
        "places": ["Dzukou Valley", "Kohima War Cemetery", "Khonoma Village"],
        "food": "Smoked dishes, bamboo-shoot dishes and rice",
        "culture": "Naga tribal traditions, crafts and Hornbill Festival",
        "best_time": "October to May"
    },
    "Odisha": {
        "capital": "Bhubaneswar",
        "places": ["Konark Sun Temple", "Jagannath Temple", "Chilika Lake"],
        "food": "Dalma, pakhala bhata and chhena poda",
        "culture": "Odissi dance, Pattachitra art and Rath Yatra",
        "best_time": "October to March"
    },
    "Puducherry": {
        "capital": "Puducherry",
        "places": ["Promenade Beach", "Auroville", "French Quarter"],
        "food": "South Indian dishes and French-influenced cuisine",
        "culture": "French colonial architecture, Tamil traditions and festivals",
        "best_time": "October to March"
    },
    "Punjab": {
        "capital": "Chandigarh",
        "places": ["Golden Temple", "Jallianwala Bagh", "Wagah Border ceremony"],
        "food": "Sarson da saag, makki di roti and lassi",
        "culture": "Bhangra, Giddha, Punjabi music and harvest festivals",
        "best_time": "October to March"
    },
    "Rajasthan": {
        "capital": "Jaipur",
        "places": ["Hawa Mahal, Jaipur", "Jaisalmer Fort", "Lake Pichola, Udaipur", "Ranthambore National Park"],
        "food": "Dal baati churma, gatte ki sabzi and ker sangri",
        "culture": "Ghoomar, folk music, colourful handicrafts and desert festivals",
        "best_time": "October to March"
    },
    "Sikkim": {
        "capital": "Gangtok",
        "places": ["Tsomgo Lake", "Nathula Pass", "Rumtek Monastery"],
        "food": "Momos, thukpa and gundruk",
        "culture": "Buddhist monasteries, Losar and traditional dances",
        "best_time": "March to May; October to December"
    },
    "Tamil Nadu": {
        "capital": "Chennai",
        "places": ["Meenakshi Amman Temple", "Mahabalipuram", "Ooty"],
        "food": "Idli, dosa, pongal and Chettinad dishes",
        "culture": "Bharatanatyam, Carnatic music, temple architecture and Pongal",
        "best_time": "November to March"
    },
    "Telangana": {
        "capital": "Hyderabad",
        "places": ["Charminar", "Golconda Fort", "Ramappa Temple"],
        "food": "Hyderabadi biryani, haleem and double ka meetha",
        "culture": "Bonalu, Bathukamma, Deccani heritage and crafts",
        "best_time": "October to March"
    },
    "Tripura": {
        "capital": "Agartala",
        "places": ["Ujjayanta Palace", "Neermahal", "Unakoti"],
        "food": "Mui borok and chakhwi",
        "culture": "Tribal festivals, bamboo crafts and traditional dance",
        "best_time": "October to March"
    },
    "Uttar Pradesh": {
        "capital": "Lucknow",
        "places": ["Taj Mahal", "Varanasi ghats", "Fatehpur Sikri"],
        "food": "Awadhi kebabs, chaat, kachori and peda",
        "culture": "Kathak, classical music, religious heritage and crafts",
        "best_time": "October to March"
    },
    "Uttarakhand": {
        "capital": "Dehradun (winter), Gairsain (summer)",
        "places": ["Kedarnath Temple", "Nainital", "Valley of Flowers"],
        "food": "Kafuli, aloo ke gutke and bal mithai",
        "culture": "Garhwali and Kumaoni traditions, folk music and fairs",
        "best_time": "March to June; September to November"
    },
    "West Bengal": {
        "capital": "Kolkata",
        "places": ["Victoria Memorial", "Darjeeling", "Sundarbans"],
        "food": "Macher jhol, shorshe ilish and mishti doi",
        "culture": "Durga Puja, Baul music, literature and crafts",
        "best_time": "October to March"
    },
}

# ---------------- HELPER FUNCTIONS ----------------

def find_state(state_name):
    """Find a state without case sensitivity."""
    for name in state_info:
        if name.lower() == state_name.strip().lower():
            return name
    return None


def show_state_details(state_name):
    """Display complete tourism information for one state."""
    details = state_info[state_name]

    print("\n" + "=" * 45)
    print("          " + state_name.upper())
    print("=" * 45)
    print("Capital       :", details["capital"])
    print("Best time     :", details["best_time"])
    print("Famous food   :", details["food"])
    print("Culture       :", details["culture"])
    print("Tourist places:")

    for place in details["places"]:
        print("  -", place)


def show_all_states():
    """Print all available states and union territories."""
    print("\nINDIAN STATES AND UNION TERRITORIES")
    print("-" * 40)
    for number, name in enumerate(state_info, start=1):
        print(str(number) + ".", name)


def search_tourist_place():
    """Search a tourist place and show the state where it is listed."""
    place_name = input("Enter tourist place name: ").strip().lower()
    found = False

    for state, details in state_info.items():
        for place in details["places"]:
            if place_name in place.lower():
                print("\nPlace:", place)
                print("State:", state)
                print("Capital:", details["capital"])
                found = True

    if not found:
        print("Sorry, this place was not found in our data.")
        print("Try another spelling or search a shorter name.")


def smart_trip_planner():
    """Create a simple day-wise plan from the listed tourist places."""
    state_input = input("Enter state name: ").strip()
    state = find_state(state_input)

    if state is None:
        print("State not found. Please check the spelling.")
        return

    try:
        days = int(input("How many days is your trip? "))
        if days <= 0:
            print("Please enter at least 1 day.")
            return
    except ValueError:
        print("Please enter the number of days in digits.")
        return

    places = state_info[state]["places"]
    print("\nYour", days, "day trip plan for", state)
    print("Best time to visit:", state_info[state]["best_time"])

    for day in range(1, days + 1):
        place_index = (day - 1) % len(places)
        print("Day", day, ": Visit", places[place_index])

    print("Note: This is a sample plan. Travel time and opening hours are not included.")


def travel_budget_calculator():
    """Calculate an estimated trip budget using user-entered costs."""
    try:
        days = int(input("Enter number of travel days: "))
        hotel_per_day = float(input("Enter hotel cost per day (Rs): "))
        food_per_day = float(input("Enter food cost per day (Rs): "))
        travel_per_day = float(input("Enter local travel cost per day (Rs): "))

        if days <= 0 or hotel_per_day < 0 or food_per_day < 0 or travel_per_day < 0:
            print("Days must be positive and costs cannot be negative.")
            return

        hotel_total = days * hotel_per_day
        food_total = days * food_per_day
        travel_total = days * travel_per_day
        total = hotel_total + food_total + travel_total

        print("\n------- ESTIMATED TRIP BUDGET -------")
        print("Hotel cost : Rs", round(hotel_total, 2))
        print("Food cost  : Rs", round(food_total, 2))
        print("Travel cost: Rs", round(travel_total, 2))
        print("Total      : Rs", round(total, 2))
        print("------------------------------------")
    except ValueError:
        print("Invalid input. Please enter numbers only.")


def compare_two_states():
    """Compare tourism information for two states."""
    first_input = input("Enter first state: ").strip()
    second_input = input("Enter second state: ").strip()
    first = find_state(first_input)
    second = find_state(second_input)

    if first is None or second is None:
        print("One or both state names were not found.")
        return

    if first == second:
        print("Please enter two different states to compare.")
        return

    first_data = state_info[first]
    second_data = state_info[second]

    print("\n=========== STATE COMPARISON ===========")
    print("First state :", first)
    print("Capital     :", first_data["capital"])
    print("Food        :", first_data["food"])
    print("Culture     :", first_data["culture"])
    print("Best time   :", first_data["best_time"])
    print("Tourist places:", ", ".join(first_data["places"]))

    print("\nSecond state:", second)
    print("Capital     :", second_data["capital"])
    print("Food        :", second_data["food"])
    print("Culture     :", second_data["culture"])
    print("Best time   :", second_data["best_time"])
    print("Tourist places:", ", ".join(second_data["places"]))
    print("========================================")


def manage_favourites(favourites):
    """Add a tourist place to favourites or display saved favourites."""
    print("\n1. Add a favourite place")
    print("2. Show favourite places")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        place_name = input("Enter place name: ").strip()
        found_place = None

        for details in state_info.values():
            for place in details["places"]:
                if place.lower() == place_name.lower():
                    found_place = place
                    break
            if found_place:
                break

        if found_place:
            if found_place not in favourites:
                favourites.append(found_place)
                print(found_place, "added to your favourites!")
            else:
                print("This place is already in your favourites.")
        else:
            print("Place not found in our tourism data.")

    elif choice == "2":
        if len(favourites) == 0:
            print("Your favourites list is empty.")
        else:
            print("\nYOUR FAVOURITE PLACES")
            for number, place in enumerate(favourites, start=1):
                print(str(number) + ".", place)
    else:
        print("Invalid choice.")


# ---------------- MAIN PROGRAM ----------------

def main():
    """Display the menu and run the selected feature."""
    favourites = []

    print("=" * 48)
    print("          INCREDIBLE INDIA")
    print("       SMART TOURISM EXPLORER")
    print("=" * 48)

    while True:
        print("\n--------------- MAIN MENU ---------------")
        print("1. Explore a State")
        print("2. Show All States")
        print("3. Search Tourist Place")
        print("4. Smart Trip Planner")
        print("5. Travel Budget Calculator")
        print("6. Compare Two States")
        print("7. Favourite Places")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            state_input = input("Enter state name: ").strip()
            state = find_state(state_input)
            if state:
                show_state_details(state)
            else:
                print("State not found. Please check the spelling.")

        elif choice == "2":
            show_all_states()

        elif choice == "3":
            search_tourist_place()

        elif choice == "4":
            smart_trip_planner()

        elif choice == "5":
            travel_budget_calculator()

        elif choice == "6":
            compare_two_states()

        elif choice == "7":
            manage_favourites(favourites)

        elif choice == "8":
            print("Thank you for using Incredible India. Happy travelling!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


# Start the program
if __name__ == "__main__":
    main()
