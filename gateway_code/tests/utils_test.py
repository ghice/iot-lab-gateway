# -*- coding: utf-8 -*-

# This file is a part of IoT-LAB gateway_code
# Copyright (C) 2015 INRIA (Contact: admin@iot-lab.info)
# Contributor(s) : see AUTHORS file
#
# This software is governed by the CeCILL license under French law
# and abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info.
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.


# pylint: disable=missing-docstring

import unittest
from . import utils


class TestUtilsMock(unittest.TestCase):

    def test_read_config_mock(self):

        read_cfg = utils.read_config_mock('m3', test_key='value')
        self.assertEquals('m3', read_cfg('board_type'))

        # No robot by default
        self.assertRaises(IOError, read_cfg, 'robot')
        self.assertEquals(None, read_cfg('robot', None))

        # Extra key
        self.assertEquals('value', read_cfg('test_key'))
        self.assertEquals('value', read_cfg('test_key', 'default'))
