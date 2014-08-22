__all__ = ["Layout"]

from buttons import TextButton
from scene   import *

BDBG = (1.0, 1.0, 1.0) # Button Default BackGround
BPBG = (0.8, 0.8, 0.8) # Button Pressed BackGround

SDBG = (0.73, 0.74, 0.76) # Special button Default BackGround
SPBG = (1.0, 1.0, 1.0) # Special button Default BackGround

TDFG = (0.0, 0.0, 0.0) # Text Default ForeGround
TPFG = (0.0, 0.0, 0.0) # Text Pressed ForeGround


class Layout(object):
    """
    Represents a layout for keyboard.
    """
    def __init__(self):
        self.keyboard = None
        self.buttons  = []
        self.ids      = []
        self.daction  = None
        self.dsize    = Size(10, 10)
    
    def newID(self):
        """
        Returns a new, unused ID.
        """
        for id in self.ids:
            if not id + 1 in self.ids:
                return id + 1
    
    def setDefaultSize(self, size):
        if not isinstance(size, Size):
            size = Size(*size)
        self.dsize = size
    
    def addTextButton(self,
                        text,
                        value,
                        pos,
                        size=None,
                        bgcolours=[BDBG, BPBG],
                        fgcolours=[TDFG, TPFG],
                        fontfamily="Arial",
                        fontsize=28,
                        action=None,
                        id=-1):
        """
        Add a TextButton to layout.
        
        text       --> button text
        value      --> button value (will be used with action func)
        pos        --> button position
        size       --> button size
        bgcolours  --> a list of length 2 with backround colours for two modes:
                            default and pressed.
        fgcolours  --> a list of length 2 with foreground colours for two modes:
                            default and pressed.
        fontfamily --> font family used to render button's text
        fontsize   --> font size used to render button's text
        action     --> function to be executed when button is clicked
        id         --> button ID
        """
        if not size:
            size = self.dsize
        
        if not isinstance(pos, Point):
            pos = Point(*pos)
        if not isinstance(size, Size):
            size = Size(*size)
        
        if id == -1:
            id = self.newID()
        button = TextButton(text,
                            value,
                            pos,
                            size,
                            bgcolours,
                            fgcolours,
                            fontfamily,
                            fontsize,
                            action,
                            id)
        self.buttons.append(button)
    
    def addSpecialTextButton(self,
                                text,
                                value,
                                pos,
                                size=None,
                                fontfamily="Arial",
                                fontsize=28,
                                action=None,
                                id=-1):
        """
        Add a special TextButton to layout.
        Basically just adds a TextButton
            with different bg and fg colours.
        """
        return self.addTextButton(text,
                                    value,
                                    pos,
                                    size,
                                    [SDBG, SPBG],
                                    [TDFG, TPFG],
                                    fontfamily,
                                    fontsize,
                                    action,
                                    id)
    
    def getButtonByID(self, id):
        for button in self.buttons:
            if button.button_id == id:
                return button
    
    def init(self, keyboard):
        """
        This method inits all buttons.
        It is called automatically by Keyboard class.
        """
        self.keyboard = keyboard
        self.daction  = keyboard.daction
        for button in self.buttons:
            button.init(self.keyboard)
    
    def kbd_size(self):
        return Size(0, 0)
