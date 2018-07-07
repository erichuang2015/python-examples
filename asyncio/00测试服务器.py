from flask import Flask
import time
 
 
app = Flask(__name__)


@app.route('/')
def index():
    time.sleep(3)
    return 'Hello!'
 

if __name__ == '__main__':
    # hreaded，这表明 Flask 启动了多线程模式，不然默认是只有一个线程的。
    # 如果不开启多线程模式，同一时刻遇到多个请求的时候，只能顺次处理
    app.run(threaded=True)
