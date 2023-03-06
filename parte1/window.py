import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from load_window import LoadWindow


class MainWindow(Gtk.Window):
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    button = Gtk.Button(label="Listar Videojuegos")
    label = Gtk.Label("Juegos más esperados")

    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.box)
        #self.add(self.button)
        self.box.pack_start(self.button, True, True, 0)
        self.box.pack_start(self.label, True, True, 0)


    def on_button_clicked(self):
        w = LoadWindow()
        w.show_all()
