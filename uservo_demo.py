# 添加uservo.py的系统路径
# import sys
# sys.path.append("../../src")

# PySerial 负责串口总线通信
import time
import serial
import struct
import math
# UartServoManager 总线伺服舵机管理器
from uservo import UartServoManager
# 参数配置
# 角度定义
# USERVO_PORT_NAME = '/dev/ttyUSB0'  # 替换为实际的串口名称
USERVO_PORT_NAME = 'COM3'  # Windows系统下的串口名称
SERVO_BAUDRATE = 500000 # 舵机的波特率
SERVO_ID = 0  # 舵机的ID号

# 初始化串口
uart = serial.Serial(port=USERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,\
                     parity=serial.PARITY_NONE, stopbits=1,\
                     bytesize=8,timeout=0)
# 初始化舵机管理器
uservo = UartServoManager(uart,is_debug=True)

# 舵机通讯检测
# is_online = uservo.ping(SERVO_ID)
# print("舵机ID={} 是否在线: {}".format(SERVO_ID, is_online))


# print("[单圈模式]设置舵机角度为-90.0°, 添加功率限制")
# uservo.set_servo_angle(SERVO_ID, -90.0, power=500) # 设置舵机角度(指定功率 单位mW)
# uservo.wait() # 等待舵机静止


# print("[多圈模式]设置舵机角度为900.0°, 周期1000ms")
# uservo.set_servo_angle(SERVO_ID, 900.0, interval=1000, is_mturn=True) # 设置舵机角度(指定周期 单位ms)
# uservo.wait() # 等待舵机静止
# print("-> {}".format(uservo.query_servo_angle(SERVO_ID)))

# print("[多圈模式]设置舵机角度为-900.0°, 设置转速为200 °/s")
# uservo.set_servo_angle(SERVO_ID, -900.0, velocity=200.0, t_acc=100, t_dec=100, is_mturn=True) # 设置舵机角度(指定转速 单位°/s) dps: degree per second
# uservo.wait() # 等待舵机静止
# print("-> {}".format(uservo.query_servo_angle(SERVO_ID)))

# print("[多圈模式]设置舵机角度为-850.0°, 添加功率限制")
# uservo.set_servo_angle(SERVO_ID, 0.0, power=0, is_mturn=True) # 设置舵机角度(指定功率 单位mW)
# uservo.wait() # 等待舵机静止
# print("-> {}".format(uservo.query_servo_angle(SERVO_ID)))

# 重设多圈角度
# uservo.reset_multi_turn_angle(SERVO_ID)

# uservo.set_wheel_norm(SERVO_ID,is_cw=True,mean_dps=200.0)
# time.sleep(5.0)

# uservo.wheel_stop(SERVO_ID)
# time.sleep(1)

# 定圈模式
# print("测试定圈模式")
# uservo.set_wheel_turn(SERVO_ID, turn=5, is_cw=False, mean_dps=300.0)

# 定时模式
# print("测试定时模式")
# uservo.set_wheel_time(SERVO_ID, interval=5000, is_cw=True, mean_dps=300.0)
