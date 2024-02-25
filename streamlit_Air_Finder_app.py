import streamlit as st

from PIL import Image


@st.cache
def transcribe_from_link(link, categories: bool):
    _id = link.strip()

    
img2 = "https://up6.cc/2024/02/170888210390851.png"
st.image(img2)
   
    
st.markdown("<h1 style='font-size: 22px;text-align: center;'>البحث عن المفقودين من خلال استخدام الطائرات بدون طيار، تمتاز هذه الطائرات بالقدرة على تحديد المواقع بدقة، وتوفير صور مباشرة، والتنقل بفعالية في المناطق الصعبة, مما يتيح لفرق البحث والإنقاذ الحصول على معلومات دقيقة وفورية حول المناطق المستهدفة وضحايا الحوادث</div>", unsafe_allow_html=True)

st.write('             ')
st.write('             ')
st.write('             ')

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
        st.image("https://up6.cc/2024/02/170890109939031.png")
    with right_column:
        st.write(' ')
            
    with right1_column:
            
        st.image(img1,caption="", width = 110)
        st.image("https://up6.cc/2024/02/170889724740481.png")
            
    with left2_column:
            st.write(' ')
            
            
            
            
            

