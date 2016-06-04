# -*- coding: utf-8 -*-
"""
    monkeylive Tests
    ~~~~~~~~~~~~~~

    Tests the monkeylive application.

    :copyright: (c) 2016 by monkeylive
"""
import os
import monkeylive
import tempfile
import unittest

class monkeyliveTestCase(unittest.TestCase):
	def setUp(self):
		self.db_fd, monkeylive.app.config['DATABASE'] = tempfile.mkstemp()
		monkeylive.app.config['TESTING'] = True
		self.app = monkeylive.app.test_client()
		monkeylive.init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(monkeylive.app.config['DATABASE'])

	def test_home_page(self):
		rv = self.app.get('/')
		assert 'Hello my web' in rv.data


if __name__=='__main__':
	unittest.main()
