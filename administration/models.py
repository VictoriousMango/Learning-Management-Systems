from django.db import models

# Create your models here.
'''
Model Info
 - Users: (user_id, name, email, role, password) 
 - Courses: (course_id, title, description, course_incharge_id) 
 - Enrollments: (enrollment_id, user_id, course_id, status) 
 - Assessments: (assessment_id, course_id, type, max_score) 
 - Submissions: (submission_id, user_id, assessment_id, score)
'''
class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    role = models.CharField(max_length=100)
    enrolments = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    course_incharge_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Assessments(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    max_score = models.IntegerField()

class Submissions(models.Model):
    submission_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    assessment_id = models.ForeignKey(Assessments, on_delete=models.CASCADE)
    score = models.IntegerField()