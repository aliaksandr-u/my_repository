from psycopg2 import connect
from psycopg2._psycopg import cursor
#from psycopg2.extras import NamedTupleCursor
#from datetime import datetime

#postgres://username:password@host:port/db_name
with connect(dsn="postgres://user13:UUsBwRoy2@217.76.60.77:6666/admin") as conn:
    with conn.cursor() as cur:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tags(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(16) NOT NULL UNIQUE CHECK ( length(name) >= 2 )
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS topics(
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(128) NOT NULL CHECK ( length(title) >= 2 ),
                    body TEXT NOT NULL,
                    date_created TIMESTAMP NOT NULL DEFAULT (now()),
                    is_published BOOLEAN NOT NULL DEFAULT (false)
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS topic_tags(
                tag_id INTEGER,
                topic_id INTEGER,
                PRIMARY KEY (tag_id, topic_id),
                FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE RESTRICT ON UPDATE CASCADE,
                FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE RESTRICT ON UPDATE CASCADE
                );
            """)
            conn.commit()