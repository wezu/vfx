from panda3d.core import *
import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from vfx import vfx
from vfx import P2Pvfx
from vfx import MovingVfx
from vfx import short_vfx
from direct.interval.IntervalGlobal import *

# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
      pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

class vfxDemo(DirectObject):
    def __init__(self): 
        self.smiley = loader.loadModel('smiley')
        self.smiley.reparentTo(render)
        self.smiley.setPos(-5,30,0)
        
        self.frowney = loader.loadModel('frowney')
        self.frowney.reparentTo(render)
        self.frowney.setPos(5,30,0)
        
        self.accept('1', self.MakeVfx, [1])
        self.accept('2', self.MakeVfx, [2])
        self.accept('3', self.MakeVfx, [3])
        self.accept('4', self.MakeVfx, [4])
        
        self.inst1 = addInstructions(0.95,"1: make Smiley explode")
        self.inst2 = addInstructions(0.90,"2: make Frowney do magic")
        self.inst3 = addInstructions(0.85,"3: make a lightning between Smiley and Frowney")
        self.inst4 = addInstructions(0.80,"4: projectile")
        self.fire=None
        
    def MakeVfx(self, mode):
        if mode ==1:
            vfx(self.smiley, texture='boom_fire.png',scale=2.0).start()
        elif mode ==2:
            vfx(self.frowney, texture='vfx3.png',scale=2.0).start()  
        elif mode ==3:
            P2Pvfx(self.smiley,self.frowney,'lightning.png',scale=0.5).start()              
        else:
            MovingVfx(self.smiley,  self.frowney, texture='plasm2.png', gravity=5, time=0.5 ).start()
            impact=vfx(self.frowney, texture='m_blast.png',scale=2.0)  
            Sequence(Wait(0.4), Func(impact.start)).start()  
demo = vfxDemo()    
run()         