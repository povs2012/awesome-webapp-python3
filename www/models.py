#!/usr/bin/env python3   
# -*- coding: utf-8 -*-
"""Models for user, blog, comment"""

import orm
import time
import uuid


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(orm.Model):
    __table__ = 'users'

    id = orm.StringField(is_primary_key=True, default=next_id(), ddl='varchar(50)')
    email = orm.StringField(ddl='varchar(50)')
    passwd = orm.StringField(ddl='varchar(50)')
    admin = orm.BooleanField()
    name = orm.StringField(ddl='varchar(50)')
    image = orm.StringField(ddl='varchar(500)')
    created_at = orm.FloatField(default=time.time())


class Blog(orm.Model):
    __table__ = 'blogs'

    id = orm.StringField(is_primary_key=True, default=next_id(), ddl='varchar(50)')
    user_id = orm.StringField(ddl='varchar(50)')
    user_name = orm.StringField(ddl='varchar(50)')
    user_image = orm.StringField(ddl='varchar(500)')
    name = orm.StringField(ddl='varchar(50)')
    summary = orm.StringField(ddl='varchar(200)')
    content = orm.TextField()
    created_at = orm.FloatField(default=time.time())


class Comment(orm.Model):
    __table__ = 'comments'

    id = orm.StringField(is_primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = orm.StringField(ddl='varchar(50)')
    user_id = orm.StringField(ddl='varchar(50)')
    user_name = orm.StringField(ddl='varchar(50)')
    user_image = orm.StringField(ddl='varchar(500)')
    content = orm.TextField()
    created_at = orm.FloatField(default=time.time)
user = User(id=123, name='Jim')
user.insert()
users = User.find_all()
