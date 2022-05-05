from time import time

from flask import jsonify

from werkzeug.security import generate_password_hash


def send_result(data=None, message="OK", code=200, version=1, status=True):
    """
    Args:
        data: simple result object like dict, string or list
        message: message send to client, default = OK
        code: code default = 200
        version: version of api
    :param data:
    :param message:
    :param code:
    :param version:
    :param status:
    :return:
    json rendered sting result
    """
    res = {
        "jsonrpc": "2.0",
        "status": status,
        "code": code,
        "message": message,
        "data": data,
        "version": get_version(version)
    }

    return jsonify(res), 200


def send_error(data=None, message="Error", code=200, version=1, status=False):
    """

    :param data:
    :param message:
    :param code:
    :param version:
    :param status:
    :return:
    """
    res_error = {
        "jsonrpc": "2.0",
        "status": status,
        "code": code,
        "message": message,
        "data": data,
        "version": get_version(version)
    }
    return jsonify(res_error), code


def get_version(version):
    """
    if version = 1, return api v1
    version = 2, return api v2
    Returns:

    """
    return "API v2.0" if version == 2 else "API v1.0"


def hash_password(str_pass):
    """

    Args:
        str_pass:

    Returns:

    """
    return generate_password_hash(str_pass)


def get_timestamp_now():
    """
        Returns:
            current time in timestamp
    """
    return int(time())
