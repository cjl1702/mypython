#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import db

class User(db.Document):
    # 字段
    name = db.StringField()
    gender = db.StringField()

    def __str__(self):
        return "name:{}-gender:{}".format(self.name,self.gender)