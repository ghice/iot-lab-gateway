#! /usr/bin/env python
# -*- coding:utf-8 -*-

# pylint: disable=missing-docstring
# pylint: disable=protected-access
# pylint <= 1.3
# pylint: disable=too-many-public-methods
# pylint >= 1.4
# pylint: disable=too-few-public-methods
# pylint: disable=no-member

import mock
import unittest
from cStringIO import StringIO
import gateway_code.board_config as board_config


class TestGetClass(unittest.TestCase):

    @mock.patch('gateway_code.board_config.BoardConfig.find_board_type')
    def test_get_class(self, mock_func):
        mock_func.return_value = 'm3'
        self.assertEquals(
            board_config.BoardConfig().board_class.TTY, '/dev/ttyON_M3')

    @mock.patch('gateway_code.board_config.BoardConfig.find_board_type')
    def test_inexisting_class(self, mock_func):
        mock_func.return_value = 'unknown'
        with self.assertRaises(ValueError):
            board_config.BoardConfig()


class TestGetHostname(unittest.TestCase):

    def test_get_hosname(self):
        self.assertNotEquals('', board_config.BoardConfig().hostname())


class TestsBoardAndRobotType(unittest.TestCase):

    def setUp(self):
        board_config._BOARD_CONFIG = {}
        self.string_io = StringIO()

        self.open_mock_patcher = mock.patch('gateway_code.board_config.open',
                                            create=True)

        self.open_mock = self.open_mock_patcher.start()
        self.open_mock.return_value = self.string_io

    def tearDown(self):
        self.open_mock_patcher.stop()

    def test_board_type(self):

        self.string_io.write('M3\n')
        self.string_io.seek(0)
        board_config.BoardConfig()

        self.assertEquals('m3', board_config.BoardConfig().find_board_type())

        self.open_mock.side_effect = Exception()
        self.assertEquals('m3', board_config.BoardConfig().find_board_type())

    def test_board_type_not_found(self):
        self.open_mock.side_effect = IOError()
        with self.assertRaises(IOError):
            board_config.BoardConfig()

    def test_robot_type_not_found(self):
        self.open_mock.side_effect = IOError()
        with self.assertRaises(IOError):
            self.assertEquals(None, board_config.BoardConfig().robot_type())