
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Personal Portfolio", page_icon=":tada:", layout="wide")


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottieur("https://lottie.host/6d2ce265-1088-46b4-8420-a48c3e855b20/WhDzDFdmCF.json")


with st.container():
    st.subheader("Hi,I am Ashutosh :wave:")
    st.title("A Data Scientist From India")
    st.write("I am a student and passsionate about finding ways to use Python which will be more efficient for bussieness settings.")
    st.write("[Know More >](https://www.linkedin.com/in/ashutosh-patil-7a90811b5/)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
              I am student , I am in third year of B.tech CSE :
                - are looking to learn python in different ways.
                - are learning diffrent ways to solve tasks and problems.
                - want to learn Data Analysis and Data Science to perform meaningful analyses.
                - are Very curious to Learn.
                """                                                              
         )
        st.write("[Linkedin Profile > ](https://www.linkedin.com/in/ashutosh-patil-7a90811b5/)")  
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")




        with st.container():
            st.write("---")
            st.header("My Projects")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
        with image_column:
               

            with text_column:
                    st.subheader("Data Modeling")
                    st.write(
                        """
                        Learn how to Implement data using data modeling!
                        Data modeling is the process of creating a visual representation of either a whole information system or parts of it to communicate connections between data points and structures.
                        I have made a project based on this!!
                        """
                    )
                    st.markdown("[Project Link...](https://miro.com/welcomeonboard/TkRZckNIRlRadWxYTndtMzNZTzQ4Qk11UlhLMUhtdnJPclFCaXZ5YmtGOHc4UTFyMnRENnhKYVdMTjZVOGNEQXwzNDU4NzY0NTYwOTUyMTI5NzYyfDI=?share_link_id=103009020871)")
            with text_column:
                    st.subheader("Madlibs")
                    st.write(
                        """
                        Learn how to develop a game using simple python!
                       
                        I have made a project based on this!!
                        """
                    )
                    st.markdown("")
                        