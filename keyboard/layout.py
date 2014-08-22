from scene import *

#####################################################################################
# Classes
#####################################################################################

#####################################################################################
#
# Keyboard
#
#####################################################################################

class Keyboard(object):
    def __init__(self, scrsize, pos=Point(0, 0)):
        self.size    = (scrsize.w, scrsize.h/2.)
        self.bounds  = Rect(pos.x, pos.y, *self.size)
        self.bg      = (0.8118, 0.8235, 0.8353)
        self.layouts = {}
        self.clayout = None
        self.daction = lambda text: None
        self.scrsize = scrsize
        self.setup()
    
    def setup(self):
        """
        This method will be called after __init__ method.
        """
        pass
    
    def addLayout(self, name, layout):
        self.layouts[name] = layout
        self.layouts[name].init(self)
    
    def setLayout(self, name, layout=None):
        if layout:
            self.addLayout(name, layout)
        self.clayout = name
        self.size = self.layouts[self.clayout].kbd_size()
        self.bounds.w, self.bounds.h = self.size
    
    def setDefaultAction(self, action):
        self.daction = action
        
    def draw(self):
        fill(*self.bg)
        rect(*self.bounds)
        for button in self.layouts[self.clayout].buttons:
            button.draw()
    
    def touch_began(self, touch):
        for button in self.layouts[self.clayout].buttons:
            if touch.location in button.bounds:
                button.touch_began(touch)
                return
    
    def touch_moved(self, touch):
        for button in self.layouts[self.clayout].buttons:
            button.touch_moved(touch)
    
    def touch_ended(self, touch):
        for button in self.layouts[self.clayout].buttons:
            if touch.location in button.bounds:
                button.touch_ended(touch)
                return

    def init(self):
        """
        This method should be called before keyboard is used.
        """
        pass
