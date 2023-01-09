"""
Author: Erutaner
Date: 2023.01.09
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time
import seaborn as sns

item_dloc = r"D:\桌面\武大本科期间文件\实习\大二寒假_亚马逊\1月4日第一次岗前培训\用户行为数据\item.csv"
user_dloc = r"D:\桌面\武大本科期间文件\实习\大二寒假_亚马逊\1月4日第一次岗前培训\用户行为数据\user_behavior.csv"


df_user = pd.read_csv(user_dloc)  # 读入用户文件

#  转化一下日期列的类型
df_user["time"] = pd.to_datetime(df_user["time"],format="%Y-%m-%d %H")


#  由于有两个月的数据，所以我们把十一月十二月分开，便于后面画图, 地理位置列
#  大量数据为空，直接把这列去掉
df_user_dec = df_user[df_user["time"].dt.month == 12].drop(columns ="user_geohash").reset_index(drop=True)


# PV（访问量）：具体是指网站页面浏览量或者点击量，页面被刷新一次就计算一次，按天算的话需先按天分组再统计各组数量
# UV（访问客户）：访问您网站的一台个客户端为一个访客，与上面类似，但是同一个用户多次访问只算为一次
df_user_dec_day = df_user_dec["user_id"].groupby(df_user_dec["time"].dt.day).agg([("PV", "count"), ("UV", "nunique")]).\
    reset_index().astype({"time":str})


# 对十一月份的数据进行类似的处理
df_user_nov = df_user[df_user["time"].dt.month == 11].drop(columns = "user_geohash").reset_index(drop=True)


df_user_nov_day = df_user_nov["user_id"].groupby(df_user_nov["time"].dt.day).agg([("PV","count"),("UV","nunique")]).\
    reset_index().astype({"time":str})

#  每行俩图共享一个y轴，这样十一月十二月正好连续起来
fig, axes = plt.subplots(2,2,sharey='row')
# fig应该是用来定义大图特征的
fig.suptitle("UV & PV in Nov and Dec")
axes[0, 0].plot(df_user_nov_day["time"], df_user_nov_day["UV"])

axes[0, 1].plot(df_user_dec_day["time"], df_user_dec_day["UV"], "tab:green")

axes[1, 0].plot(df_user_nov_day["time"], df_user_nov_day["PV"])

axes[1, 1].plot(df_user_dec_day["time"], df_user_dec_day["PV"], "tab:green")

axes[0,0].set(ylabel="UV")
axes[0,1].set(ylabel="UV")
axes[1,0].set(xlabel="Nov_day",ylabel="PV")
axes[1,1].set(xlabel="Dec_day",ylabel="PV")
#  避免使用科学计数法
plt.ticklabel_format(axis="y",style='plain')

