import numpy as np
import matplotlib.pylab as plt

t1 = 61.13
t2 = 60.28
t3 = 60.59
t4 = 60.52
t5 = 60.39
t6 = 62.17

x1 = 4
x2 = 10
x3 = 12
x4 = 80
x5 = 50
x6 = 40

y1 = 100
y2 = 5
y3 = 80
y4 = 50
y5 = 50
y6 = 200

var_y1 = np.var(t1)
var_y2 = np.var(t2)
var_y3 = np.var(t3)
var_y4 = np.var(t4)
var_y5 = np.var(t5)
var_y6 = np.var(t6)

def modelo(x,t):
	xt=x*t
	return xt

def chi(y_obs, y_mod):
    chi = 0.5*np.sum((y_obs-y_mod)**2/var_y1)
    return np.exp(-chi)

caminata1=[]
caminata2=[]
caminata3=[]
caminata4=[]
caminata5=[]
caminata6=[]
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []

b1.append(x1)
b2.append(x2)
b3.append(x3)
b4.append(x4)
b5.append(x5)
b6.append(x6)

iteraciones=10

ymodelo1 = modelo(b1[0], t1)
ymodelo2 = modelo(b2[0], t2)
ymodelo3 = modelo(b3[0], t3)
ymodelo4 = modelo(b4[0], t4)
ymodelo5 = modelo(b5[0], t5)
ymodelo6 = modelo(b6[0], t6)

caminata1.append(chi(y1,ymodelo1))
caminata2.append(chi(y2,ymodelo2))
caminata3.append(chi(y3,ymodelo3))
caminata4.append(chi(y4,ymodelo4))
caminata5.append(chi(y5,ymodelo5))
caminata6.append(chi(y6,ymodelo6))

for i in range(iteraciones):
	b1futuro = np.random.uniform(10,0.5)
	b2futuro = np.random.uniform(10,0.5)
	b3futuro = np.random.uniform(10,0.5)
	b4futuro = np.random.uniform(10,0.5)
	b5futuro = np.random.uniform(10,0.5)
	b6futuro = np.random.uniform(10,0.5)

	ymodelo1 = modelo(b1[i], t1)
	ymodelo2 = modelo(b2[i], t2)
	ymodelo3 = modelo(b3[i], t3)
	ymodelo4 = modelo(b4[i], t4)
	ymodelo5 = modelo(b5[i], t5)
	ymodelo6 = modelo(b6[i], t6)

	yfuturo1 = modelo(b1futuro, t1)
	yfuturo2 = modelo(b2futuro, t2)
	yfuturo3 = modelo(b3futuro, t3)
	yfuturo4 = modelo(b4futuro, t4)
	yfuturo5 = modelo(b5futuro, t5)
	yfuturo6 = modelo(b6futuro, t6)

	chifuturo1 = chi(y1, yfuturo1)
	chifuturo2 = chi(y2, yfuturo2)
	chifuturo3 = chi(y3, yfuturo3)
	chifuturo4 = chi(y4, yfuturo4)
	chifuturo5 = chi(y5, yfuturo5)
	chifuturo6 = chi(y6, yfuturo6)

	chimodelo1 = chi(y1, ymodelo1)
	chimodelo2 = chi(y2, ymodelo2)
	chimodelo3 = chi(y3, ymodelo3)
	chimodelo4 = chi(y4, ymodelo4)
	chimodelo5 = chi(y5, ymodelo5)
	chimodelo6 = chi(y6, ymodelo6)

	alpha1 = chifuturo1/chimodelo1
	alpha2 = chifuturo2/chimodelo2
	alpha3 = chifuturo3/chimodelo3
	alpha4 = chifuturo4/chimodelo4
	alpha5 = chifuturo5/chimodelo5
	alpha6 = chifuturo6/chimodelo6

	if(alpha1>=1.0):
		b1.append(b1futuro)
		
		caminata1.append(chifuturo1)
	else:
		beta1 = np.random.random()
		if(beta1<=alpha1):
			b1.append(b1futuro)
		
			caminata1.append(chifuturo1)
		else:
			b1.append(b1[i])
	
			caminata1.append(chimodelo1)
	if(alpha2>=1.0):
		b2.append(b2futuro)
		
		caminata2.append(chifuturo2)
	else:
		beta2 = np.random.random()
		if(beta2<=alpha2):
			b2.append(b2futuro)
		
			caminata2.append(chifuturo2)
		else:
			b2.append(b2[i])
	
			caminata2.append(chimodelo2)
	if(alpha3>=1.0):
		b3.append(b3futuro)
		
		caminata3.append(chifuturo3)
	else:
		beta3 = np.random.random()
		if(beta3<=alpha3):
			b3.append(b3futuro)
		
			caminata3.append(chifuturo3)
		else:
			b3.append(b3[i])
	
			caminata3.append(chimodelo3)
	if(alpha4>=1.0):
		b4.append(b4futuro)
		
		caminata4.append(chifuturo4)
	else:
		beta4 = np.random.random()
		if(beta4<=alpha4):
			b4.append(b4futuro)
		
			caminata4.append(chifuturo4)
		else:
			b4.append(b4[i])
	
			caminata4.append(chimodelo4)
	if(alpha5>=1.0):
		b5.append(b5futuro)
		
		caminata5.append(chifuturo5)
	else:
		beta5 = np.random.random()
		if(beta5<=alpha5):
			b5.append(b5futuro)
		
			caminata5.append(chifuturo5)
		else:
			b5.append(b5[i])
	
			caminata5.append(chimodelo5)
	if(alpha6>=1.0):
		b6.append(b6futuro)
		
		caminata6.append(chifuturo6)
	else:
		beta6 = np.random.random()
		if(beta6<=alpha6):
			b6.append(b6futuro)
		
			caminata6.append(chifuturo6)
		else:
			b6.append(b6[i])
	
			caminata6.append(chimodelo6)

print("La coordenada x:", yfuturo3)
print("La coordenada y:", yfuturo1)
print("Tiempo de lanzamiento:", t1)
print("Velocidad del sonido:", yfuturo4)
