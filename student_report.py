import streamlit as st
import pandas as pd

st.header("Students Marks calculator")

name=st.text_input("please enter your name")

out_of=st.number_input("what is the max marks for each subject")

marks1=st.number_input("enter your subect marks",key=1)

marks2=st.number_input("enter your subect marks",key=2)

marks3=st.number_input("enter your subect marks",key=3)

marks4=st.number_input("enter your subect marks",key=4)

marks5=st.number_input("enter your subect marks",key=5)

marks6=st.number_input("enter your subect marks",key=6)


addition=marks1+marks2+marks3+marks4+marks5+marks6

st.write(f"{name} hey you got total of {addition}")

percentage=(addition/600)*100

st.write(f"you got {percentage} %")

st.subheader("Congratulation idiot")

st.image(r"https://t3.ftcdn.net/jpg/02/80/01/64/240_F_280016442_I5DcWCRT7JTr5Ut86a9VvqNoOfDt854G.jpg")

st.markdown(r"![Alt Text](https://i.gifer.com/origin/16/162b41786d99b9d7e7b03549c4e19ae2_w200.gif)")

st.line_chart(data=[marks1,marks2,marks3,marks4,marks5,marks6])

df=pd.DataFrame({'Telugu':marks1,'Hindi':marks2,'English':marks3,'Mathematics':marks4,'social':marks5,'science':marks6},columns=['subjects','marks'])

st.dataframe(df)
