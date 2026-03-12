# arm-production

## 写参数

### 什么手臂就用哪款手臂下的set-param.py文件，以violin-U25为例，特别注明：cello使用High_Rigidity_High_Jitter.py

步骤1： 修改set-param.py文件中的BAUDRATE参数为115200并保存文件，如下所示

```bash
BAUDRATE = 115200
```

步骤2： 运行set-param.py文件

```bash
python3 ./violin-U25/set-param.py 
```

步骤3： 修改set-param.py文件中的BAUDRATE参数为1000000并保存文件，如下所示

```bash
BAUDRATE = 1000000
```

步骤4： 运行set-param.py文件

```bash
python3 ./violin-U25/set-param.py 
```

步骤5： 手臂重新上下电后，运行freedom.py文件，进行关节自由度测试,检查零点是否正确，舵机转动是否有异响

```bash
python3 ./freedom.py
```
