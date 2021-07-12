import sys
import requests


endPoint = 'https://mach-eight.uc.r.appspot.com/'

from src.functions1 import On2
from src.functions2 import pandasMode
from src.functions3 import combinationsMode


def getInstances(wayToDo='pandas'):
    
    res = requests.get(endPoint)
    data = res.json().get('values',[])

    if len(sys.argv) > 1:
        totalHeight = int(sys.argv[1])
    else:
        totalHeight = int(input())

    
    if wayToDo == 'O(n^2)':
        On2(data, totalHeight)
    elif wayToDo == 'pandas':
        pandasMode(data, totalHeight)
    elif wayToDo == 'combinations':
        combinationsMode(data, totalHeight)


if __name__ == '__main__':
    getInstances('pandas')
