import matplotlib.pyplot as plt
import math



class CoordSelector:
    def __init__(self, image,keys=None):
        self.image = image
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.resultx = []
        self.resulty = []
        self.keys = keys
        if keys is not None:
            self.XY_info_dicts = []


    def onclick(self, event):
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
        x = math.ceil(event.xdata)
        y = math.ceil(event.ydata)

        plt.scatter(x, y, s=100, c='red', marker='o', alpha=0.4)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


        self.resultx.append(x)
        self.resulty.append(y)
        if self.keys is not None:
            info_dict = {}
            for key in self.keys:
                info_dict[key] = input(key + "=")
            self.XY_info_dicts.append(info_dict)



    def create_device(self):
        plt.imshow(self.image, cmap='gray_r')
        plt.show()
        if self.keys is None:
            return self.resultx, self.resulty
        return self.resultx, self.resulty, self.XY_info_dicts

def select_coord_on_pic(pic, keys=None):
    devcr = CoordSelector(pic, keys)
    return devcr.create_device()

