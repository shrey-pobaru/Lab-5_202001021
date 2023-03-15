# -*- coding: utf-8 -*-
"""Sanket_Doshi_A1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Lhta2tVhIBj6tbRfR81voYEgYGJLuY4

# **Machine Learning (IE 406)**
# **Lab 1 Gradient Descent**
# **Name - Sanket Doshi**
# **ID - 202001008**



---

### 1. $f(w)=w_1^2 + w_2^2 + 5$
"""

import numpy as np
import matplotlib.pyplot as plt 
import math
plt.rcParams["figure.figsize"] = (12, 9)

from matplotlib import rc

def cost_function(w1, w2):
  #given cost/loss function
  return w1 * w1 + w2 * w2 + 5

"""**Step 1 : Plot the surface plot and contour plot for the function f(w) to visualize its shape. Is it convex or
non-convex? Verify it quantitatively.**
"""

def f(xRange = 1.0, yRange = 1.0, increment = 0.01):
  #w1, w2 are the two individual vectors for w
  w1 = np.arange( -xRange, xRange, increment )
  w2 = np.arange( -yRange, yRange, increment )

  #Value of cost function (2D array) for each (w1, w2) pair
  val = np.zeros( ( w1.size, w2.size ) )

  cx = 0
  for x in w1:
      cy = 0
      for y in w2:
          val[cx, cy] = cost_function(x, y)
          cy += 1
      cx += 1

  return w1, w2, val

def plot3D(x, y, z, colorMap = 'viridis', ax = None, title = 'Plot of $f(w)$'):
  """Generate a 3D-Surface plot based on given x, y, z grid co-ordinates"""
  #generate a 2D grid for our (w1, w2) pairs
  X, Y = np.meshgrid(x, y)

  #plotting the 3D surface
  
  if ax != None:
    ax.plot_surface(X, Y, z, cmap=colorMap)
  else:
    ax = plt.axes( projection='3d' )
    ax.plot_surface(X, Y, z, cmap=colorMap)

  ax.set_title(title, fontsize = 20)
  ax.set_xlabel('$w_1$', fontsize = 15)
  ax.set_ylabel('$w_2$', fontsize = 15)
  ax.set_zlabel('$f(w)$', fontsize = 15)

def plotContour(x, y, z, noOfContours = 20, ax = None):
  """Generate a 2D-Contour plot based on given x, y, z grid co-ordinates"""
  X, Y = np.meshgrid(x, y)

  if ax != None:
    ax.contour(X, Y, z, noOfContours)
  else:
    contourPlot = plt.contour(X, Y, z, noOfContours)
    plt.clabel(contourPlot, inline = True)

  plt.title('Plot of $f(w)$', fontsize = 20)
  plt.xlabel('$w_1$', fontsize = 15)
  plt.ylabel('$w_2$', fontsize = 15)

[x, y, z] = f()

plot3D(x, y, z)
plt.show()

"""From the plot it seems that it is a convex function."""

plotContour(x, y, z, 40)
plt.show()

def diffW1(w1, w2):
  return 2 * w1

def diffW2(w1, w2):
  return 2 * w2

def gradientDescent(w1_initial, w2_initial, alpha, recordAt = 100, max_iterations = 1000):
  xEstimate = w1_initial
  yEstimate = w2_initial

  learningRate = alpha

  episilon1 = 1e10
  episilon2 = 1e10

  episilon = 1e10

  t = max_iterations

  xHistory = []; yHistory = []

  while (episilon1 >= 1e-5 or episilon2 >= 1e-5):
    if t % recordAt == 0:
      xHistory.append(xEstimate)
      yHistory.append(yEstimate)

    if t <= 0:
      break

    newX = xEstimate - learningRate * diffW1(xEstimate, yEstimate)
    newY = yEstimate - learningRate * diffW2(xEstimate, yEstimate)

    episilon1 = abs(newX - xEstimate)
    episilon2 = abs(newY - yEstimate)

    # episilon = abs(cost_function(newX, newY) - cost_function(xEstimate, yEstimate))

    xEstimate = newX
    yEstimate = newY

    # print(f"{xEstimate}, {yEstimate}")

    t -= 1
  
  xHistory.append(xEstimate)
  yHistory.append(yEstimate)

  return xHistory, yHistory

#3a - plot gradient descent progression
alpha = [ 0.001, 0.1, 0.5, 1, 5 ]

fig, ax = plt.subplots(2, 3, figsize=(25, 15))

for i in range(0, len(alpha)):
  if alpha[i] == 5:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 1, max_iterations=3)
  elif alpha[i] < 0.1:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 100, max_iterations=2000)
  else:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 5)

  if alpha[i] == 5:
    [x, y, z] = f(1000, 1000, 1)
  else:
    [x, y, z] = f()
  
  contourPlot = plotContour(x, y, z, ax=ax[i//3, i%3])
  ax[i//3, i%3].scatter(xHistory, yHistory)

  for j in range(1, len(xHistory)):
    ax[i//3, i%3].annotate('', xy=np.array([xHistory[j], yHistory[j]]), xytext=np.array([xHistory[j-1], yHistory[j-1]]),
                   arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
                   va='center', ha='center')
    
  ax[i//3, i%3].legend([f'Learning Rate = {alpha[i]}'])

plt.show()

alpha = [ 0.001, 0.1, 0.5, 1, 5 ]
fig, ax = plt.subplots(2, 3, figsize=(25, 15), subplot_kw=dict(projection='3d'))

for i in range(0, len(alpha)):
  if alpha[i] == 5:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 1, max_iterations=3)
  elif alpha[i] < 0.1:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 100)
  else:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 5)

  if alpha[i] == 5:
    [x, y, z] = f(400, 400, 10)
  else:
    [x, y, z] = f()

  plot3D(x, y, z, colorMap = 'GnBu', ax=ax[i//3, i%3], title = f"Learning Rate : {alpha[i]}")
  
  valueOfF = []
  for j in range(0, len(xHistory)):
    valueOfF.append(xHistory[j] * xHistory[j] + yHistory[j] * yHistory[j] + 5)

  ax[i//3, i%3].scatter(xHistory, yHistory, valueOfF, s = 40, c='black')

plt.show()

"""<div class="markdown-google-sans">
<h3><b>Quantative Analysis for Question (1), $f(w)=w_1^2 + w_2^2 + 5$</b></h3>
Hessian of a function $f$ with two variables $x, y$ is given by:

$f_{xx} f_{yy} - f_{xy}^2 = 
\begin{vmatrix}
f_{xx} & f_{xy}\\
f_{xy} & f_{yy}
\end{vmatrix}$

Calculating Partial Derivatives $f_{w_1 w_1}, f_{w_1 w_2} f_{w_2 w_2}$,

$f_{w_1} = \frac{\partial (w_1^2 + w_2^2 + 5)}{\partial w_1} = 2w_1$
<br>
$f_{w_2} = \frac{\partial (w_1^2 + w_2^2 + 5)}{\partial w_1} = 2w_2$
<br>
$f_{w_1 w_1} = \frac{\partial^2 (w_1^2 + w_2^2 + 5)}{\partial w_1^2} = 2$
<br>
$f_{w_2 w_2} = \frac{\partial^2 (w_1^2 + w_2^2 + 5)}{\partial w_2^2} = 2$
<br>
$f_{w_1 w_2} = \frac{\partial^2 (w_1^2 + w_2^2 + 5)}{\partial w_1 w_2} = 0$
<br>
<br>
Hessian Matrix is given by,<br>
$H=\begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}$

Calculating eigenvalues of given function $f(w)=w_1^2 + w_2^2 + 5$ from the Hessian matrix obtained,

$|H-λI|=0$

$\implies \left| {\begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}} - λ {\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}} \right| = 0$

$\implies \left| {\begin{bmatrix}
2 - λ & 0\\
0 & 2 - λ
\end{bmatrix}} \right| = 0$

$\implies (2-λ)^2 = 0$

$\implies \boxed{ λ = 2 }$

Since, the only eigenvalue of given function is $λ = 2 \ge 0$, therefore we can say that given function is a <b>Convex function</b>.
</div>

---

### 2. $f(w)=w_1^2+w_2^2-6w_1+8w_2+9$
"""

def cost_function(w1, w2):
  #given cost/loss function
  return w1*w1 + w2*w2 - 6*w1 + 8*w2 + 9

[x, y, z] = f(100, 100, 1)

plot3D(x, y, z)
plt.show()

"""From the plot it seems that it is a convex function."""

plotContour(x, y, z, noOfContours = 20)
plt.show()

def diffW1(w1, w2):
  return 2*w1 - 6

def diffW2(w1, w2):
  return 2*w2 + 8

#3a - plot gradient descent progression
alpha = [ 0.001, 0.1, 0.5, 1, 5 ]

fig, ax = plt.subplots(2, 3, figsize=(25, 15))

for i in range(0, len(alpha)):
  if alpha[i] == 5:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 1, max_iterations=3)
  elif alpha[i] < 0.1:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 100)
  else:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 5)

  if alpha[i] == 5:
    [x, y, z] = f(1000, 1000, 1)
  else:
    [x, y, z] = f(10, 10, 0.01)
  
  contourPlot = plotContour(x, y, z, ax=ax[i//3, i%3])
  ax[i//3, i%3].scatter(xHistory, yHistory)

  for j in range(1, len(xHistory)):
    ax[i//3, i%3].annotate('', xy=np.array([xHistory[j], yHistory[j]]), xytext=np.array([xHistory[j-1], yHistory[j-1]]),
                   arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
                   va='center', ha='center')
    
  ax[i//3, i%3].legend([f'Learning Rate = {alpha[i]}'])

plt.show()

alpha = [ 0.001, 0.1, 0.5, 1, 5 ]
fig, ax = plt.subplots(2, 3, figsize=(25, 15), subplot_kw=dict(projection='3d'))

for i in range(0, len(alpha)):
  if alpha[i] == 5:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 1, max_iterations=3)
  elif alpha[i] < 0.1:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 100)
  else:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 5)

  if alpha[i] == 5:
    [x, y, z] = f(1000, 1000, 10)
  elif alpha[i] == 1:
    [x, y, z] = f(5, 5, 0.1)
  elif alpha[i] <= 0.5:
    [x, y, z] = f(3, 3, 0.1)

  plot3D(x, y, z, colorMap = 'GnBu', ax=ax[i//3, i%3], title = f"Learning Rate : {alpha[i]}")
  
  valueOfF = []
  for j in range(0, len(xHistory)):
    valueOfF.append(cost_function(xHistory[j], yHistory[j]))

  ax[i//3, i%3].scatter(xHistory, yHistory, valueOfF, s = 40, c='black')

plt.show()

"""<div class="markdown-google-sans">
<h3><b>Quantative Analysis for Question (2), $f(w)=w_1^2 + w_2^2 - 6w_1 + 8w_2 + 9$</b></h3>
<h4>
Hessian of a function $f$ with two variables $x, y$ is given by:

$f_{xx} f_{yy} - f_{xy}^2 = 
\begin{vmatrix}
f_{xx} & f_{xy}\\
f_{xy} & f_{yy}
\end{vmatrix}$

<h4>
Calculating Partial Derivatives $f_{w_1 w_1}, f_{w_1 w_2} f_{w_2 w_2}$,

$f_{w_1} = \frac{\partial (w_1^2 + w_2^2 - 6w_1 + 8w_2 + 9)}{\partial w_1} = 2w_1-6$
<br>
$f_{w_2} = \frac{\partial (w_1^2 + w_2^2 - 6w_1 + 8w_2 + 9)}{\partial w_1} = 2w_2+8$
<br>
$f_{w_1 w_1} = \frac{\partial^2 (w_1^2 + w_2^2 - 6w_1 + 8w_2 + 9)}{\partial w_1^2} = 2$
<br>
$f_{w_2 w_2} = \frac{\partial^2 (w_1^2 + w_2^2 - 6w_1 + 8w_2 + 9)}{\partial w_2^2} = 2$
<br>
$f_{w_1 w_2} = \frac{\partial^2 (w_1^2 + w_2^2 - 6w_1 + 8w_2 + 9)}{\partial w_1 w_2} = 0$
<br>
<br>

<h4>
Equating $f_{w_1}$ and $f_{w_2}$ with $0$ we get,
<br>
$f_{w_1} = 0 \implies 2w_1-6 = 0 \implies \boxed{w_1 = 3}$
<br>
$f_{w_2} = 0 \implies 2w_2+8 = 0 \implies \boxed{w_2 = -4}$
<br>
Hence, the corner point is $(w_1, w_2) = (3, -4)$
<h4>
Hessian Matrix is given by,<br>
$H=\begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}$

<h4>
Calculating eigenvalues of given function $f(w)=w_1^2 + w_2^2 - 6w_1 + 8w_2 + 9$ from the Hessian matrix obtained,

$|H-λI|=0$

$\implies \left| {\begin{bmatrix}
2 & 0\\
0 & 2
\end{bmatrix}} - λ {\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}} \right| = 0$

$\implies \left| {\begin{bmatrix}
2 - λ & 0\\
0 & 2 - λ
\end{bmatrix}} \right| = 0$

$\implies (2-λ)^2 = 0$

$\implies \boxed{ λ = 2 }$

<h4>
Since, the only eigenvalue of given function is $λ = 2 \ge 0$, therefore we can say that given function is a <b>Convex function</b>, having global minima at point $(w_1, w_2) = (3, -4)$.
</div>

---

### 3. $f(w)=3w_1^2-5w_2^2$
"""

def cost_function(w1, w2):
  #given cost/loss function
  return 3*w1*w1 - 5*w2*w2

[x, y, z] = f(100, 100, 1)

plot3D(x, y, z)
plt.show()

"""It is a concave function"""

plotContour(x, y, z, noOfContours = 20)
plt.show()

def diffW1(w1, w2):
  return 6*w1

def diffW2(w1, w2):
  return -10*w2

#3a - plot gradient descent progression
alpha = [ 0.001, 0.1, 0.5, 1, 5 ]

fig, ax = plt.subplots(2, 3, figsize=(25, 15))

for i in range(0, len(alpha)):
  if alpha[i] >= 0.01:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 1, max_iterations=3)
  elif alpha[i] < 0.1:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 5, max_iterations=100)
  else:
    [xHistory, yHistory] = gradientDescent(-1, -1, alpha[i], recordAt = 5, max_iterations=100)

  if alpha[i] == 5:
    [x, y, z] = f(150000, 150000, 500)
  elif alpha[i] == 1:
    [x, y, z] = f(1500, 1500, 10)
  elif alpha[i] == 0.5:
    [x, y, z] = f(250, 250, 1)
  else:
    [x, y, z] = f(10, 10, 0.01)
  
  contourPlot = plotContour(x, y, z, ax=ax[i//3, i%3])
  ax[i//3, i%3].scatter(xHistory, yHistory)

  for j in range(1, len(xHistory)):
    ax[i//3, i%3].annotate('', xy=np.array([xHistory[j], yHistory[j]]), xytext=np.array([xHistory[j-1], yHistory[j-1]]),
                   arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
                   va='center', ha='center')
    
  ax[i//3, i%3].legend([f'Learning Rate = {alpha[i]}'])

plt.show()

alpha = [ 0.001, 0.1, 0.5, 1, 5 ]
fig, ax = plt.subplots(2, 3, figsize=(25, 15), subplot_kw=dict(projection='3d'))

for i in range(0, len(alpha)):
  if alpha[i] >= 0.01:
    [xHistory, yHistory] = gradientDescent(0, -1.5, alpha[i], recordAt = 1, max_iterations=3)
  elif alpha[i] < 0.1:
    [xHistory, yHistory] = gradientDescent(0, -1.5, alpha[i], recordAt = 5, max_iterations=100)
  else:
    [xHistory, yHistory] = gradientDescent(0, -1.5, alpha[i], recordAt = 5, max_iterations=100)

  if alpha[i] == 5:
    [x, y, z] = f(150000, 150000, 5000)
  elif alpha[i] == 1:
    [x, y, z] = f(1500, 1500, 100)
  elif alpha[i] == 0.5:
    [x, y, z] = f(250, 250, 10)
  elif alpha[i] == 0.1:
    [x, y, z] = f(10, 10, 0.1)
  else:
    [x, y, z] = f(3, 3, 0.01)

  plot3D(x, y, z, colorMap = 'GnBu', ax=ax[i//3, i%3], title = f"Learning Rate : {alpha[i]}")
  
  valueOfF = []
  for j in range(0, len(xHistory)):
    valueOfF.append(cost_function(xHistory[j], yHistory[j]))
  ax[i//3, i%3].scatter(xHistory, yHistory, valueOfF, s = 40, c='black')

plt.show()

"""<div class="markdown-google-sans">
<h3><b>Quantative Analysis for Question (3), $f(w)=3w_1^2 - 5w_2^2$</b></h3>
<h4>
Hessian of a function $f$ with two variables $x, y$ is given by:

$f_{xx} f_{yy} - f_{xy}^2 = 
\begin{vmatrix}
f_{xx} & f_{xy}\\
f_{xy} & f_{yy}
\end{vmatrix}$

<h4>
Calculating Partial Derivatives $f_{w_1 w_1}, f_{w_1 w_2} f_{w_2 w_2}$,

$f_{w_1} = \frac{\partial (3w_1^2 - 5w_2^2)}{\partial w_1} = 6w_1$
<br>
$f_{w_2} = \frac{\partial (3w_1^2 - 5w_2^2)}{\partial w_1} = -10w_2$
<br>
$f_{w_1 w_1} = \frac{\partial^2 (3w_1^2 - 5w_2^2)}{\partial w_1^2} = 6$
<br>
$f_{w_2 w_2} = \frac{\partial^2 (3w_1^2 - 5w_2^2)}{\partial w_2^2} = -10$
<br>
$f_{w_1 w_2} = \frac{\partial^2 (3w_1^2 - 5w_2^2)}{\partial w_1 w_2} = 0$
<br>
<br>
<h4>
Equating $f_{w_1}$ and $f_{w_2}$ with $0$ we get,
<br>
$f_{w_1} = 0 \implies 6w_1 = 0 \implies \boxed{w_1 = 0}$
<br>
$f_{w_2} = 0 \implies -10w_2 = 0 \implies \boxed{w_2 = 0}$
<br>
Hence, the corner point is $(w_1, w_2) = (0, 0)$
<h4>
Hessian Matrix is given by,<br>
$H=\begin{bmatrix}
6 & 0\\
0 & -10
\end{bmatrix}$

<h4>
Calculating eigenvalues of given function $f(w)=3w_1^2 - 5w_2^2$ from the Hessian matrix obtained,

$|H-λI|=0$

$\implies \left| {\begin{bmatrix}
6 & 0\\
0 & -10
\end{bmatrix}} - λ {\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}} \right| = 0$

$\implies \left| {\begin{bmatrix}
6 - λ & 0\\
0 & -10 - λ
\end{bmatrix}} \right| = 0$

$\implies (6-λ)(-10-λ) = 0$

$\implies \boxed{ λ = 6, -10 }$

<h4>
Since, the one of the eigenvalues of given function is $λ = -10 \lt 0$, therefore we can say that given function is a <b>Non-Convex function</b> with is no global minimum and hence, the obtained corner point is actually a <b>saddle point</b>.
</div>

### 4. $f(w)=sin(w)*cos(w)$
"""

def cost_function(w1, w2):
  #given cost/loss function
  return math.sin(w1) * math.cos(w2)

[x, y, z] = f(5, 5, 0.01)

plot3D(x, y, z)
plt.show()

plotContour(x, y, z, noOfContours = 20)
plt.show()

def diffW1(w1, w2):
  return math.cos(w1) * math.cos(w2)

def diffW2(w1, w2):
  return - math.sin(w1) * math.sin(w2)

#3a - plot gradient descent progression
alpha = [ 0.001, 0.1, 0.5, 1, 5 ]

fig, ax = plt.subplots(2, 3, figsize=(25, 15))

for i in range(0, len(alpha)):
  if alpha[i] == 5:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 1, max_iterations=3)
  elif alpha[i] < 0.1:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 1000, max_iterations=20000)
  else:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 5)

  if alpha[i] == 5:
    [x, y, z] = f(10, 10, 0.1)
  else:
    [x, y, z] = f(4, 4, 0.1)
  
  contourPlot = plotContour(x, y, z, noOfContours = 30, ax=ax[i//3, i%3])
  ax[i//3, i%3].scatter(xHistory, yHistory)

  # print(cost_function(xHistory[-1], yHistory[-1]))
  # print((xHistory[-1], yHistory[-1]))
  # print(xHistory)
  # print(yHistory)

  # for j in range(0, len(xHistory)):
  #   print(cost_function(xHistory[j], yHistory[j]), end=" ")

  # print()


  for j in range(1, len(xHistory)):
    ax[i//3, i%3].annotate('', xy=np.array([xHistory[j], yHistory[j]]), xytext=np.array([xHistory[j-1], yHistory[j-1]]),
                   arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
                   va='center', ha='center')
    
  ax[i//3, i%3].legend([f'Learning Rate = {alpha[i]}'])

plt.show()

alpha = [ 0.001, 0.1, 0.5, 1, 5 ]
fig, ax = plt.subplots(2, 3, figsize=(25, 15), subplot_kw=dict(projection='3d'))

for i in range(0, len(alpha)):
  if alpha[i] == 5:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 1, max_iterations=3)
  elif alpha[i] < 0.1:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 100, max_iterations=5000)
  else:
    [xHistory, yHistory] = gradientDescent(1, -1, alpha[i], recordAt = 5)

  if alpha[i] == 5:
    [x, y, z] = f(6, 6, 0.01)
  else:
    [x, y, z] = f(2.5, 2.5, 0.01)

  plot3D(x, y, z, colorMap = 'GnBu', ax=ax[i//3, i%3], title = f"Learning Rate : {alpha[i]}")
  
  valueOfF = []
  for j in range(0, len(xHistory)):
    valueOfF.append(cost_function(xHistory[j], yHistory[j]))

  print(cost_function(xHistory[-1], yHistory[-1]))
  ax[i//3, i%3].scatter(xHistory, yHistory, valueOfF, s = 40, c='black')

plt.show()

"""<div class="markdown-google-sans">
<h3><b>Quantative Analysis for Question (3). $f(w)=sin(w_1)cos(w_2)$</b></h3>
<h4>
Hessian of a function $f$ with two variables $x, y$ is given by:

$f_{xx} f_{yy} - f_{xy}^2 = 
\begin{vmatrix}
f_{xx} & f_{xy}\\
f_{xy} & f_{yy}
\end{vmatrix}$

<h4>
Calculating Partial Derivatives $f_{w_1 w_1}, f_{w_1 w_2} f_{w_2 w_2}$,

$f_{w_1} = \frac{\partial (sin(w_1)cos(w_2))}{\partial w_1} = cos(w_1)cos(w_2)$
<br>
$f_{w_2} = \frac{\partial (sin(w_1)cos(w_2))}{\partial w_1} = -sin(w_1)sin(w_2)$
<br>
$f_{w_1 w_1} = \frac{\partial^2 (sin(w_1)cos(w_2))}{\partial w_1^2} = -sin(w_1)cos(w_2)$
<br>
$f_{w_2 w_2} = \frac{\partial^2 (sin(w_1)cos(w_2))}{\partial w_2^2} = -sin(w_1)cos(w_2)$
<br>
$f_{w_1 w_2} = \frac{\partial^2 (sin(w_1)cos(w_2))}{\partial w_1 w_2} = -cos(w_1)sin(w_2)$
<br>
<br>
<h4>
Equating $f_{w_1}$ and $f_{w_2}$ with $0$ we get,
<br>
$f_{w_1} = 0 \implies 6w_1 = 0 \implies \boxed{w_1 = 0}$
<br>
$f_{w_2} = 0 \implies -10w_2 = 0 \implies \boxed{w_2 = 0}$
<br>
Hence, the corner point is $(w_1, w_2) = (0, 0)$
<h4>
Hessian Matrix is given by,<br>
$H=\begin{bmatrix}
-sin(w_1)cos(w_2) & 0\\
0 & -10
\end{bmatrix}$

<h4>
Calculating eigenvalues of given function $f(w)=sin(w_1)cos(w_2)$ from the Hessian matrix obtained,

$|H-λI|=0$

$\implies \left| {\begin{bmatrix}
-sin(w_1)cos(w_2) & -cos(w_1)sin(w_2)\\
-cos(w_1)sin(w_2) & -sin(w_1)cos(w_2)
\end{bmatrix}} - λ {\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}} \right| = 0$

$\implies \left| {\begin{bmatrix}
-sin(w_1)cos(w_2) - λ & -cos(w_1)sin(w_2)\\
-cos(w_1)sin(w_2) & -sin(w_1)cos(w_2) - λ
\end{bmatrix}} \right| = 0$

$\implies (-sin(w_1)cos(w_2)-λ)(-sin(w_1)cos(w_2)-λ) - cos^2(w_1)sin^2(w_2)= 0$
<br>
$\implies (sin(w_1)cos(w_2)+λ)^2 - cos^2(w_1)sin^2(w_2)= 0$
<br>
<br>
For $(w_1, w_2) = (\frac{\pi}{4}, \frac{\pi}{4}), \boxed{ \implies λ = -1, 0 }$

<h4>
Since, the one of the eigenvalues of given function is $λ = -1 \lt 0$, therefore we can say that given function is a <b>Non-Convex function</b> with infinite local minimum with value -1. The obtained corner point $(0, 0)$ is actually a <b>saddle point</b> because $|H| = 0$ at $(w_1, w_2) = (0, 0)$.
</div>
"""