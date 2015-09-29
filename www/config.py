#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration
"""
import config_default


class Dict(dict):
    """
    Simple dict but support access as x.y style.
    """
    def __init__(self, names=(), values=(), **kwargs):
        super(Dict, self).__init__(**kwargs)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def to_dict(d):
    diction = Dict()
    for k, v in d.items():
        diction[k] = to_dict(v) if isinstance(v, dict) else v
    return diction


configs = config_default.configs
try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    import config_override
    pass
configs = to_dict(configs)
