import plotly as pt
import numpy as np
import pickle
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
st.title("Welcome to IPL Match predictions")
a=st.selectbox("Select the batting team",['Royal Challengers Bangalore', 'Kings XI Punjab',
       'Delhi Daredevils', 'Kolkata Knight Riders', 'Rajasthan Royals',
       'Mumbai Indians', 'Chennai Super Kings', 'Deccan Chargers',
       'Pune Warriors', 'Kochi Tuskers Kerala', 'Sunrisers Hyderabad',
       'Rising Pune Supergiants', 'Gujarat Lions',
       'Rising Pune Supergiant', 'Delhi Capitals', 'Punjab Kings',
       'Gujarat Titans', 'Lucknow Super Giants',
       'Royal Challengers Bengaluru'],index=0)
b=st.selectbox("Select the bowling team",['Royal Challengers Bangalore', 'Kings XI Punjab',
       'Delhi Daredevils', 'Kolkata Knight Riders', 'Rajasthan Royals',
       'Mumbai Indians', 'Chennai Super Kings', 'Deccan Chargers',
       'Pune Warriors', 'Kochi Tuskers Kerala', 'Sunrisers Hyderabad',
       'Rising Pune Supergiants', 'Gujarat Lions',
       'Rising Pune Supergiant', 'Delhi Capitals', 'Punjab Kings',
       'Gujarat Titans', 'Lucknow Super Giants',
       'Royal Challengers Bengaluru'],index=0)
c= st.slider("select the over", min_value=0,max_value=19)
d=st.slider("select the ball",min_value=0,max_value=6)
e=st.selectbox("How many wickets down?",[0,1,2,3,4,5,6,7,8,9])
f= st.number_input("whats the score?")
g= st.number_input("whats the target?")
h=st.number_input("Overs to chase that target?",min_value=1,max_value=20)
i= st.selectbox("Where is the match?",['M Chinnaswamy Stadium',
       'Punjab Cricket Association Stadium, Mohali', 'Feroz Shah Kotla',
       'Wankhede Stadium', 'Eden Gardens', 'Sawai Mansingh Stadium',
       'Rajiv Gandhi International Stadium, Uppal',
       'MA Chidambaram Stadium, Chepauk', 'Dr DY Patil Sports Academy',
       'Newlands', "St George's Park", 'Kingsmead', 'SuperSport Park',
       'Buffalo Park', 'New Wanderers Stadium', 'De Beers Diamond Oval',
       'OUTsurance Oval', 'Brabourne Stadium',
       'Sardar Patel Stadium, Motera', 'Barabati Stadium',
       'Brabourne Stadium, Mumbai',
       'Vidarbha Cricket Association Stadium, Jamtha',
       'Himachal Pradesh Cricket Association Stadium', 'Nehru Stadium',
       'Holkar Cricket Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Subrata Roy Sahara Stadium',
       'Maharashtra Cricket Association Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'JSCA International Stadium Complex', 'Sheikh Zayed Stadium',
       'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Saurashtra Cricket Association Stadium', 'Green Park',
       'M.Chinnaswamy Stadium',
       'Punjab Cricket Association IS Bindra Stadium',
       'Rajiv Gandhi International Stadium', 'MA Chidambaram Stadium',
       'Arun Jaitley Stadium', 'MA Chidambaram Stadium, Chepauk, Chennai',
       'Wankhede Stadium, Mumbai', 'Narendra Modi Stadium, Ahmedabad',
       'Arun Jaitley Stadium, Delhi', 'Zayed Cricket Stadium, Abu Dhabi',
       'Dr DY Patil Sports Academy, Mumbai',
       'Maharashtra Cricket Association Stadium, Pune',
       'Eden Gardens, Kolkata',
       'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'Rajiv Gandhi International Stadium, Uppal, Hyderabad',
       'M Chinnaswamy Stadium, Bengaluru',
       'Barsapara Cricket Stadium, Guwahati',
       'Sawai Mansingh Stadium, Jaipur',
       'Himachal Pradesh Cricket Association Stadium, Dharamsala',
       'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam'])
CRR=(f*6)/((c*6)+d)
Rr=((g-f)*6)/((6*h)-((c*6)+d))
input_data=[[a,b,e,f,g,h,i,CRR,Rr]]
with open("C://Users//Lenovo//pipe_model.pkl", 'rb') as f:
     pipe = pickle.load(f)

if st.button("Click here to predict"):
    if(Rr>=36):
           st.write("No Chance to win")
    else:
              prediction = pipe.predict_proba(input_data)
              defending_prob = prediction[0][0] * 100  # Probability for the first team
              Chasing_prob = prediction[0][1] * 100 
              st.write(f"Win percentage for {a} would be {Chasing_prob:.2f}%")
              st.write(f"Win percentage for {b} would be {defending_prob:.2f}%")
    