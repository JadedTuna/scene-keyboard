from scene import *

#####################################################################################
# Functions
#####################################################################################

def cylinder(x=0, y=0, w=0, h=0, r=0):
    rect(x + h / 2, y, w - h, h)
    ellipse(x, y, h, h)
    ellipse(x + w - h, y, h, h)

def round_rect(x, y, w, h, r=0):
    """
    From Hydrogen. Thanks, BashedCrab!
    """

    if(r <= 0):
        rect(x, y, w, h)
    elif(r >= h):
        cylinder(x, y, w, h)
    else:
        d = r * 2
        rect(x + r, y, w - d, h)
        rect(x, y + r, w, h - d)
        ellipse(x, y, d, d)
        ellipse(x, y + h - d, d, d)
        ellipse(x + w - d, y, d, d)
        ellipse(x + w - d, y + h - d, d, d)

def shaded_rect(x, y, w, h, colour, shade_colour, border=1):
    r = 5 # Default button radius
    fill(*shade_colour)
    round_rect(x, y - border, w, h, r)
    fill(*colour)
    round_rect(x, y, w, h, r)

#####################################################################################
# Variables
#####################################################################################

DSHADE_COLOUR = (0.5, 0.5, 0.5)

#####################################################################################
# Classes
#####################################################################################

class TextButton(object):
    def __init__(self,
                 text,
                 value,
                 pos,
                 size,
                 bgcolours,
                 fgcolours,
                 fontfamily,
                 fontsize,
                 action,
                 id):
        self.size   = size
        self.bounds = Rect(pos.x, pos.y, *size)
        
        self.dbg, self.pbg = bgcolours # Default bg and pressed bg
        self.dfg, self.pfg = fgcolours # Default fg and pressed fg
        self.shade_colour  = DSHADE_COLOUR
        self.drawbg        = self.dbg
        self.drawfg        = self.dfg
        self.drawbounds    = None
        
        self.drawfunc  = lambda x, y, w, h: shaded_rect(x, y, w, h, self.drawbg, self.shade_colour)
        
        self.text      = text
        self.textpos   = self.bounds.center()
        self.fontfam   = fontfamily
        self.fontsize  = fontsize
        self.value     = value
        
        self.touch_id  = None
        self.parent    = None
        self.action    = action
        self.button_id = id
    
    def init(self, parent):
        """
        Init a button, give it a parent keyboard!
        """
        self.parent     = parent
        x, y, w, h      = self.bounds
        self.drawbounds = (x + self.parent.bounds.x,
                            y + self.parent.bounds.y,
                            w,
                            h)
        self.action     = self.action if self.action else parent.daction
    
    def draw(self):
        fill(*self.drawbg) # This is needed incase some other drawing functions is used
        self.drawfunc(*self.drawbounds)
        x, y = self.textpos
        tint(*self.drawfg)
        text(self.text, self.fontfam, self.fontsize, x, y)
    
    def hit_test(self, point):
        return point in self.bounds
    
    def touch_began(self, touch):
        if not self.touch_id:
            self.touch_id = touch.touch_id
            self.drawbg   = self.pbg
            self.drawfg   = self.pfg
    
    def touch_moved(self, touch):
        if touch.touch_id == self.touch_id:
            if touch.location in self.bounds:
                self.drawbg = self.pbg
                self.drawfg = self.pfg
            else:
                self.drawbg = self.dbg
                self.drawfg = self.dfg

    def touch_ended(self, touch):
        if touch.touch_id == self.touch_id:
            self.touch_id = None
            self.drawbg   = self.dbg
            self.drawfg   = self.dfg
            if touch.location in self.bounds:
                self.clicked()
    
    def clicked(self):
        if self.action:
            self.action(self.value)
        print 'Button %s clicked' % self.text
