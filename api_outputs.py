import fs_to_db as fsdb
import json

available_endpoints = {"/tests/database",
                       "/tests/filesystem", "/tests/json", "/tests/cache", "/authenticated/read_quota"}


def auth_from_json(db_con, json_in):
    """
    Expected JSON input:
    { "username":"foo", "key":"bar"}
    """
    in_dict = json.loads(json_in)
    return fsdb.dg.validate_user_info(db_con, in_dict["username"], in_dict["key"])


#print(auth_from_json(fsdb.dg.auth_to_db("infoMan", "placeholder"),
#      '{"username": "zane.reick", "key": "23d72d65-ad82-11ec-a614-020054746872"}'))
