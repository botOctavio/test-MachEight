from random import sample
from matplotlib import pyplot as plt
import requests

from app import On2, pandasMode,combinationsMode, numpyIterTools, endPoint

n = 6

def On2Test(x):
    return On2(x, n, False)
def PandasTest(x):
    pandasMode(x, n, False)
def CombinationsTest(x):
    combinationsMode(x, n, False)

# Other authors
def NumpyIter(x):
    numpyIterTools(x, n, False)


from simple_benchmark import benchmark
from iteration_utilities import first
data = requests.get(endPoint).json().get('values',[])
b = benchmark(
    [On2Test, PandasTest, CombinationsTest],#, NumpyIter],
    {2**i: set(range(2**i)) for i in range(1, 12)},
    argument_name='set size',
    function_aliases={first: 'First'}
)

b.plot()
plt.show()