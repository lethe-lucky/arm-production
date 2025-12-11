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

uservo.reset_multi_turn_angle(0xff)
time.sleep(1.02)

# 初始化舵机到0度位置
for i in range(7):
    uservo.set_servo_angle(i, 0.0, interval=2000, is_mturn=True)
    time.sleep(0.05)

# 60Hz舵机控制程序
# 控制舵机：0,1,2,4号舵机
servo_ids = [0, 1, 2, 4]
# 角度范围：0度到2度
start_angle = 0.0
end_angle = 2.0
# 分割份数：60份
steps = 60
# 60Hz控制频率，每个周期16.67ms
interval_time = 16.67  # ms

while True:
    # 从0度到2度，切割60份
    for i in range(steps + 1):
        # 计算当前角度并转换为整数（乘以100）
        current_angle = start_angle + (end_angle - start_angle) * i / steps
        angle_int = int(current_angle * 10)  # 角度乘以100转换为整数
        
        # 只控制0,1,2,4号舵机
        command_data_list = []
        for servo_id in servo_ids:
            command_data = struct.pack('<BhHHHH', servo_id, angle_int, 350, 20, 20, 0)  # 总时间17ms，加速减速各1ms
            command_data_list.append(command_data)
        
        uservo.send_sync_anglebyinterval(11, len(servo_ids), command_data_list)
        time.sleep(0.016)  # 16ms等待，实现60Hz
    
    # 从2度回到0度，同样切割60份
    for i in range(steps + 1):
        # 计算当前角度并转换为整数（乘以100）
        current_angle = end_angle - (end_angle - start_angle) * i / steps
        angle_int = int(current_angle * 10)  # 角度乘以100转换为整数
        
        # 只控制0,1,2,4号舵机
        command_data_list = []
        for servo_id in servo_ids:
            command_data = struct.pack('<BhHHHH', servo_id, angle_int, 350, 20, 20, 0)  # 总时间17ms，加速减速各1ms
            command_data_list.append(command_data)
        
        uservo.send_sync_anglebyinterval(11, len(servo_ids), command_data_list)
        time.sleep(0.016)  # 16ms等待，实现60Hz