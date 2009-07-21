import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Label import Label
from pyjamas import Window
from pyjamas.ui.TextArea import TextArea

def greet(fred):
    print "greet button"
    Window.alert("Hello, AJAX!")

class TextBoxListener:
    def onClick(self, sender):
        print "on_click"

    def onKeyUp(self, sender, keyCode, modifiers):
        print "on_key_up"

    def onKeyDown(self, sender, keyCode, modifiers):
        print "on_key_down"

    def onKeyPress(self, sender, keyCode, modifiers):
        print "on_key_press"


if __name__ == '__main__':
    pyjd.setup("../templates/Hello.html")
    b = Button("Click me", greet, StyleName='teststyle')
    h = HTML("<b>Hello World</b> (html)", StyleName='teststyle')
    l = Label("Hello World (label)", StyleName='teststyle')
    t = TextArea()
    listener = TextBoxListener()
    t.addKeyboardListener(listener)
    t.addClickListener(listener)
    RootPanel().add(b)
    RootPanel().add(h)
    RootPanel().add(l)
    RootPanel().add(t)
    pyjd.run()
