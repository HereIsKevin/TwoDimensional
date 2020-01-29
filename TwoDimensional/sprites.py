from PIL import Image as PILImage
from PIL import ImageTk as PILImageTk


class Sprite(object):
    def __init__(self, parent):
        self._parent = parent
        self._tag = None
        self._position = [0, 0]
    
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    def position(self):
        return self._position

    def destory(self):
        self._parent._canvas.delete(self._tag)
        self._parent.update()

    def move_to(self, position):
        self._parent._canvas.coords(self.tag, *position)
        self._parent.update()
        self._position = position

    def move_by(self, position):
        self._parent._canvas.move(self._tag, *position)
        self._parent.update()
        self._position[0] += position[0]
        self._position[1] += position[1]


class Image(Sprite):
    def __init__(self, parent, path, dimensions=[None, None], antialias=True):
        super().__init__(parent)

        self._path = path
        self._image = PILImage.open(self._path)
        self._antialias = antialias

        if dimensions[0] == None and dimensions[1] == None:
            self._dimensions = list(self._image.size)
        else:
            self._dimensions = list(dimensions)

            if self._antialias:
                self._image = self._image.resize(
                    self._dimensions, PILImage.ANTIALIAS
                )
            else:
                self._image = self._image.resize(
                    self._dimensions, PILImage.ANTIALIAS
                )

        self._tkimage = PILImageTk.PhotoImage(self._image)

    @property
    def image(self):
        return self._path

    @image.setter
    def image(self, value):
        self._path = value
        self._image = PILImage.open(self._path)
        self._dimensions = list(self._image.size)
        self._tkimage = PILImageTk.PhotoImage(self._image)

    @property
    def antialias(self):
        return self._antialias

    @antialias.setter
    def antialias(self, value):
        self._antialias = value

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        self._dimensions = value

        if self._antialias:
            self._image = self._image.resize(
                self._dimensions, PILImage.ANTIALIAS
            )
        else:
            self._image = self._image.resize(
                self._dimensions, PILImage.ANTIALIAS
            )
    
    def draw(self):
        self._tag = self._parent._canvas.create_image(
            *self._position, image=self._tkimage
        )
        self._parent.update()



class Line(Sprite):
    def __init__(self, parent, coords, fill="black"):
        super().__init__(parent)

        self._coords = coords
        self._fill = fill
    
    def draw(self):
        self._tag = self._parent._canvas.create_line(*self._coords, fill=self._fill)
