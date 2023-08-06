import streamlit as st
st.title("可视化")
st.markdown("Visualization helps to identify patterns and errors in the data provided."
            "在streamlit中可以创建visualization dashboard数据看板。")
st.markdown("以bar直方图为例子，横坐标是相互独立的元素，比如地区，纵坐标是关心的指标，比如感染新冠的人数。")
import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.randn(40,4),columns=['C1','C2','C3','C4'])
st.bar_chart(df)
st.markdown("以line折线图为例子，横坐标是连续变动的元素，比如时间，纵坐标是关心的指标，比如股票的价格。")
st.line_chart(df)
st.markdown("以area面积图为例子，横坐标是连续变动的元素，比如位移，纵坐标是关心的指标，比如力，而面积图则突出了横纵的乘积就是能量指标")
st.area_chart(df)
st.markdown("streamlit可以讨论地图数据的可视化。")
st.title('map地图数据')
st.markdown("和散点图很类似，不过画布不再是XY轴而是世界地图。")
locate_map= pd.DataFrame(np.random.randn(50,2)/[10,10]+[15.4589,75.0078], columns=['latitude','longitude'])
st.map(locate_map)

st.markdown("graphviz是一个开源的python库，可以创建有节点和边的图对象。")
st.title('Graphviz')
st.graphviz_chart('''
digraph{
"Training data" -> "ML algorithm"
"ML algorithm" -> "Model"
"Model" -> "Result- Forecasting"
"New Data" -> "Model"
}
''')
st.markdown("python的seaborn也是一个可以渲染数据的library。violin图，提琴图是用于观察数据"
            "的中位数等统计特性。提琴图的横坐标一般是时间，纵坐标是关心的量比如账单总数，提琴图可以反应"
            "一个酒吧中男性客户和女性客户的账单总额的分布情况。男性和女性是不同group的数据。"
            "小提琴中可以展示四个维度的数据，横纵坐标是一个维度，不同的group是一个维度，还有核密度图的统计特征置信程度也是一个维度。")
# 如果要生成随机的小提琴图，需要输入 x,y 和 分组的变量。如何产生随机0,1变量。
year = ['2015','2016','2017','2018']
from random import choice
data=np.empty([50,2])
for i in range(50):
    data[i,0]=choice(year)
    data[i,1]=np.random.normal(100,30,1)
df_violin= pd.DataFrame(data, columns=['year','Bill'])
import matplotlib.pyplot as plt
import seaborn as sns
fig_violin= plt.figure(figsize=(10,5))
sns.violinplot(x="year", y= "Bill",data=df_violin)
st.pyplot(fig_violin)
st.markdown("有意思的点在于，violin这个图其实是从一个excel表中抽取数据，x和y是要抓取的列名，类似于特征抽取，所以需要dataframe这样的有列名的数据。")

st.title("strip graph")
st.markdown("strip图就是分组散点图。")
fig_strip= plt.figure(figsize=(10,5))
sns.stripplot(x="year", y= "Bill",data=df_violin)
st.pyplot(fig_strip)

