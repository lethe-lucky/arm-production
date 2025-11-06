# 添加uservo.py的系统路径
# import sys
# sys.path.append("../../src")

# PySerial 负责串口总线通信
import time
import serial
import struct
import math

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

SERVO_ID=3
targetangle=-0.4

uservo.reset_multi_turn_angle(0xff)
time.sleep(1.02)

while(True):
    uservo.set_servo_angle(servo_id=SERVO_ID, angle=targetangle, interval=350, t_acc=50, t_dec=50, power=0, is_mturn=True)
    time.sleep(1.02)
    curren_angle = uservo.query_servo_angle(servo_id=SERVO_ID)
    print(f"角度: {curren_angle:.1f}")