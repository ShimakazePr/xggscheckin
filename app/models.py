# -*- coding:utf-8 -*-
from flask import current_app
from . import db
from datetime import datetime


class Info(db.Model):
    __tablename__ = 'Info'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64), index=True)
    sex = db.Column(db.String(8))
    job_title = db.Column(db.String(32))
    work_location_name = db.Column(db.String(64))
    taxation_num = db.Column(db.String(64))
    check_in = db.Column(db.Boolean, default=False, index=True)

    def to_json(self):
        json_data = {
            'id': self.id,
            'name': self.name,
            'sex': self.sex,
            'job_title': self.job_title,
            'work_location_name': self.work_location_name,
            'taxation_num': self.taxation_num,
            'check_in': self.check_in
        }
        return json_data
