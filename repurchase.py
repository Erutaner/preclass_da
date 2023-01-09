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
# 十一月下半月和十二月上半月的复购率分开算
# 先算十二月的
df_user_dec = df_user[df_user["time"].dt.month == 12].drop(columns ="user_geohash").reset_index(drop=True)
df_user_dec["day"] = df_user_dec["time"].dt.day
df_user_dec = df_user_dec.astype({"day":str})
# 把购买行为，即代号4的抽取出来
df_buy_dec = df_user_dec[df_user_dec["behavior_type"]==4]
# 筛选复购数据, nunique相当于去重之后再计数
rep = df_buy_dec.groupby("user_id").filter(lambda x : x["day"].nunique()>1)

print("The repurchase rate of december is:",rep["user_id"].nunique()/df_user_dec["user_id"].nunique())
# 输出结果：The repurchase rate of december is: 0.6408828591677634

# 下面处理十一月份
df_user_nov = df_user[df_user["time"].dt.month == 11].drop(columns ="user_geohash").reset_index(drop=True)
df_user_nov["day"] = df_user_nov["time"].dt.day
df_user_nov = df_user_nov.astype({"day":str})
df_buy_nov = df_user_nov[df_user_nov["behavior_type"]==4]
rep_nov = df_buy_nov.groupby("user_id").filter(lambda x : x["day"].nunique()>1)
print("The repurchase rate of november is:",rep_nov["user_id"].nunique()/df_user_nov["user_id"].nunique())
# 输出结果：The repurchase rate of november is: 0.49321100917431193