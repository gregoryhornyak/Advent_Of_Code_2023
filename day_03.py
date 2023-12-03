"""
1. read in input
2. find symbols' coordinates
3. assign coordinates to every number every digit, into a collection
 like in Battleships: 
 
 889 is {ser_num: {num: 889, coords: [[0,0],[1,0],[2,0]] } } 

4. find numbers around symbols - adjacent to a symbol (+diagonally)
5. collect them into a list
"""

def read_in_file():
    input_text = ""

    with open("input3.txt","r") as f:
        input_text = f.read()

    games = input_text.split("\n")
    return games[0:-1]

symbols_list = ["*","/","+","@","$","%","#","&","=","-"]

symbols_loc_list = [] # ["*",[x,y]]

numbers_list = {}

def scan_schematic(input):
    number_counter = 0
    y=0
    x=0
    while y < len(input): 
        x=0
        while x < len(input[y]): 
            if input[y][x] in symbols_list:
                temp_coords = [x,y]
                symbols_loc_list.append([input[y][x],temp_coords])
            if input[y][x].isnumeric(): #is digit
                temp_dict = {}
                temp_dict["num"] = input[y][x]
                temp_dict["coords"] = []
                temp_dict["coords"].append([x,y])
                # scan following characters
                #* only working up to 3 digit numbers  
                if x<len(input[y])-1 and input[y][x+1].isnumeric(): #is digit
                    temp_dict["num"]+=input[y][x+1]
                    temp_dict["coords"].append([x+1,y])
                    if x<len(input[y])-2 and input[y][x+2].isnumeric():
                        temp_dict["num"]+=input[y][x+2]
                        temp_dict["coords"].append([x+2,y])
                        x+=1
                    x+=1
                numbers_list[number_counter] = temp_dict
                number_counter+=1
            x+=1
        y+=1

    total_sum = 0
    total_multi_sum = 0
    for sym in symbols_loc_list: # for each symbol
        sym_coords = sym[1]
        symbol = sym[0]
        temp_numbers_seen = []
        match_counter = 0
        gear_numbers = []
        for ser_num,num_details in numbers_list.items(): # for each number
            # create 3x3 array extension of sym_coords
            for ext_x in range(sym_coords[0]-1,sym_coords[0]+2):
                for ext_y in range(sym_coords[1]-1,sym_coords[1]+2):
                    temp_coord = [ext_x,ext_y]
                    if temp_coord in num_details["coords"]: # if around symbol
                        #* bingo!
                        
                        if ser_num not in temp_numbers_seen:
                            if symbol == "*": # gear
                                match_counter+=1
                                gear_numbers.append(int(num_details["num"]))
                            total_sum += int(num_details["num"])
                            temp_numbers_seen.append(ser_num)
                    
            # check if gear, with two matches
            
        if match_counter == 2:
            total_multi_sum += (gear_numbers[0]*gear_numbers[1])
        match_counter = 0
        gear_numbers = []                

    print("total_sum:",total_sum)
    print("total_multi_sum:",total_multi_sum)





    

scan_schematic(read_in_file())