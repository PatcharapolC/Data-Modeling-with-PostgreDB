# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES


songplay_table_create = ("""create table if not exists songplays (
                                        songplay_id serial PRIMARY KEY, 
                                        start_time timestamp not null REFERENCES time (start_time), 
                                        user_id int not null REFERENCES users (user_id), 
                                        level varchar,
                                        song_id varchar REFERENCES songs (song_id), 
                                        artist_id varchar REFERENCES artists (artist_id), 
                                        session_id int, 
                                        location varchar, 
                                        user_agent varchar
                                    );
""")


user_table_create = ("""create table if not exists users (
                                    user_id int PRIMARY KEY, 
                                    first_name varchar, 
                                    last_name varchar, 
                                    gender varchar, 
                                    level varchar
                                );
""")

song_table_create = ("""create table if not exists songs (
                                    song_id varchar PRIMARY KEY,
                                    title varchar not null, 
                                    artist_id varchar REFERENCES artists (artist_id),
                                    year int, 
                                    duration float not null
                                );
""")

artist_table_create = ("""create table if not exists artists (
                                    artist_id varchar PRIMARY KEY, 
                                    name varchar not null, 
                                    location varchar,
                                    latitude float, 
                                    longitude float
                                );
""")

time_table_create = ("""create table if not exists time(
                            start_time timestamp PRIMARY KEY, 
                            hour varchar,
                            day varchar,
                            week varchar,
                            month varchar,
                            year int,
                            weekday varchar
                        );
""")

# INSERT RECORDS

# INSERT INTO table_name (column1, column2, column3, ...)
# VALUES (value1, value2, value3, ...);

songplay_table_insert = ("""insert into songplays(
                                        start_time, 
                                        user_id, 
                                        level,
                                        song_id, 
                                        artist_id, 
                                        session_id, 
                                        location, 
                                        user_agent
                            )
                             values (%s, %s, %s, %s, %s, %s, %s, %s)
                             ON CONFLICT 
                             DO NOTHING;
""")

user_table_insert = ("""insert into users(
                                    user_id, 
                                    first_name, 
                                    last_name, 
                                    gender, 
                                    level
                            )
                             values (%s, %s, %s, %s, %s)
                             ON CONFLICT (user_id) 
                             DO UPDATE 
                             SET level = EXCLUDED.level;
""")

song_table_insert = ("""insert into songs(
                                    song_id, 
                                    title, 
                                    artist_id, 
                                    year, 
                                    duration
                            )
                             values (%s, %s, %s, %s, %s)
                             ON CONFLICT (song_id) 
                             DO NOTHING;
""")

artist_table_insert = ("""insert into artists(
                                    artist_id, 
                                    name, 
                                    location,
                                    latitude, 
                                    longitude
                            )
                             values (%s, %s, %s, %s, %s)
                             ON CONFLICT (artist_id) 
                             DO NOTHING;
""")


time_table_insert = ("""insert into time(
                                    start_time, 
                                    hour , 
                                    day,
                                    week, 
                                    month, 
                                    year, 
                                    weekday
                            )
                             values (%s, %s, %s, %s, %s, %s, %s)
                             ON CONFLICT (start_time) 
                             DO NOTHING;
""")

# FIND SONGS

song_select = (""" 
select songs.song_id, artists.artist_id 
from songs JOIN artists
on songs.artist_id= artists.artist_id
where songs.title= %s AND artists.name= %s AND songs.duration= %s;
""")

# QUERY LISTS

#songplay ref user song
#user ref non
#songs ref artist
#artist ref non
#seq : user > song > artist > time > songplay
#create_table_queries = [user_table_create, songplay_table_create, song_table_create, artist_table_create, time_table_create]

create_table_queries = [artist_table_create, song_table_create, user_table_create, time_table_create, songplay_table_create]

drop_table_queries = [artist_table_create, song_table_create, user_table_drop, time_table_drop, songplay_table_drop]