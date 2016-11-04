#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-04 10:47:22
# @Author  : whchen (chenweihong@gzyouai.com)
# @Link    : 
# @Version : $Id$

import os
import threading
import functools

def async(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.setDaemon(True)
        my_thread.start()
    return wrapper
