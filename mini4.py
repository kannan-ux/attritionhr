import pandas as pd
import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
with open("C:/Users/sakth/attrition2.pkl",'rb')as file:
    model=pickle.load(file)
with open("C:/Users/sakth/job1.pkl","rb")as file:
    model1=pickle.load(file)
with open("C:/Users/sakth/rating.pkl","rb")as file:
    model2=pickle.load(file)
with open("C:/Users\sakth\promotion.pkl","rb")as file:
    model3=pickle.load(file)
import streamlit as st
from streamlit_option_menu import option_menu
st.sidebar.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #ADD8E6;  /* Light Blue Background */
        }
        .css-1d391kg { 
            color: black;  /* Text color */
        }
        .css-1v3fvcr {
            background-color: #0077B6 !important;  /* Dark Blue Highlight */
        }
    </style>
    """,
    unsafe_allow_html=True
)
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #005B96;'>🔍 Select a Prediction Task</h2>", unsafe_allow_html=True)

    selection = option_menu(
        menu_title="Choose The Prediction",
        options=["Attrition Prediction", "Job Stasification ", "Rating", "Promotion"],
        icons=['person-dash-fill', 'people-fill', 'star-fill', 'arrow-up-circle-fill'],
        menu_icon="bar-chart-fill",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#ADD8E6"},
            "icon": {"color": "#005B96", "font-size": "20px"},
            "nav-link": {"color": "black", "font-size": "18px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#0077B6", "color": "white"},
        }
    )

if selection=="Attrition Prediction":
    st.markdown(
        f"""
                <style>
                   .stApp {{
                    background-color:#87ceeb
                }}
                   .main-content {{
                        padding: 20px;
                        border-radius: 10px;
                        background-color: 	rgba(160, 230, 255, 0.6); /* Add slight transparency */
                        color: black;
                        text-align: center;
                    }}
                </style>
                """,
        unsafe_allow_html=True)
    st.markdown("<div class='main-content'><h1>ATTRITION PREDICTION</h1><p></p></div>",
                unsafe_allow_html=True)
    st.image("C:/Users/sakth\Downloads\Employee-Attrition.jpg")
    col1,col2=st.columns(2)
    with col1:
       Age=st.number_input("Age")
       MonthlyIncome=st.number_input("MonthlyIncome")
       JobSatisfaction=st.number_input("JobSatisfaction")
       YearsAtCompany=st.number_input("YearsAtCompany")
       MaritalStatus = st.number_input("MaritalStatus")
    with col2:
      OverTime=st.number_input("OverTime")
      HumanResources=st.number_input("HumanResources")
      Research_Development=st.number_input("Research_Development")
      Sales=st.number_input("Sales")
    inputdata=np.array([Age,MonthlyIncome,JobSatisfaction,YearsAtCompany,MaritalStatus,OverTime,
    HumanResources,	Research_Development	,Sales]).reshape(1,-1)
    feature_names=model.feature_names_in_
    inputdata_df =pd.DataFrame(inputdata,columns=feature_names)
    if st.button("Predict"):
        prediction=model.predict(inputdata)
        if prediction[0]==0:
            st.write("Employee is not attributed")
        else:
            st.write("Employee is attributed")
elif selection=="Job Stasification ":
    st.markdown(
        f"""
                    <style>
                       .stApp {{
                        background-color:#FFD700

                    }}
                       .main-content {{
                            padding: 20px;
                            border-radius: 10px;
                            background-color: 	rgb(245, 222, 179); /* Add slight transparency */
                            color: black;
                            text-align: center;
                        }}
                    </style>
                    """,
        unsafe_allow_html=True)
    st.markdown("<div class='main-content'><h1>JOB STASIFICATION  </h1><p></p></div>",
                unsafe_allow_html=True)
    st.image("C:/Users\sakth\Downloads\Importance-of-job-satisfaction-1.jpg")
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.number_input("Age")
        Gender=st.number_input("Gender")
        MonthlyIncome=st.number_input("MonthlyIncome")
        RelationshipSatisfaction=st.number_input("RelationshipSatisfaction")
        TrainingTimesLastYear=st.number_input("TrainingTimesLastYear")
        Human_Resources=st.number_input("Human_Resources")
    with col2:
        Research_Development=st.number_input("Research_Development")
        Sales=st.number_input("Sales")
        Healthcare_Representative=st.number_input("Healthcare_Representative")
        Human_Resources1=st.number_input("Human_Resources1")
        Laboratory_Technician=st.number_input("Laboratory_Technician")
        Manager=st.number_input("Manager")
    with col3:
        Manufacturing_Director=st.number_input("Manufacturing_Director")
        Research_Director=st.number_input("Research_Director")
        Research_Scientist=st.number_input("Research_Scientist")
        Sales_Executive=st.number_input("Sales_Executive")
        Sales_Representative=st.number_input("Sales_Representative")
    inputdata = np.array([Age, Gender, MonthlyIncome, RelationshipSatisfaction,
       TrainingTimesLastYear, Human_Resources, Research_Development,
       Sales, Healthcare_Representative, Human_Resources1,
       Laboratory_Technician, Manager, Manufacturing_Director,
       Research_Director, Research_Scientist, Sales_Executive,
       Sales_Representative]).reshape(1, -1)
    feature_names = model1.feature_names_in_
    inputdata_df = pd.DataFrame(inputdata, columns=feature_names)
    if st.button("Predict"):
        prediction = model1.predict(inputdata)
        if prediction[0] == 1:
            st.write("Employee is not stasified")
        elif prediction[0] ==2:
            st.write(" Employee is not stasified")
        elif prediction[0] ==3:
            st.write(" Employee is literally stasified")
        else:
            st.write(" Employee is stasified")
elif selection=="Rating":
    st.markdown(
        f"""
                        <style>
                           .stApp {{
                            background-color:#D3D3D3

                        }}
                           .main-content {{
                                padding: 20px;
                                border-radius: 10px;
                                background-color: 	rgba(50, 50, 50, 0.6); /* Add slight transparency */
                                color: black;
                                text-align: center;
                            }}
                        </style>
                        """,
        unsafe_allow_html=True)
    st.markdown("<div class='main-content'><h1>RATING  </h1><p></p></div>",
                unsafe_allow_html=True)
    st.image("C:/Users\sakth\Downloads/62ff418801c3d8cbe5341724_Blog banners_Performance Rating Scales.png")
    col1,col2=st.columns(2)
    with col1:
        Education=st.number_input("Education")
        JobInvolvement=st.number_input("JobInvolvement")
        JobLevel=st.number_input("JobLevel")
    with col2:
        MonthlyIncome=st.number_input("MonthlyIncome")
        YearsAtCompany=st.number_input("YearsAtCompany")
        YearsInCurrentRole=st.number_input("YearsInCurrentRole")
    inputdata=np.array([Education,JobInvolvement,JobLevel,MonthlyIncome,YearsAtCompany,YearsInCurrentRole]).reshape(1,-1)
    feature_names=model2.feature_names_in_
    input_data_df=pd.DataFrame(inputdata,columns=feature_names)
    if st.button("Predict"):
        prediction=model2.predict(inputdata)
        st.write(f" The Employee Rating is :{prediction}")
elif selection=="Promotion":
    st.markdown(
        f"""
                     <style>
                        .stApp {{
                         background-color:#E6E6FA

                     }}
                        .main-content {{
                             padding: 20px;
                             border-radius: 10px;
                             background-color: 	rgb(245, 222, 179); /* Add slight transparency */
                             color: black;
                             text-align: center;
                         }}
                     </style>
                     """,
        unsafe_allow_html=True)
    st.markdown("<div class='main-content'><h1>PROMOTION  </h1><p>  </p></div>",
                unsafe_allow_html=True)
    st.image("C:/Users\sakth\Downloads\employee-promotion-slide1.png")
    col1,col2=st.columns(2)
    with col1:
        JobLevel=st.number_input("JobLevel")
        TotalWorkingYears=st.number_input("TotalWorkingYears")
        YearsInCurrentRole=st.number_input("YearsInCurrentRole")
    with col2:
        PerformanceRating=st.number_input("PerformanceRating")
        Education=st.number_input("Education")
    inputdata=np.array([JobLevel,TotalWorkingYears,YearsInCurrentRole,PerformanceRating,Education]).reshape(1,-1)
    feature_names=model3.feature_names_in_
    inputdata_df=pd.DataFrame(inputdata,columns=feature_names)
    if st.button("Predict"):
        prediction=model3.predict(inputdata)
        st.write(f" The Employee Last Promoted is:{prediction} years")

