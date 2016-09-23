# # /usr/bin/python
# #coding:utf-8
#
# __Date__ = "2016-05-16 13:02"
# __Author__ = 'eyu Fanne'


warning_command = ['init','stop','start','restart','kill',';','&&']
allow_command = ['patch','com.my9yu.h5game.modules.patch']

myCommand = raw_input('输入你的命令:')
# print myCommand

for i in warning_command:
    if i in  myCommand:
        print 'warning...'



# if myCommand in allow_command and myCommand not in warning_command:
#     print 'succesfully'
# else:
#     print 'command error'


