import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.special import erfc
from commpy import QAMModem
from commpy.channelcoding import Trellis, conv_encode, viterbi_decode


"""
INICJALIZACJA KLAS, MODUŁÓW I WARTOŚCI POCZĄTKOWYCH
"""

memory = np.array([2])
gMatrix = np.array([[0o5,0o7]])
ENCODER = Trellis(memory=memory, g_matrix=gMatrix)
qamSize = 64
QAM64 = QAMModem(qamSize)
noiseVar = 0.2

"""
GENEROWANIE DANYCH
"""

toCode = np.random.randint(0,2,32)

"""
KODOWANIE
"""
toModulate = conv_encode(toCode, ENCODER)
print("Przed zakodowaniem: \t", toCode)

"""
MODULACJA
"""
value = QAM64.modulate(toModulate)
print("Zmodulowane: \t\t",value)

"""
KANAŁ TRANSMISYJNY - TODO ZAIMPLEMENOTWAĆ
"""

"""
DEMODULACJA
"""
demodulated = QAM64.demodulate(value, 'soft', noise_var=0.2)

"""
DEKODOWANIE
"""
decoded = np.array(viterbi_decode(demodulated, ENCODER,5*(2+1), 'unquantized'))
decoded = decoded[0:-4]
print("Zdekodowane: \t\t", decoded)

exit()

"""
WYKRESY
"""
x = [ele.real for ele in value]
y = [ele.imag for ele in value]

plt.scatter(x, y) 
plt.xlabel('Real') 
plt.ylabel('Imag') 
plt.grid()
plt.show() 

EbN0DB = np.arange(start=-10,stop=13,step=0.2)

BER_eq = erfc(np.sqrt(10**(EbN0DB/10)))/64

fig, ax = plt.subplots(nrows=1,ncols = 1)
#ax.semilogy(EbN0dBs,BER_sim,color='r',marker='o',linestyle='',label='BPSK Sim')
ax.semilogy(EbN0DB,BER_eq,marker='',linestyle='-',label='QAM64 Theory')
ax.set_xlabel('$E_b/N_0(dB)$')
ax.set_ylabel('BER ($P_b$)')
ax.set_title('Probability of Bit Error for QAM64')
ax.set_xlim(-5,13);ax.grid(True)
ax.legend();plt.show()