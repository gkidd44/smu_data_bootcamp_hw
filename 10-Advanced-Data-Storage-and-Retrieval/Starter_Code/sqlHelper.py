# Code structure and elements borrowed from the instructor's example materials during the lecture. 
# This Python script is establishing a Flask API with custom routes where a user can query a database 
# based on pre-defined SQL queries, and recieve data back within a browser as JSON. 

from sqlalchemy import create_engine
import pandas as pd

class SQLHelper():
    
    def __init__(self):
        self.database_path = "Resources/hawaii.sqlite"
        self.connection_str = f"sqlite:///{self.database_path}"
        self.engine = create_engine(self.connection_str)

    def executeQuery(self, query):
        df = pd.read_sql(query, self.engine)
        return(df)
    
    def get_precip(self):
        query = f"""
                SELECT 
                    m.date,
                    m.prcp
                FROM 
                    measurement m
                WHERE
                    date >= '2016-08-23'
                ORDER BY
                    date ASC;
                """
        return(self.executeQuery(query))

    def get_stations(self):
        query = f"""
                SELECT 
                    *
                FROM
                    station;
                """
        return(self.executeQuery(query))

    def get_tobs(self):
        query = f"""
                SELECT
                    *
                FROM
                    measurement
                WHERE
                    station = 'USC00519281' AND date >= '2016-08-23'
                ORDER BY
                    date ASC;
                """
        return(self.executeQuery(query))
