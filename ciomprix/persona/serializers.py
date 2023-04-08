from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'id', 
            'first_name', 
            'last_name', 
            'birth_date', 
            'rol', 
            'identificacion', 
            'telefono',
            'email',
            'username',
            'password'
            )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
          password = validated_data['password']
          del validated_data['password']
          user = Persona.objects.create(**validated_data)
          user.set_password(password) 
          user.save()



          return user
