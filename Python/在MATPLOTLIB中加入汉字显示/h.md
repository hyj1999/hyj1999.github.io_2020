## 程序

```python
#!/usr/local/bin/python
# -*- coding: gbk -*-
#============================================================
# TEST1.PY                     -- by Dr. ZhuoQing 2020-08-29
#
# Note:
#============================================================
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
t = linspace(0, 10, 400)
sindata = sin(t)
cosdata = cos(t**2)
#font = FontProperties(fname=r'c:\windows\fonts\STSong.ttf', size=16)
#plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.rcParams['axes.unicode_minus'] = False  # Solve the minus sign problems
font = {'family':'SimHei',
        'weight':'bold',
        'size':'12'}
plt.rc('font', **font)
plt.rc('axes', unicode_minus=False)
plt.plot(t, sindata, label='sin(x)正弦')
plt.plot(t, cosdata, label='cos(x^2)余弦')
plt.xlabel("时间(秒)")
plt.ylabel("函数值(X)")
plt.title('显示sin，cos曲线')
#plt.xlabel("时间(秒)", fontproperties=font)
#plt.ylabel("函数值(X)", fontproperties=font)
#plt.title('显示sin，cos曲线', fontproperties=font)
plt.grid(True)
plt.tight_layout() #密致布局
plt.legend(loc='upper right') #显示图例
plt.show()
#------------------------------------------------------------
#        END OF FILE : TEST1.PY
#============================================================
```

## 程序说明与原文链接

https://blog.csdn.net/zhuoqingjoking97298/article/details/108290519