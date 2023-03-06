import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import MainWindow
#from load_window import LoadWindow

win = MainWindow()
win.show_all()

Gtk.main()

"""
w= LoadWindow()
w.show_all()

Gtk.main()
"""
