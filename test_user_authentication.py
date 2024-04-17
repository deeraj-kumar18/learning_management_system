import unittest
from app import app

class UserAuthenticationTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_successful_login(self):
        response = self.app.post('/login', data={'username': 'test_user', 'password': 'test_password'}, follow_redirects=True)
        self.assertIn(b'Welcome, test_user!', response.data)

    def test_failed_login(self):
        response = self.app.post('/login', data={'username': 'invalid_user', 'password': 'invalid_password'}, follow_redirects=True)
        self.assertIn(b'Invalid username or password', response.data)

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
