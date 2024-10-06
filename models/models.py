from flask_sqlalchemy import SQLAlchemy
import json
db = SQLAlchemy()


user_skills = db.Table('user_skills',
    db.Column('user_id', db.Integer, db.ForeignKey('user_profiles.user_id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skills.skill_id'), primary_key=True)
)

user_locations = db.Table('user_locations',
    db.Column('user_id', db.Integer, db.ForeignKey('user_profiles.user_id'), primary_key=True),
    db.Column('location_id', db.Integer, db.ForeignKey('locations.location_id'), primary_key=True)
)


job_skills = db.Table('job_skills',
    db.Column('job_id', db.Integer, db.ForeignKey('job_postings.job_id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey('skills.skill_id'), primary_key=True)
)


class Skill(db.Model):
    __tablename__ = 'skills'
    
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {
            'skill_id': self.skill_id,
            'skill_name': self.skill_name
        }


class Location(db.Model):
    __tablename__ = 'locations'
    
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(255), nullable=False, unique=True)

    def to_dict(self):
        return {
            'location_id': self.location_id,
            'location_name': self.location_name
        }


class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)
    desired_roles = db.Column(db.Text, nullable=False)  # 
    job_type = db.Column(db.String(50), nullable=False)

 
    skills = db.relationship('Skill', secondary=user_skills, backref=db.backref('user_profiles', lazy='dynamic'))
    locations = db.relationship('Location', secondary=user_locations, backref=db.backref('user_profiles', lazy='dynamic'))

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'skills': [skill.to_dict() for skill in self.skills],
            'experience_level': self.experience_level,
            'desired_roles': json.loads(self.desired_roles),
            'locations': [location.to_dict() for location in self.locations],
            'job_type': self.job_type
        }


class JobPosting(db.Model):
    __tablename__ = 'job_postings'
    
    job_id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'), nullable=False)  
    job_type = db.Column(db.String(50), nullable=False)
    experience_level = db.Column(db.String(50), nullable=False)


    required_skills = db.relationship('Skill', secondary=job_skills, backref=db.backref('job_postings', lazy='dynamic'))
    location = db.relationship('Location', backref='job_postings') 

    def to_dict(self):
        return {
            'job_id': self.job_id,
            'job_title': self.job_title,
            'company': self.company,
            'required_skills': [skill.to_dict() for skill in self.required_skills], 
            'location': self.location.location_name if self.location else None,
            'job_type': self.job_type,
            'experience_level': self.experience_level
        }
