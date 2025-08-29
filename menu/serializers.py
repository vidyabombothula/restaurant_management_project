from rest_framework import seializers

class DishSerializer(seializers.Seializer):
    name=seializers.CharField()
    price=seializers.FloatField()