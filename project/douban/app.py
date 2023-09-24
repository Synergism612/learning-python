from flask import Flask
from flask_cors import CORS

import json

from project.douban.src.dataBase import MyDB
from project.douban.src.myServer import MyServer

# 创建Flask应用程序实例
app = Flask(__name__)
CORS(app)

db = MyDB()
db.link()
datasource = db.query("SELECT * FROM movie")
server = MyServer(datasource)


# 定义路由和视图函数
@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/types/category')
def types():
    return json.dumps(server.getTypesCategory())


@app.route('/types/cloud')
def typesData():
    return json.dumps(server.getTypesCloud())


@app.route('/year')
def year():
    return json.dumps(server.getYear())


@app.route('/duration')
def duration():
    return json.dumps(server.getDuration())


@app.route('/country')
def country():
    return json.dumps(server.getCountry())


@app.route('/all/<int:number>')
def all(number):
    return json.dumps(server.getAll(number))


# 运行应用程序
if __name__ == '__main__':
    app.run()
