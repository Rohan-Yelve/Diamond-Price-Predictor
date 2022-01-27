import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title('Diamond Price Predictor')

carat = st.number_input('Carat (Weight)')

color = st.selectbox('Color (from J (worst) to D (best))',['D','E','F','G','H','I','J'])

clarity = st.selectbox('Clarity (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)',['I1','SI2','SI1',
'VS2','VS1','VVS2','VVS1','IF'])

length = st.number_input('Length in mm')

width = st.number_input('Width in mm')

depth = st.number_input('Depth in mm')

if st.button('Predict Price'):
    
    if color == 'D':
        color = 6
    elif color == 'E':
        color = 5
    elif color == 'F':
        color = 4
    elif color == 'G':
        color = 3
    elif color == 'H':
        color = 2
    elif color == 'I':
        color = 1
    else:
        color = 0

    if clarity == 'I1':
        clarity = 0
    elif clarity == 'SI2':
        clarity = 1
    elif clarity == 'SI1':
        clarity = 2
    elif clarity == 'VS2':
        clarity = 3
    elif clarity == 'VS1':
        clarity = 4
    elif clarity == 'VVS2':
        clarity = 5
    elif clarity == 'VVS1':
        clarity = 6
    else:
        clarity =7

    query = np.array([carat,color,clarity,length,width,depth])
    query = query.reshape(1,6)

    st.title("Your diamond cost is $ "+ str(int(np.exp(model.predict(query)[0]))))
