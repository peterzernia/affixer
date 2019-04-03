from rest_framework import serializers
from words.models import Word
from lexical_categories.models import Adjective, Adverb, Noun, Verb
from transformations.models import Transformation


class WordSerializer(serializers.ModelSerializer):
    '''
    Serializer for Word model.
    '''
    class Meta:
        model = Word
        fields = ('word',)


class AdjectiveSerializer(serializers.ModelSerializer):
    '''
    Serializer for Adjective model.
    '''
    able = WordSerializer()
    al = WordSerializer()
    an = WordSerializer()
    centric = WordSerializer()
    ed = WordSerializer()
    ese = WordSerializer()
    ful = WordSerializer()
    ian = WordSerializer()
    ic = WordSerializer()
    ical = WordSerializer()
    ish = WordSerializer()
    ive = WordSerializer()
    ist = WordSerializer()
    less = WordSerializer()
    like = WordSerializer()
    ly = WordSerializer()
    ous = WordSerializer()
    proof = WordSerializer()
    ward = WordSerializer()
    y = WordSerializer()

    class Meta:
        model = Adjective
        fields = (
            'able', 'al', 'an', 'centric', 'ed', 'ese', 'ful', 'ian', 
            'ic', 'ical', 'ish', 'ive', 'ish', 'ive', 'ist', 'less', 'like', 
            'ly', 'ous', 'proof', 'ward', 'y'
        )


class AdverbSerializer(serializers.ModelSerializer):
    '''
    Serializer for Adverb model.
    '''
    ly = WordSerializer()
    ward = WordSerializer()
    wards = WordSerializer()

    class Meta:
        model = Adverb
        fields = ('ly', 'ward', 'wards')


class NounSerializer(serializers.ModelSerializer):
    '''
    Serializer for Noun model.
    '''
    age = WordSerializer()
    al = WordSerializer()
    an = WordSerializer()
    ance = WordSerializer()
    ancy = WordSerializer()
    ation = WordSerializer()
    ee = WordSerializer()
    ence = WordSerializer()
    ency = WordSerializer()
    ese = WordSerializer()
    er = WordSerializer()
    ess = WordSerializer()
    ette = WordSerializer()
    ful = WordSerializer()
    hood = WordSerializer()
    ian = WordSerializer()
    ing = WordSerializer()
    ism = WordSerializer()
    ist = WordSerializer()
    ity = WordSerializer()
    ment = WordSerializer()
    ness = WordSerializer()
    ocracy = WordSerializer()
    ology = WordSerializer()
    pr = WordSerializer()
    phile = WordSerializer()
    phobe = WordSerializer()
    phobia = WordSerializer()
    ship = WordSerializer()

    class Meta:
        model = Noun
        fields = (
            'age', 'al', 'an', 'ance', 'ancy', 'ation', 'ee', 'ence', 'ency',
            'ese', 'er', 'ess', 'ette', 'ful', 'hood', 'ian', 'ing', 'ism', 
            'ist', 'ity', 'ment', 'ness', 'ocracy', 'ology', 'pr', 'phile',
            'phobe', 'phobia', 'ship'
        )


class VerbSerializer(serializers.ModelSerializer):
    '''
    Serializer for Verb model.
    '''
    ate = WordSerializer()
    en = WordSerializer()
    ify = WordSerializer()
    ise = WordSerializer()
    ize = WordSerializer()

    class Meta:
        model = Verb
        fields = ('ate', 'en', 'ify', 'ise', 'ize')


class TransformationSerializer(serializers.ModelSerializer):
    '''
    Serializer for Transformation model.
    '''
    adjectives = AdjectiveSerializer()
    adverbs = AdverbSerializer()
    nouns = NounSerializer()
    verbs = VerbSerializer()

    class Meta:
        model = Transformation
        fields = ('adjectives', 'adverbs', 'nouns', 'verbs',)
