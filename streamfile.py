# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import pickle
import numpy as np



@st.cache
def load_data():
    yieldAreaColumns = ["Crop","p2006","p2007","p2008","p2009","p2010","area2006","area2007","area2008","area2009","area2010","yield2006","yield2007","yield2008","yield2009","yield2010"]
    yieldAreadf = pd.read_csv("input/datafile (2).csv",names=yieldAreaColumns)
    
    barNames = ["Crop","y2005","y2006","y2007","y2008","y2009","y2010","y2011","y2012"]
    barRawdf = pd.read_csv("input/datafile.csv",names=barNames)
    
    return yieldAreadf,barRawdf
    
    
yieldAreadf,barRawdf=load_data()



st.title("Your Agri Companion")

name  = st.text_input("Enter your Name ", "User")

state = st.selectbox(
     'State of Where you are planning grow your crops',
     ("Andhra Pradesh","Arunachal Pradesh", "Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                "Himachal Pradesh",
                "Jammu and Kashmir",
                "Jharkhand","Karnataka","Kerala",
                "Madhya Pradesh", "Maharashtra","Manipur",
                "Meghalaya",
                "Mizoram","Nagaland",
                "Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
                "Telangana","Tripura","Uttarakhand",
                "Uttar Pradesh","West Bengal","Andaman and Nicobar Islands",
                "Chandigarh","Dadra and Nagar Haveli",
                "Daman and Diu","Delhi","Lakshadweep","Puducherry"))


user_crop=st.selectbox("Pick your preferred crop",yieldAreadf.Crop)



st.subheader("Your model needs certain parameters to predict which crop is best for you.")
st.subheader("Please enter them below")


ph=st.slider('Enter the Ph Level of Soil',0.0,14.0,14.0,0.01)

n= st.number_input('Nitrogen Value of the Soil ',0,150)
p=st.number_input('Phosporous Level ',0,150)
k=st.number_input('Potassium Level ',0,200)

temp=st.number_input('Average Temperature in your Area ',0,50)

humidity=st.number_input('Humidity Level in your Area ',0,100)

rainfall=st.number_input('Average Rainfall in your Area ',0,300)

model = pickle.load(open("finalized_model.sav", 'rb'))




inv_mapper ={0: 'apple',1: 'banana',2: 'blackgram',3: 'chickpea',4: 'coconut', 5: 'coffee',
 6: 'cotton', 7: 'grapes',8: 'jute',
 9: 'kidneybeans', 10: 'maize',
 11: 'mango', 12: 'mothbeans',
 13: 'mungbean', 14: 'muskmelon',
 15: 'orange', 16: 'papaya',
 17: 'pigeonpeas', 18: 'pomegranate',
 19: 'rice', 20: 'watermelon', 21: 'wheat'}



if st.button('Submit'):
    outp=model.predict(np.array([n,p,k,temp,humidity,ph,rainfall]).reshape(1, -1))
    out=inv_mapper[int(outp)]
    st.subheader(f"your AI model recommended : {out}")
    ans=out
    
    #replace with ML answer
    ml_crop = ans[0].upper()+ans[1:]
    
    uyieldData = []
    uareaData = []
    myieldData = []
    mareaData = []
    
    uprodData = []
    mprodData = []
    
    barFlag = 0
    
    ubarData = []
    mbarData = []
    
    for index,rows in yieldAreadf.iterrows():
        if(rows.Crop == user_crop):
            uareaData = [rows.area2006,rows.area2007,rows.area2008,rows.area2009,rows.area2010]
            uyieldData = [rows.yield2006,rows.yield2007,rows.yield2008,rows.yield2009,rows.yield2010]
            uprodData = [rows.p2006,rows.p2007,rows.p2008,rows.p2009,rows.p2010]
    
    for index,rows in yieldAreadf.iterrows():
        if(rows.Crop == ml_crop):
            mareaData = [rows.area2006,rows.area2007,rows.area2008,rows.area2009,rows.area2010]
            myieldData = [rows.yield2006,rows.yield2007,rows.yield2008,rows.yield2009,rows.yield2010]
            mprodData = [rows.p2006,rows.p2007,rows.p2008,rows.p2009,rows.p2010]
    
    for index,rows in barRawdf.iterrows():
        if(rows.Crop == user_crop):
            ubarData = [int(rows.y2005),int(rows.y2006),int(rows.y2007),int(rows.y2008),int(rows.y2009),int(rows.y2010),int(rows.y2011),int(rows.y2012)]
            barFlag = 1
    
    for index,rows in barRawdf.iterrows():
        if(rows.Crop == ml_crop):
            mbarData = [int(rows.y2005),int(rows.y2006),int(rows.y2007),int(rows.y2008),int(rows.y2009),int(rows.y2010),int(rows.y2011),int(rows.y2012)]
            barFlag = 1
    
    ugraphdf = pd.DataFrame(uyieldData,uareaData)
    st.write(f"### Yield of {user_crop}  vs Area cultivated")
    st.line_chart(ugraphdf)
    
    mgraphdf = pd.DataFrame(myieldData,mareaData)
    st.write(f"### Yield of {ans}  vs Area cultivated")
    st.line_chart(mgraphdf)
    
    uproddf = pd.DataFrame(uprodData,[2006,2007,2008,2009,2010])
    st.write(f"### Production of {user_crop} from 2006 to 2010")
    st.bar_chart(uproddf)
    
    mproddf = pd.DataFrame(mprodData,[2006,2007,2008,2009,2010])
    st.write(f"### Production of {ans} crop from 2006 to 2010")
    st.bar_chart(mproddf)
    
    
    if(barFlag == 1):
        st.write(f"### Yield of {user_crop} crop from 2005 to 2012")
        ubarDf = pd.DataFrame(ubarData,[2005,2006,2007,2008,2009,2010,2011,2012])
        st.bar_chart(ubarDf)
        st.write(f"### Yield of {ans} crop from 2005 to 2012")
        mbarDf = pd.DataFrame(mbarData,[2005,2006,2007,2008,2009,2010,2011,2012])
        st.bar_chart(mbarDf)
        
   



#st_shap(shap.plots.waterfall(shap_values[0]))
#shap_values = explainer.shap_values(np.array([n,p,k,temp,humidity,ph,rainfall]).reshape(1, -1))
# visualize the first prediction's explanation (use matplotlib=True to avoid Javascript)
#st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], df.iloc[0,:]))

# visualize the training set predictions
#st_shap(shap.force_plot(explainer.expected_value, shap_values, df), 400)
 