import streamlit as st 
st.title('Welcome to the BMI Calculator')

weight = st.number_input('Enter your weight in kgs')
status = st.radio('Select your height format:', ('cms', 'meters', 'feet'))

try:
    if status == 'cms':
        height = st.number_input('centimeters')
        bmi = weight/((height/100)**2) 

    elif status == 'meters':
        height = st.number_input('meters')
        bmi = weight/((height)**2)

    elif status == 'feet':
        height = st.number_input('feet')
        bmi = weight/((height/3.28)**2) 

except: 
    print('Zero division error') 

if st.button('Calculate BMI'):
    st.write('Your BMI index is {}. '.format(round(bmi))) 

    if bmi<16: 
        st.error('you are extremely underweight')
    elif (bmi>=16 and bmi<18):
        st.warning('you are underweight')
    elif(bmi>=18 and bmi<25):
        st.success('you are healthy')
    elif (bmi>=25 and bmi<30):
        st.warning('you are overweight')
    elif (bmi>=30): 
        st.error('Extremely overweight') 
   