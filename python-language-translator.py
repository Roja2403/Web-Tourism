import streamlit as st
from google_trans_new import google_translator 

def main():
    st.title('LANGUAGE TRANSLATOR')
    from_text = st.text_input("Enter a sentence which transforms to Tamil")
    st.text('To Tamil')
    translator = google_translator() 
    a=translator.translate(from_text,lang_tgt='ta')
    st.success(a)

    from_text = st.text_input("Enter a sentence which transforms to English")
    st.text('To English')
    translator = google_translator() 
    a=translator.translate(from_text,lang_tgt='en')
    st.success(a)


if __name__=="__main__":
    main()
    
    
    
