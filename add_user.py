# -*- coding: utf-8 -*-
__author__ = 'cheungchan'
__date__ = '2018/12/7 20:35'
"""
添加用户的话使用docker exec -it threatbook_airflow_worker_1_e8a682d9cd70 python
进入环境, 然后复制这里的代码, 粘贴到解释器执行.
"""
import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

user = PasswordUser(models.User())
user.username = 'new_user_name'
user.email = 'new_user_email@example.com'
user.password = 'set_the_password'
session = settings.Session()
session.add(user)
session.commit()
session.close()
