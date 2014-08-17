# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

import os

from django.db import models
from django.contrib.auth.models import User


@python_2_unicode_compatible
class Discipline(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        name = self.name
        return name

    class Meta:
        verbose_name = u"1. Matière"


@python_2_unicode_compatible
class ExoAlias(models.Model):
    title = models.CharField(max_length=50, null=True)
    discipline = models.ForeignKey(Discipline)
    exo_number = models.IntegerField()

    class Meta:
        unique_together = (("discipline", "exo_number"))
        verbose_name = "2. Identifiant des exercice"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        query = ExoAlias.objects.filter(discipline=self.discipline).order_by("-exo_number").values_list('exo_number', flat=True)
        if query:
            query = query[0]
        else:
            query = 0
        self.exo_number = query + 1
        super(ExoAlias, self).save(*args, **kwargs)


class Exercise(models.Model):
    discipline = models.ForeignKey(Discipline, null=True, blank=True)
    title = models.ForeignKey(ExoAlias, null=True)
    exo_number = models.IntegerField(null=True, blank=True)
    question = models.TextField()
    answer = models.CharField(max_length=120)
    is_published = models.BooleanField(default=True)
    file = models.FileField(upload_to='static/exercises', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.exo_number = self.title.exo_number
        self.discipline = self.title.discipline
        super(Exercise, self).save(*args, **kwargs)

    def question_as_list(self):  # used to send question to a checkbox template
        return self.question[:-1].split(';')

    def answer_to_formatedanswer(self):  # removed the ';' in the end if checkbox
        formatedanswer = self.answer[:]
        if formatedanswer[-1] == ';':
            formatedanswer = formatedanswer[:-1].split(';')
            formatedanswer = ' et '.join(formatedanswer)
        return formatedanswer

    def file_extension(self):
        name, extension = os.path.splitext(self.file.name)
        if extension in ('.jpg', '.jpeg', '.png', '.gif'):
            return 'image'
        if extension in ('.wav', '.mp3'):
            return 'audio'
        if extension in ('.pdf'):
            return 'pdf'
        else:
            return extension

    class Meta:
        verbose_name = "3. Liste des exercice"

""" classes containing the result. Exoresult: with the total score for one exercise,
                                   Exoresultdetail: score (bool) for each question inside exercise."""


class Exo(models.Model):
    user = models.ForeignKey(User)
    discipline = models.ForeignKey(Discipline, null=True)
    exo_number = models.IntegerField()
    result_date = models.DateTimeField(null=True)
    try_number = models.IntegerField(default='1')

    class Meta:
        abstract = True


class ExoResult(Exo):
    result = models.IntegerField(null=True)

    def result_to_letter(self):
        if self.result < 50:
            return 'C'
        elif self.result < 75:
            return 'B'
        else:
            return 'A'


class ExoResultDetail(Exo):
    truth = models.BooleanField(default=False)
    exo_number_detail = models.IntegerField(default=0)


