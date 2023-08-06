import streamlit as st
def main():
    st.markdown('Heroku是一个部署app的云平台，相当于提供了硬件支持。部署的英文是deploy。'
                '')
    st.markdown('需要安装re, textblob, nltk包。textblob是对句子进行词性标注。')
    st.title('NLP')
    st.subheader('欢迎使用自然语言处理应用。')
    text= st.text_area('请输入文本：')
    # 清洗文本cleaning.
    import re
    from textblob import TextBlob
    from nltk.stem.wordnet import WordNetLemmatizer
    #Keeping only Text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    #Removes Whitespaces
    text = re.sub(r"\'s", " ", text)
    # Removing Links if any
    text = re.sub(r"http\S+", " link ", text)
    # Removes Punctuations and Numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # Splitting Text
    text = text.split()
    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words =[lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)
    if st.button("Analyze"):
        blob = TextBlob(text)
        result = blob.sentiment.polarity
        if result > 0.0:
            custom_emoji = ':blush:'
            st.success('Happy : {}'.format(custom_emoji))
        elif result < 0.0 :
            custom_emoji = ':disappointed:'
            st.warning('Sad : {}'.format(custom_emoji))
        else:
            custom_emoji = ':confused:'
            st.info('Confused : {}'.format(custom_emoji))
            st.success("Polarity Score is: {}".format(result))
if __name__=='__main__':
    main()
