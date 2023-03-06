import shutil

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import requests
import threading


class DetailWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.connect("destroy", Gtk.main_quit)

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
        #    result.append({"descripcion": descripcion})
         #   result.append({"nombre": nombre})


        GLib.idle_add(self.start_main_window, result)