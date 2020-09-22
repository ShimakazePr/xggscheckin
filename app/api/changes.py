# -*- coding:utf-8 -*-
from flask import jsonify, request, flash, render_template, current_app, redirect
from . import api
from ..models import Info, db
from datetime import datetime, timedelta


def delete(name):
    try:
        db.session.delete(name)
        db.session.commit()
        return True
    except Exception:
        return False


@api.route('/changes/deleteByName/<name>', methods=['GET', 'POST'])
def deleteByName(name):
    name = Info.query.filter_by(name=name).first()
    if name is None:
        return jsonify({'code': -1, 'message': '该名字不存在'})
    if delete(name):
        return jsonify({'code': 1, 'message': '删除成功，请重新添加'})
    else:
        return jsonify({'code': 0, 'message': '删除失败'})
