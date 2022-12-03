import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
st.title("Welcome to House predictor app")
## Building models




## ENd of building
## Sidebar template to choose different parameters

a=st.sidebar.selectbox("Enter the type of dwelling involved",["1-STORY 1946 & NEWER ALL STYLES","1-STORY 1945 & OLDER",
"1-STORY W/FINISHED ATTIC ALL AGES","1-1/2 STORY - UNFINISHED ALL AGES","1-1/2 STORY FINISHED ALL AGES","2-STORY 1946 & NEWER","2-STORY 1945 & OLDER",
"2-1/2 STORY ALL AGES","SPLIT OR MULTI-LEVEL","SPLIT FOYER","DUPLEX - ALL STYLES AND AGES","1-STORY PUD (Planned Unit Development) - 1946 & NEWER",
 "1-1/2 STORY PUD - ALL AGES","2-STORY PUD - 1946 & NEWER","PUD - MULTILEVEL - INCL SPLIT LEV/FOYER","2 FAMILY CONVERSION - ALL STYLES AND AGES"],index=1)
b=st.sidebar.number_input("Enter street in feets")
c=st.sidebar.number_input("Enter lotsize in square feet")
d=st.sidebar.number_input("Give an Overallquality rating")
e=st.sidebar.number_input("Give an overallcondition rating")
f=st.sidebar.number_input("Enter the Type1 finished in square feet")
g=st.sidebar.number_input("Enter Unfinished Square feet of basement area")
h=st.sidebar.number_input("Enter total basement area in square feet")
i=st.sidebar.number_input("Enter area of second floor in square feet")
j=st.sidebar.number_input("Enter amount of area above ground")
k=st.sidebar.number_input("Enter number of bathrooms in basement")
l=st.sidebar.number_input("Enter number of bathrooms above ground")
m=st.sidebar.number_input("Enter number of half baths above ground")
n=st.sidebar.number_input("Enter number of bedrooms above ground")
o=st.sidebar.number_input("Enter number of kitchen's above ground")
p=st.sidebar.number_input("Enter number of Fireplaces")
q=st.sidebar.number_input("Enter size of garage in car capacity")
r=st.sidebar.number_input("Enter area of wood deck in square feet")
s=st.sidebar.number_input("Enter amount of open area in square feet")
t=st.sidebar.number_input("Enter screen porch area in square feet")
u=st.sidebar.number_input("Enter how old is your house")
v=st.sidebar.number_input("Enter the number of years house has been remodeled")
 
## end of sidebar

## Function for conversion
def inversion(a):
    match a:
        case "1-STORY 1946 & NEWER ALL STYLES":
            return 20
        case "1-STORY 1945 & OLDER":
            return 30
        case "1-STORY W/FINISHED ATTIC ALL AGES":
            return 40
        case "1-1/2 STORY - UNFINISHED ALL AGES":
            return 45
        case "1-1/2 STORY FINISHED ALL AGES":
            return 50
        case "2-STORY 1946 & NEWER":
            return 60
        case "2-STORY 1945 & OLDER":
            return 70
        case "2-1/2 STORY ALL AGES":
            return 75
        case "SPLIT OR MULTI-LEVEL":
            return 80
        case "SPLIT FOYER":
            return 85
        case "DUPLEX - ALL STYLES AND AGES":
            return 90
        case "1-STORY PUD (Planned Unit Development) - 1946 & NEWER":
            return 120
        case "1-1/2 STORY PUD - ALL AGES":
            return 150
        case "2-STORY PUD - 1946 & NEWER":
            return 160
        case "PUD - MULTILEVEL - INCL SPLIT LEV/FOYER":
            return 180
        case "2 FAMILY CONVERSION - ALL STYLES AND AGES":
            return 190


##

## Importing the datasets
X_data=pd.read_csv("C:/Users/ankus/PycharmProjects/flaskProject1//X_sampletest1.csv")
Y_data=pd.read_csv("C:/Users/ankus/PycharmProjects/flaskProject1//Y_sampletest1.csv")

df_X=pd.DataFrame(X_data)
df_Y=pd.DataFrame(Y_data)

Reg_ml4=RandomForestRegressor()
clf_ml4=Reg_ml4.fit(df_X,df_Y)
z=inversion(a)
X_test=np.array([z,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v]).reshape(1,22)
y_ml4_pred=clf_ml4.predict(X_test)
st.image('houseimage.jpg')
##

if st.button("Predict",type='secondary'):
    st.write("The resale value of the house price could be " ,y_ml4_pred[0])
    