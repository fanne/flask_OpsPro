# /usr/bin/python
#coding:utf-8

__Date__ = "2016-04-08 11:09"
__Author__ = 'eyu Fanne'

from app import create_app

app = create_app('default')

if __name__ == '__main__':
    app.run(debug=True,port=5003,host='0.0.0.0')
