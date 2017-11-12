import os
import shutil
import json
import unittest


from model import (
    Ocean,
    Shark,
    Guppies,
    init,
    generate_ocean,
    read_ocean,
    write_ocean
)


class TestWork(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.makedirs('tmp', exist_ok=True)

        with open('tmp/config.json', 'w') as f:
            config_json = {
                "size": 100000,
                "shark": {
                    "fullness": 100000,
                    "reproduction": 100000,
                    "life": 100000
                },
                "guppies": {
                    "reproduction": 100000,
                    "life": 100000
                }
            }
            str_json = json.dumps(config_json)
            f.write(str_json)

    def test_init(self):
        init('tmp/config.json')

        with self.subTest(i=0):
            self.assertEqual(Ocean.DEFAULT_SIZE, 100000)

        with self.subTest(i=1):
            self.assertEqual(Shark.FULLNESS, 100000)

        with self.subTest(i=2):
            self.assertEqual(Shark.REPRODUCTION, 100000)

        with self.subTest(i=3):
            self.assertEqual(Shark.LIFE, 100000)

        with self.subTest(i=4):
            self.assertEqual(Guppies.REPRODUCTION, 100000)

        with self.subTest(i=5):
            self.assertEqual(Guppies.LIFE, 100000)

    def test_read_write(self):
        ocean = generate_ocean(10)

        write_ocean('tmp/result.txt', ocean)
        new_ocean = read_ocean('tmp/result.txt', ocean.size)

        for idx, (c1, c2) in enumerate(zip(ocean, new_ocean)):
            with self.subTest(i=idx):
                self.assertIs(c1.__class__, c2.__class__)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('tmp'):
            shutil.rmtree('tmp')


if __name__ == '__main__':
    unittest.main()
