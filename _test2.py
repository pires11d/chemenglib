from Chemical import *
from matplotlib import animation
import matplotlib.pyplot as plt

s = Substance('solvent')
s.Density0 = 680.0
s.Viscosity0 = 1e-3
s.SpecificHeat0 = 2
s.MolarMass = 40e-3

o = Substance('oil')
o.Density0 = 900.0
o.Viscosity0 = 1e-5
o.SpecificHeat0 = 3
o.MolarMass = 100e-3

m = Mixture([s,o])
m.wi = [0.2,0.8]
m.V = 20

s = Stream([s,o])
s.wi = [1.0,0.0]
s.Vf = 1.5


from UnitOp import Hopper, Mixer
h = Hopper(100)
h.Mixture = m
h.Inlets = [s]
h.OutletVolumeFlow = 1.0


#region ANIMATION

# Canvas #
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(5,5)
ax = plt.axes(xlim=(-1, 1), ylim=(-0.5, 2))

def init():
    ax.add_patch(h.DrawContour)
    return h.DrawContour,

def animate(i):
    h.NextTime
    # print(h.OutletStream.MassFractions)
    print(h.NextMixture.MassFractions)
    patch = h.DrawLiquid
    ax.add_patch(patch)
    return patch,

# Function Call #
anim = animation.FuncAnimation(fig,animate,init_func=init,frames=1000,interval=30,blit=True)
plt.show()

#endregion