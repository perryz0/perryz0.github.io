import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Perry Chien", url=os.getenv("URL"))

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
