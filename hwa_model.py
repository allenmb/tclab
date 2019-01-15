from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt

m = GEKKO()
m.time = np.linspace(0,1200,1201)

Q = m.Param(value=100) 			#% heater
T0 = m.Param(value=23+273.15)	#K
U = m.Param(value=10)			#W/m2K
mass = m.Param(value=4/1000)	#kg
cp = m.Param(value=0.5*1000)	#J/kgK
A = m.Param(value=12/100**2)	#m2
alpha = m.Param(value=0.01)		#W/% heater
eps = m.Param(value=0.9)		#emissivity
sig = m.Const(5.67e-8)			#stef-boltz const

T = m.Var(value=T0)
m.Equation(mass * cp * T.dt() == U * A * (T0-T) + eps*sig*A*(T0**4 - T**4) + alpha * Q)

m.options.IMODE = 4

m.solve()
plt.plot(m.time,T.value)
plt.savefig("simulation1.png")
print(T.value[-1])
print((T.value[-1]-273.15)*9/5 + 32)
plt.show()
