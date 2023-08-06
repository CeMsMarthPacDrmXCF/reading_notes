import streamlit as st
st.title("Media elements")
st.markdown("如何在streamlit网页中添加图片，音频，视频和一些streamlit自带的特效，比如雪花等等等")
st.markdown("如何找一些自己喜欢的歌手的专辑呢？")
st.markdown("机器学习算法的数据集可以是音频、视频和图片。这就是为什么media element也同样重要的原因。")
st.snow()
st.image(r'read_book_note/files/ex_1.jpg',caption='新疆的牧民在更换牧场',width=500)

st.markdown('图片的来源可以是本地的文件夹，也可以是url。图片的channel决定了图片是彩色or黑白。')
st.markdown('多张图片的展示')
images_animals=[r'read_book_note/files/xianhe_1.jpg',
        r'read_book_note/files/xianhe_2.jpg',
        r'read_book_note/files/xiaozhizhu_1.jpg',
        r'read_book_note/files/xiaozhizhu_2.jpg']
st.image(images_animals,width=150)
st.caption('图片来源：中国国家地理')
st.markdown('使用图片作为背景图片。')
import base64 #是一种编码数据的方式
def add_local_background_image_(image):
        with open(image,'rb') as image:
                encode_string = base64.b64encode(image.read())

                st.markdown(
                        f"""
                        <style>
                        .stApp{{
                        background-image:ulr(data:read_book_note/files/{"jpg"};base64,{encode_string.decode()});
                        background-size:cover
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                )
                st.write("背景图片")

add_local_background_image_(r'read_book_note/files/sky_background.jpg')
st.markdown('设置网页背景的实验失败了。')
st.title('给网页插入音频数据')
audio_sample= open(r'read_book_note/files/NO COPYRIGHT MUSIC - Ofshane - Back To The Future.mp3',"rb")
st.audio(audio_sample,start_time=0)
st.caption("音频来源：freeSound无版权音乐网站")

st.title('给网页插入视频数据')
sample_video=open(r'read_book_note/files/demo_video.mp4',"rb").read()
st.video(sample_video)

st.markdown('streamlit还支持ballon, snowflake动画和简单的Emojis。这里就不一一展示了。')

