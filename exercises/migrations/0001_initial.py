# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Discipline'
        db.create_table(u'exercises_discipline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'exercises', ['Discipline'])

        # Adding model 'ExoAlias'
        db.create_table(u'exercises_exoalias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercises.Discipline'])),
            ('exo_number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'exercises', ['ExoAlias'])

        # Adding unique constraint on 'ExoAlias', fields ['discipline', 'exo_number']
        db.create_unique(u'exercises_exoalias', ['discipline_id', 'exo_number'])

        # Adding model 'Exercise'
        db.create_table(u'exercises_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercises.Discipline'], null=True)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercises.ExoAlias'], null=True)),
            ('exo_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'exercises', ['Exercise'])

        # Adding model 'ExoResult'
        db.create_table(u'exercises_exoresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercises.Discipline'], null=True)),
            ('exo_number', self.gf('django.db.models.fields.IntegerField')()),
            ('result_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('try_number', self.gf('django.db.models.fields.IntegerField')(default='1')),
            ('result', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'exercises', ['ExoResult'])

        # Adding model 'ExoResultDetail'
        db.create_table(u'exercises_exoresultdetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercises.Discipline'], null=True)),
            ('exo_number', self.gf('django.db.models.fields.IntegerField')()),
            ('result_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('try_number', self.gf('django.db.models.fields.IntegerField')(default='1')),
            ('truth', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('exo_number_detail', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'exercises', ['ExoResultDetail'])


    def backwards(self, orm):
        # Removing unique constraint on 'ExoAlias', fields ['discipline', 'exo_number']
        db.delete_unique(u'exercises_exoalias', ['discipline_id', 'exo_number'])

        # Deleting model 'Discipline'
        db.delete_table(u'exercises_discipline')

        # Deleting model 'ExoAlias'
        db.delete_table(u'exercises_exoalias')

        # Deleting model 'Exercise'
        db.delete_table(u'exercises_exercise')

        # Deleting model 'ExoResult'
        db.delete_table(u'exercises_exoresult')

        # Deleting model 'ExoResultDetail'
        db.delete_table(u'exercises_exoresultdetail')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exercises.discipline': {
            'Meta': {'object_name': 'Discipline'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'exercises.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercises.Discipline']", 'null': 'True'}),
            'exo_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercises.ExoAlias']", 'null': 'True'})
        },
        u'exercises.exoalias': {
            'Meta': {'unique_together': "(('discipline', 'exo_number'),)", 'object_name': 'ExoAlias'},
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercises.Discipline']"}),
            'exo_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        u'exercises.exoresult': {
            'Meta': {'object_name': 'ExoResult'},
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercises.Discipline']", 'null': 'True'}),
            'exo_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'result_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'try_number': ('django.db.models.fields.IntegerField', [], {'default': "'1'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'exercises.exoresultdetail': {
            'Meta': {'object_name': 'ExoResultDetail'},
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercises.Discipline']", 'null': 'True'}),
            'exo_number': ('django.db.models.fields.IntegerField', [], {}),
            'exo_number_detail': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'truth': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'try_number': ('django.db.models.fields.IntegerField', [], {'default': "'1'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['exercises']