import numpy as np
from scipy.special import erfc


M = 64 # wartość qam
k = np.log2(M) # ilość bitów
d = 2 # odległość amplitudy pomiędzy wartościami

# "{0:b}".format(value) - int do stringa bitowego
# int(value,2) - string bitowy do inta
# //64 - przesuń bity o 6
# %64 - wyciągnij 6 bitów

def b2i(input:str):
     return int(input,2)

def i2b(input:int):
     return "{0:b}".format(input)
     

map_string = dict()
for imag in [-7j,-5j,-3j,-1j,1j,3j,5j,7j]:
    for real in [-7,-5,-3,-1,1,3,5,7]:
        val = real+imag
        map_string[val] = ""
        pass

for i in  map_string.keys():
    match np.imag(i):
        case -7.0:
             map_string[i] += "000"
        case -5.0:
             map_string[i] += "001"
        case -3.0:
             map_string[i] += "011"
        case -1.0:
             map_string[i] += "010"
        case 1.0:
             map_string[i] += "110"
        case 3.0:
             map_string[i] += "111"
        case 5.0:
             map_string[i] += "101"
        case 7.0:
             map_string[i] += "100"
    match np.real(i):
        case -7.0:
             map_string[i] += "000"
        case -5.0:
             map_string[i] += "001"
        case -3.0:
             map_string[i] += "011"
        case -1.0:
             map_string[i] += "010"
        case 1.0:
             map_string[i] += "110"
        case 3.0:
             map_string[i] += "111"
        case 5.0:
             map_string[i] += "101"
        case 7.0:
             map_string[i] += "100"

ints_map = dict()

for i in  map_string:
     ints_map[int( map_string[i],2)] = i

# Returns a list of encoded complex values. Accepts a string.
def encode_complex_string(input: str):
    toReturn = list() 
    while input != "":
        toReturn.append(ints_map[int(input[-6:],2)])
        input = input[:-6]
        
    return toReturn

# Returns a list of encoded complex values. 
# Accepts a number and size. 
# If no size provided, last 0 might be omitted.
# Size represents number of 6 bit strings we want to encode.
def encode_complex_int(input: int, size = None):
    toReturn = list() 
    if size == None:
        while input != 0:
            toReturn.append(ints_map[input%64])
            input //= 64
        return toReturn
    for i in range(size):
         toReturn.append(ints_map[input%64])
         input //= 64
    return toReturn