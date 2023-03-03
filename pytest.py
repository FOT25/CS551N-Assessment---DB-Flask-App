import pytest
from flask import Flask, url_for
from flask_testing import TestCase
from wapp import app
from flask_mysqldb import MySQL

mysql = MySQL(app)

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        return app

    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute('TRUNCATE TABLE tbl_users')
            mysql.connection.commit()

    def test_index_page(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')

    def test_login_page_get(self):
        response = self.client.get(url_for('login_page'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('login.html')

    def test_login_page_post(self):
        data = {
            'fname': 'John',
            'lname': 'Doe'
        }
        response = self.client.post(url_for('login_page'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

    def test_register_page_get(self):
        response = self.client.get(url_for('register_page'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('register.html')

    def test_register_page_post(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'password': 'password'
        }
        response = self.client.post(url_for('register_page'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

    def test_home_page(self):
        response = self.client.get(url_for('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('home.html')

    def test_reset_page_get(self):
        response = self.client.get(url_for('reset_page'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('reset.html')

    def test_reset_page_post(self):
        data = {
            'email': 'john@example.com'
        }
        response = self.client.post(url_for('reset_page'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'success', response.data)

    def test_country_page(self):
        response = self.client.get(url_for('country_page'))
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('country.html')