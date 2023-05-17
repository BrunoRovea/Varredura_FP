#%%
import numpy as np


# Bibliotecas para conversão polat <-> retangular
def pol2ret(abs, angles):
    return abs * np.exp(1j*angles)


def ret2pol(x):
    return abs(x), np.rad2deg(np.angle(x))


# Tolerância especificada
tol = 1E-8


# Impedância da linha de distribuição em ohm/km
Z_ld = 0.6045 + 0.4290j

# Impedância das LD em Ohms
Z_12=0.20209*(Z_ld)
Z_23=0.42971*(Z_ld)
Z_24=0.59489*(Z_ld)
Z_25=0.69728*(Z_ld)


# Potência inicial em cada nó
FP = 0.9
phi = np.arccos(0.9)

S1_in = 10000E3*np.exp(1j*phi)
S2_in = 320E3*np.exp(1j*phi)
S3_in = 320E3*np.exp(1j*phi)
S4_in = 320E3*np.exp(1j*phi)
S5_in = 320E3*np.exp(1j*phi)


# Tensão inicial em cada nó
V1 = 35.535E3
V2 = 35.535E3
V3 = 35.535E3
V4 = 35.535E3
V5 = 35.535E3



err = 100
k = 0
while(err>tol):
    #Backward sweep
    i3 = np.conjugate(S3_in/V3)
    i4 = np.conjugate(S4_in/V4)
    i5 = np.conjugate(S5_in/V5)
    i2 = np.conjugate(S2_in/V2)
    i1 = i2 + i3 + i4 + i5

    #Forward Sweep
    V2 = V1 - i1*Z_12
    V3 = V2 - i3*Z_23
    V4 = V2 - i4*Z_24
    V5 = V2 - i5*Z_25

    #Potência injetada nas barras
    S1 = V1*np.conj(i1)
    S3 = V3*np.conj(i3)
    S4 = V4*np.conj(i4)
    S5 = V5*np.conj(i5)
    S2 = V2*np.conj(i2)

    err = max(np.abs(S2-S2_in), np.abs(S3-S3_in), np.abs(S4-S4_in), np.abs(S5-S5_in))
    k += 1


print('Corrente nos ramos:')
print('Corrente no ramo 5:', i5)
print('Corrente no ramo 4:', i4)
print('Corrente no ramo 3:', i3)
print('Corrente no ramo 2:', i2)
print('Corrente no ramo 1:', i1)
print('----------------------------------------------')

print('Tensão nas barras:')
print('Tensão na barra 1:', V5)
print('Tensão na barra 2:', V4)
print('Tensão na barra 3:', V3)
print('Tensão na barra 4:', V2)
print('Tensão na barra 5:', V1)
print('----------------------------------------------')

print('Potência injetada nas barras:')
print('Potência injetada na barra 1:', S5)
print('Potência injetada na barra 2:', S4)
print('Potência injetada na barra 3:', S3)
print('Potência injetada na barra 4:', S2)
print('Potência injetada na barra 5:', S1)
print('----------------------------------------------')

print('Total de iterações:', k)
print('Erro', err)

print('Teste git')

# %%
