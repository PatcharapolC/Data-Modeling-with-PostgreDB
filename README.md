# Songplays Data Modeling with Postgre Database

## Background

    A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. 
    Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Objective

    - Song play data tables Designed for data analysis. 
    - Queries optimization on with a Postgres Database.
    - ETL pipeline and database schema for data analysis.
    - Evaluated data modeling with Sparkify's expected results.

### Data Fields for each table in this project
    songplays table :
        1. songplay_id 
        2. start_time
        3. user_id
        4. level
        5. song_id
        6. artist_id
        7. session_id
        8. location
        9. user_agent

    users table:
        1. user_id
        2. first_name
        3. last_name
        4. gender
        5. level

    songs table:
        1. song_id
        2. title
        3. artist_id
        4. year
        5. duration


    artists table :
        1. artist_id
        2. name
        3. location
        4. latitude
        5. longitude

    time
        1. start_time
        2. hour
        3. day
        4. week
        5. month
        6. year
        7. weekday

## Schema diagram

<a href="https://ibb.co/yqmqnqD"><img src="https://i.ibb.co/L1D1z1M/songplays-schema.png" alt="songplays-schema" border="0"></a>

## Project files

- `sql_queries.py` - SQL commands for creating tables, insert values, drop tables and select tables.
- `create_tables.py` - Create and drop table from 'sql_queries.py' commands.
- `etl.ipynb` - worksheet for ETL process implementation and processing with songplays data from  `song_data` and `log_data` labels; source : 'http://millionsongdataset.com/'
- `test.ipynb` - Checking all commands in 'sql_queries.py' are correct.
- `etl.py` - Final ETL Processing file from etl.ipynb and ready to use it for dataset or song metadata files !

## For implementation this project
    1. Open your Terminal and clear all existed tables
    2. Created tables in your database
       command : python create_tables.py
    3. Executed for test SQL command
       run 'test.ipynb'
    4. ETL Process implementation on 'etl.ipynb'
    5. run etl.py when ETL Process implementation is completed
        5.1. Don't forget copy etl.ipynb command to 'etl.py'
        5.2. Don't forget deleted or drop existed talbes before running all files
    6. Finished or Completed, If not have ERROR after ran 'etl.py'
    
## How to run ?
    0. Open your Terminal and clear all existed tables
    1. Created tables in your database
       command : python create_tables.py
    2. Executed for ETL process and data processing
       command : python etl.py
    3. DONE !
    
## My git : https://gist.github.com/MosesOhYes
## My Project : https://gist.github.com/MosesOhYes/6f5e761c74fde816cb83d10338786ec6