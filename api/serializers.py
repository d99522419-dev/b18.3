from rest_framework import serializers

from main.models import Student,Teacher,Group


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"  


class GroupModelSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Group
        fields = "__all__"
        

class StudentSerializer(serializers.Serializer):
    avatar = serializers.ImageField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    phone_number = serializers.CharField()
    parent_phone_number = serializers.CharField()
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
                                
    def create(self, validated_data):
        Student.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.parent_phone_number = validated_data.get('parent_phone_number', instance.parent_phone_number)
        instance.group = validated_data.get('group', instance.group)
        instance.save()
        return instance

class TeacherSerializer(serializers.Serializer):
    avatar = serializers.ImageField()
    first_name = serializers.CharField()
    direction = serializers.ChoiceField(choices=Teacher.DIRECTION_CHOICES)
    
    def create(self, validated_data):
        Teacher.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.direction = validated_data.get('direction', instance.direction)
        instance.save()
        return instance
        
class GroupSerializer(serializers.Serializer):
    name = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    course = serializers.CharField()
    students_count = serializers.IntegerField()
    contract = serializers.FloatField()
    mentor = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    created_at = serializers.DateTimeField()
    
    def create(self, validated_data):
        Group.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.course = validated_data.get('course', instance.course)
        instance.students_count = validated_data.get('students_count', instance.students_count)
        instance.contract = validated_data.get('contract', instance.contract)
        instance.mentor = validated_data.get('mentor', instance.mentor)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()