import shutil

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import requests
import threading
from main_window import MainWindow



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
        response = requests.get('https://raw.githubusercontent.com/CarlosAfundacion/EXAMEN/main/games.json')
        json_list = response.json()

        result = []

        for json_item in json_list:
            nombre = json_item.get("nombre")
            descripcion = json_item.get("descripcion")
            image_url = json_item.get("imagen_url")
            r = requests.get(image_url, stream=True)
            with open("temp.png", 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            image = Gtk.Image.new_from_file("temp.png")
            result.append({"image_url": image})
            result.append({"nombre": nombre})

        GLib.idle_add(self.start_main_window, result)

    def start_main_window(self, loaded_items_list):
        win = MainWindow(loaded_items_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()
