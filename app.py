import qam64_utils as qam64
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.special import erfc



test_stream = "000000000011101010010101110001111111"
value = qam64.b2i(test_stream)
size = math.ceil(len(test_stream)/6)

string_output = 0
int_output = 0
int_output_size = 0

string_output = qam64.encode_complex_string(test_stream)

int_output = qam64.encode_complex_int(value)

int_output_size = qam64.encode_complex_int(value, size)

print("string", string_output)
print("int no size",int_output)
print("int size", int_output_size)



# [ele.real for ele in data] 
x = [ele.real for ele in int_output_size]
y = [ele.imag for ele in int_output_size]

plt.scatter(x, y) 
plt.xlabel('Real') 
plt.ylabel('Imag') 
plt.grid()
plt.show() 

EbN0DB = np.arange(start=-10,stop=13,step=0.2)

BER_eq = erfc(np.sqrt(10**(EbN0DB/10)))/qam64.M

fig, ax = plt.subplots(nrows=1,ncols = 1)
#ax.semilogy(EbN0dBs,BER_sim,color='r',marker='o',linestyle='',label='BPSK Sim')
ax.semilogy(EbN0DB,BER_eq,marker='',linestyle='-',label='QAM64 Theory')
ax.set_xlabel('$E_b/N_0(dB)$')
ax.set_ylabel('BER ($P_b$)')
ax.set_title('Probability of Bit Error for QAM64')
ax.set_xlim(-5,13);ax.grid(True)
ax.legend();plt.show()