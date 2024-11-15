#Setting up SQL with Streamlit involves integrating a SQL database with a Streamlit application. This allows you to build interactive web apps with real-time data querying and visualization. Here's a step-by-step guide:

# 1. Install Required Packages
First, make sure you have Streamlit installed along with the appropriate database connector for your SQL database. You can install these using pip.

pip install streamlit

# For SQLite:

pip install sqlite3

# For PostgreSQL:

pip install psycopg2

# For MySQL:

pip install mysql-connector-python

# For SQLAlchemy (Universal SQL toolkit):

pip install sqlalchemy

# 2. Set Up Your Database
# Make sure you have your SQL database set up:

# For SQLite, this could be a simple .db file.
# For PostgreSQL and MySQL, ensure the database is running and you have credentials to access it.
# Example setup for SQLite:

import sqlite3

# Create a SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')
conn.commit()
conn.close()


# 3. Create a Streamlit App
# Create a new Python file (e.g., app.py) for your Streamlit application.

import streamlit as st
import sqlite3
import pandas as pd

# Set up the SQLite connection
def init_connection():
    return sqlite3.connect('example.db')

# Function to query the database
def run_query(query):
    with init_connection() as conn:
        return pd.read_sql_query(query, conn)

# Streamlit App
st.title("SQL with Streamlit")

# Input fields for SQL query
query = st.text_area("Enter SQL query", "SELECT * FROM users")

if st.button("Run Query"):
    try:
        data = run_query(query)
        st.write(data)
    except Exception as e:
        st.error(f"Error: {str(e)}")


# 4. Run Your Streamlit App
# To launch your Streamlit app, use the following command in your terminal:

streamlit run app.py


# 5. Connect to Different Databases (Optional)
# You might want to connect to a specific SQL database like PostgreSQL or MySQL. Here’s how you can adjust the connection:

# PostgreSQL Example

import psycopg2
import pandas as pd
import streamlit as st

def init_connection():
    return psycopg2.connect(
        host="localhost",
        database="your_database",
        user="your_user",
        password="your_password"
    )

def run_query(query):
    with init_connection() as conn:
        return pd.read_sql_query(query, conn)

# MySQL Example

import mysql.connector
import pandas as pd
import streamlit as st

def init_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_user",
        password="your_password",
        database="your_database"
    )

def run_query(query):
    with init_connection() as conn:
        return pd.read_sql(query, conn)


# 6. Advanced: Use SQLAlchemy for Flexibility
# Using SQLAlchemy can be advantageous as it supports multiple database backends with the same interface.

#  Install SQLAlchemy:

pip install sqlalchemy

# Sample code:

from sqlalchemy import create_engine
import pandas as pd
import streamlit as st

engine = create_engine("sqlite:///example.db")

def run_query(query):
    with engine.connect() as conn:
        return pd.read_sql_query(query, conn)

query = st.text_area("Enter SQL query", "SELECT * FROM users")
if st.button("Run Query"):
    data = run_query(query)
    st.write(data)

# 7. Secure Your Application
# Never expose sensitive information like database passwords in your code. Use environment variables or a configuration file.
# For example, using environment variables:

import os
db_password = os.getenv("DB_PASSWORD")

# 8. Deploy Your App (Optional)
# You can deploy your Streamlit app using platforms like Streamlit Community Cloud, Heroku, or AWS. Make sure to set the environment variables and install required packages in the server environment.

# Additional Tips:
# Use caching with @st.cache_data to improve performance for repetitive queries.
# Use st.sidebar for input fields to create a cleaner UI.

@st.cache_data
def cached_query(query):
return run_query(query)






