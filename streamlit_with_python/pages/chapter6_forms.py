import streamlit as st
st.title('Forms')
st.markdown('这一章节讨论用户可能的输入形式。目的就在于making application dynamic。比如根据'
            '用户说的话和上传的文件给予相应的反馈。')
st.title('Text box')
name = st.text_input("输入你最喜欢的数字")
st.write('你最喜欢的数字是',name)

st.markdown('text area控件可以支持多行文本的输入。')
input_text=st.text_area('做个自我介绍吧？')
st.write("""你是一个 \n""", input_text, """\n 的人""")

st.markdown('可以用number_input和time_input创建数字和时间输入的控件。'
            '还可以用date_input创建日期输入的控件。')

st.markdown('颜色选择控件, color picker。')
color_code = st.color_picker('Select your color.')
st.markdown('颜色是')
st.write(color_code)

st.title('处理txt & docx文件。')
st.markdown('这一章节主要讲了各种文档,docx, pdf, csv的upload和save操作。')
import docx2txt
text_file= st.file_uploader("Upload document", type=["docx","txt"])
details =st.button ("check details")
if details:
    if text_file is not None:
        doc_details= {"file_names":text_file.name, "file_type": text_file.type,
                      "file_size":text_file.size}
        st.write(doc_details)
        if text_file.type=="text/plain":
            raw_text= str(text_file.read(), "utf-8")
            st.write(raw_text)
        else:
            docx_text= docx2txt.process(text_file)
            st.write(docx_text)
st.markdown("也支持用pdfplumber包处理pdf文件， 结合panda包处理csv表格数据集。")
st.title("submit button.")
my_form= st.form(key='form')
name_submit =my_form.text_input(label='你是谁')
submit_button = my_form.form_submit_button(label= 'Submit')
st.write(name_submit)
st.markdown('这个按钮的功能就是重启浏览器。但是局限于刷新和这个text_input控件相关的内容而不是重新加载整个网页。')



