import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class LoadWindow(Gtk.Window):
    label = Gtk.Label("Cargando elementos...")
    spinner = Gtk.Spinner()
    box = Gtk.Box
    spinner = Gtk.Spinner()
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

    def __init__(self):
        super().__init__()
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(60)
        self.set_resizable(True)
        self.spinner.props.active = True

        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.spinner, True, True, 0)
        self.add(self.box)
