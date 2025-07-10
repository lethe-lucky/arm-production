'''
总线伺服舵机
> Python SDK同步指令 Example <
--------------------------------------------------
 * 作者: 深圳市华馨京科技有限公司
 * 网站：https://fashionrobo.com/
 * 更新时间: 2024/12/23
--------------------------------------------------
'''
# 添加uservo.py的系统路径
import sys
sys.path.append("../../src")


import time
import serial
import struct
# 导入串口舵机管理器
from uservo import UartServoManager
# 设置日志输出模式为INFO
USERVO_PORT_NAME = '/dev/ttyUSB0'  # 替换为实际的串口名称
# USERVO_PORT_NAME = 'COM3'  # Windows系统下的串口名称
uart = serial.Serial(port=USERVO_PORT_NAME, baudrate=1000000,\
                     parity=serial.PARITY_NONE, stopbits=1,\
                     bytesize=8,timeout=0)
srv_num = 7# 舵机个数
uservo = UartServoManager(uart, is_debug=True)


command_data_list1 = [
    struct.pack('<BhHHHH', 0, 0, 2000, 100, 100, 0) , # 同步命令角度模式控制(基於加减速時間)
    struct.pack('<BhHHHH', 1, 0, 2000, 100, 100, 0) , #id2+度数40+总时间+启动加速时间+运动减速时间+功率
    struct.pack('<BhHHHH', 2, 0, 2000, 100, 100, 0) ,
    struct.pack('<BhHHHH', 3, 0, 2000, 100, 100, 0) ,
    struct.pack('<BhHHHH', 4, 0, 2000, 100, 100, 0) ,
    struct.pack('<BhHHHH', 5, 0, 2000, 100, 100, 0) ,
    struct.pack('<BhHHHH', 6, 0, 2000, 100, 100, 0) ,
]
uservo.send_sync_anglebyinterval(11, 7, command_data_list1)
time.sleep(2.02)

uservo.set_servo_angle(0, -50.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(0, 50.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(0, 0.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)

uservo.set_servo_angle(1, -50.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(1, 20.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(1, -70.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)

uservo.set_servo_angle(2, 60.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(2, -20.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(2, 60.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)

uservo.set_servo_angle(3, -60.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(3, 60.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(3, 0.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)

uservo.set_servo_angle(4, -60.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(4, 60.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(4, 0.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)

uservo.set_servo_angle(5, -60.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(5, 60.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(5, 0.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)

uservo.set_servo_angle(6, 45.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(6, 0.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)
uservo.set_servo_angle(6, 45.0,interval=1000,t_acc=100,t_dec=100,power=0)
time.sleep(1.02)

command_data_list2 = [
    struct.pack('<BhHHHH', 0, 0, 2000, 100, 100, 0) , # 同步命令角度模式控制(基於加减速時間)
    struct.pack('<BhHHHH', 1, 0, 2000, 100, 100, 0) , #id2+度数40+总时间+启动加速时间+运动减速时间+功率
    struct.pack('<BhHHHH', 2, 0, 2000, 100, 100, 0) ,
    struct.pack('<BhHHHH', 3, 0, 2000, 100, 100, 0) ,
    struct.pack('<BhHHHH', 4, 0, 2000, 100, 100, 0) ,
    struct.pack('<BhHHHH', 5, 0, 2000, 100, 100, 0) ,
    struct.pack('<BhHHHH', 6, 0, 2000, 100, 100, 0) ,
]
uservo.send_sync_anglebyinterval(11, 7, command_data_list2)
time.sleep(2.02)
