import fs_to_db as fsdb
import json

available_endpoints = {"/tests/database",
                       "/tests/filesystem", "/tests/json", "/tests/cache", "/authenticated/read_quota", "/help", "/info", "/authenticated/read_quota/human"}


def auth_from_json(db_con, json_in):
    """
    Expected JSON input:
    { "username":"foo", "key":"bar"}
    This will return an int if user is valid, False if invalid
    """
    in_dict = json.loads(json_in)
    return fsdb.dg.validate_user_info(db_con, in_dict["username"], in_dict["key"])


def read_usage_data(db_con, json_in, human):
    """
    Expected JSON input:
    { "username":"foo", "key":"bar"}
    """
    is_user_valid = auth_from_json(db_con, json_in)
    in_dict = json.loads(json_in)

    if type(is_user_valid) is int:
        bytes_used = fsdb.rw_usage(db_con, in_dict["username"])
        bytes_quota = fsdb.dg.find_data_cap(db_con, in_dict["username"])
        if human == False:
            pass
        else:
            bytes_used = fsdb.fsc.convert_bytes(convert_bytes(bytes_used))
            bytes_quota = fsdb.fsc.convert_bytes(convert_bytes(bytes_quota))
        output = '{ "usage": "' + \
            str(bytes_used) + '", "quota": "' + str(bytes_quota) + '"}'
        return output
    elif is_user_valid == False:
        output = '{ "usage": "-1", "quota": "-1"}'
        return output


def handle_endpoint(path, db_con, json_in):
    if path in available_endpoints:
        if path == "/authenticated/read_quota":
            return read_usage_data(db_con, json_in, False)
        elif path == "/authenticated/read_quota/human":
            return read_usage_data(db_con, json_in, True)
        elif path == "/info":
            return {"message": "This is an API for customers to query to find thier data usage on our service"}
        elif path == "/help":
            return {"message": "For information on how to use this API, please contact support or refer to the API documentation"}
    else:
        return {"error": "CEC601"}

# print(read_usage_data(fsdb.dg.auth_to_db("infoMan", "placeholder"),
#      '{"username": "zane.reick", "key": "23d72d65-ad82-11ec-a614-020054746872"}'))
