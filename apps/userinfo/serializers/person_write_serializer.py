from rest_framework import serializers
from django.core.exceptions import ValidationError
from apps.userinfo.models.person import Person


class PersonWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
    
    def validate_full_name(self, name):
        if name:
            is_valid_name = len(name) > 2
            if not is_valid_name:
                raise ValidationError("Ensure this field has no less than 3 characters.")
            return name
    
    def validate_name(self, first_name):
        if first_name:
            is_valid_name_caracters = len(first_name) > 2
            if not is_valid_name_caracters:
                raise ValidationError("Ensure this field has no less than 3 characters.")
            return first_name
        
