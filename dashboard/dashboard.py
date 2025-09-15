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
    cols = st.columns(4)
    with cols[0]:
        select_region = st.selectbox('Select region:', df["WORKPLACE_REGION"].unique())
    with cols[1]:
        select_occupation = st.selectbox('Select occupation:', df.query('WORKPLACE_REGION == @select_region')["OCCUPATION"].unique())
    with cols[2]:
        select_company = st.selectbox('Select company:', df.query('WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation')["EMPLOYER_NAME"].unique())
        
    with cols[3]:
        select_headline = st.selectbox('Select headline:', df.query('WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & EMPLOYER_NAME == @select_company')["HEADLINE"])
        
    st.markdown("## Job listings data")
    st.markdown(df.query(
        "WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & HEADLINE == @select_headline & EMPLOYER_NAME == @select_company"
    )["DESCRIPTION_HTML"].values[0],
    unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    cols = st.columns(4)
    with cols[0]:
        st.markdown("<h4 style= 'color:steelblue'> Vacancies </h4>", unsafe_allow_html=True)
        st.markdown(df.query('WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & HEADLINE == @select_headline & EMPLOYER_NAME == @select_company'
    )['VACANCIES'].values[0])
        
    with cols[1]:
        st.markdown("<h4 style= 'color:steelblue'> Application deadline </h4>", unsafe_allow_html=True)
        st.markdown(df.query("WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & HEADLINE == @select_headline & EMPLOYER_NAME == @select_company"
    )['APPLICATION_DEADLINE'].values[0])
        
    with cols[2]:
        st.markdown("<h4 style= 'color:steelblue'> Duration </h4>", unsafe_allow_html=True)
        st.markdown(f'**{df.query("WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & HEADLINE == @select_headline & EMPLOYER_NAME == @select_company"
    )['DURATION'].values[0]}**')
        
    with cols[3]:
        st.markdown("<h4 style= 'color:steelblue'> Employment type </h4>", unsafe_allow_html=True)
        st.markdown(df.query("WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & HEADLINE == @select_headline & EMPLOYER_NAME == @select_company"
    )['EMPLOYMENT_TYPE'].values[0])
    
    cols = st.columns(4)
    
    with cols[0]:
        st.markdown("<h4 style= 'color:steelblue'> Salary type </h4>", unsafe_allow_html=True)
        st.markdown(df.query("WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & HEADLINE == @select_headline & EMPLOYER_NAME == @select_company"
    )['SALARY_TYPE'].values[0])
        
    with cols[1]:
        st.markdown("<h4 style= 'color:steelblue'> Job ID </h4>", unsafe_allow_html=True)
        st.markdown(df.query("WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & HEADLINE == @select_headline & EMPLOYER_NAME == @select_company"
    )['JOB_DESCRIPTION_ID'].values[0])
        
    with cols[2]:
        st.markdown("<h4 style= 'color:steelblue'> Occupation group </h4>", unsafe_allow_html=True)
        st.markdown(df.query("WORKPLACE_REGION == @select_region & OCCUPATION == @select_occupation & HEADLINE == @select_headline & EMPLOYER_NAME == @select_company"
    )['OCCUPATION_GROUP'].values[0])
        

    
if page == "Start":
    st.title("Välkommen till dashboarden")
    layout_graphs(df_test)
elif page == "job ad":
    layout_ads(df_test)


    
