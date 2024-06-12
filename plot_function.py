import matplotlib.pyplot as plt
import numpy as np
import math


plot = True
# plot = False


if not plot:
    def gaussian_value(esperance, equart, x):
        exposant = -( (x-esperance)**2 / (2*equart**2) )
        proba = 1 / (equart * math.sqrt(2*math.pi)) * math.exp(exposant)
        print("esperance:", esperance, ", equart:", equart, ", x:", x, " ---> proba:", proba)
    
    gaussian_value(esperance=10, equart=0.1, x=10)
    gaussian_value(esperance=10, equart=0.1, x=1)
    gaussian_value(esperance=10, equart=0.1, x=1000000)
    exit()






ax = plt.subplot()

xmin=7.0
xmax=14.0
step=0.01
t = np.arange(xmin, xmax, step)

def gaussian(esperance, equart, t, w):
    exposant = -( (t-esperance)**2 / (2*equart**2) )
    return w * 1 / (equart * math.sqrt(2*math.pi)) * np.exp(exposant)

s = []
esperances = [11, 10, 12, 9]
equarts = [0.35, 0.35, 0.3, 0.5]
weights = [0.5, 0.3, 0.1, 0.1]

for i in range(len(esperances)):
    sx = gaussian(esperances[i], equarts[i], t, weights[i])
    s.append(sx)

gaussian_mixture_model = s[0].copy()
for i in range(1, len(s)):
    gaussian_mixture_model += s[i]



colors = ["#9673A6", "#6C8EBF", "#D79B00", "#82B366"]
for i in range(len(s)):
    line, = plt.plot(t, s[i], lw=2, color=colors[i])
    ax.fill_between(t, s[i], alpha=0.4, color=colors[i])
    line.set_label("μ=" + str(esperances[i]) + ", σ=" + str(equarts[i]) + ", w=" + str(weights[i]))


line, = plt.plot(t, gaussian_mixture_model, lw=2, color="red", linestyle=":")
line.set_label("Modèle de mélange gaussien")

plt.legend()
plt.xlabel("Valeur de caractèristique")
plt.ylabel("Densité")
plt.ylim(0, 1)
plt.xlim(xmin, xmax)
# plt.show()

plt.savefig("./gmm.pdf")