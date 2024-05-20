from .db import get_db
from sqlalchemy.sql import text

class Query:
    def __init__(self):
        pass

    async def __execute(self, db, query):
        try:
            query_data = db.execute(text(query))
            db.commit()
            return query_data
        except Exception as e:
            raise e

    async def insertUser(self, db, name, mail, phone, type=0):
        if not name or not mail or not phone:
            raise Exception(f'Missing someing from {name}, {mail}, {phone}')
        
        user = self.selectUsers(db, phone=phone)

        if user:
            raise Exception(f'User {name} already exists!')

        table = 'users'
        query = f'''
        
        INSERT INTO {table} (name, mail, phone, type)
        VALUES ('{name}', '{mail}', '{phone}', {type}) 

        '''

        try:
            _ = await self.__execute(db, query)
        except Exception as e:
            raise e
        
        return True
    
    async def selectUsers(self, db, name=None, mail=None, phone=None, type=None):
        if not name and not mail and not phone and not type:
            raise Exception(f'Need one of {name}, {mail}, {phone} or {type}')

        query = 'SELECT * FROM {table}'
        table = 'user'
        added = False
        if name:
            query = f'{query} WHERE name={name}'
            added = True
        if mail:
            if added:
                query = f'{query} AND mail={mail}'
            else:
                query = f'{query} WHERE mail={mail}'
        if phone:
            if added:
                query = f'{query} AND phone={phone}'
            else:
                query = f'{query} WHERE phone={phone}'
        if type:
            if added:
                query = f'{query} AND type={type}'
            else:
                query = f'{query} WHERE type={type}'
        

        try:
            query_data = await self.__execute(db, query)
        except Exception as e:
            raise e
        
        return query_data
    

        
