from urllib import parse


url1 = 'https://www.baidu.com/artist?id=11363'
url2 = 'https://music.163.com/#/artist?id=11363'


result = parse.urlparse(url1)
a, b, c, d, e, f = result
print(result)
print(a, b, c, d, e, f)


