"""
Author: Erutaner
Date: 2023.01.09
"""
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

item_dloc = r"D:\桌面\武大本科期间文件\实习\大二寒假_亚马逊\1月4日第一次岗前培训\用户行为数据\item.csv"
user_dloc = r"D:\桌面\武大本科期间文件\实习\大二寒假_亚马逊\1月4日第一次岗前培训\用户行为数据\user_behavior.csv"
df_user = pd.read_csv(user_dloc)  # 读入用户文件
df_user_behavior = df_user["behavior_type"].value_counts().reset_index(drop=True)
df_user_behavior.info()

# print(df_user_behavior[0])
ls = [1]
ls.extend([df_user_behavior[i+1]/df_user_behavior[i] for i in range(3)])
data = {
    "behavior_type":["browse","add","collect","purchase"],
    "count": df_user_behavior,
    "inversion_rate_1":ls,
    "inversion_rate_2":[df_user_behavior[i]/df_user_behavior[0] for i in range(4)]
}
df = pd.DataFrame(data)

df.info()

df["rate_2_Percentage"] = df["inversion_rate_2"].apply(lambda x : format(x,".0%"))
df["behavior_type"] = df["behavior_type"]+": "+df["rate_2_Percentage"]

c = (
    Funnel(init_opts=opts.InitOpts(width="900px", height="600px",theme = ThemeType.PURPLE_PASSION ))
    .add(
        "commodity",
        df[["behavior_type","inversion_rate_2"]].values,
        sort_="descending",
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Funnel_Analysis", pos_bottom = "90%", pos_right = "17%"))
)
c.render("./test_1.html")