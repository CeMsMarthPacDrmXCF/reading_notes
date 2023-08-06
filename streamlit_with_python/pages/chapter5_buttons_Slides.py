import time

import streamlit as st
st.title("buttons and sliders")
button= st.button('点我变成小白兔') # 返回的是一个boolean
if button:
    st.write('我变成小白兔啦')
else:
    st.write('小白兔在哪里呢？')

st.markdown('radio button就是相当于多选一的选择框。')
Rbutton= st.radio("你喜欢的人是？",('自己','所有人','猫猫')) # 返回一个字符串
if Rbutton== '自己':
    st.write('你不喜欢别人哦')
elif Rbutton== '所有人':
    st.write('你喜欢所有人呢。')
else:
    st.write('猫星人嗷呜！')

st.markdown("check box控件。相当于一个多选题。")
st.write('你有什么爱好呢？')
check_1= st.checkbox('Books',value=True)
check_2= st.checkbox('吉他')
check_3= st.checkbox('跑鞋')

st.markdown('drop-down就是下拉框。')
st.selectbox('choose your hobby:',('二次元','电影','火锅'))
st.markdown('多选框，可以多选多，返回是文本标签')
hobbies=st.multiselect('你有什么爱好呢',['二次元','电影','火锅'])

st.markdown('progrress bar进度条。')
download= st.progress(0)
for i in range(10):
    time.sleep(0.1)
    download.progress(i*10+10)
st.write('下载成功')
# 终于搞懂进度条如何实现了。
st.markdown('还有一个和进度条类似的控件叫做spinner。')
with st.spinner('Loading...'):
    time.sleep(2)
st.write('加载成功')
