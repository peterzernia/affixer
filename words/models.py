from django.db import models


class Word(models.Model):
    '''
    Describes the words of the English language as basic parts of speech.
    '''
    word = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.word
