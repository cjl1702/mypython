#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import app
print(app.path)
from flask import Flask,jsonify,request,abort
from datetime import datetime
from models.user import User
from models.device import Device1


@app.route('/api/v1/user',methods=['GET'])
def get_user():
    devices = Device1.objects().all()
    print(devices)

    user = User.objects(name='test2').first()
    print(user)

