import shutil

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import requests
import threading
from main_window import MainWindow2


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

       # self.load_json()
        self.launch_load()

    def launch_load(self):
        thread = threading.Thread(target=self.load_json, args=())
        thread.start()

    def load_json(self):
        response = requests.get('https://github.com/CarlosAfundacion/EXAMEN/blob/main/games.json')
        json_list = response.json()

        result = []

        for json_item in json_list:
            name = json_item.get("name")
            descripcion = json_item.get("descripcion")
            image_url = json_item.get("imagen_url")
            r = requests.get("imagen_url", stream=True)
            with open("temp.png", 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            image = Gtk.image.new_from_file("temp.png")
            result.append({"nombre": name}, {"descripcion": descripcion}, {"gtk_image": image})

        GLib.idle_add(self.start_main_window, result)

    def start_main_window(self, loaded_items_list):
        win = MainWindow2(loaded_items_list)
        win.show_all()
        # self.disconnect_by_func(Gtk.main_quit)
        self.close()
