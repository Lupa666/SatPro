import qam64_utils as qam64
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

coded_list = list()
"010010010001111111"
value = int("010010010001111111", 2)
coded_list.append(qam64.ints_map.get(int(value%64)))
value /= 64
coded_list.append(qam64.ints_map.get(int(value%64)))
value /= 64
coded_list.append(qam64.ints_map.get(int(value%64)))

# [ele.real for ele in data] 
x = [ele.real for ele in coded_list]
y = [ele.imag for ele in coded_list]

plt.scatter(x, y) 
plt.xlabel('Real') 
plt.ylabel('Imag') 
plt.grid()
plt.show() 

EbN0DB = np.arange(start=-10,stop=13,step=0.2)

BER_eq = erfc(np.sqrt(10**(EbN0DB/10)))/2

fig, ax = plt.subplots(nrows=1,ncols = 1)
#ax.semilogy(EbN0dBs,BER_sim,color='r',marker='o',linestyle='',label='BPSK Sim')
ax.semilogy(EbN0DB,BER_eq,marker='',linestyle='-',label='BPSK Theory')
ax.set_xlabel('$E_b/N_0(dB)$')
ax.set_ylabel('BER ($P_b$)')
ax.set_title('Probability of Bit Error for QAM64 over AWGN channel')
ax.set_xlim(-5,13);ax.grid(True)
ax.legend();plt.show()