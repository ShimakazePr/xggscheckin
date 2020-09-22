# -*- coding:utf-8 -*-
from flask import jsonify, request, current_app
from sqlalchemy import text

from . import api
from ..models import Info, db


@api.route('/gets/getCheckInNum', methods=['GET'])
def getCheckInNum():
    num = Info.query.filter_by(check_in=True).all()
    return jsonify({'value': len(num)})


@api.route('/gets/getCheckInInfo', methods=['GET'])
def getCheckInInfo():
    info = Info.query.filter_by(check_in=True).all()
    json_data = []
    for i in range(0, int(len(info) / 3)):
        json_data.append({'name1': info[3 * i].name, 'name2': info[3 * i + 1].name, 'name3': info[3 * i + 2].name})
    if len(info) % 3 == 2:
        json_data.append({'name1': info[-(len(info) % 3)].name, 'name2': info[-((len(info) % 3)-1)].name})
    elif len(info) % 3 == 1:
        json_data.append({'name1': info[-(len(info) % 3)].name})

    return jsonify(json_data)


@api.route('/gets/getCheckByName/<name>', methods=['GET'])
def getCheckByName(name):
    name_check = Info.query.filter_by(name=name).first()
    if name_check is not None:
        return jsonify({'code': 1, 'message': '该名字已存在'})
    else:
        return jsonify({'code': 0, 'message': '该名字不存在'})
