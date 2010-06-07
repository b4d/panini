#!/usr/bin/env python

# example helloworld2.py

import pygtk
pygtk.require('2.0')
import gtk
import stickers

class HelloWorld2:

    # Our new improved callback.  The data passed to this method
    # is printed to stdout.
    def callback(self, widget, data):
        print "Hello again - %s was pressed" % data

    # another callback
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Euro 2008")
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)
        self.box1 = gtk.HBox(False, 0)
        self.window.add(self.box1)
        self.button1 = gtk.Button("Zapri")

        # Now when the button is clicked, we call the "callback" method
        # with a pointer to "button 1" as its argument
        self.button1.connect("clicked", self.callback, "button 1")

        # Instead of add(), we pack this button into the invisible
        # box, which has been packed into the window.
        self.box1.pack_start(self.button1, True, True, 0)

        # Always remember this step, this tells GTK that our preparation for
        # this button is complete, and it can now be displayed.
        self.button1.show()


        # The order in which we show the buttons is not really important, but I
        # recommend showing the window last, so it all pops up at once.
        self.box1.show()
        self.window.show()

def main():
    gtk.main()

if __name__ == "__main__":
    hello = HelloWorld2()
    main()
