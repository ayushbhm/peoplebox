from flask import Blueprint, request, jsonify
from models.models import db, JobPosting
from sqlalchemy.exc import SQLAlchemyError

job_bp = Blueprint('job', __name__)

@job_bp.route('/recommend_jobs', methods=['POST'])
def recommend_jobs():
    try:
        data = request.json
        if not data or 'name' not in data or 'skills' not in data:
            return jsonify({'error': 'Invalid input: name and skills are required.'}), 400

        user_name = data['name']
        user_skills = set(data['skills'])  
        experience_level = data.get('experience_level', None)
        desired_roles = set(data['preferences'].get('desired_roles', []))
        preferred_locations = set(data['preferences'].get('locations', []))
        job_type = data['preferences'].get('job_type', None)

        job_postings = JobPosting.query.all()
        recommendations = []
        for job in job_postings:
            score = 0

            if job.job_title in desired_roles:
                score += 2

            if job.job_type == job_type:
                score += 1

            if job.location.location_name in preferred_locations:
                score += 1

            required_skills = set(skill.skill_name for skill in job.required_skills)
            matching_skills = user_skills.intersection(required_skills)
            if matching_skills:
                score += len(matching_skills)

            if job.experience_level == experience_level:
                score += 1

            if score > 0:
                recommendations.append({
                    "job_title": job.job_title,
                    "company": job.company,
                    "location": job.location.location_name,
                    "job_type": job.job_type,
                    "required_skills": list(required_skills),
                    "experience_level": job.experience_level,
                    "score": score
                })

        recommendations.sort(key=lambda x: x['score'], reverse=True)

        if not recommendations:
            return jsonify({
                'message': 'No suitable job postings found. Consider broadening your search criteria.',
                
            }), 200
        print(recommendations)

        return jsonify(recommendations), 200

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': 'Database error occurred: ' + str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500
