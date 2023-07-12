# pyquadim
简单移植 quadim 到 Python 中。

## 用法
~~~ python
from PIL import Image
import pyquadim

img = Image.open("./test.jpg")
img = img.convert("RGBA")

w, h = img.size
data = img.getdata()

result = pyquadim.render(data, w, h, shape="yr-add", thres_ay=10., stroke_width=6)

img.putdata(result)
img.show()
~~~


## 链接
[Quadim](https://github.com/eternal-io/quadim)