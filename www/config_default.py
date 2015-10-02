#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Default configurations.
"""

configs = {
    'debug': True,
    'db': {
        'host': '192.168.56.101',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
