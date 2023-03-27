import streamlit as st 
from streamlit_option_menu import option_menu
import pickle
import pandas as pd



with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Login Page","Predection Page"]
    )


if selected == 'Predection Page':


    st.title('Concrete Compressive Strength Prediction')

    lasso = pickle.load(open('lasso.pkl','rb'))


    select_cement = st.slider('Cement',min_value = 0,max_value = 419,step = 1,value = 10)
    
    select_blast_furnace_slag = st.slider('Blast furnace slag',min_value = 0,max_value = 214,step = 1,value = 10)
    
    select_fly_ash = st.slider('Fly ash',min_value = 0,max_value = 200,step = 1,value = 10)
    
    select_water= st.slider('Water',min_value = 0,max_value = 221,step = 1,value = 10)
    
    select_superplasticizer = st.slider('Superplasticizer',min_value = 0,max_value = 23,step = 1,value = 1)
    
    select_coarse_aggregate = st.slider('Coarse aggregate',min_value = 0,max_value = 1090,step = 1,value = 50)
    
    select_fine_aggregate = st.slider('Fine aggregate',min_value = 0,max_value = 900,step = 1,value = 40)
    
    select_age = st.slider('Age',min_value = 0,max_value = 100,step = 1,value = 5)
    
    
            
        
        
    if st.button('Predict'):
        input_df = pd.DataFrame({'cement':[select_cement],
                                 'blast_furnace_slag':[select_blast_furnace_slag],
                                 'fly_ash':[select_fly_ash],
                                'water':[select_water],
                                'superplasticizer':[select_superplasticizer],
                                'coarse_aggregate':[select_coarse_aggregate],
                                'fine_aggregate ':[select_fine_aggregate],
                                'age':[select_age]})

        #st.table(input_df)
        result = float(lasso.predict(input_df))
        #result_percentage = lasso.predict_proba(input_df)
        
        st.title('Predicted Outcome...')
        
        st.header('Concrete Compressive Strength')
        
        st.info(result)
    




# 'cement', 'blast_furnace_slag', 'fly_ash', 'water', 'superplasticizer',
#        'coarse_aggregate', 'fine_aggregate ', 'age',
#        'concrete_compressive_strength']

