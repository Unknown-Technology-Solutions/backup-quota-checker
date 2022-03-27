import mysql.connector
import datetime as dt

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


def does_cache_exist(connection, username):
    """
    Check if a cache exists for a given user
    """
    cur = connection.cursor()
    query = "SELECT `user` FROM previous_quota_check_cache WHERE user = '" + username + "'"
    cur.execute(query)
    return_array = cur.fetchone()
    if type(return_array) is not tuple:
        print("Didn't exist!")
        return False
    elif len(return_array) == 1:
        print("Did exist!")
        return True
    else:
        print("Invalid cache!")
        return "invalid"


def check_cache_ttl(connection, username):
    """
    Verify that cached data is within its TTL
    Return true if cache is valid, false if it is old
    """

    ttl = 43200  # 12 hours in seconds

    cur = connection.cursor()
    c_state = does_cache_exist(connection, username)
    if c_state == True:
        query = "SELECT `cached_time` FROM previous_quota_check_cache WHERE user = '" + username + "'"
        cur.execute(query)

        return_array = cur.fetchone()

        if dt.datetime.now() >= (return_array[0] + dt.timedelta(seconds=ttl)):
            return False
        else:
            return True
    elif c_state == False:
        return False
    elif c_state == "invalid":
        # TODO: Handle invalid caches
        return False


def update_data_usage_cache(connection, username, usage):
    """
    Cache the amount of used data
    """
    cur = connection.cursor()
    # print(type(return_array))

    c_state = does_cache_exist(connection, username)

    if c_state == False:
        query = "INSERT INTO previous_quota_check_cache (user, last_bytes) VALUES (%s, %s)"
        data = (username, usage)
        cur.execute(query, data)
        connection.commit()
        return True
    elif c_state == True:
        query = "UPDATE previous_quota_check_cache SET last_bytes = %s, cached_time = current_timestamp() WHERE user = %s"
        data = (usage, username)
        cur.execute(query, data)
        connection.commit()
        return True
    elif c_state == "invalid":
        return False


def update_old_cache(connection, username, usage):
    """
    Update cache if it needs it
    """
    c_state = check_cache_ttl(connection, username)

    if c_state == False:
        update_data_usage_cache(connection, username, usage)
        print("Updating cache for " + username)
        return True
    elif c_state == True:
        return True
