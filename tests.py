import unittest 

from get_hash import take_head 
from clone_dir import get_clone_dir


class TestTake(unittest.IsolatedAsyncioTestCase):
    async def test_wrong(self):
        res = await take_head('.git/hooks/', 'HEAD')
        self.assertEqual(res, None)

    async def test_nothing(self):
        res = await take_head('', '')
        self.assertEqual(res, None)

    async def test_actual(self):
        res = await take_head('.git/', 'HEAD')
        self.assertIsNotNone(res)
        if res:
            self.assertEqual(len(res), 41)


class TestClone(unittest.IsolatedAsyncioTestCase):
    def test_get_wrong(self):
        self.assertRaises(FileNotFoundError, get_clone_dir, 'wrong_file')

