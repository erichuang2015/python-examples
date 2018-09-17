"""从数据库中读取指定图片二进制流，并通过PIL展现出来。"""

import sqlite3
from io import BytesIO

from PIL import Image


def look_img(info: dict, nj: int, method: str='and') -> Image:
    """查看指定信息所有照片.

    :param info: 查询的信息;
                 key支持字段: xm(姓名), xb(性别), xh(学号), bj(班级), xy(学院), zy(专业).
                 value支持通配符:'_': 替代一个字符.
                                '%': 替代0个或多个字符.
                 value支持多字段查询, 如{'xm':['刘__', '王%']}.
                 
    :param nj: 查询的年级.
    
    :param method: 查询方法, and或者or.
    """
    
    lst = []
    for k, v in info.items():
        if isinstance(v, (list, tuple)):
            s = ' or '.join('{} like "{}"'.format(k, i) for i in v)
        else:
            s = '{} like "{}"'.format(k, v)
        lst.append('({})'.format(s))
    condition = ' {} '.format(method).join(lst)

    db = sqlite3.connect('students.sqlite')
    cursor = db.cursor()
    # TODO 注意这里会被sql注入, 实际中不能这么用
    cursor.execute('select img from info{} where {}'.format(nj, condition))
    lst = cursor.fetchall()
    
    imgs = Image.new('RGBA', (150 * 6, 200 * (len(lst) // 6 + 1)))  # 打底背景
    x, y = 0, 0  # 照片坐标
    for stream in lst:
        with BytesIO(stream[0]) as f:
            img = Image.open(f)
            img = img.resize((144, 192))  # resize照片
            imgs.paste(img, (x % 6 * 150, y * 200))  # 在打底背景上铺设照片
        x += 1
        if x % 6 == 0:  # 每行显示6张照片
            y += 1
    return imgs


def main():
    nj = 2014
    info = {'xm': ['王__'], 'xb': '男', 'bj': '%计科3'}
    look_img(info, nj).show()


if __name__ == '__main__':
    main()
