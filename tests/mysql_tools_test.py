import unittest
from unittest.mock import Mock
from qiyue_db import export, shardsql


class TestMysql_Tools(unittest.TestCase):
    def setUp(self):
        self.mock_dbhelper = Mock()

    def test_if_export_work_right(self):
        self.mock_dbhelper.queryall = Mock(return_value=(
            (1, ),
            (2, ), ))
        res = export(self.mock_dbhelper)(lambda: "select all")()
        self.assertEqual(res, ((1, ), (2, )))
        self.assertEqual(len(res), 2)
        res = export(
            self.mock_dbhelper)(lambda: ["select all", "select all"])()
        self.assertEqual(res, ((1, ), (2, ), (1, ), (2, )))
        self.assertEqual(len(res), 4)

    def test_if_sharsql_work_right(self):
        self.assertEqual(shardsql(2)(lambda: "a{}")(), ["a00", "a01"])
        self.assertEqual(shardsql(range(2))(lambda: "a{}")(), ["a00", "a01"])
