import database_gather as dg
import fs_check as fsc

def rw_usage(con, username):
    """
    Read and write usage to and from the database depending on its validity (TTL based)
    """

    ttl_state = dg.check_cache_ttl(con, username)
#    ttl_state = False

    if ttl_state:
        return dg.read_data_usage_cache(con, username)
    elif ttl_state == False:
        total_usage = fsc.folderSize(dg.find_backup_dir(con, username), False)
        dg.update_data_usage_cache(con, username, total_usage)
        return total_usage


print(rw_usage(dg.auth_to_db("infoMan", "placeholder"), "zane.reick"))