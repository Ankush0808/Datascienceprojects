import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import numpy as np
################################################################################################
# All the functions
st.set_page_config(layout='wide')
custom_css = """
<style>
body {
    overflow: hidden;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


def bound_percentage(filtered_df):
    return (filtered_df['Number_of_4s']*4)+(filtered_df['Number_of_6s']*6)*100//filtered_df['Runs_scored']

def summary(filtered_df):
    max_rs=filtered_df['Runs_scored'].max()
    min_rs=filtered_df['Runs_scored'].min()
    Avg_rs=filtered_df['Runs_scored'].mean()
    min_sr=filtered_df['Strike_rate'].min()
    max_sr=filtered_df['Strike_rate'].max()
    Avg_sr=filtered_df['Strike_rate'].mean()
    max_nof=filtered_df['Number_of_4s'].max()
    min_nof=filtered_df['Number_of_4s'].min()
    Nof_hundreds=len(filtered_df[filtered_df['Runs_scored']>=100])
    filtered_df['Boundary_percentage']=bound_percentage(filtered_df)
    df_summary = pd.DataFrame({
        'Max Runs Scored': [max_rs],
        'Min Runs Scored': [min_rs],
        'Avg Runs Scored': [Avg_rs],
        'Min Strike Rate': [min_sr],
        'Max Strike Rate': [max_sr],
        'Avg Strike Rate': [Avg_sr],
        'Max Number of 4s': [max_nof],
        'Min Number of 4s': [min_nof],
        'Number of 100s':[Nof_hundreds],
        'Boundary percentage':filtered_df['Boundary_percentage'].mean()
    })
 
    st.dataframe(df_summary.T)

def graphy(df_test):
        col1,col2=st.columns(2)
        col1.header("Average Runs scored / year")
        col1.line_chart(df_test.groupby(['Year'])['Runs_scored'].mean())
        col1.header("Average Strike rate / year")
        col1.line_chart(df_test.groupby(['Year'])['Strike_rate'].mean())
        col2.header("Number of Fours every Year")
        col2.bar_chart(df_test.groupby(['Year'])['Number_of_4s'].sum())
        col2.header("Number of 100s each year")
        col2.bar_chart(df_test.groupby(['Year'])['Number_of_100s'].sum())
def graphy20(df_test):
        col1,col2=st.columns(2)
        col1.header("Average Runs scored / year")
        col1.line_chart(df_test.groupby(['Year'])['Runs_scored'].mean())
        col1.header("Average Strike rate / year")
        col1.line_chart(df_test.groupby(['Year'])['Strike_rate'].mean())
        col2.header("Number of Fours every Year")
        col2.bar_chart(df_test.groupby(['Year'])['Number_of_4s'].sum())
        col2.header("Number of 50s each year")
        col2.bar_chart(df_test.groupby(['Year'])['Number_of_50s'].sum())

def distibution(filtered_df):
    st.sidebar.image('Virat_RM.jpg')
    #st.sidebar.markdown('In the History of Cricket, there are many who bat, then there are people with extraordinary talent and then there is Virat Kohli')
    values2=filtered_df['Runs_scored']
    fig1=px.histogram(filtered_df['Runs_scored'],title='Distribution Plot',labels={'x':'values2','y':'Frequency'})
    fig1.update_layout(
        title_font_size=42,
        width=500,
        height=500
    )
    st.plotly_chart(fig1)
def dismisal(filtered_df):
    st.sidebar.image('Virat_dis.jpeg')
    values=filtered_df['Dismissal'].value_counts()
    names=filtered_df['Dismissal'].unique()
    figy=px.pie(values=values,names=names,title='Pie chart')
    st.plotly_chart(figy)
    figy.update_layout(title_font_size=70)

def chasy(df_odi):
    st.sidebar.image('Virat_4.jpg')
    #st.sidebar.markdown("Although Virat is said to be have a good average at run chases it appears that he's been equally good at the 1st innings as well")
    fig3=px.scatter(df_odi,x='Runs_scored',y='Balls_Faced', color='Innings', color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig3)
    st.header("Average runs Scored every year while chasing")
    fig4=px.bar(df_odi.groupby(['Year','Innings'])['Runs_scored'].mean().reset_index(),x='Year',y='Runs_scored',color='Innings',
    color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig4)
    fig5=px.bar(df_odi.groupby(['Year','Innings'])['Number_of_100s'].sum().reset_index(),x='Year',y='Number_of_100s',color='Innings',
    color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig5)

def chasy1(df_t20):
    st.sidebar.image('Virat_4.jpg')
    st.sidebar.markdown("Although Virat is said to be have a good average at run chases it appears that he's been equally good at the 1st innings as well")
    fig6=px.scatter(df_t20,x='Runs_scored',y='Balls_Faced', color='Innings', color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig6)
    st.header("Average runs Scored every year while chasing")
    fig7=px.bar(df_t20.groupby(['Year','Innings'])['Runs_scored'].mean().reset_index(),x='Year',y='Runs_scored',color='Innings',color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig7)
    fig8=px.bar(df_t20.groupby(['Year','Innings'])['Number_of_50s'].sum().reset_index(),x='Year',y='Number_of_50s',color='Innings',color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig8)
###################################################################################################
    

df_odi=pd.read_csv("C:/Users/ankus/Virat_odi.csv")
df_test=pd.read_csv("C:/Users/ankus/Virat_tests.csv")
df_t20=pd.read_csv('C:/Users/ankus/Virat_T20.csv')
st.markdown("<h1 style='color:Black ; font-family:Arial,Impact;'> Virat Kohli 👑🏏</h1>", unsafe_allow_html=True)
df_odi['Strike_rate']=pd.to_numeric(df_odi['Strike_rate'],errors='coerce')
df_odi['Number_of_4s']=pd.to_numeric(df_odi['Number_of_4s'],errors='coerce')
df_odi['Year'] = pd.to_numeric(df_odi['Year'], errors='coerce')
df_odi['Number_of_100s']=np.where(df_odi['Runs_scored']>=100,int(1),int(0))
df_odi['Innings'] = df_odi['Innings'].astype(str)
df_t20['Innings']=df_t20['Innings'].astype(str)
df_test['Innings']=df_test['Innings'].astype(str)
chase_filter=df_odi[df_odi['Innings']==2]
chase_filter_test=df_test[df_test['Innings']==4]

##################################################

##########################################################
year=st.sidebar.slider("Select the year",min_value=2008,max_value=2024)
filtered_df=df_odi[df_odi['Year']==year]
filtered_df_test=df_test[df_test['Year']==year]
filtered_df_t20=df_t20[df_t20['Year']==year]

#################################################################


rbtn=st.sidebar.radio("Select the format",options=['Test','Odi','T20I'])
a=st.sidebar.selectbox("Want to know more about Virat?",
['None','Why the run machine?','How Virat gets dismissed?','Stats','Graphical representation of stats','Why Chase Master?','Lean Patch'],index=0)
if(a=='Why the run machine?'):
    if(rbtn=='Odi'):
        distibution(filtered_df)
    elif(rbtn=='T20I'):
        distibution(filtered_df_t20)
    else:
        distibution(filtered_df_test)
elif(a=='How Virat gets dismissed?'):
    if(rbtn=='Odi'):
        dismisal(filtered_df)
    elif(rbtn=='T20I'):
        dismisal(filtered_df_t20)
    else:
        dismisal(filtered_df_test)

elif(a=='Stats'):
    if(rbtn=='Odi'):
        summary(filtered_df)
    elif(rbtn=='T20I'):
        summary(filtered_df_t20)
    else:
        summary(filtered_df_test)

elif(a=='Graphical representation of stats'):
    if(rbtn=='Odi'):
        graphy(df_odi)
    elif(rbtn=='T20I'):
        graphy20(df_t20)
    else:
        graphy(df_test)
elif(a=='Why Chase Master?'):
    if(rbtn=='Odi'):
        chasy(df_odi)
    elif(rbtn=='T20I'):
        chasy1(df_t20)
    else:
        chasy(df_test)
elif(a=='Lean Patch'):
    df_odi[df_odi['Year'].isin([2020,2021,2022])]
else:
    st.image('Virat_FC.jpg')



