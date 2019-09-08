from django.db import models
#from django.conf import settings
#settings.configure()


class UserInput(models.Model):
    """
    Table to store information of user input.
    """
    PICTURE_TYPE = (
        (0, 'Mine'),
        (1, 'Other')
    )

    GENDER_TYPE = (
        (0, 'FeMale'),
        (1, 'Male')
    )

    ANGLE_TYPE = (
        (0, 'Front'),
        (1, 'Back')
    )

    user_id = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images')
    picture = models.IntegerField(choices=PICTURE_TYPE, default=0)
    gender = models.IntegerField(choices=GENDER_TYPE, default=0)
    angle = models.IntegerField(choices=ANGLE_TYPE, default=0)
    bust_waist = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    waist_hips = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    legs_body = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    body_waist = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    shoulder_hips = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_inputs'


class Post(models.Model):
    """
    """
    user_id = models.PositiveIntegerField(null=True)
    input_id = models.PositiveIntegerField(null=True)
    tag_person = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    age = models.CharField(max_length=256, null=True, blank=True)
    height = models.CharField(max_length=256, null=True, blank=True)
    weight = models.CharField(max_length=256, null=True, blank=True)
    race = models.CharField(max_length=256, null=True, blank=True)
    caption = models.CharField(max_length=256, null=True, blank=True)
    note = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'
