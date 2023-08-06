# import streamlit library.
import streamlit as st
st.title("streamlit与格式化文本")
st.header("这是一个标题")
st.subheader("这是一个副标题")
st.caption("这是一个小标题，用于描述脚注，表格，图片和视频。")
st.text("文本的展示方式：title,header, subheader, caption,text,其实也可以用markdown的方式来处理文本")
st.markdown("# markdown格式下的标题哦")
st.text("还支持用latex语法来写数学公式.")
st.latex(r'x^2+y^2=1')
st.text("还支持写代码块.")
code ='''def hello(): 
print('hello!')'''
st.code(code,language='python')

st.markdown("# 接下来讨论不同data elements_presentation")
st.markdown("dataframe is one of the most important data formats used in data science.It consists of two-dimensional data with"
            "rows and columns that acted as labeled data. "
            )
st.markdown("the following is an example to represent DataFrame-like table using st.dataframe. ")
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(30,10),columns=('col_no %d'%i for i in range(10) ))
st.dataframe(df)
st.markdown("If choose to representa data as a table form. 可以看到略有不同，table的话会遍历表格的所有数据。")
st.table(df)
st.markdown("还有一种数据叫做metrics。比如温度数据，如果关注点在于这个数据的变化，用metrics就比较合适。")
c1,c2,c3=st.columns(3)
c1.metric(label="Temperature",value="31℃",delta="1.2℃")
c2.metric(label="爱情",value="90",delta="10分")
c3.metric(label="青春",value="90",delta="-10分")
st.markdown("用Streamlit来展示json数据。 ")
st.json({
 "BookName": "Beginners Guide to Streamlit with Python",
 "BookID" : "2",
 "Publisher" : "Apress",
 "Year" : "2022",
 "Edition" : "First",
 "Language" : "Python"
 } )
st.markdown("st.write()类似于python中的print。 ")
st.write(df)
st.markdown("用网页来展示一些图表的数据。 ")
df2 = pd.DataFrame(np.random.rand(10,2),columns=['a','b'])
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Wawati TC']
fig = plt.figure()
# 绘图
plt.plot(df2.values[:,0],#x轴
df2.values[:,1],
linestyle = '-',# 折线类型
linewidth = 2,# 折线宽度
color = 'steelblue',# 折线颜色
marker = 'o',# 点的形状
markersize = 6,# 点的大小
markeredgecolor='black',# 点的边框色
markerfacecolor='steelblue'# 点的填充色
         )
plt.title('Title')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend(loc='best',frameon=False)

st.pyplot(fig) #吃进去一张画布。
