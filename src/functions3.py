from itertools import combinations

from . import formatter, message

def combinationsMode(data, totalHeight, fromDict=True):
    """I used the itertools tool to generate the combined list of possible iterations "combinations" and then went through it

    Args:
        data (list): List of data that will be combined
        
        totalHeight (int): Data provided by the user for the search
        
        fromDict (bool, optional): Tells us if the data that is entered is 
        with the data from the specified path or is a list of integers . 
        Defaults to True.
    """
    counter = 0
    if fromDict:
        for i,j in combinations(data, 2):
            if int(i['h_in'])+int(j['h_in']) == totalHeight:
                print(formatter(i['first_name'], i['last_name'], j['first_name'], j['last_name']))
                counter+=1
    else:
        for i,j in combinations(data, 2):
            heightSum = int(i)+int(j)
            if heightSum == totalHeight:
                print(f'{i}-{j}')
                counter+=1
    if counter < 1:
        print(message)