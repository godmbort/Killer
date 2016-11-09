from __future__ import unicode_literals
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models


class Label(models.Model):
	label = models.CharField(max_length=50)
	img = models.CharField(max_length=200)  # redo

	def __unicode__(self):
		return self.label

	class Meta:
		ordering = ('label', )

class Article(models.Model):
	title = models.CharField(max_length=60)
	text = models.CharField(max_length=20000)
	preview = models.CharField(max_length=200)
	img = models.CharField(max_length=200) # path to img via string. redo in next versions
	labes = models.ManyToManyField(Label, blank=True)

	def __unicode__(self):
		return self.title

	def set_preview(self):
		self.preview = self.text[:200]

	def save(self, *args, **kwargs):
		self.set_preview()
		super(Article, self).save(*args, **kwargs)