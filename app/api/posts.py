# -*- coding:utf-8 -*-
from flask import jsonify, request, current_app
from ..models import Info, db
from . import api
import os


@api.route('/posts/upLoadProfile', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        sex = data.get('sex')
        job_title = data.get('job_title')
        work_location_name = data.get('work_location_name')
        taxation_num = data.get('taxation_num')

        name_test = Info.query.filter_by(name=name).first()
        if name_test is not None:
            return jsonify({'code': 0, 'message': '已经报到'})

        info = Info(
            name=name,
            sex=sex,
            job_title=job_title,
            work_location_name=work_location_name,
            taxation_num=taxation_num,
            check_in=True
        )

        try:
            db.session.add(info)
            db.session.commit()
            return jsonify({'code': 1, 'message': '报到成功'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'code': -1, 'message': '报到失败'})
