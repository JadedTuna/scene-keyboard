# This is a beta version, so you may expect some bugs!
from scene import *

BDBG = (1.0, 1.0, 1.0) # Button Default BackGround
BPBG = (0.8, 0.8, 0.8) # Button Pressed BackGround
SBBG = (0.73, 0.74, 0.76) # Special Button BackGround

TDFG = (0.0, 0.0, 0.0) # Text Default ForeGround
TPFG = (0.0, 0.0, 0.0) # Text Pressed ForeGround

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
# Classes
#####################################################################################

class TextButton(object):
    def __init__(self,
                 parent,
                 pos,
                 size,
                 text,
                 bgcolours,
                 fgcolours,
                 font_size=28,
                 action=None):
        self.size = size
        self.bounds = Rect(pos.x, pos.y, *size)
        
        self.dbg, self.pbg = bgcolours # Default bg and pressed bg
        self.dfg, self.pfg = fgcolours # Default fg and pressed fg
        self.shade_colour  = (0.5, 0.5, 0.5)
        self.drawbg = self.dbg
        self.drawfg = self.dfg
        self.drawfunc = lambda x, y, w, h: shaded_rect(x, y, w, h, self.drawbg, self.shade_colour)
        
        self.text     = text
        self.textpos  = self.bounds.center()
        self.fontsize = font_size
        
        self.touch_id = None
        self.parent   = parent
        self.action   = action
    
    def draw(self):
        fill(*self.drawbg) # This is needed incase some other drawing functions is used
        tint(*self.drawfg)
        x, y, w, h = self.bounds
        x += self.parent.bounds.x
        y += self.parent.bounds.y
        self.drawfunc(x, y, w, h)
        text(self.text, "Arial", self.fontsize, *self.textpos)
    
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
            self.action()
        print 'Button %s clicked' % self.text

class Keyboard(object):
    def __init__(self, scrsize, pos=Point(0, 0)):
        self.scrsize   = scrsize
        
        gx = self.getXPosition
        gy = self.getYPosition

        self.BTNSIZE = BTNSIZE = Size(gx(81), gy(75))
        self.BTNPAD  = BTNPAD  = gx(12) # Padding between buttons
        PADLEFT      = gx(6.5) # Padding left for 1st, 3rd and 4th rows
        
        self.size      = (scrsize.w, BTNSIZE[1]*4 + BTNPAD*5) # This size is for iPad3 LANDSCAPE mode
        self.bounds    = Rect(pos.x, pos.y, *self.size)
        self.bg        = (0.8118, 0.8235, 0.8353)
        self.layouts   = {}
        # For now we will have just one layout
        self.curlayout = "letters"
        
        # Adding buttons to letters layouts
        
        # Row $1
        self.addTextButton("letters", (PADLEFT, BTNPAD * 4 + BTNSIZE[1] * 3), "Q")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 1 + BTNSIZE[0] * 1,
                                BTNPAD * 4 + BTNSIZE[1] * 3), "W")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 2 + BTNSIZE[0] * 2,
                                BTNPAD * 4 + BTNSIZE[1] * 3), "E")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 3 + BTNSIZE[0] * 3,
                                BTNPAD * 4 + BTNSIZE[1] * 3), "R")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 4 + BTNSIZE[0] * 4, 
                                BTNPAD * 4 + BTNSIZE[1] * 3), "T")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 5 + BTNSIZE[0] * 5, 
                                BTNPAD * 4 + BTNSIZE[1] * 3), "Y")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 6 + BTNSIZE[0] * 6, 
                                BTNPAD * 4 + BTNSIZE[1] * 3), "U")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 7 + BTNSIZE[0] * 7, 
                                BTNPAD * 4 + BTNSIZE[1] * 3), "I")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 8 + BTNSIZE[0] * 8, 
                                BTNPAD * 4 + BTNSIZE[1] * 3), "O")
        self.addTextButton("letters", (PADLEFT + BTNPAD * 9 + BTNSIZE[0] * 9, 
                                BTNPAD * 4 + BTNSIZE[1] * 3), "P")
    
        # Row $2
        self.addTextButton("letters", (gx(45), BTNPAD * 3 + BTNSIZE[1] * 2), "A")
        self.addTextButton("letters", (gx(45) + BTNPAD * 1 + BTNSIZE[0] * 1,
                                BTNPAD * 3 + BTNSIZE[1] * 2), "S")
        self.addTextButton("letters", (gx(45) + BTNPAD * 2 + BTNSIZE[0] * 2,
                                BTNPAD * 3 + BTNSIZE[1] * 2), "D")
        self.addTextButton("letters", (gx(45) + BTNPAD * 3 + BTNSIZE[0] * 3,
                                BTNPAD * 3 + BTNSIZE[1] * 2), "F")
        self.addTextButton("letters", (gx(45) + BTNPAD * 4 + BTNSIZE[0] * 4,
                                BTNPAD * 3 + BTNSIZE[1] * 2), "G")
        self.addTextButton("letters", (gx(45) + BTNPAD * 5 + BTNSIZE[0] * 5,
                                BTNPAD * 3 + BTNSIZE[1] * 2), "H")
        self.addTextButton("letters", (gx(45) + BTNPAD * 6 + BTNSIZE[0] * 6,
                                BTNPAD * 3 + BTNSIZE[1] * 2), "J")
        self.addTextButton("letters", (gx(45) + BTNPAD * 7 + BTNSIZE[0] * 7,
                                BTNPAD * 3 + BTNSIZE[1] * 2), "K")
        self.addTextButton("letters", (gx(45) + BTNPAD * 8 + BTNSIZE[0] * 8,
                                BTNPAD * 3 + BTNSIZE[1] * 2), "L")
        self.addTextButton("letters", (gx(45) + BTNPAD * 9 + BTNSIZE[0] * 9,
                                        BTNPAD * 3 + BTNSIZE[1] * 2),
                                        "return",
                                        [gx(136), BTNSIZE[1]],
                                        [SBBG, SBBG],
                                        font_size=23)
    
        # Row $3
        self.addTextButton("letters", (gx(98), BTNPAD * 2 + BTNSIZE[1]), "Z")
        self.addTextButton("letters", (gx(98) + BTNSIZE[0] + BTNPAD,
                                        BTNPAD * 2 + BTNSIZE[1]), "X")
        self.addTextButton("letters", (gx(98) + BTNSIZE[0] * 2 + BTNPAD * 2,
                                        BTNPAD * 2 + BTNSIZE[1]), "C")
        self.addTextButton("letters", (gx(98) + BTNSIZE[0] * 3 + BTNPAD * 3,
                                        BTNPAD * 2 + BTNSIZE[1]), "V")
        self.addTextButton("letters", (gx(98) + BTNSIZE[0] * 4 + BTNPAD * 4,
                                        BTNPAD * 2 + BTNSIZE[1]), "B")
        self.addTextButton("letters", (gx(98) + BTNSIZE[0] * 5 + BTNPAD * 5,
                                        BTNPAD * 2 + BTNSIZE[1]), "N")
        self.addTextButton("letters", (gx(98) + BTNSIZE[0] * 6 + BTNPAD * 6,
                                        BTNPAD * 2 + BTNSIZE[1]), "M")
        self.addTextButton("letters", (gx(98) + BTNSIZE[0] * 7 + BTNPAD * 7,
                                        BTNPAD * 2 + BTNSIZE[1]), ",")
        self.addTextButton("letters", (gx(98) + BTNSIZE[0] * 8 + BTNPAD * 8,
                                        BTNPAD * 2 + BTNSIZE[1]), ".")
    
        # Row $4
        self.addTextButton("letters", (PADLEFT, BTNPAD),
            ".?123",
            (BTNSIZE[0] * 1.5, BTNSIZE[1]),
            [SBBG, SBBG],
            font_size=22)
        self.addTextButton("letters",
            (PADLEFT + BTNPAD * 3 + BTNSIZE[0] * 3, BTNPAD),
            "",
            (BTNSIZE[0] * 6 + BTNPAD * 5, BTNSIZE[1]))
    
    def getXPosition(self, xpos):
        """
        Return X position for current screen size.
        
        1024 is screen width for iPad3 in LANDSCAPE mode.
        """
        return xpos * self.scrsize.w/1024.
    
    def getYPosition(self, ypos):
        """
        Return Y position for current screen size.
        
        748. is screen height for iPad3 in LANDSCAPE mode.
        """
        return ypos * self.scrsize.h/748.
        
    
    def addTextButton(self, layout, pos, text, size=None,
                        bgcolours=[BDBG, BPBG], fgcolours=[TDFG, TPFG],
                        font_size=None):
        if not size:
            size = self.BTNSIZE
        if not font_size:
            font_size = 28
        
        if not isinstance(pos, Point):
            pos = Point(*pos)
        if not isinstance(size, Size):
            size = Size(*size)
        
        button = TextButton(self, pos, size, text, bgcolours, fgcolours, font_size)
        if not layout in self.layouts:
            self.layouts[layout] = []
        self.layouts[layout].append(button)
        
    def draw(self):
        fill(*self.bg)
        rect(*self.bounds)
        for button in self.layouts[self.curlayout]:
            button.draw()
    
    def touch_began(self, touch):
        for button in self.layouts[self.curlayout]:
            if touch.location in button.bounds:
                button.touch_began(touch)
                return
    
    def touch_moved(self, touch):
        for button in self.layouts[self.curlayout]:
            button.touch_moved(touch)
    
    def touch_ended(self, touch):
        for button in self.layouts[self.curlayout]:
            if touch.location in button.bounds:
                button.touch_ended(touch)
                return

class KeyboardTest(Scene):
    def setup(self):
        self.keyboard = Keyboard(self.size)
    
    def draw(self):
        self.keyboard.draw()
    
    def touch_began(self, touch):
        if touch.location in self.keyboard.bounds:
            self.keyboard.touch_began(touch)
            
    def touch_moved(self, touch):
        if touch.location in self.keyboard.bounds:
            self.keyboard.touch_moved(touch)
            
    def touch_ended(self, touch):
        if touch.location in self.keyboard.bounds:
            self.keyboard.touch_ended(touch)

run(KeyboardTest(), LANDSCAPE)
