from psycopg2 import connect
#from psycopg2._psycopg import cursor
#from psycopg2.extras import NamedTupleCursor
#from datetime import datetime

#postgres://username:password@host:port/db_name
with connect(dsn="postgres://user13:UUsBwRoy2@217.76.60.77:6666/admin") as conn:
    ...