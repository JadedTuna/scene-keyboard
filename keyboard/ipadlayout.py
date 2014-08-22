from layout import Layout
from scene import *

class LSLayout(Layout):
    def kbd_size(self):
        return (self.keyboard.scrsize.w, 362)

#####################################################################################
# iPad layouts
#####################################################################################

#####################################################################################
#
# Landscape Text
#
#####################################################################################
TLandscape = LSLayout()

ROW1PAD   = 6.5
BTNSIZE   = Size(81, 75)
BTNPAD    = 12
ROW2PAD   = 45
ROW3PAD   = 98

BTNSIZE_RETURN = (136, BTNSIZE[1])
BTNSIZE_SPACEBAR = (BTNSIZE[0] * 6 + BTNPAD * 5, BTNSIZE[1])

TLandscape.setDefaultSize(BTNSIZE)
# Rows are counted from top
# Row $1
TLandscape.addTextButton("Q", "q", (ROW1PAD, BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("W", "w", (ROW1PAD + BTNPAD * 1 + BTNSIZE[0] * 1,
                                BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("E", "e", (ROW1PAD + BTNPAD * 2 + BTNSIZE[0] * 2,
                                BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("R", "r", (ROW1PAD + BTNPAD * 3 + BTNSIZE[0] * 3,
                                BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("T", "t", (ROW1PAD + BTNPAD * 4 + BTNSIZE[0] * 4, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("Y", "y", (ROW1PAD + BTNPAD * 5 + BTNSIZE[0] * 5, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("U", "u", (ROW1PAD + BTNPAD * 6 + BTNSIZE[0] * 6, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("I", "i", (ROW1PAD + BTNPAD * 7 + BTNSIZE[0] * 7, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("O", "o", (ROW1PAD + BTNPAD * 8 + BTNSIZE[0] * 8, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
TLandscape.addTextButton("P", "p", (ROW1PAD + BTNPAD * 9 + BTNSIZE[0] * 9, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))

# Row $2
TLandscape.addTextButton("A", "a", (ROW2PAD, BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addTextButton("S", "s", (ROW2PAD + BTNPAD * 1 + BTNSIZE[0] * 1,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addTextButton("D", "d", (ROW2PAD + BTNPAD * 2 + BTNSIZE[0] * 2,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addTextButton("F", "f", (ROW2PAD + BTNPAD * 3 + BTNSIZE[0] * 3,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addTextButton("G", "g", (ROW2PAD + BTNPAD * 4 + BTNSIZE[0] * 4,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addTextButton("H", "h", (ROW2PAD + BTNPAD * 5 + BTNSIZE[0] * 5,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addTextButton("J", "j", (ROW2PAD + BTNPAD * 6 + BTNSIZE[0] * 6,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addTextButton("K", "k", (ROW2PAD + BTNPAD * 7 + BTNSIZE[0] * 7,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addTextButton("L", "l", (ROW2PAD + BTNPAD * 8 + BTNSIZE[0] * 8,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
TLandscape.addSpecialTextButton("return", "\n", (ROW2PAD + BTNPAD * 9 + BTNSIZE[0] * 9,
                                        BTNPAD * 3 + BTNSIZE[1] * 2),
                                        BTNSIZE_RETURN,
                                        "Arial",
                                        23)

# Row $3
TLandscape.addTextButton("Z", "z", (ROW3PAD, BTNPAD * 2 + BTNSIZE[1]))
TLandscape.addTextButton("X", "x", (ROW3PAD + BTNSIZE[0] + BTNPAD,
                                        BTNPAD * 2 + BTNSIZE[1]))
TLandscape.addTextButton("C", "c", (ROW3PAD + BTNSIZE[0] * 2 + BTNPAD * 2,
                                        BTNPAD * 2 + BTNSIZE[1]))
TLandscape.addTextButton("V", "v", (ROW3PAD + BTNSIZE[0] * 3 + BTNPAD * 3,
                                        BTNPAD * 2 + BTNSIZE[1]))
TLandscape.addTextButton("B", "b", (ROW3PAD + BTNSIZE[0] * 4 + BTNPAD * 4,
                                        BTNPAD * 2 + BTNSIZE[1]))
TLandscape.addTextButton("N", "n", (ROW3PAD + BTNSIZE[0] * 5 + BTNPAD * 5,
                                        BTNPAD * 2 + BTNSIZE[1]))
TLandscape.addTextButton("M", "m", (ROW3PAD + BTNSIZE[0] * 6 + BTNPAD * 6,
                                        BTNPAD * 2 + BTNSIZE[1]))
TLandscape.addTextButton(",", ",", (ROW3PAD + BTNSIZE[0] * 7 + BTNPAD * 7,
                                        BTNPAD * 2 + BTNSIZE[1]))
TLandscape.addTextButton(".", ".", (ROW3PAD + BTNSIZE[0] * 8 + BTNPAD * 8,
                                        BTNPAD * 2 + BTNSIZE[1]))

# Row $4
TLandscape.addSpecialTextButton(".?123", ".?123", (ROW1PAD, BTNPAD),
            (BTNSIZE[0] * 1.5, BTNSIZE[1]),
            "Arial",
            22,
            id=5000)
TLandscape.addTextButton("", " ",
            (ROW1PAD + BTNPAD * 3 + BTNSIZE[0] * 3, BTNPAD),
            BTNSIZE_SPACEBAR)

#####################################################################################
#
# Portrait Text
#
#####################################################################################
TPortrait  = Layout()

#####################################################################################
#
# Landscape Numbers
#
#####################################################################################
NLandscape = LSLayout()
ROW1PAD   = 6.5
BTNSIZE   = Size(81, 75)
BTNPAD    = 12
ROW2PAD   = 45
ROW3PAD   = 98

BTNSIZE_UNDO     = (BTNSIZE[0] * 2 + BTNPAD, BTNSIZE[1])
BTNSIZE_RETURN   = (136, BTNSIZE[1])
BTNSIZE_SPACEBAR = (BTNSIZE[0] * 6 + BTNPAD * 5, BTNSIZE[1])

NLandscape.setDefaultSize(BTNSIZE)
# Rows are counted from top
# Row $1
NLandscape.addTextButton("1", "1", (ROW1PAD, BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("2", "2", (ROW1PAD + BTNPAD * 1 + BTNSIZE[0] * 1,
                                BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("3", "3", (ROW1PAD + BTNPAD * 2 + BTNSIZE[0] * 2,
                                BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("4", "4", (ROW1PAD + BTNPAD * 3 + BTNSIZE[0] * 3,
                                BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("5", "5", (ROW1PAD + BTNPAD * 4 + BTNSIZE[0] * 4, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("6", "6", (ROW1PAD + BTNPAD * 5 + BTNSIZE[0] * 5, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("7", "7", (ROW1PAD + BTNPAD * 6 + BTNSIZE[0] * 6, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("8", "8", (ROW1PAD + BTNPAD * 7 + BTNSIZE[0] * 7, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("9", "9", (ROW1PAD + BTNPAD * 8 + BTNSIZE[0] * 8, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))
NLandscape.addTextButton("0", "0", (ROW1PAD + BTNPAD * 9 + BTNSIZE[0] * 9, 
                                BTNPAD * 4 + BTNSIZE[1] * 3))

# Row $2
NLandscape.addTextButton("-", "-", (ROW2PAD, BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addTextButton("/", "/", (ROW2PAD + BTNPAD * 1 + BTNSIZE[0] * 1,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addTextButton(":", ":", (ROW2PAD + BTNPAD * 2 + BTNSIZE[0] * 2,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addTextButton(";", ";", (ROW2PAD + BTNPAD * 3 + BTNSIZE[0] * 3,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addTextButton("(", "(", (ROW2PAD + BTNPAD * 4 + BTNSIZE[0] * 4,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addTextButton(")", ")", (ROW2PAD + BTNPAD * 5 + BTNSIZE[0] * 5,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addTextButton("$", "$", (ROW2PAD + BTNPAD * 6 + BTNSIZE[0] * 6,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addTextButton("&", "&", (ROW2PAD + BTNPAD * 7 + BTNSIZE[0] * 7,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addTextButton("@", "@", (ROW2PAD + BTNPAD * 8 + BTNSIZE[0] * 8,
                                BTNPAD * 3 + BTNSIZE[1] * 2))
NLandscape.addSpecialTextButton("return", "\n", (ROW2PAD + BTNPAD * 9 + BTNSIZE[0] * 9,
                                        BTNPAD * 3 + BTNSIZE[1] * 2),
                                        BTNSIZE_RETURN,
                                        "Arial",
                                        23)

# Row $3
NLandscape.addTextButton("undo", "undo", (ROW3PAD, BTNPAD * 2 + BTNSIZE[1]),
                                        BTNSIZE_UNDO)
NLandscape.addTextButton(".", ".", (ROW3PAD + BTNSIZE[0] * 2 + BTNPAD * 2,
                                        BTNPAD * 2 + BTNSIZE[1]))
NLandscape.addTextButton(",", ",", (ROW3PAD + BTNSIZE[0] * 3 + BTNPAD * 3,
                                        BTNPAD * 2 + BTNSIZE[1]))
NLandscape.addTextButton("?", "?", (ROW3PAD + BTNSIZE[0] * 4 + BTNPAD * 4,
                                        BTNPAD * 2 + BTNSIZE[1]))
NLandscape.addTextButton("!", "!", (ROW3PAD + BTNSIZE[0] * 5 + BTNPAD * 5,
                                        BTNPAD * 2 + BTNSIZE[1]))
NLandscape.addTextButton("'", "'", (ROW3PAD + BTNSIZE[0] * 6 + BTNPAD * 6,
                                        BTNPAD * 2 + BTNSIZE[1]))
NLandscape.addTextButton("\"", "\"", (ROW3PAD + BTNSIZE[0] * 7 + BTNPAD * 7,
                                        BTNPAD * 2 + BTNSIZE[1]))
NLandscape.addSpecialTextButton("#+=", "#+=", (ROW1PAD,
                                        BTNPAD * 2 + BTNSIZE[1]),
                                        fontsize=22)

# Row $4
NLandscape.addSpecialTextButton("ABC", "ABC", (ROW1PAD, BTNPAD),
            (BTNSIZE[0] * 1.5, BTNSIZE[1]),
            "Arial",
            22,
            id=5000)
NLandscape.addTextButton("", " ",
            (ROW1PAD + BTNPAD * 3 + BTNSIZE[0] * 3, BTNPAD),
            BTNSIZE_SPACEBAR)
# Rows are counted from top

#####################################################################################
#
# Portrait Numbers
#
#####################################################################################
NPortrait  = Layout()
