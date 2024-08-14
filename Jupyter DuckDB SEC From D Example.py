#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports
import pandas as pd
import duckdb as db
import numpy as np
from dateutil import parser


# In[2]:


"""
Specify path where form D files are stored. 
These can be downloaded from https://www.sec.gov/data-research/sec-markets-data/form-d-data-sets.
This notebook is structured to have each folder from the SEC data set stored in the folder Form_D_data. 
"""
path = "../Form_D_data"


# In[3]:


#Load the offerings TSVs from every folder in the Form D directory
offerings = db.read_csv(f"{path}/*/OFFERING.tsv", dtype={'TOTALOFFERINGAMOUNT': 'VARCHAR','TOTALREMAINING': 'VARCHAR'}).df()
offerings


# In[4]:


#Load the issuers TSVs from every folder in the Form D directory
issuers = db.read_csv(f"{path}/*/ISSUERS.tsv", dtype={'ISSUERPHONENUMBER':'VARCHAR','ZIPCODE':'VARCHAR'}).df()
issuers


# In[5]:


#Load the form_d_submissions TSVs from every folder in the Form D directory
form_d_submission = db.read_csv(f"{path}/*/FORMDSUBMISSION.tsv", dtype={'FILING_DATE':'VARCHAR'}).df()
form_d_submission


# In[6]:


#This query joins the three data frames together 

joins = """
select * from offerings as o 
left join issuers as i on i.ACCESSIONNUMBER = o.ACCESSIONNUMBER
left join form_d_submission as fds on fds.ACCESSIONNUMBER = o.ACCESSIONNUMBER
"""

where = """
where INVESTMENTFUNDTYPE = 'Venture Capital Fund'
"""

query = joins + where

df = db.query(f'{query}').df()
df


# In[7]:


def normalize_date(date_str):
    if pd.isna(date_str):
        return np.nan
    try:
        # Try to parse the date string
        parsed_date = parser.parse(date_str)
        # Return the date in a standard format
        return parsed_date.strftime('%Y-%m-%d')
    except:
        # If parsing fails, return NaN or the original string
        return np.nan  # or return date_str if you prefer

# Apply the function to your DataFrame column
df['normalized_date'] = df['FILING_DATE'].apply(normalize_date)


# In[8]:


#Filter out prior filings for the same fund
previous_accession_numbers = set(df['PREVIOUSACCESSIONNUMBER'].dropna())
vc = df[~df['ACCESSIONNUMBER'].isin(previous_accession_numbers)]


# In[9]:


# Create a new DuckDB database file
vc_database = db.connect('vc_database.duckdb')

# Execute the join query and write the results directly to the new database
vc_database.execute(f"""
CREATE TABLE vc_data AS
select * from vc
""")

vc_database.execute(f'select * from vc').df()


# In[10]:


# Close the connection
vc_database.close()

