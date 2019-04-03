from django.db import models
from lexical_categories.models import Adjective, Adverb, Noun, Verb


class Transformation(models.Model):
    '''
    Describes all of the Tranformations of a single root in their respective lexical categories.
    '''
    root = models.CharField(max_length=255, null=False, blank=False)
    adjectives = models.ForeignKey(
        Adjective, on_delete=models.CASCADE, null=True, blank=True)
    adverbs = models.ForeignKey(
        Adverb, on_delete=models.CASCADE, null=True, blank=True)
    nouns = models.ForeignKey(
        Noun, on_delete=models.CASCADE, null=True, blank=True)
    verbs = models.ForeignKey(
        Verb, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.root
