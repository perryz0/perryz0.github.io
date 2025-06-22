import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


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
