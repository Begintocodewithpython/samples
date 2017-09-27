# EG8-26 Pirate Treasure Tuple

def get_treasure_location():
    ''' 
    Get the location of the treasure
    returns a tuple:
    [0] is a string naming the landmark to start
    [1] is the number of paces north
    [2] is the number of paces east
    '''
    # get the location from the pirate
    return ('The old oak tree',20,30)

location=get_treasure_location()
print ('Start at',location[0], 'walk',location[1],'paces north','and', location[2],'paces south')
