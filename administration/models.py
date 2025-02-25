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
    enrolments = models.JSONField(default=dict, null=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user_id

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    LandingPicture = models.CharField(max_length=100, default="Null")
    description = models.TextField()
    resources = models.JSONField(default=None)
    course_incharge_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_id} : {self.title}"

class Assessments(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    questions = models.JSONField(default=None) # List of questions
    max_score = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.assessment_id} : {self.course_id}"

class Submissions(models.Model):
    submission_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    assessment_id = models.ForeignKey(Assessments, on_delete=models.CASCADE)
    response_data = models.JSONField(default=None) # List of responses
    score = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.submission_id} : {self.assessment_id} : {self.user_id}"