"""Take 3 cat HEAD file repo and hash sha256."""
import asyncio 
import aiofiles
import hashlib


async def take_head(clone_dir: str, head: str = '', last: bool = False) -> str | None:
    """Take clone_dir and head. Return str or None, print except."""
    try:
        async with aiofiles.open(clone_dir + head, 'r') as cat:
            read_cat = await cat.readline() 
            if last:
                return read_cat
            else:
                result = await take_head(clone_dir, head=read_cat.split()[1], last = True)
                return result
    except FileNotFoundError as e:
        print(e)


async def main(clone_dir_git: str, head: str) -> None:
    """create 3 tasks, for entry param clone_dir_git, head, return None"""
    task_one = asyncio.create_task(take_head(clone_dir_git, head))
    task_two = asyncio.create_task(take_head(clone_dir_git, head))
    task_three = asyncio.create_task(take_head(clone_dir_git, head))

    await task_one
    await task_two
    await task_three

    head_data_book = (task_one.result(), task_two.result(), task_three.result())
    for head_data in head_data_book:
        if head_data:
            print(hashlib.sha256(head_data.encode()).hexdigest())  

