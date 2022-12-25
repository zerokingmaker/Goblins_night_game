gamers = []
def add_gamer(gamer, gamers_list) :
    if "name" not in gamer or "availability" not in gamer :
        return "Incorrect Data"
    else :
        gamers_list.append(gamer)
        
kimberly = {"name" : "Kimberly Warner", "availability" : ["Monday", "Tuesday", "Fridays"]}
add_gamer(kimberly, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
print(gamers)

def build_daily_frequency_table() :
    return {"Monday" : 0, "Tuesday" : 0, "Wednesday" : 0, "Thursday" : 0, "Friday" : 0, "Saturday" : 0, "Sunday" : 0}
    
count_availability = build_daily_frequency_table()


def calculate_availability(gamers_list, available_frequency) :
    for gamer in gamers_list :
        for available_day in gamer["availability"] :
            if available_day in available_frequency :
                available_frequency[available_day] += 1

calculate_availability(gamers, count_availability)

print(count_availability)

def find_best_night(availability_table) :
    biggest_frequency =  max(availability_table.values())
    most_frequent_day = ''
    for day, frequency in availability_table.items() :
        if frequency == biggest_frequency :
            most_frequent_day = day
    return most_frequent_day

game_night = find_best_night(count_availability)

def available_on_night(gamers_list, day) :
    available_gamers = []
    for gamer in gamers_list :
        if day in gamer["availability"] :
            available_gamers.append(gamer["name"])
    return available_gamers

attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)

form_email = "Hello {name} ! We will be playing {game} on {day_of_week} ! Hope to see you there !"

def send_email(gamers_who_can_attend, day, game) :
    for gamer in gamers_who_can_attend :
        print(form_email.format(name = gamer, game = game, day_of_week = day))

send_email(attending_game_night, game_night, "Abruptly Golblins!")

unable_to_attend_best_night = []
for gamer in gamers :
    if gamer["name"] not in attending_game_night :
        unable_to_attend_best_night.append(gamer)

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)

send_email(available_second_game_night, second_night, "Abruptly Goblins!")
