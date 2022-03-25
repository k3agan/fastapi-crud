from app.api.models import NoteSchema, NoteDB
from app.db import notes, database


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)


async def get(id: int):
    query = notes.select().where(notes.c.id == id)
    return await database.fetch_one(query=query)


async def get_all():
    query = notes.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: NoteSchema):
    query = (notes
             .update()
             .where(notes.c.id == id)
             .values(title=payload.title, description=payload.description)
             .returning(notes.c.id)
             )
    return await database.execute(query=query)


async def delete(id: int):
    query = notes.delete().where(notes.c.id == id)
    return await database.execute(query=query)


async def delete_all():
    query = notes.delete()
    return await database.execute(query=query)
