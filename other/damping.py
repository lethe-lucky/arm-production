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

uservo.reset_multi_turn_angle(0xff)
time.sleep(1.02)

uservo.stop_on_control_mode(0xff,0x12,900)
time.sleep(1.02)
