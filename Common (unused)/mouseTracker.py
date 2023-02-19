import tkinter


class trackMouse:

    def pointers(self, rootName):
        def callback(e):
            x = e.x
            y = e.y
            print("Pointer is currently at %d, %d" % (x, y))

        rootName.bind('<Motion>', callback)
