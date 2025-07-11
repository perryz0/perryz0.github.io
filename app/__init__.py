import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306)

# print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

# TimelinePost.drop_table()
# TimelinePost.create_table()


@app.route('/')
def index():
    return render_template('index.html', title="Perry Chien", url=os.getenv("URL"))

@app.route('/experiences')
def experiences():
    work_experiences = [
        {
            'job_title': 'Production Engineering Fellow',
            'company': 'Meta x MLH',
            'duration': 'June 2025 - Sep 2025',
            'description': 'DevOps and production engineering'
        },
        {
            'job_title': 'Firmware Engineer Intern',
            'company': 'Delta Electronics',
            'duration': 'May 2025 - Aug 2025',
            'description': 'Field applications engineering for Azure datacenters'
        },
        {
            'job_title': 'Undergraduate Researcher',
            'company': 'UW Computer Systems Lab',
            'duration': 'May 2025 - Present',
            'description': 'Domain-specific language for distributed systems scheduling'
        },
        {
            'job_title': 'Software Engineer',
            'company': 'Husky Robotics',
            'duration': 'Jan 2023 - Present',
            'description': 'Hardware- and software-defined networking and communications for UAVs'
        },
        {
            'job_title': 'Engineering Intern',
            'company': 'Taiwan Semiconductor Manufacturing',
            'duration': 'June 2024 - Sep 2024',
            'description': 'Thin-films physical vapor deposition'
        }
    ]
    return render_template('experiences.html', title="Work Experiences", work_experiences=work_experiences, url=os.getenv("URL"))

@app.route('/education')
def educations():
    educations = [
        {
            'school': 'University of Washington',
            'location': 'Seattle, WA',
            'degree': 'B.S. in Computer Science',
            'duration': 'Sep 2022 - Jun 2026'
        },
        {
            'school': 'American High School',
            'location': 'Fremont, CA',
            'degree': 'High School Diploma',
            'duration': 'Sep 2020 - Jun 2022'
        },
        {
            'school': 'SMIC Private School',
            'location': 'Shanghai, China',
            'degree': 'N/A',
            'duration': 'Sep 2018 - Jun 2020'
        }
    ]
    return render_template('education.html', title="Education", educations=educations, url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    hobby_items = [
        {'title': 'Soccer', 'img': 'soccer.jpg'},
        {'title': 'Music', 'img': 'music.jpg'},
        {'title': 'Video Games', 'img': 'video_games.png'}
    ]
    return render_template('hobbies.html', title="Hobbies", hobbies=hobby_items, url=os.getenv("URL"))

@app.route('/travel')
def travel():
    locations = [
        {"name": "Shanghai, China", "lat": 31.2304, "lon": 121.4737},
        {"name": "Osaka, Japan", "lat": 34.6937, "lon": 135.5023},
        {"name": "Seattle, Washington", "lat": 47.6062, "lon": -122.3321},
        {"name": "Portland, Oregon", "lat": 45.5051, "lon": -122.6750},
        {"name": "Los Angeles, CA", "lat": 34.0522, "lon": -118.2437},
        {"name": "San Francisco, CA", "lat": 37.7749, "lon": -122.4194},
        {"name": "Prague, Czechia", "lat": 50.0755, "lon": 14.4378},
        {"name": "Brno, Czechia", "lat": 49.1951, "lon": 16.6068},
        {"name": "Dresden, Germany", "lat": 51.0504, "lon": 13.7373},
        {"name": "Frankfurt, Germany", "lat": 50.1109, "lon": 8.6821},
        {"name": "Salzburg, Austria", "lat": 47.8095, "lon": 13.0550},
        {"name": "Vienna, Austria", "lat": 48.2082, "lon": 16.3738},
        {"name": "Zurich, Switzerland", "lat": 47.3769, "lon": 8.5417},
        {"name": "Paris, France", "lat": 48.8566, "lon": 2.3522},
        {"name": "Rome, Italy", "lat": 41.9028, "lon": 12.4964},
        {"name": "Vancouver, Canada", "lat": 49.2827, "lon": -123.1207},
        {"name": "Xi'an, China", "lat": 34.3416, "lon": 108.9402},
        {"name": "Beijing, China", "lat": 39.9042, "lon": 116.4074},
        {"name": "Qingdao, China", "lat": 36.0671, "lon": 120.3826},
        {"name": "Singapore, Singapore", "lat": 1.3521, "lon": 103.8198},
        {"name": "Bali, Indonesia", "lat": -8.4095, "lon": 115.1889},
        {"name": "Bangkok, Thailand", "lat": 13.7563, "lon": 100.5018},
        {"name": "Tokyo, Japan", "lat": 35.6762, "lon": 139.6503},
        {"name": "Taipei, Taiwan", "lat": 25.0330, "lon": 121.5654},
        {"name": "Guangzhou, China", "lat": 23.1291, "lon": 113.2644},
        {"name": "Taichung, Taiwan", "lat": 24.1477, "lon": 120.6736},
        {"name": "Vaduz, Liechtenstein", "lat": 47.1410, "lon": 9.5215},
        {"name": "Chengdu, Sichuan", "lat": 30.5728, "lon": 104.0668},
        {"name": "Hong Kong, China", "lat": 22.3193, "lon": 114.1694},
        {"name": "Hangzhou, China", "lat": 30.2741, "lon": 120.1551}
    ]
    return render_template('travel.html', title="Travel Map", locations=locations, url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
