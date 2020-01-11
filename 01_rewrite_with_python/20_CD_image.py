import time
from skimage import io
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Icon():
    def get_icon_width(self):
        pass

    def get_icon_height(self):
        pass

    def paint_icon(self):
        pass


class ImageProxy(Icon):
    def __init__(self, img_src):
        print('CD 封面加载中，请稍候...')
        time.sleep(2)
        self.image_icon = ImageIcon(img_src)
        if self.image_icon != None:
            self.paint_icon()
        else: 
            print('加载失败！')

    def get_icon_width(self):
        if self.image_icon != None:
            return self.image_icon.get_icon_width()
        else:
            return 800

    def get_icon_height(self):
        if self.image_icon != None:
            return self.image_icon.get_icon_height()
        else:
            return 600

    def paint_icon(self):
        self.image_icon.paint_icon()


class ImageIcon(Icon):
    def __init__(self, img_src):
        self.image = io.imread(img_src)

    def get_icon_width(self):
        print(self.image.shape[1])  #图片宽度

    def get_icon_height(self):
        print(self.image.shape[0])  #图片高度

    def paint_icon(self):
        io.imshow(self.image)
        io.show()


url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2104351895,3299575660&fm=26&gp=0.jpg'
image = ImageProxy(url)