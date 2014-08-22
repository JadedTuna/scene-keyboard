from scene import *
import keyboard
reload(keyboard) # Needed on iOS
ipad = keyboard.ipadlayout

class MyKeyboard(keyboard.Keyboard):
    def setup(self):
        print "MyKeyboard created!"
    
    def init(self):
        btn_abc = self.layouts["numbers-landscape"].getButtonByID(5000)
        btn_abc.action = lambda text: self.setLayout("letters-landscape")
        
        btn_123 = self.layouts["letters-landscape"].getButtonByID(5000)
        btn_123.action = lambda text: self.setLayout("numbers-landscape")

class KeyboardTest(Scene):
    def setup(self):
        self.keyboard = MyKeyboard(self.size)
        self.keyboard.setDefaultAction(self.settext)
        self.keyboard.setLayout("letters-landscape", ipad.TLandscape)
        self.keyboard.addLayout("letters-portrait",  ipad.TPortrait)
        
        self.keyboard.addLayout("numbers-landscape", ipad.NLandscape)
        self.keyboard.addLayout("numbers-portrait",  ipad.NPortrait)
        self.keyboard.init()
        
        self.text     = "Hello, Pythonista! Press any keyboard key."
    
    def settext(self, text):
        self.text = `text`[1:-1]
    
    def draw(self):
        background(0, 0, 0.5)
        tint(1, 1, 0)
        text(self.text, "Arial", 25, self.size.w/2., self.size.h/1.5)
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
