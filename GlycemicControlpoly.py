from scipy.integrate import odeint
from math import exp
import numpy as np

def Glycemic(state,T):
# unpack the state vector
  G = state[0]
  X = state[1]
  I = state[2]

  # these are our constants
  Gd = -0.01*G - X*(G + 4.5) + 0.0167*T
  Xd = -0.025*X + 0.000013*I
  Id = -0.093*(I + 15) + 0.083*8.333
  Td = 1

  # return the state derivatives
  return [Gd, Xd, Id]

def Glycemic1(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5) + 0.0167*T
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*8.333*(G - 3)
    Td = 1
    return [Gd, Xd, Id]

def Glycemic2(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5) + 0.0167*T
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*41.67
    Td = 1
    return [Gd, Xd, Id]

def Glycemic3(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5) + 0.0056*(120 - T)
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*8.333
    Td = 1
    return [Gd, Xd, Id]

def Glycemic4(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5) + 0.0056*(120 - T)
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*8.333
    Td = 1
    return [Gd, Xd, Id]

def Glycemic5(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5) + 0.0056*(120 - T)
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*8.333*(G - 3)
    Td = 1
    return [Gd, Xd, Id]

def Glycemic6(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5) + 0.0056*(120 - T)
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*41.67
    Td = 1
    return [Gd, Xd, Id]

def Glycemic7(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5)
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*8.333
    Td = 1
    return [Gd, Xd, Id]

def Glycemic8(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5)
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*8.333*(G - 3)
    Td = 1
    return [Gd, Xd, Id]

def Glycemic8(state,T):
    # unpack the state vector
    G = state[0]
    X = state[1]
    I = state[2]
    # these are our constants
    Gd = -0.01*G - X*(G + 4.5)
    Xd = -0.025*X + 0.000013*I
    Id = -0.093*(I + 15) + 0.083*41.67
    Td = 1
    return [Gd, Xd, Id]

'''state0 = [1, 0, 0.05]
t = np.arange(0.0, 30.0, 0.01)
L1 = 0
L2 = 0
L3 = 0
L4 = 0
L5 = 0
L6 = 0
L7 = 0
L8 = 0
L9 = 0'''
    #for j in range(0,100):
    #g1 = np.random.uniform(-2,2)
    #g2 = np.random.uniform(-2,2)
    #x1 = np.random.uniform(-0.5, 0.5)
    #x2 = np.random.uniform(-0.5,0.5)
    #i1 = np.random.uniform(-0.1,0.1)
    #i2 = np.random.uniform(-0.1,0.1)
    #t1 = np.random.uniform(0,720)
    #t2 = np.random.uniform(0,720)
    #L1 = max(L1,np.linalg.norm(np.array(Glycemic([g1,x1,i1,t1],t1)) - np.array(Glycemic([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))
    # L2 = max(L2,np.linalg.norm(np.array(Glycemic1([g1,x1,i1,t1],t1)) - np.array(Glycemic1([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))
    #L3 = max(L3,np.linalg.norm(np.array(Glycemic2([g1,x1,i1,t1],t1)) - np.array(Glycemic2([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))
    #L4 = max(L4,np.linalg.norm(np.array(Glycemic3([g1,x1,i1,t1],t1)) - np.array(Glycemic3([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))
    #L5 = max(L5,np.linalg.norm(np.array(Glycemic4([g1,x1,i1,t1],t1)) - np.array(Glycemic4([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))
    #L6 = max(L6,np.linalg.norm(np.array(Glycemic5([g1,x1,i1,t1],t1)) - np.array(Glycemic5([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))
    #L7 = max(L6,np.linalg.norm(np.array(Glycemic6([g1,x1,i1,t1],t1)) - np.array(Glycemic6([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))
    #L8 = max(L6,np.linalg.norm(np.array(Glycemic7([g1,x1,i1,t1],t1)) - np.array(Glycemic7([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))
#L9 = max(L6,np.linalg.norm(np.array(Glycemic8([g1,x1,i1,t1],t1)) - np.array(Glycemic8([g2,x2,i2,t2],t2)), np.inf)/(np.linalg.norm(np.array([g1,x1,i1,t1]) - np.array([g2,x2,i2,t2]), np.inf)))


#state = odeint(Glycemic, state0, t)

# do some fancy 3D plotting
#from mpl_toolkits.mplot3d import Axes3D
#fig = matplotlib.figure()
#ax = fig.gca(projection='3d')
#ax.plot(state[:,0],state[:,1],state[:,2])
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#show()