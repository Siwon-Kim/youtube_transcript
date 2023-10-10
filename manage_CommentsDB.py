import sqlite3
from extract_video_transcript import *

database = sqlite3.connect("Comments.sqlite")
databaseCursor = database.cursor()


# databaseCursor.execute('''CREATE TABLE IF NOT EXISTS Comments(
#                             id INTEGER PRIMARY KEY ASC,
#                             comment_id TEXT, 
#                             video_id TEXT, 
#                             text_display TEXT,
#                             author_name TEXT,
#                             author_channel_url TEXT, 
#                             like_count INTEGER,
#                             published_at TEXT,
#                             total_reply_count INTEGER
#                             )''')
# database.commit()


def execute_batch(query, data):
    """
    일괄 삽입을 위한 도우미 함수
    """
    databaseCursor.executemany(query, data)

def insert_comments_batch_metadata(comments_data_list):
    """
    여러 댓글 데이터를 일괄로 DB에 삽입
    """
    print('db executed')
    
    query = '''INSERT INTO Comments(comment_id, video_id, text_display, author_name, author_channel_url, like_count, published_at, total_reply_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''

    # 리스트 내 각 항목이 딕셔너리인지 확인하고 데이터 추출
    data = [(video.get('video_id', ''), video.get('channel_id', ''), video.get('channel_name', ''),
                video.get('title', ''), video.get('published_at', ''))
            for video in comments_data_list]

    execute_batch(query, data)
    database.commit()