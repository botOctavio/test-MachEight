from . import formatter, message

def On2(data : list, totalHeight: int, fromDict=True):
    """This algorithm represents the O (n ^ 2) optimization and it does not 
    need to do what it should do, it only represents the upper limit of the
    test on python

    Args:
        data (list): List of data that will be combined
        
        totalHeight (int): Data provided by the user for the search
        
        fromDict (bool, optional): Tells us if the data that is entered is 
        with the data from the specified path or is a list of integers . 
        Defaults to True.
    """
    counter = 0
    if fromDict:
        for i in data:
            for j in data:
                height= int(i['h_in'])+int(j['h_in'])
                counter+=1

                if height == totalHeight:
                    print(
                        formatter(
                            i['first_name'], 
                            i['last_name'], 
                            j['first_name'], 
                            j['last_name']
                        )
                    )
    else:
        for i in data:
            for j in data:
                height = int(i)+int(j)
                if height == totalHeight:
                    print(f'{i}-{j}')
    if counter < 1:
        print(message)