import sqlite3

database = sqlite3.connect("news_transcript.sqlite")
databaseCursor = database.cursor()


databaseCursor.execute('''CREATE TABLE IF NOT EXISTS news_video(
                            id INTEGER PRIMARY KEY ASC,
                            video_id TEXT, 
                            channel_id TEXT,
                            channel_name TEXT,
                            title TEXT, 
                            published_at TEXT,
                            transcript TEXT
                            )''')
database.commit()

def execute_batch(query, data):
    """
    일괄 삽입을 위한 도우미 함수
    """
    databaseCursor.executemany(query, data)

def insert_news_metadata(metadata):
    print("DB function executed")
    databaseCursor.execute("""INSERT INTO news_video(video_id, channel_id, channel_name, title, published_at) VALUES (?, ?, ?, ?, ?)""", (metadata['video_id'], metadata['channel_id'], metadata['channel_name'], metadata['title'], metadata['published_at']))
    database.commit()

def insert_news_batch_metadata(video_data_list):
    """
    여러 비디오 데이터를 일괄로 DB에 삽입
    """
    print('db executed')
    
    query = '''INSERT INTO news_video(video_id, channel_id, channel_name, title, published_at)
                VALUES (?, ?, ?, ?, ?)'''

    # 리스트 내 각 항목이 딕셔너리인지 확인하고 데이터 추출
    data = [(video.get('video_id', ''), video.get('channel_id', ''), video.get('channel_name', ''),
                video.get('title', ''), video.get('published_at', ''))
            for video in video_data_list]

    execute_batch(query, data)
    database.commit()



def insert_transcript(video_id):
    pass