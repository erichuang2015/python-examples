#!/usr/bin/env python3
# coding: utf-8

"""验证码生成模块."""

__author__ = 'zzzzer'

import io
import platform
import re
from random import choice, randint
from string import ascii_letters, digits

from PIL import Image, ImageDraw, ImageFont


class Captcha:
    """验证码类."""

    size = (70, 32)
    length = 4
    characters = re.sub(r'[oOiI]', '', ascii_letters) + digits * 4
    color_list = ('black', 'darkblue', 'darkred', 'darkgreen')
    if platform.system() == 'Linux':
        font = ImageFont.truetype('/usr/share/fonts/winfonts/arial.ttf', 24)
    elif platform.system() == 'Windows':
        font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 24)

    @classmethod
    def _rand_text(cls):
        """生成指定长度英文数字混合字符串.

        :rtype: str.       
        """

        return ''.join(choice(cls.characters) for i in range(cls.length))

    @classmethod
    def _rand_color(cls):
        """获取一个随机颜色.

        :rtype: str.
        """

        return choice(cls.color_list)

    def __init__(self):
        self.image = Image.new('RGB', self.size, (255, 255, 255))
 
    def draw(self):
        """绘制验证码图片, 返回验证码答案.

        :rtype: str.
        """

        draw = ImageDraw.Draw(self.image)
        width, height = self.size

        # 绘制验证码字符串
        text = self._rand_text()
        offset = 0
        for i in range(self.length):
            position = (offset, randint(-5, 5))
            draw.text(xy=position, text=text[i], font=self.font, fill=self._rand_color())
            offset += width // self.length

        # 绘制干扰点
        for i in range(int(width * height * 0.05)):
            draw.point((randint(0, width), randint(0, height)), fill=self._rand_color())
        # 绘制干扰线条
        for i in range(2):
            start = (0, randint(0, height - 1))
            end = (width, randint(0, height - 1))
            draw.line((start, end), fill=self._rand_color(), width=1)
        # 绘制干扰曲线
        for i in range(2):
            start = (-50, -50)
            end = (width + 10, randint(0, height + 10))
            draw.arc(start + end, 0, 360, fill=self._rand_color())

        return text
 
    def raw(self):
        """生成验证码图片字节流, 可通过HttpResponse发给用户.

        :rtype: bytes.
        """

        stream = io.BytesIO()
        self.image.save(stream, 'png')
        return stream.getvalue()

    def show(self):
        """在图片浏览器中查看生成的验证码.
        
        """

        self.image.show()

    def save(self, img_name='temp.jpg'):
        """保存生成的验证码.
        
        """
        
        self.image.save(img_name)


def build_captcha():
    """返回验证码字符串和验证码图片字节流.

    :rtype: (str, raw).
    """
    captcha = Captcha()
    code = captcha.draw()
    raw = captcha.raw()
    return code, raw


if __name__ == '__main__':

    # from finished import finished
    # # 检查性能
    # @finished
    # def test():
    #     for i in range(3000):
    #         img = Captcha()
    #         code = img.draw()
    # test()

    img = Captcha()
    code = img.draw()
    img.show()
