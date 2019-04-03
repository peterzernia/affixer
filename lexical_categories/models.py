from django.db import models
from words.models import Word


class Adjective(models.Model):
    '''
    Describes all of the Adjectives made from a single root.
    '''
    able = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="able_adjective")
    al = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="al_adjective")
    an = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="an_adjective")
    centric = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="centric_adjective")
    ed = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ed_adjective")
    ese = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ese_adjective")
    ful = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ful_adjective")
    ian = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ian_adjective")
    ic = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ic_adjective")
    ical = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ical_adjective")
    ish = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ish_adjective")
    ive = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ive_adjective")
    ist = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ist_adjective")
    less = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="less_adjective")
    like = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="like_adjective")
    ly = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ly_adjective")
    ous = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ous_adjective")
    proof = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="proof_adjective")
    ward = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ward_adjective")
    y = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="y_adjective")


class Adverb(models.Model):
    '''
    Describes all of the adverbs made from a single root.
    '''
    ly = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ly_adverb")
    ward = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ward_adverb")
    wards = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="wards_adverb")

class Noun(models.Model):
    '''
    Describes all of the nouns made from a single root.
    '''
    age = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="age_noun")
    al = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="al_noun")
    an = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="an_noun")
    ance = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ance_noun")
    ancy = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ancy_noun")
    ation = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ation_noun")
    ee = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ee_noun")
    ence = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ence_noun")
    ency = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ency_noun")
    ese = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ese_noun")
    er = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="er_noun")
    ess = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ess_noun")
    ette = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ette_noun")
    ful = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ful_noun")
    hood = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="hood_noun")
    ian = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ian_noun")
    ing = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ing_noun")
    ism = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ism_noun")
    ist = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ist_noun")
    ity = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ity_noun")
    ment = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ment_noun")
    ness = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ness_noun")
    ocracy = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ocracy_noun")
    ology = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ology_noun")
    pr = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="or_noun")
    phile = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="phile_noun")
    phobe = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="phobe_noun")
    phobia = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="phobia_noun")
    ship = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ship_noun")


class Verb(models.Model):
    '''
    Describes all of the verbs made from a single root.
    '''
    ate = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ate_verb")
    en = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="en_verb")
    ify = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ify_verb")
    ise = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ise_verb")
    ize = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True, related_name="ize_verb")