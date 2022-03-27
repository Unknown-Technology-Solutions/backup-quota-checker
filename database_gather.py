import mysql.connector

info_db = mysql.connector.connect(
    host="localhost",
    user="infoMan",
    password="placeholder",
    database="backup_resources"
)


def validate_user_info(connection, username, auth_key):
    """
    Check if a given username and key combo is valid
    """
    cur = connection.cursor()
    query = "SELECT `id` FROM auth_keys WHERE user = '" + \
        username + "' AND auth_key = '" + auth_key + "'"
    cur.execute(query)
    return_array = cur.fetchone()
    if len(return_array) == 1:
        # return 1st value, that should be the only value
        return return_array[0]
    else:
        raise ValueError


def find_backup_dir(connection, username):
    """
    Find a given user's backup directory
    """
    cur = connection.cursor()
    query = "SELECT `directory` FROM user_mapping WHERE username = '" + username + "'"
    cur.execute(query)
    return_array = cur.fetchone()
    if len(return_array) == 1:
        # return 1st value, that should be the only value
        return return_array[0]
    else:
        raise ValueError


def find_data_cap(connection, username):
    """
    Find a given user's data cap in bytes
    """
    cur = connection.cursor()
    query = "SELECT `data_cap` FROM user_mapping WHERE username = '" + username + "'"
    cur.execute(query)
    return_array = cur.fetchone()
    if len(return_array) == 1:
        # return 1st value, that should be the only value
        return return_array[0]
    else:
        raise ValueError
