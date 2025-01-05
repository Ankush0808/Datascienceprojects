import streamlit as st
import pandas as pd
import plotly.express as px
import plotly as pt
import matplotlib.pyplot as plt
df_RWAC=pd.read_csv("C://Users//Lenovo//RCB_Wins_at_Chinnaswamy.csv")
st.title(" why RCB doesn't win a cup?")
st.image("C://Users//Lenovo//Documents//VK.webp")
st.title("Streamlit Sidebar with Buttons")

st.sidebar.title("Know about RCB")
st.sidebar.markdown("Choose an option below:")
if st.sidebar.button("problem with RCB bowling?"):
    st.write("lets see RCB bowling")
elif st.sidebar.button("problem with middle order"):
    st.write("Lets see RCB middle order")
elif st.sidebar.button("Cant defend at chinnaswamy?"):
    st.write("At Chinnaswamy up until now RCB has played 123 matches and out of that 123 44 have been won by RCB out of these 25 have been won while defending and 19 while chasing.")
    df_RWAC[df_RWAC['toss_winner'].isin(["Royal Challengers Bangalore", "Royal Challengers Bengaluru"])]['toss_decision'].value_counts().plot(kind='barh')
    st.write("At chinnaswamy RCB out of the 44 matches won 39 matches while chasing and only 5 matches while defending  ")

st.write("Explore the buttons in the sidebar to see the content change!")




