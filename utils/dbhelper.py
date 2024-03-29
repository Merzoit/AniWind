import asyncio
import aiomysql


class Database:
    def __init__(self):
        self.host = '109.71.243.208'
        self.port = 3306
        self.user = 'gen_user'
        self.password = 'eDZdRS8inql'
        self.db = 'default_db'
        self.conn = None

    async def connect(self):
        try:
            self.conn = await aiomysql.connect(
                host=self.host, 
                port=self.port,                             
                user=self.user, 
                password=self.password,
                db=self.db
            )
            print("Successfully connected to the database.")
        except Exception as e:
            print(f"Failed to connect to the database: {e}")

    async def close(self):
        if self.conn:
            try:
                await self.conn.close()
                print("Database connection closed.")
            except Exception as e:
                print(f"Failed to close the database connection: {e}")

    async def execute(self, query, params=None):
        if self.conn is None:
            await self.connect()
            return
        async with self.conn.cursor() as cursor:
            await cursor.execute(query, params)
            await self.conn.commit()

    async def fetchall(self, query, params=None):
        async with self.conn.cursor() as cursor:
            await cursor.execute(query, params)
            result = await cursor.fetchall()
            return result

    async def fetchone(self, query, params=None):
        async with self.conn.cursor() as cursor:
            await cursor.execute(query, params)
            result = await cursor.fetchone()
            return result

    async def register_user(self, user_id, username, first_name, last_name, reg_date, status='В меню'):
        try:
            query = """
            INSERT INTO Users (id, username, first_name, last_name, reg_date, status) 
            VALUES (%s, %s, %s, %s, %s, %s) AS new
            ON DUPLICATE KEY UPDATE 
                username = new.username, 
                first_name = new.first_name, 
                last_name = new.last_name,
                reg_date = new.reg_date,
                status = new.status;
            """
            # Предполагаем, что reg_date уже в правильном формате
            await self.execute(query, (
            user_id, username, first_name, last_name, reg_date.strftime("%Y-%m-%d"), status))
        except Exception as e:
            print(f"Failed to register user: {e}")

    async def queue_user_add(self, user_id):
        if self.conn is None:
            await self.connect()

        try:
            query = """
            INSERT INTO Queue (user_id) VALUES (%s)
            """
            await self.execute(query, (user_id,))
            print("User added to the queue successfully.")
        except Exception as e:
            print(f"Failed to add user to the queue: {e}")
