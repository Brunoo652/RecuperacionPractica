import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Cell(Gtk.EventBox):
    name = None

    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
#        self.box.pack_start(Gtk.Label(label=name), False, False, 0)
#        self.box.pack_start(image, True, True, 0)
        self.add(box)

