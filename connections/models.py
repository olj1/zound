from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Language(models.Model):
    english_name = models.CharField(max_length=100)
    iso_639_1_code = models.CharField(max_length=7, null=True)
    iso_639_2_code = models.CharField(max_length=7, null=True)
    iso_693_3_type = models.CharField(max_length=20, null=True)
    iso_693_3_code = models.CharField(max_length=7, null=True) 
    def __str__(self):
        return f"{self.english_name}"

class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='words')
    text = models.CharField(max_length=250)
    is_word = models.BooleanField(default=True)
    number_of_syllables = models.IntegerField()
    english_transcription_system = models.CharField(max_length=250)
    transcription = models.TextField()
    international_phonetic_alphabet = models.TextField()

class Connection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='connections')
    query = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='queries')
    result = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='results')
    phonetic_relationship = models.BooleanField()
    semantic_relationship = models.BooleanField()



