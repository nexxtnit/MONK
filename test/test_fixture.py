# -*- coding: utf-8 -*-
#
# MONK automated test framework
#
# Copyright (C) 2013 DResearch Fahrzeugelektronik GmbH
# Written and maintained by MONK Developers <project-monk@dresearch-fe.de>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version
# 3 of the License, or (at your option) any later version.
#

from os.path import dirname, abspath
import inspect
import logging

from nose import tools as nt

from monk_tf import dev
from monk_tf import conn
from monk_tf import fixture

logger = logging.getLogger(__name__)
here = dirname(abspath(inspect.getfile(inspect.currentframe())))

def test_simple():
    """ create a simple Fixture instance
    """
    # set up + assert; make sure there are no exceptions
    sut = fixture.Fixture(__file__)

def test_simple_parse():
    """ create a config like dict and see if it gets parsed
    """
    # se
    # execute
    sut._logger.info("start execute")
    sut._initialize()
    # verify
    assert(isinstance(sut.devs[0], LoadedMock))
    assert sut.devs[0].name== test_name

class LoadedMock(object):
    def __init__(self, name="wrong", *args, **kwargs):
        self.name = name
