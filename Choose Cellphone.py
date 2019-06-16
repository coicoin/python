class Camera:
    def camera_method(self, px, zoom):
        self.px = px
        self.zoom = zoom
        print("Это родительский метод из класса Camera")
        print("У данного телефона камера", self.px, "MP. А zoom =", self.zoom)
        if (self.px >= 5):
            print("Твои снимки будут четкими")
        else:
            print("Не плохая камера. Но у моей бабушки и то камера была лучше!")
            
class Radio:
    def radio_method(self):
        print("Это родительский метод из класса Radio")

class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print("Это дочерний метод класса CellPhone")

cell_phone_a = CellPhone()
cell_phone_a.camera_method(5, 24)
cell_phone_a.radio_method()
