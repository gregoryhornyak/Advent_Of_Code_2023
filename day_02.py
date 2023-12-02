
def read_in_file():
    input_text = ""

    with open("input.txt","r") as f:
        input_text = f.read()

    games = input_text.split("\n")
    return games[0:-1]

# parse the lines into blue, red, green counter - into smallest datas

def flag_possibility(games):

    #count_of_red, count_of_blue, count_of_green = 0,0,0

    possible_count = 0
    records = {}

    for game in games:
        is_possible = True
        data = game.split(": ")[1]
        game_id = game.split(": ")[0]
        sets = data.split(";")
        
        records[game_id] = []
        for i in range(len(sets)): # for each set
            ind_set = sets[i].split(",")
            temp_dict = {}
            for j in range(len(ind_set)):
                show = ind_set[j]
                show = show.strip(" ")
                show_details = show.split(" ")
                count = int(show_details[0])
                colour = show_details[1]
                if (colour == "red" and count > 12) or (colour == "green" and count > 13) or (colour == "blue" and count > 14):
                    is_possible = False
                
                temp_dict[colour] = count
            records[game_id].append(temp_dict)
        game_id_num = int(game_id.split(" ")[1])
        if is_possible:
            possible_count+=game_id_num
    #print(records)
    print("Possible games id sum:",possible_count)
    return records
            
def find_max(records):
    #'Game 100': 
    # [ {'green': 12, 'blue': 8, 'red': 2}, 
    #   {'blue': 7, 'red': 14, 'green': 8}, 
    #   {'red': 14, 'blue': 1, 'green': 4} ]
    total_sum = 0
    for game_id, game in records.items():
        # check green
        green_ids_list = [] # ser num = order in list 
        for i in range(len(game)):
            if "green" in game[i]:
                green_ids_list.append(game[i]["green"])
        # check red
        red_ids_list = []
        for i in range(len(game)):
            if "red" in game[i]:
                red_ids_list.append(game[i]["red"])
        # check blue
        blue_ids_list = []
        for i in range(len(game)):
            if "blue" in game[i]:
                blue_ids_list.append(game[i]["blue"])
        red_max = max(red_ids_list)
        green_max = max(green_ids_list)
        blue_max = max(blue_ids_list)
        # assume no empty lists
        the_power = red_max*green_max*blue_max
        #print(game_id,":",the_power)
        total_sum += the_power
    print("Total sum of all powers:",total_sum)


def main():
    lines = read_in_file()
    records = flag_possibility(lines)
    find_max(records)

main()
