from django.db.models import CharField, Model, DateTimeField


class Tomatoes(Model):
    variety = CharField(max_length=30)
    name = CharField(max_length=30)
    age = CharField(max_length=4)
    climate = CharField(max_length=50)
    color = CharField(max_length=10)
    spot_size = CharField(max_length=10)
    spot_color = CharField(max_length=20)
    spot_dist = CharField(max_length=100)
    leaf_texture = CharField(max_length=100)
    overall_health = CharField(max_length=255)
    nearby_plant_observations = CharField(max_length=200)
    spore_fungal = CharField(max_length=5)  # yes or no
    onset_time = CharField(max_length=5)
    recent_pest_activities = CharField(max_length=255)
    disease_history = CharField(max_length=200)
    diagnosis = CharField(max_length=200)
    created_at = DateTimeField(auto_now_add=True)