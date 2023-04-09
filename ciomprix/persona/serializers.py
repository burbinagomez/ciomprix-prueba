from rest_framework import serializers
from .models import Persona

class BaseSerializer(serializers.ModelSerializer):
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
            'password',
            )

class CreatePersonaSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        extra_kwargs = {
            'email': {'required': True}, 
            'username': {'required': False}, 
            'identificacion': {'required': True},
            'password': {'required': True, 'write_only': True}
        }

    def create(self, validated_data):
          password = validated_data['password']
          validated_data['username'] = validated_data['email']
          del validated_data['password']
          user = Persona.objects.create(**validated_data)
          user.set_password(password) 
          user.save()
          return user   
    
class PersonaSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        extra_kwargs = {
             'identificacion': {'required': False},
             'username': {'required': False},
             'password': {'required': False, 'write_only': True}
             }
        read_only_fields = ('id',)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.rol = validated_data.get('rol', instance.rol)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()
        return instance