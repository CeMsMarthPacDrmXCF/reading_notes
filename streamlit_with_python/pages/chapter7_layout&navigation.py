import streamlit as st
import numpy as np
st.title('布局')
st.title('columns')
col1,col2=st.columns(2)
col1.write('第一列')
col2.write('第二列')
st.markdown('padding说的是列与列之间的间距。')
st.title('grid')
for i in range(4):
    cols=st.columns((1,1,1,1))
    cols[0].write('第{0}行第1列'.format(i+1))
    cols[1].write('第{}行第2列'.format(i+1))
    cols[2].write('第{}行第3列'.format(i+1))
    cols[3].write('第{}行第4列'.format(i + 1))
st.title('expanders')
st.markdown('这个控件是为了折叠一些信息。')
with st.expander('streamlit to develop app!'):
    st.write('it can be done in minutes!')
st.title('containers')
with st.container():
    st.write('容器内的元素')
    st.line_chart(np.random.randn(40,4))
    st.markdown('容器和expander的差别就在于容器可以容纳多个元素和控件。')
st.title('sidebar侧边栏')
st.sidebar.title('侧边栏')
st.sidebar.markdown('侧边栏就相当于是一个容器')
st.sidebar.slider('选择一个数字',0,10)
