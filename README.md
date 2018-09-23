# Python值得注意的地方（想到哪写到哪）

- `python -m http.server`，可以起一个 HTTP 服务器，可以用来下载当前目录下的文件。

- `python -c 'import os; print(os.urandom(16))'`，生成一串随机密钥。

- 把生成器转为列表后，生成器会耗尽（走一轮），所以不要把无限大小的生成器转换为列表！

- `a = b or c`，如果 `b` 是 `False`，那么值为 `or` 右边那个子表达式的值。

- 定义一个匿名函数：`lambda x, y: x * y`。

- Python中，`bool` 类型是 `int` 类型的一个子类：

  ```python
  isinstance(True, int)   # True
  isinstance(False, int)  # True

  True == 1 == 1.0 and False == 0 == 0.0  # True

  another_dict = {}
  another_dict[True] = "JavaScript"
  another_dict[1] = "Ruby"
  another_dict[1.0] = "Python"

  another_dict[True]  # Python
  ```

- 函数参数的默认值，会在每个模块加载进来时求出，所以不要用非静态类型做函数参数默认值，如：

  ```python
  # 每次调用时间都是一样的
  def log(message, when=datetime.now()):
      print('%s: %s' % (when, message))
  ```

  正确做法是，令 `when=None`，在函数内部调用 `when=datatime.now()` 。

- 四个推导式：

  ```python
  # 列表推导式
  [x * x for x in range(1, 11) if x % 2 == 0]
  
  # 字典推导式
  dic = {v:k for k, v in d.items()} # 逆转 key 和 value
  
  # 集合推导式
  a = {x for x in 'abracadabra' if x not in 'abc'}
  
  # 生成器推导式
  t = (x for x in range(9))
  ```

- 装饰器也在加载模块时执行。

- 调用函数时，指定参数名可以让函数更明确，用命名关键字参数强制要求指定参数名，如：

  ```python
  def person(name, age, *, city='Beijing', job)
  ```

- Python中有个内置变量 `_` 会存储上一次结果的值。

- 把字符串切割成列表的小技巧：如切割 `s = '1, 2, 3, 4, 5'`，逗号后面有空格，直接 `s.split(',')` 会留下空格，其实可以用 `s.replcae(',', ' ').split()`，这样就不会有空格了。

- 如果要调用函数来保存状态，那就应该定义新的类，并实现其 `__call__` 方法，而不要定义带状态的闭包。

- 总是应该使用内置的 `super()` 函数来初始化父类：

  ```python
  Class Implicit(MyBaseClass):
      def __init__(self, value):
          super().__init__(value*2)
  ```

- 使用 `+`，`*`，内置函数 `sorted()`，`reversed()`，对列表进行操作都会返回新到列表，但使用 `+=` 和列表的方法操作则会在原列表上修改。

- 原地操作函数一般会返回 `None`。

- 当 `count` 是数字或任何不可变类型时，`count += 1` 和 `count = count + 1` 一样。

- 通过调用 `id()` 函数来判断是否是同一对象，或操作后对象是否改变，如：

  ```python
  a = 10
  b = 10
  id(a) == id(b) # True
  
  L = []
  L += ['a']
  # 前后 id 没变
  
  L2 = []
  L2 = L2 + ['a']
  # 前后 id 改变，说明返回了一个新列表
  ```

- Python 采用基于值的内存管理模式，Python 变量中并不直接存放值，而是存放值到引用。所以在 Python 中修改变量值的操作，并不是直接修改变量的值，而是修改了变量指向的内存地址（引用），如 `a = a + 9` 或 `a += 6`，Python 解释器先读取变量 a 原来的值，然后将其加 6，并将结果存放于内存中，最后将变量 a 指向该内存。如果不同变量赋值为相同值，这个值在内存中只有一份，多个变量指向这个内存。**注意**：不同类型的变量的管理方式可能会不同。

- 获取字典中的最大或最小值：

  ```python
  d = {'a': -1, 'b': -2, 'c': -3}
  
  min(d, key=lambda k: d[k])  # -3
  max(d, key=lambda k: d[k])  # -1
  ```

  但以上方法无法获取键，可以用以下方法获取键和值：

  ```python
  min(d.items(), key=lambda x: x[1])  # ('c', -3)
  max(d.items(), key=lambda x: x[1])  # ('a', -1)
  ```

- 把两个列表变成一个字典可以：

  ```python
  keys = ['a', 'b', 'c', 'd']
  values = [1, 2, 3, 4]
  d = dict(zip(keys, values))
  ```

  字典转 `(key, value)` 组成的列表，可以：

  ```python
  lst = list(d.items()）
  ```

- `zip()` 函数生成到列表的长度是传入到最短列表成员长度，并且返回一个迭代器；若要返回最长的列表，则用 `itertools` 模块中的 `zip_longest()`，缺失的内容会被 `None`填充。

- 利用 `set()` 函数去掉列表，元组等其他可迭代对象中的重复元素，返回一个集合，集合只能包含不可变类型。

- 凡是无法计算哈希值（调用 `hash()` 函数抛出异常）的对象，都不是不可变类型。

- 字典和集合的 `in` 操作比列表快很多，因为 Python 字典和集合都用 hash 表来存储元素。

- 逻辑运算符 `and` 和 `or` 与C语言中一样，具有短路特性。

- 函数参数，不可变参数通过值传递，可变参数通过引用传递（对其任何修改会影响实参）。

- 可以用 `函数名.__defaults__` 随时查看函数所有默认值参数的当前值。

- 使字符串中连续多个不等长空格变为一个空格的方法：

  ```python
  s = 'aaa     bbb c     ddd'
  ' '.join(s.split())
  ```

- `isinstance` 和 `type` 的区别在于：

  ```python
  # 假设B继承于A
  
  # type() 不会认为子类是父类的一种类型
  type(B()) == A # False
  # isinstance() 认为子类是父类的一种类型
  isinstance(B(), A) # True
  ```

- 列表中元素必须全部是 `str` 类型，才能用 `join()` 方法。

- 列表操作：令 `a = [1, 2, 3, 4]`，可以使 `a[:2] = 5`，结果为 `[5, 3, 4]`；或 `del a[:2]`，结果为 `[4]` 。

- `a = 1, 2, 3` 相当于 `a = (1, 2, 3)`，但不建议这么写，不明确。

- 解包：`lst = [1, 2, 3, 4, 5]`，令 `a, *b, c = lst`，结果为 `a = 1; b = [2, 3, 4]; c = 5` 。`lst` 也可以是元组，但 `b` 还会是 `list` 类型。

- 解包2：`lst = [1, 2]`，令 `a, *b = lst`，结果为`a = 1; b = [2]` 。

- 字典操作：`dict(A=1, B='foo')`，结果为 `{'A':1, 'B':'foo'}`。

- `[.122, 1.]`，结果为 `[0.122, 1.0]`。

- 一个迷之操作：`t = (1, 2, [30, 40]); t += [50, 60]`，会抛出异常，但 `t` 的元素也改变了。因为元组虽然不可变，但若其成员可变，是能改变其成员值的。可以用 `t[2].extend([50, 60])` 避免这个异常，但是最好不要把可变对象放在元组中。

- 用切片来逆序列表，字符串等：`L[::-1]; word[::-1]`。

- 列表切片的高级操作：

  ```python
  l = [1, 2, 3, 4, 5, 6, 7]
  
  l[::-1] # [7, 6, 5, 4, 3, 2, 1]
  l[-1::-1] # [7, 6, 5, 4, 3, 2, 1]
  l[-1:0:-1] # [7, 6, 5, 4, 3, 2]
  l[-2:1:-1] # [6, 5, 4, 3]
  
  # 可以看到，当步长为 -1 时，切片序号要颠倒
  ```

- 每个 `.py` 文件都有一个 `__name__` 属性，当作为脚本运行时，该属性为 `__main__`，当作为模块导入时，该属性为模块名。

- 每个函数也有一个 `__name__` 属性可以获取函数名，还有个 `__module__` 属性可以获取所在模块名。

- 用 `__file__` 属性获取脚本文件路径，注意该路径不一定与 `os.getcwd()` 函数获取的路径相同。

- 用 `dir(name)` 查看模块，函数或类拥有的属性和方法；用 `help(name)` 查看模块，函数或类帮助。

- `dir(__builtins__)` 查看所有内置对象名称。

- `from dis import dis; dis(name)`，可以查看相关内容的Python字节码。

- `==` 运算符比较两个对象的值（对象中保存的数据），而 `is` 比较对象的标识（id），例子：

  ```python
  a = {'name':'hh', 'age': 7}
  b = c
  c = {'name':'hh', 'age': 7}
  
  a == b # True
  a == c # True
  
  a is b # True
  a is c # False
  ```

- Python 允许在 `class` 中定义一个 `__slots__` 属性，来限制该 `class` 实例能添加的属性，用法 `__slots__ = ('name', 'age')`，要注意，该属性只对当前类其作用，对继承它的子类不起作用。

- `import` 查找路径，先从当前目录下找，再从 `sys.path` 中找，找不到则抛出 `ModuleNotFoundError` 异常。

- 位运算符只能用于整数。

- 解除一个装饰器：通过访问被装饰函数的 `__wrapped__` 属性来获取原函数，注意这只对单个装饰器包装的函数有效。


- 元组或列表之间，可以相互比较，从第一个元素开始比，如果前面的比较已经可以确定结果了，后面的比较操作就不会发生了：

  ```python
  a = (1, 2)
  b = (1, 3)
  c = (2, 1)
  
  a < b  # True
  a < c  # True
  b < c  # True
  ```

  既然可以比较，那么它们组成的列表就可以用 `sort`，`min`，`max` 。

- 寻找两个字典的共同点：

  ```python
  # Find keys in common
  a.keys() & b.keys() # { 'x', 'y' }
  # Find keys in a that are not in b
  a.keys() - b.keys() # { 'z' }
  # Find (key,value) pairs in common
  a.items() & b.items() # { ('y', 2) }
  
  # 注意以上都是集合类型
  ```

  这些操作也可以用于修改或者过滤字典元素。比如，假如你想以现有字典构造一个排除几个指定键的新字典。下面利用字典推导来实现这样的需求：

  ```python
  # Make a new dictionary with certain keys removed
  c = {key:a[key] for key in a.keys() - {'z', 'w'}}
  # c is {'x': 1, 'y': 2}
  ```
