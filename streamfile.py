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
    
    sColumn = ["state","district","year", "season", "crop", "area", "production"]
    stateDatadf = pd.read_csv("input/AgrcultureDataset.csv", names=sColumn,dtype='unicode')
    
    return yieldAreadf,barRawdf,stateDatadf
    
    
yieldAreadf,barRawdf,stateDatadf=load_data()



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


district=st.selectbox("Select your Districe Name ",
('NICOBARS', 'NORTH AND MIDDLE ANDAMAN', 'SOUTH ANDAMANS', 'ANANTAPUR', 'CHITTOOR', 'EAST GODAVARI', 'GUNTUR', 'KADAPA', 'KRISHNA', 'KURNOOL', 'PRAKASAM', 'SPSR NELLORE', 'SRIKAKULAM', 'VISAKHAPATANAM', 'VIZIANAGARAM', 'WEST GODAVARI', 'ANJAW', 'CHANGLANG', 'DIBANG VALLEY', 'EAST KAMENG', 'EAST SIANG', 'KURUNG KUMEY', 'LOHIT', 'LONGDING', 'LOWER DIBANG VALLEY', 'LOWER SUBANSIRI', 'NAMSAI', 'PAPUM PARE', 'TAWANG', 'TIRAP', 'UPPER SIANG', 'UPPER SUBANSIRI', 'WEST KAMENG', 'WEST SIANG', 'BAKSA', 'BARPETA', 'BONGAIGAON', 'CACHAR', 'CHIRANG', 'DARRANG', 'DHEMAJI', 'DHUBRI', 'DIBRUGARH', 'DIMA HASAO', 'GOALPARA', 'GOLAGHAT', 'HAILAKANDI', 'JORHAT', 'KAMRUP', 'KAMRUP METRO', 'KARBI ANGLONG', 'KARIMGANJ', 'KOKRAJHAR', 'LAKHIMPUR', 'MARIGAON', 'NAGAON', 'NALBARI', 'SIVASAGAR', 'SONITPUR', 'TINSUKIA', 'UDALGURI', 'ARARIA', 'ARWAL', 'AURANGABAD', 'BANKA', 'BEGUSARAI', 'BHAGALPUR', 'BHOJPUR', 'BUXAR', 'DARBHANGA', 'GAYA', 'GOPALGANJ', 'JAMUI', 'JEHANABAD', 'KAIMUR (BHABUA)', 'KATIHAR', 'KHAGARIA', 'KISHANGANJ', 'LAKHISARAI', 'MADHEPURA', 'MADHUBANI', 'MUNGER', 'MUZAFFARPUR', 'NALANDA', 'NAWADA', 'PASHCHIM CHAMPARAN', 'PATNA', 'PURBI CHAMPARAN', 'PURNIA', 'ROHTAS', 'SAHARSA', 'SAMASTIPUR', 'SARAN', 'SHEIKHPURA', 'SHEOHAR', 'SITAMARHI', 'SIWAN', 'SUPAUL', 'VAISHALI', 'CHANDIGARH', 'BALOD', 'BALODA BAZAR', 'BALRAMPUR', 'BASTAR', 'BEMETARA', 'BIJAPUR', 'BILASPUR', 'DANTEWADA', 'DHAMTARI', 'DURG', 'GARIYABAND', 'JANJGIR-CHAMPA', 'JASHPUR', 'KABIRDHAM', 'KANKER', 'KONDAGAON', 'KORBA', 'KOREA', 'MAHASAMUND', 'MUNGELI', 'NARAYANPUR', 'RAIGARH', 'RAIPUR', 'RAJNANDGAON', 'SUKMA', 'SURAJPUR', 'SURGUJA', 'DADRA AND NAGAR HAVELI', 'NORTH GOA', 'SOUTH GOA', 'AHMADABAD', 'AMRELI', 'ANAND', 'BANAS KANTHA', 'BHARUCH', 'BHAVNAGAR', 'DANG', 'DOHAD', 'GANDHINAGAR', 'JAMNAGAR', 'JUNAGADH', 'KACHCHH', 'KHEDA', 'MAHESANA', 'NARMADA', 'NAVSARI', 'PANCH MAHALS', 'PATAN', 'PORBANDAR', 'RAJKOT', 'SABAR KANTHA', 'SURAT', 'SURENDRANAGAR', 'TAPI', 'VADODARA', 'VALSAD', 'AMBALA', 'BHIWANI', 'FARIDABAD', 'FATEHABAD', 'GURGAON', 'HISAR', 'JHAJJAR', 'JIND', 'KAITHAL', 'KARNAL', 'KURUKSHETRA', 'MAHENDRAGARH', 'MEWAT', 'PALWAL', 'PANCHKULA', 'PANIPAT', 'REWARI', 'ROHTAK', 'SIRSA', 'SONIPAT', 'YAMUNANAGAR', 'CHAMBA', 'HAMIRPUR', 'KANGRA', 'KINNAUR', 'KULLU', 'LAHUL AND SPITI', 'MANDI', 'SHIMLA', 'SIRMAUR', 'SOLAN', 'UNA', 'ANANTNAG', 'BADGAM', 'BANDIPORA', 'BARAMULLA', 'DODA', 'GANDERBAL', 'JAMMU', 'KARGIL', 'KATHUA', 'KISHTWAR', 'KULGAM', 'KUPWARA', 'LEH LADAKH', 'POONCH', 'PULWAMA', 'RAJAURI', 'RAMBAN', 'REASI', 'SAMBA', 'SHOPIAN', 'SRINAGAR', 'UDHAMPUR', 'BOKARO', 'CHATRA', 'DEOGHAR', 'DHANBAD', 'DUMKA', 'EAST SINGHBUM', 'GARHWA', 'GIRIDIH', 'GODDA', 'GUMLA', 'HAZARIBAGH', 'JAMTARA', 'KHUNTI', 'KODERMA', 'LATEHAR', 'LOHARDAGA', 'PAKUR', 'PALAMU', 'RAMGARH', 'RANCHI', 'SAHEBGANJ', 'SARAIKELA KHARSAWAN', 'SIMDEGA', 'WEST SINGHBHUM', 'BAGALKOT', 'BANGALORE RURAL', 'BELGAUM', 'BELLARY', 'BENGALURU URBAN', 'BIDAR', 'CHAMARAJANAGAR', 'CHIKBALLAPUR', 'CHIKMAGALUR', 'CHITRADURGA', 'DAKSHIN KANNAD', 'DAVANGERE', 'DHARWAD', 'GADAG', 'GULBARGA', 'HASSAN', 'HAVERI', 'KODAGU', 'KOLAR', 'KOPPAL', 'MANDYA', 'MYSORE', 'RAICHUR', 'RAMANAGARA', 'SHIMOGA', 'TUMKUR', 'UDUPI', 'UTTAR KANNAD', 'YADGIR', 'ALAPPUZHA', 'ERNAKULAM', 'IDUKKI', 'KANNUR', 'KASARAGOD', 'KOLLAM', 'KOTTAYAM', 'KOZHIKODE', 'MALAPPURAM', 'PALAKKAD', 'PATHANAMTHITTA', 'THIRUVANANTHAPURAM', 'THRISSUR', 'WAYANAD', 'AGAR MALWA', 'ALIRAJPUR', 'ANUPPUR', 'ASHOKNAGAR', 'BALAGHAT', 'BARWANI', 'BETUL', 'BHIND', 'BHOPAL', 'BURHANPUR', 'CHHATARPUR', 'CHHINDWARA', 'DAMOH', 'DATIA', 'DEWAS', 'DHAR', 'DINDORI', 'GUNA', 'GWALIOR', 'HARDA', 'HOSHANGABAD', 'INDORE', 'JABALPUR', 'JHABUA', 'KATNI', 'KHANDWA', 'KHARGONE', 'MANDLA', 'MANDSAUR', 'MORENA', 'NARSINGHPUR', 'NEEMUCH', 'PANNA', 'RAISEN', 'RAJGARH', 'RATLAM', 'REWA', 'SAGAR', 'SATNA', 'SEHORE', 'SEONI', 'SHAHDOL', 'SHAJAPUR', 'SHEOPUR', 'SHIVPURI', 'SIDHI', 'SINGRAULI', 'TIKAMGARH', 'UJJAIN', 'UMARIA', 'VIDISHA', 'AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'BEED', 'BHANDARA', 'BULDHANA', 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA', 'HINGOLI', 'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR', 'MUMBAI', 'NAGPUR', 'NANDED', 'NANDURBAR', 'NASHIK', 'OSMANABAD', 'PALGHAR', 'PARBHANI', 'PUNE', 'RAIGAD', 'RATNAGIRI', 'SANGLI', 'SATARA', 'SINDHUDURG', 'SOLAPUR', 'THANE', 'WARDHA', 'WASHIM', 'YAVATMAL', 'BISHNUPUR', 'CHANDEL', 'CHURACHANDPUR', 'IMPHAL EAST', 'IMPHAL WEST', 'SENAPATI', 'TAMENGLONG', 'THOUBAL', 'UKHRUL', 'EAST GARO HILLS', 'EAST JAINTIA HILLS', 'EAST KHASI HILLS', 'NORTH GARO HILLS', 'RI BHOI', 'SOUTH GARO HILLS', 'SOUTH WEST GARO HILLS', 'SOUTH WEST KHASI HILLS', 'WEST GARO HILLS', 'WEST JAINTIA HILLS', 'WEST KHASI HILLS', 'AIZAWL', 'CHAMPHAI', 'KOLASIB', 'LAWNGTLAI', 'LUNGLEI', 'MAMIT', 'SAIHA', 'SERCHHIP', 'DIMAPUR', 'KIPHIRE', 'KOHIMA', 'LONGLENG', 'MOKOKCHUNG', 'MON', 'PEREN', 'PHEK', 'TUENSANG', 'WOKHA', 'ZUNHEBOTO', 'ANUGUL', 'BALANGIR', 'BALESHWAR', 'BARGARH', 'BHADRAK', 'BOUDH', 'CUTTACK', 'DEOGARH', 'DHENKANAL', 'GAJAPATI', 'GANJAM', 'JAGATSINGHAPUR', 'JAJAPUR', 'JHARSUGUDA', 'KALAHANDI', 'KANDHAMAL', 'KENDRAPARA', 'KENDUJHAR', 'KHORDHA', 'KORAPUT', 'MALKANGIRI', 'MAYURBHANJ', 'NABARANGPUR', 'NAYAGARH', 'NUAPADA', 'PURI', 'RAYAGADA', 'SAMBALPUR', 'SONEPUR', 'SUNDARGARH', 'KARAIKAL', 'MAHE', 'PONDICHERRY', 'YANAM', 'AMRITSAR', 'BARNALA', 'BATHINDA', 'FARIDKOT', 'FATEHGARH SAHIB', 'FAZILKA', 'FIROZEPUR', 'GURDASPUR', 'HOSHIARPUR', 'JALANDHAR', 'KAPURTHALA', 'LUDHIANA', 'MANSA', 'MOGA', 'MUKTSAR', 'NAWANSHAHR', 'PATHANKOT', 'PATIALA', 'RUPNAGAR', 'S.A.S NAGAR', 'SANGRUR', 'TARN TARAN', 'AJMER', 'ALWAR', 'BANSWARA', 'BARAN', 'BARMER', 'BHARATPUR', 'BHILWARA', 'BIKANER', 'BUNDI', 'CHITTORGARH', 'CHURU', 'DAUSA', 'DHOLPUR', 'DUNGARPUR', 'GANGANAGAR', 'HANUMANGARH', 'JAIPUR', 'JAISALMER', 'JALORE', 'JHALAWAR', 'JHUNJHUNU', 'JODHPUR', 'KARAULI', 'KOTA', 'NAGAUR', 'PALI', 'PRATAPGARH', 'RAJSAMAND', 'SAWAI MADHOPUR', 'SIKAR', 'SIROHI', 'TONK', 'UDAIPUR', 'EAST DISTRICT', 'NORTH DISTRICT', 'SOUTH DISTRICT', 'WEST DISTRICT', 'ARIYALUR', 'COIMBATORE', 'CUDDALORE', 'DHARMAPURI', 'DINDIGUL', 'ERODE', 'KANCHIPURAM', 'KANNIYAKUMARI', 'KARUR', 'KRISHNAGIRI', 'MADURAI', 'NAGAPATTINAM', 'NAMAKKAL', 'PERAMBALUR', 'PUDUKKOTTAI', 'RAMANATHAPURAM', 'SALEM', 'SIVAGANGA', 'THANJAVUR', 'THE NILGIRIS', 'THENI', 'THIRUVALLUR', 'THIRUVARUR', 'TIRUCHIRAPPALLI', 'TIRUNELVELI', 'TIRUPPUR', 'TIRUVANNAMALAI', 'TUTICORIN', 'VELLORE', 'VILLUPURAM', 'VIRUDHUNAGAR', 'ADILABAD', 'HYDERABAD', 'KARIMNAGAR', 'KHAMMAM', 'MAHBUBNAGAR', 'MEDAK', 'NALGONDA', 'NIZAMABAD', 'RANGAREDDI', 'WARANGAL', 'DHALAI', 'GOMATI', 'KHOWAI', 'NORTH TRIPURA', 'SEPAHIJALA', 'SOUTH TRIPURA', 'UNAKOTI', 'WEST TRIPURA', 'AGRA', 'ALIGARH', 'ALLAHABAD', 'AMBEDKAR NAGAR', 'AMETHI', 'AMROHA', 'AURAIYA', 'AZAMGARH', 'BAGHPAT', 'BAHRAICH', 'BALLIA', 'BANDA', 'BARABANKI', 'BAREILLY', 'BASTI', 'BIJNOR', 'BUDAUN', 'BULANDSHAHR', 'CHANDAULI', 'CHITRAKOOT', 'DEORIA', 'ETAH', 'ETAWAH', 'FAIZABAD', 'FARRUKHABAD', 'FATEHPUR', 'FIROZABAD', 'GAUTAM BUDDHA NAGAR', 'GHAZIABAD', 'GHAZIPUR', 'GONDA', 'GORAKHPUR', 'HAPUR', 'HARDOI', 'HATHRAS', 'JALAUN', 'JAUNPUR', 'JHANSI', 'KANNAUJ', 'KANPUR DEHAT', 'KANPUR NAGAR', 'KASGANJ', 'KAUSHAMBI', 'KHERI', 'KUSHI NAGAR', 'LALITPUR', 'LUCKNOW', 'MAHARAJGANJ', 'MAHOBA', 'MAINPURI', 'MATHURA', 'MAU', 'MEERUT', 'MIRZAPUR', 'MORADABAD', 'MUZAFFARNAGAR', 'PILIBHIT', 'RAE BARELI', 'RAMPUR', 'SAHARANPUR', 'SAMBHAL', 'SANT KABEER NAGAR', 'SANT RAVIDAS NAGAR', 'SHAHJAHANPUR', 'SHAMLI', 'SHRAVASTI', 'SIDDHARTH NAGAR', 'SITAPUR', 'SONBHADRA', 'SULTANPUR', 'UNNAO', 'VARANASI', 'ALMORA', 'BAGESHWAR', 'CHAMOLI', 'CHAMPAWAT', 'DEHRADUN', 'HARIDWAR', 'NAINITAL', 'PAURI GARHWAL', 'PITHORAGARH', 'RUDRA PRAYAG', 'TEHRI GARHWAL', 'UDAM SINGH NAGAR', 'UTTAR KASHI', '24 PARAGANAS NORTH', '24 PARAGANAS SOUTH', 'BANKURA', 'BARDHAMAN', 'BIRBHUM', 'COOCHBEHAR', 'DARJEELING', 'DINAJPUR DAKSHIN', 'DINAJPUR UTTAR', 'HOOGHLY', 'HOWRAH', 'JALPAIGURI', 'MALDAH', 'MEDINIPUR EAST', 'MEDINIPUR WEST', 'MURSHIDABAD', 'NADIA', 'PURULIA'))


user_crop=st.selectbox("Pick your Preferred crop",yieldAreadf.Crop)





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
    st.subheader(f"your AI model has recommended : {out} , {name}")
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
    
    uyears = []
    uprod = []
    myears = []
    mprod = []
    usFlag = 0
    msFlag = 0
    # for index,rows in stateDatadf.iterrows():
    #     if(rows.state == state and rows.crop.lower() == user_crop.lower()):
    #         uyears.append(int(rows.year))
    #         try:
    #             uprod.append(float(rows.production))
    #         except:
    #             uprod.append(float(1000))
    #         usFlag = 1
    #     if(rows.state == state and rows.crop.lower() == ml_crop.lower()):
    #         myears.append(int(rows.year))
    #         try:
    #             mprod.append(float(rows.production))
    #         except:
    #             mprod.append(1000)
    #         msFlag = 1

    user_state_crop =stateDatadf[(stateDatadf['state']==state) & (stateDatadf['crop'] == user_crop) & (stateDatadf['district']==district)]
    user_state_crop.reset_index(inplace=True)

    if(user_state_crop.any()[0]):
        usFlag = 1
        for i in range( len(user_state_crop)):
            uyears.append(int(user_state_crop.loc[i]['year']))
            uprod.append(float(user_state_crop.loc[i]['production']))
            
    
    ml_state_crop =stateDatadf[(stateDatadf['state']==state) & (stateDatadf['crop'] == ml_crop) & (stateDatadf['district']==district)]
    ml_state_crop.reset_index(inplace=True)

    if(ml_state_crop.any()[0]):
        msFlag = 1
        for i in range( len(ml_state_crop)):
            myears.append(int(ml_state_crop.loc[i]['year']))
            mprod.append(float(ml_state_crop.loc[i]['production']))
            


    if(usFlag == 1):
        st.write(f"### Production of {user_crop} in {state} at {district}")
        ustatedf = pd.DataFrame(uprod,uyears)
        st.bar_chart(ustatedf)
    else:
        st.write(f"### Data for production of {user_crop} in {state} at {district} is unavailable , {name} .")
    
    if(msFlag == 1):
        st.write(f"### Production of {ml_crop} in {state} at {district}")
        mstatedf = pd.DataFrame(mprod,myears)
        st.bar_chart(mstatedf)
    else:
        st.write(f"### Data for production of {ml_crop} in {state} at {district} is unavailable , {name} .")


#st_shap(shap.plots.waterfall(shap_values[0]))
#shap_values = explainer.shap_values(np.array([n,p,k,temp,humidity,ph,rainfall]).reshape(1, -1))
# visualize the first prediction's explanation (use matplotlib=True to avoid Javascript)
#st_shap(shap.force_plot(explainer.expected_value, shap_values[0,:], df.iloc[0,:]))

# visualize the training set predictions
#st_shap(shap.force_plot(explainer.expected_value, shap_values, df), 400)
 