from PIL import Image as PILImage
from PIL import ImageTk

class Sprite(object):
    pass

class Image(Sprite):
    def __init__(self, parent, path, dimensions=(None, None)):
        self.image = PILImage.open(path)

        if dimensions != (None, None):
            self.resize(dimensions[0], dimensions[1])

        self.tkimage = self.to_tkimage()
        self.position = [0, 0]
        self.tag = None
        self.parent = parent.canvas

    def resize(self, height, width, antialias=True):
        if antialias:
            self.image = self.image.resize((width, height), PILImage.ANTIALIAS)
        else:
            self.image = self.image.resize((width, height))

    def to_tkimage(self):
        return ImageTk.PhotoImage(self.image)

    def update_image(self):
        self.tkimage = self.to_tkimage()

    def draw(self):
        self.tag = self.parent.create_image(self.position[0], self.position[1], image=self.tkimage)
        self.parent.update()

    def destroy(self):
        self.parent.delete(self.tag)
        self.parent.update()

    def move_to(self, position):
        self.parent.coords(self.tag, position[0], position[1])
        self.parent.update()
        self.position = position

    def move_by(self, position):
        self.parent.move(self.tag, position[0], position[1])
        self.parent.update()
        self.position[0] += position[0]
        self.position[1] += position[1]

    def bind(self, key, function):
        self.parent.bind(key, function)
