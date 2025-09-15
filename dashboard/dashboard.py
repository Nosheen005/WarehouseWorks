import streamlit as st 
from connect_data_warehouse import query_job_listings
import altair as alt
import pandas as pd
mart = 'mart_construction'
query = f'SELECT * FROM {mart}'
st.set_page_config(layout="wide")
st.sidebar.header("Pages")  
page = st.sidebar.radio("Gå till", ["Start", "job ad"])
df_test = query_job_listings(query)

def layout_graphs(df):

    st.title("Construction job ads")
    st.write(
        "This dashboard shows construction job ads from arbetsförmedlingens API. "
    )
    
    cols = st.columns(2)

    with cols[0]:
        st.metric(label="Total vacancies", value=df["VACANCIES"].sum())

    with cols[1]:
        st.metric(
            label="Total ads",
            value=len(df),
        )
        
    df_employer = query_job_listings(
        """
            SELECT SUM(VACANCIES) AS VACANCIES, EMPLOYER_NAME
            FROM mart_construction
            GROUP BY EMPLOYER_NAME
            ORDER BY VACANCIES DESC
            LIMIT 10
        """
        ) 
    
    df_occupation = query_job_listings(
        """
            SELECT SUM(VACANCIES) AS VACANCIES, OCCUPATION
            FROM mart_construction
            GROUP BY OCCUPATION
            ORDER BY VACANCIES DESC
            LIMIT 10
        """
        ) 
    
    df_region = query_job_listings(
        """
            SELECT SUM(VACANCIES) AS VACANCIES, WORKPLACE_REGION
            FROM mart_construction
            GROUP BY WORKPLACE_REGION
            ORDER BY VACANCIES DESC
            LIMIT 10
        """
        ) 
    
    df_duration = query_job_listings(
        """
            SELECT SUM(VACANCIES) AS VACANCIES, DURATION
            FROM mart_construction
            GROUP BY DURATION
            ORDER BY VACANCIES DESC
            LIMIT 10
        """
        ) 
    
    df_employer = df_employer.sort_values('VACANCIES', ascending=False)
    df_employer["EMPLOYER_NAME"] = pd.Categorical(df_employer["EMPLOYER_NAME"], categories=df_employer["EMPLOYER_NAME"], ordered=True)
    
    df_occupation = df_occupation.sort_values('VACANCIES', ascending=False)
    df_occupation["OCCUPATION"] = pd.Categorical(df_occupation["OCCUPATION"], categories=df_occupation["OCCUPATION"], ordered=True)
    
    df_region = df_region.sort_values('VACANCIES', ascending=False)
    df_region["WORKPLACE_REGION"] = pd.Categorical(df_region["WORKPLACE_REGION"], categories=df_region["WORKPLACE_REGION"], ordered=True)
    
    df_duration = df_duration.sort_values('VACANCIES', ascending=False)
    df_duration["DURATION"] = pd.Categorical(df_duration["DURATION"], categories=df_duration["DURATION"], ordered=True)
    
    cols = st.columns(2)
    
    with cols[0]:
        st.write("### Top 10 Employers by Vacancies")
        st.write(alt.Chart(df_employer.sort_values('VACANCIES', ascending=False)).mark_bar().encode(
                x=alt.X('EMPLOYER_NAME', title='Employer'),
                y=alt.Y('VACANCIES', title='Vacancies'),
                color=alt.Color('EMPLOYER_NAME:N',legend=None),
                tooltip=['EMPLOYER_NAME', 'VACANCIES']
            ))
        
    with cols[1]:
        st.write("### Top 10 Occupations by Vacancies")
        st.write(alt.Chart(df_occupation.sort_values('VACANCIES', ascending=False)).mark_bar().encode(
                x=alt.X('OCCUPATION', title='Occupation'),
                y=alt.Y('VACANCIES', title='Vacancies'),
                color=alt.Color('OCCUPATION:N',legend=None),
                tooltip=['OCCUPATION', 'VACANCIES']
            ))
        
    cols = st.columns(2)
    
    with cols[0]:
        st.write("### Top 10 Regions by Vacancies")
        st.write(alt.Chart(df_region.sort_values('VACANCIES', ascending=False)).mark_bar().encode(
                x=alt.X('WORKPLACE_REGION', title='Region'),
                y=alt.Y('VACANCIES', title='Vacancies'),
                color=alt.Color('WORKPLACE_REGION:N',legend=None),
                tooltip=['WORKPLACE_REGION', 'VACANCIES']
            ))
            
    with cols[1]:
        st.write("### Duration of employment by Vacancies")
        st.write(alt.Chart(df_duration.sort_values('VACANCIES', ascending=False)).mark_bar().encode(
                x=alt.X('DURATION', title='Duration'),
                y=alt.Y('VACANCIES', title='Vacancies'),
                color=alt.Color('DURATION:N',legend=None),
                tooltip=['DURATION', 'VACANCIES']
            ))
        
def layout_ads(df):
    st.markdown("## Job listings data")
    st.dataframe(df)

    
if page == "Start":
    st.title("Välkommen till dashboarden")
    layout_graphs(df_test)
elif page == "job ad":
    layout_ads(df_test)


    
