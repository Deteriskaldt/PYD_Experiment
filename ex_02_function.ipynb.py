# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#代码文件统一命名为ex_02_function.ipynb，并由组长上传至组长的GitHub账户，
#单独建立代码仓库repository，各组统一命名为:｀PYD_Experiment｀。

#文件中，需说明函数的意图，输入参数，和返回值等信息。并应用该函数实际运算演示。

#两块钢板用三个相同的铆钉链接。已至钢板宽度b＝100mm，厚度t=10mm，铆钉直径d=20mm，
#铆钉许用切应力[τ]=100Mpa,许用挤压切应力[σ]=300Mpa
#试求许用荷载

format_str_2="Pi with five decimals:%.5f,and enter a value with percent sign:%.4f %%"
from math import pi
new_str_2=format_str_2 % (pi,3.1415926)
print("new_str_2=format_str_2 % (pi,3.1415926)->{}".format(new_str_2))

#从库中读取圆周率


#先对每个铆钉所受剪力进行校核，求铆钉的最大荷载
def simple_func(τ,d):
    F=3*τ*(pi*(d**2)/4)
    return F
#设定每个铆钉所受剪切力的计算公式
#输入参数，τ为铆钉的许用切应力，d为每个铆钉的直径，F则为铆钉的最大许用切应力。

print("simple_func(100*(10**6),20*(10**-3))->{}".format(simple_func(100*(10**6),20*(10**-3))))

#代入数据，计算结果，得到返回值


#再对钢板所受挤压力进行校核，求钢板的最大荷载
def simple_func(σ,d,t):
    N=3*σ*d*t
    return N
#设定每片钢板所受挤压力的计算公式
#输入参数，σ为钢板的许用挤压应力，d为铆钉直径，N则为钢板的最大许用挤压力

print("simple_func(300*(10**6),20*(10**-3),10*(10**-3))->{}".format(simple_func(300*(10**6),20*(10**-3),10*(10**-3))))

#代入数据，计算结果，得到返回值


#许用荷载比较
F=94247.8
N=180000.0
if F<N:
    print("94247.8")
else:
    print("180000.0")
#得到铆钉和钢板的最大许用荷载