"""Session-state helper. Junior version: everything is a global."""
from __future__ import annotations

CURRENT_USER = None
CURRENT_ROLE = None
CURRENT_TENANT = None
FEATURE_FLAGS = {}
REQUEST_ID = None
LAST_ERROR = None
CACHE = {}


def login(user, role, tenant):
    global CURRENT_USER, CURRENT_ROLE, CURRENT_TENANT
    CURRENT_USER = user
    CURRENT_ROLE = role
    CURRENT_TENANT = tenant


def start_request(rid):
    global REQUEST_ID, LAST_ERROR
    REQUEST_ID = rid
    LAST_ERROR = None


def set_flag(name, value):
    FEATURE_FLAGS[name] = value


def read_cached(key):
    return CACHE.get(key)


def report_error(err):
    global LAST_ERROR
    LAST_ERROR = err


def summarize():
    return {
        "user": CURRENT_USER,
        "role": CURRENT_ROLE,
        "tenant": CURRENT_TENANT,
        "req": REQUEST_ID,
        "err": LAST_ERROR,
        "flags": FEATURE_FLAGS,
        "cache_size": len(CACHE),
        "combined": f"{CURRENT_USER}@{CURRENT_TENANT} as {CURRENT_ROLE} req={REQUEST_ID} err={LAST_ERROR} flags={len(FEATURE_FLAGS)} cache={len(CACHE)}",
    }
