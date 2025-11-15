
import asyncio
import aiosqlite


async def async_fetch_users(db="users.db"):
    """Fetch all users asynchronously."""
    async with aiosqlite.connect(db) as conn:
        cursor = await conn.execute("SELECT * FROM users")
        return await cursor.fetchall()


async def async_fetch_older_users(db="users.db"):
    """Fetch users older than 40 asynchronously."""
    async with aiosqlite.connect(db) as conn:
        cursor = await conn.execute("SELECT * FROM users WHERE age > 40")
        return await cursor.fetchall()


async def fetch_concurrently():
    """Run both queries concurrently."""
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("All Users:")
    print(users)

    print("\nUsers Older Than 40:")
    print(older_users)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
