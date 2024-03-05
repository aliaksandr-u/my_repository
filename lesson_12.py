# # from psycopg2.extras import NamedTupleConnection, NamedTupleCursor
# #
# # with NamedTupleConnection(dsn="postgres://admin:admin@217.76.60.77:6666/admin") as connection:
# #     with connection.cursor() as cursor:  # type: NamedTupleCursor
#         # cursor.execute("""
#         #     CREATE TABLE IF NOT EXISTS departments (
#         #         id SERIAL PRIMARY KEY ,
#         #         name VARCHAR ( 32 ) NOT NULL UNIQUE
#         #     );
#         # """)
#         # cursor.execute("""
#         #     CREATE TABLE IF NOT EXISTS sub_departments (
#         #         id SERIAL PRIMARY KEY ,
#         #         name VARCHAR ( 32 ) NOT NULL UNIQUE
#         #     );
#         # """)
#         # cursor.execute("""
#         #     CREATE TABLE IF NOT EXISTS users (
#         #         id SERIAL PRIMARY KEY ,
#         #         department_id INTEGER ,
#         #         sub_department_id INTEGER,
#         #         FOREIGN KEY (department_id) REFERENCES departments(id),
#         #         FOREIGN KEY (sub_department_id) REFERENCES sub_departments(id)
#         #     );
#         # """)
#         # cursor.execute("""
#         #     CREATE TABLE IF NOT EXISTS chats (
#         #         id SERIAL PRIMARY KEY ,
#         #         name VARCHAR ( 32 ) NOT NULL UNIQUE
#         #     );
#         # """)
#         # cursor.execute("""
#         #     CREATE TABLE IF NOT EXISTS chat_relations (
#         #         id SERIAL PRIMARY KEY ,
#         #         chat_id INTEGER NOT NULL ,
#         #         department_id INTEGER ,
#         #         sub_department_id INTEGER,
#         #         FOREIGN KEY (department_id) REFERENCES departments(id),
#         #         FOREIGN KEY (sub_department_id) REFERENCES sub_departments(id),
#         #         FOREIGN KEY (chat_id) REFERENCES chats(id)
#         #     );
#         # """)
#         # connection.commit()
#         # cursor.execute(query="""
#         #     SELECT chats.name FROM chat_relations
#         #     JOIN chats ON chats.id  = chat_relations.chat_id
#         #     WHERE (
#         #         chat_relations.department_id IS NULL OR
#         #         chat_relations.department_id = (
#         #             SELECT users.department_id FROM users WHERE users.id = %(user_id)s
#         #         )
#         #     ) AND (
#         #         chat_relations.sub_department_id IS NULL OR
#         #         chat_relations.sub_department_id = (
#         #             SELECT users.sub_department_id FROM users WHERE users.id = %(user_id)s
#         #         )
#         #     );
#         # """, vars={"user_id": 3})
#         # print(cursor.fetchall())
# from redis import Redis
# from sqlalchemy import select, update, delete, insert, and_, all_, or_, any_, func, Table, alias
# from sqlalchemy.orm import selectinload, joinedload
# from lesson11 import *
#
#
# # with session_maker() as session:
#     # session.scalars()
#     # session.execute().scalars()
#     # session.scalar()
#     # session.execute().scalar()
#
# # stmt = select(Topic)
# # stmt = stmt.order_by(Topic.date_created.desc())
# # stmt = stmt.order_by(Topic.title)
# # stmt = stmt.filter(or_(Topic.id >= 2, ~Topic.title.icontains("new")))
# # # stmt = stmt.filter_by(id=5, title="sport")
# # print(stmt)
# user_id = 1
# q = select(Chat).join(ChatRelation)
# q = q.filter(
#     and_(
#         or_(
#             ChatRelation.department_id.is_(None),
#             ChatRelation.department_id == (
#                 select(User.department_id).filter(User.id == user_id)
#             )
#         ),
#         or_(
#             ChatRelation.sub_department_id.is_(None),
#             ChatRelation.sub_department_id == (
#                 select(User.sub_department_id).filter(User.id == user_id)
#             )
#         ),
#     )
# )
# # stmt = select(Topic.id + 5).filter(func.max(Topic.id))
# # print(stmt)
# # with session_maker() as session:
# #     response = session.scalars(statement=q)
# #     print(response.unique().all())
#
# # stmt = update(Topic).values(title="qwerqwer")
# # stmt = insert(Tag).values()
#
#
# # TopicTag = Table(
# #     "topic_tags",
# #     Base.metadata,
# #     Column("topic_id", INT, ForeignKey("topics.id"), primary_key=True),
# #     Column("tag_id", INT, ForeignKey("tags.id"), primary_key=True),
# # )
# # TopicTag.insert().values([{}, {}, {}])
#
# # q1 = select(TopicTag.c.topic_id).filter(TopicTag.c.tag_id == 5)
# # print(q1)
#
# # with session_maker() as session:
# #     # user = session.get(User, 1, options=[joinedload(User.department, User.sub_department)])
# #     user = session.scalar(
# #         select(User)
# #         .options(
# #             joinedload(User.department).subqueryload(Department.chats),
# #             joinedload(User.sub_department)
# #         )
# #     )
# #     print(user.department.chats)
#
#
# from pydantic import BaseModel, PositiveInt, Field
#
#
# class DepartmentDetail(BaseModel):
#     id: PositiveInt
#     name: str = Field(default=..., max_length=32)
#
#
# class SubDepartmentDetail(BaseModel):
#     id: PositiveInt
#     name: str = Field(default=..., max_length=32)
#
#
# class ChatDetail(BaseModel):
#     id: PositiveInt
#     name: str = Field(default=..., max_length=32)
#     departments: list[DepartmentDetail]
#     sub_departments: list[SubDepartmentDetail]
#
#
# # with session_maker() as session:
# #     chat = session.get(Chat, 1, options=[joinedload(Chat.departments), joinedload(Chat.sub_departments)])
# #     chat_detail = ChatDetail.model_validate(obj=chat, from_attributes=True)
# #     print(chat_detail)
#
#
# from datetime import timedelta
# from time import sleep
#
# from redis import Redis
# from json import dumps, loads
#
# redis = Redis.from_url(url="redis://0.0.0.0:6379/0")
# print(redis.keys("*u*"))
# redis.set(name="user", value=dumps({"key": "value"}))
# print(loads(redis.get("user")))
# redis.lpush("myqueue", 1, 2, 3, 4)
# print(redis.rpop("myqueue"))
# print(redis.rpop("myqueue"))
# redis.lpush("myqueue", "HELLO")
# print(redis.llen("myqueue"))
# redis.set("session", "qwerqwer", ex=timedelta(seconds=10))
# print(redis.get("session"))
# sleep(5)
# print(redis.get("session"))
# sleep(5)
# print(redis.get("session"))
from enum import IntEnum

from sqlalchemy import Column, Enum


class Status(IntEnum):
    TO_DO = 0
    IN_PROGRESS = 1
    DONE = 2