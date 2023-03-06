import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import MainWindow

win = MainWindow()
win.show_all()

Gtk.main
