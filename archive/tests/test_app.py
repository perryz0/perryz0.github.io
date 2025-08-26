import unittest
import os
import re
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def make_nav_category_regex(self, category):
        """Helper to check if a button or anchor tag containing
            the 'category' text exists.
        """
        return re.compile(
            fr'<(a|button)\b[^>]*>(\s*{re.escape(category)}\s*)</\1>',
            re.IGNORECASE
        )

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        # Assert correct title
        assert '<title>Perry\'s MLH Portfolio!</title>' in html

        # Assert a stylesheet is applied
        assert re.search(r'<link\b[^>]*\brel=["\']stylesheet["\'][^>]*>', html)

        # Assert each link is present (presumably in the navbar)
        categories = ['Experiences', 'Education', 'Hobbies', 'Travel', 'Timeline']
        for category in categories:
            pattern = self.make_nav_category_regex(category)
            assert re.search(pattern, html)


    def test_timeline(self):
        # ----- Test POST and GET API endpoints -----
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        
        # Assert response data contains an empty list of json
        assert 'timeline_posts' in json
        assert len(json['timeline_posts']) == 0

        # Assert a few posts can be made
        post_data = [
            { 'name': 'David', 'email': 'david@example.com', 'content': 'lorem ipsum 123' },
            { 'name': 'David2', 'email': 'david2@example.com', 'content': 'message' },
            { 'name': 'David123', 'email': 'david123@example.com', 'content': 'HELLO' }
        ]

        for data in post_data:
            created_post = self.client.post('/api/timeline_post', data=data)
            created_post_json = created_post.get_json()
            for attr, expected_val in data.items():
                assert created_post_json[attr] == expected_val

        # Assert new posts have persisted
        response_new_posts = self.client.get('/api/timeline_post')
        json_new_posts = response_new_posts.get_json()
        data_new_posts = json_new_posts['timeline_posts']
        assert len(data_new_posts) == 3

        # Compare fetched post data to expected data
        for i in range(len(post_data)):
            # Get post by inedex
            for posted_data in data_new_posts:
                if posted_data['id'] == i+1:
                    target_data = posted_data
                    break
            for attr, expected_val in post_data[i].items():
                assert target_data[attr] == expected_val

        # ----- Test HTML -----
        response_timeline_page = self.client.get('/timeline')
        assert response_timeline_page.status_code == 200
        html = response_timeline_page.get_data(as_text=True)

        # Assert a "submit" button exists
        assert re.search(r'<button\b[^>]*\btype=["\']submit["\'][^>]*>', html)
    
    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={
            "email": "john@example.com", "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe", "email": "john@example.com", "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
