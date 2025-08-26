import unittest
from peewee import *
from app import TimelinePost

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

MODELS = [TimelinePost]

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1

        first_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert first_post.id == 2

        expected_posts = [
            { 'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'content': 'Hello world, I\'m John!'},
            { 'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com', 'content': 'Hello world, I\'m Jane!' },
        ]

        # Assert each attribute is as expected
        for expected_post in expected_posts:
            post_obj = TimelinePost.get_by_id(expected_post['id'])
            for attr, expected_value in expected_post.items():
                assert getattr(post_obj, attr) == expected_value
                