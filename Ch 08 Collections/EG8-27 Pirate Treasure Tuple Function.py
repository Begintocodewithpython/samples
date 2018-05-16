# EG8-27 Pirate Treasure Tuple Function

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

landmark, north, east = get_treasure_location()
print ('Start at',landmark, 'walk',north,'paces north and', east,'paces east')
