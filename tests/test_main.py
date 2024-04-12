import unittest
from flask_testing import TestCase
from main import app, months

class FlaskTestCase(TestCase):

    def create_app(self):
        # Configure the Flask app for testing
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Clear and reset the months list before each test
        global months
        months.clear()
        months.extend([
            {"id": 1, "name": "January"}, {"id": 2, "name": "February"},
            {"id": 3, "name": "March"}, {"id": 4, "name": "April"},
            {"id": 5, "name": "May"}, {"id": 6, "name": "June"},
            {"id": 7, "name": "July"}, {"id": 8, "name": "August"},
            {"id": 9, "name": "September"}, {"id": 10, "name": "October"},
            {"id": 11, "name": "November"}, {"id": 12, "name": "December"}
        ])

    def test_get_all_months(self):
        # Fetch all months and verify the count
        response = self.client.get("/months")
        print("State before GET all months test: ", months)  # Debug print
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 12)

    def test_post_month(self):
        # Post a new month and verify
        response = self.client.post("/months", json={"id": 13, "name": "TestMonth"})
        print("State before POST new month test: ", months)  # Debug print
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'success': True})

    def test_put_month(self):
        # Ensure the month exists and then update it
        print("State before PUT month test: ", months)  # Debug print
        response = self.client.put("/months/1", json={"name": "Januarie"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Januarie")

    def test_delete_month(self):
        # Ensure the month exists and then delete it
        print("State before DELETE month test: ", months)  # Debug print
        response = self.client.delete("/months/1")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
