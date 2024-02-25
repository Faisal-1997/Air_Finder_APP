import streamlit as st
import youtube_dl
from PIL import Image

# Define ydl_opts if needed
ydl_opts = {}

@st.cache
def transcribe_from_link(link, categories: bool):
    _id = link.strip()

    def get_vid(_id):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(_id)

def main():
    # Custom CSS for RTL layout
    rtl_style = """
        <style>            
            body {
                direction: rtl;
                text-align: center;
                font-family: "Arial", sans-serif;
            }
            .stApp {
                background-image: url('https://up6.cc/2024/02/170888322938741.jpg'); /* Add your image URL */
                background-attachment: fixed;
                background-size: cover;
                background-position: center;
                direction: rtl;
                text-align: center;
            }
        </style>
    """

    st.markdown(rtl_style, unsafe_allow_html=True)
    
    img2 = "https://up6.cc/2024/02/170888210390851.png"
    st.image(img2)
    st.text("البحث عن المفقودين من خلال استخدام الطائرات بدون طيار،تمتاز هذه الطائرات بالقدرة على تحديد المواقع بدقة، وتوفير صور مباشرة، والتنقل بفعالية في المناطق الصعبة, مما يتيح لفرق البحث والإنقاذ الحصول على معلومات دقيقة وفورية حول المناطق المستهدفة وضحايا الحوادث.")
    img ="https://up6.cc/2024/02/170889218542041.png"
    img1 = "https://up6.cc/2024/02/17088920380311.png"
    
    link = 'https://www.youtube.com/watch?v=-zF3a5BVEvc&feature=youtu.be'

    if link:
        
        st.video(link)

    with st.container():
        
        left_column, left1_column, right_column, right1_column, left2_column, = st.columns(5)
        with left_column:
                st.write(' ')
        with left1_column:
            st.image(img, caption="", width = 110)
            st.image("https://up6.cc/2024/02/170889732506121.png")
        with right_column:
            st.write(' ')
            
        with right1_column:
            
            st.image(img1,caption="", width = 110)
            st.image("https://up6.cc/2024/02/170889724740481.png")
            
        with left2_column:
             st.write(' ')
            
            
            
            
            


if __name__ == "__main__":
    main()
