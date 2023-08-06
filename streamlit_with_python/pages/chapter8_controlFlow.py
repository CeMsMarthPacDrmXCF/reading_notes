import time

import streamlit as st

st.title('Alert box')
st.info('信息box')
st.warning('警告box')
st.success('成功信息Box')
st.error('错误信息')
st.exception('例外')
st.title('控制流')
st.markdown('控制流control flow的目的旨在改变程序的运行方式，比如希望程序不按照顺序一句一句地执行。')
name= st.text_input('千万别输入0呀')
if name== '0':
    st.info('enter any text')
    st.stop()
st.success('程序继续运行啦。')
st.markdown('echo控件')
with st.echo():
    txt= st.text_input('Text')
    st.success('代码可视化的例子。')

st.markdown('experiement_show 方法可以用于debug，和write功能类似，但是返回一个None。')
st.markdown('session state，可以用于储存一些全局变量，不会随着application rerun而初始化。')

st.title('performance')
st.markdown('提高app运行的性能，robustness.')
st.markdown('caching, 缓存。加载大型数据集时的缓存可以提高程序运行的性能。')
@st.cache
def add(x,y):
    time.sleep(5)
    return x+y
x=10
y=60
res=add(x,y)
st.write('结果是：',res)

st.markdown('在高维计算当中，利用experimental_memo来存储数据。 cache data in key-value format, 也就是'
            '以字典方式存储数据。')