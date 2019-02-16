def getinput():
    living_room_w = input("What is the width of the living room?\n")
    living_room_l = input("What is the length of the living room?\n")
    
    dining_room_w = input("What is the width of the dining room?\n")
    dining_room_l = input("What is the length of the dining room?\n")

    kitchen_w = input("What is the width of the kitchen?\n")
    kitchen_l = input("What is the length of the kitchen?\n")
    
    master_w = input("What is the width of the master bedroom?\n")
    master_l = input("What is the length of the master bedroom?\n")
    
    bedroom_1_w = input("What is the width of bedroom 1?\n")
    bedroom_1_l = input("What is the length of bedroom 1?\n")
    
    bedroom_2_w = input("What is the width of bedroom 2?\n")
    bedroom_2_l = input("What is the length of bedroom 2?\n")
    
    try:
        living_room = [int(living_room_w), int(living_room_l)]
        dining_room = [int(dining_room_w), int(dining_room_l)]
        kitchen = [int(kitchen_w), int(kitchen_l)]
        master = [int(master_w), int(master_l)]
        bedroom_1 = [int(bedroom_1_w), int(bedroom_1_l)]
        bedroom_2 = [int(bedroom_2_w), int(bedroom_2_l)]
                            
        print("It would take " + str(get_surface_area(living_room[0], living_room[1])/350.0) + " buckets to paint the living room") 
        print("It would take " + str(get_surface_area(dining_room[0], dining_room[1])/350.0) + " buckets to paint the dining room") 
        print("It would take " + str(get_surface_area(kitchen[0], kitchen[1])/350.0) + " buckets to paint the kitchen") 
        print("It would take " + str(get_surface_area(master[0], master[1])/350.0) + " buckets to paint the master bedroom") 
        print("It would take " + str(get_surface_area(bedroom_1[0], bedroom_1[1])/350.0) + " buckets to paint the first bedroom") 
        print("It would take " + str(get_surface_area(bedroom_2[0], bedroom_2[1])/350.0) + " buckets to paint the second bedroom") 
        
    except:
        print("Please enter valid dimensions")
        
def get_surface_area(length, width):
    celing = length * width
    wall1 = length*12
    wall2 = wall1
    wall3 = width*12
    wall4 = wall3
    return celing + wall1 + wall2 + wall3 + wall4

getinput()
    
