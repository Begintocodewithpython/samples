# EG9-01 Pirate Treasure Dictionary
def get_treasure_location():
    ''' 
    Get the location of the treasure
    returns a dictionary:
    ['start'] is a string naming the landmark to start
    ['n'] is the number of paces north
    ['e'] is the number of paces east
    '''
    # get the location from the pirate
    return {'start':'The old oak tree','n':20,'e':30}

location=get_treasure_location()
print ('Start at',location['start'], 'walk',location['n'],'paces north','and', location['e'],'paces east')
