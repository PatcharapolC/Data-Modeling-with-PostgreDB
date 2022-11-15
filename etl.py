import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    
    """
    This procedure processes a song file whose filepath has been provided as an arugment.
    It extracts the song information in order to store it into the songs table.
    Then it extracts the artist information in order to store it into the artists table.

    INPUTS: 
    * cur the cursor variable
    * filepath the file path to the song file
    
    CAUTION:
    Inserted procedure function is inserted in order to 
    artists table -> songs table. -> time table -> users table -> songplays table. 
    """
        
    # open song file
    df = pd.read_json(filepath, lines=True)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 
                      'artist_latitude', 'artist_longitude']].values[0].tolist()
    
    cur.execute(artist_table_insert, artist_data)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    


def process_log_file(cur, filepath):
    
    """
    This procedure processes a song file whose filepath has been provided as an arugment.
    It extracts the log data in order to store it into the time table and user table.
    Then it extracts the all data in order to store it into the songplays table (Fact table) 
    from songs table and artists table condition ie. title, duration and name.

    INPUTS: 
    * cur the cursor variable
    * filepath the file path to the log file (Log data)
    
    CAUTION:
    Inserted procedure function is inserted in order to 
    time table -> users table -> songplays table. 

    """
        
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df.loc[df['page'] =='NextSong']

    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = (df['ts'].values, df['ts'].dt.hour, df['ts'].dt.day, 
                 df['ts'].dt.weekofyear, df['ts'].dt.month, 
                 df['ts'].dt.year, df['ts'].dt.weekday)
    
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    
    dict_ts = {}
    for i in range(len(column_labels)):
        dict_ts[column_labels[i]] = time_data[i]
    
    time_df = pd.DataFrame(dict_ts)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']] 

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, 
                         artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    
    """
    Get all required parameters for system starting, all processing function and all files matching extension from directory

    INPUTS: 
    * cur the cursor variable
    * conn the psycopg2 connnection
    * filepath the file path to the log file (Log data)
    * func the fuction for processing ie. process_song_file function and process_log_file function
    """
        
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    
    """
    Python Main Function is the beginning of any Python program.
    
    CONDITION:
    *  if the conditional statement evaluates to True, it means, the .py (Python Script) file is being run or executed directly
    """
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()