"""
Variables to be used across the board everywhere.

Variables available are
    General purpose
        - logdir
        - adm_bin, adm_cfg,  adm_data
        - adm_etc, adm_keys, adm_logs
        - adm_tmp

    Permissions
        - shared group (wheel) & mode 750 for cfg, data, etc, keys
        - Mode 1777 for tmp, logs
        - Files created in etc, keys should have mode 640 and root:wheel

    For MySQL
        - dbname, dbuser, dbpass, dbport,
"""

""" General Purpose """
adm_home = '/u/admin'
adm_bin = adm_home + '/bin'
adm_cfg = adm_home + '/cfg'
adm_data = adm_home + '/data'
adm_etc = adm_home + '/etc'
adm_keys = adm_home + '/keys'
adm_logs = adm_home + '/logs'
adm_tmp = adm_home + '/tmp'

keyfile = adm_keys + '/keyfile'

logdir = adm_logs

smtp_server = 'gAAAAABaRnjQLl5_SHGQZOsI-NLA5aRwMsLIhs2y1_QlMuy1tXkhtIzhEVklYJ1A1lN7bjS0Qf4V0sPJlR_xZZFpZK7mqN0fbQ=='
smtp_port = 'gAAAAABaRnk-OlKdVvdVddkPEo76iKqyHKYv530XmgLF_38_2jZjlkYPxL20wWVZBPxtCoYBUUL4sxlzoq4EPVQQos6aPIsojg=='
smtp_user = 'gAAAAABaRner9zdw5UhBqJpvLIPuQnsF2rbB9I1ZGT6Xw4MfgMhePzoS7_8LH8mtzwukNQqkayTHJUp_A3tq9xCiDHo8nn51eyIEFQk0MRcSYF-jbBfJCp0='
smtp_passwd = 'gAAAAABaRncp-P5SkWyKz9P9ddUxtB38uoenTMRQa-dJlch3CWHDX6bLpW_89QYcndJDwfVmz2XLGjsc1U5DEknjlqdmC73QpQ=='

""" Used for the MySQL DB """
dbname = 'gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61vvzAiDWKyv\
LYOAlkomZ6NXayxVmU3XLi-ZfleZaQ=='
dbuser = 'gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61vvzAiDWKyv\
LYOAlkomZ6NXayxVmU3XLi-ZfleZaQ=='
dbpass = 'gAAAAABZ6-gp2LRJGy6PUolC5lUNd_OimzJChjJDthVVCZXSDvclKLx_6QSZZ-8SJ9ra\
UErXg5M2P7vmCKGc63T0uMr8J04C6A=='
dbport = 'gAAAAABZ6-hyadloTFpJyIY9H6Ki4cikqab9GRP9EmjqXk--I6Nz3rd9mqDb_RPpzBaO\
RVq1_XDzrKOlXozOq7n90Gsuukegbw=='


# DB Credentials for several databases in Python DICT format

db_creds = {
    "stock": {
        "db_name": "gAAAAABZ7KLVM0iwLz2RXncIEWUKUFO4mRsxsKfX_l5beQzSy2a1q-4kuQ\
xM62R-AGgtmUs588GJTOplpvZSj57Nfot68EIwKw==",
        "db_user": "gAAAAABZ7KLVM0iwLz2RXncIEWUKUFO4mRsxsKfX_l5beQzSy2a1q-4kuQ\
xM62R-AGgtmUs588GJTOplpvZSj57Nfot68EIwKw==",
        "db_pass": "gAAAAABZ7KLVM0iwLz2RXncIEWUKUFO4mRsxsKfX_l5beQzSy2a1q-4kuQ\
xM62R-AGgtmUs588GJTOplpvZSj57Nfot68EIwKw==",
        "db_port": "gAAAAABZ6-hyadloTFpJyIY9H6Ki4cikqab9GRP9EmjqXk--I6Nz3rd9mq\
Db_RPpzBaORVq1_XDzrKOlXozOq7n90Gsuukegbw=="
    },
    "lifecycle": {
        "db_name": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61\
vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_user": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61\
vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_pass": "gAAAAABZ6-fP7U7x2xo4h6qA912CYmjQOnMVrXfJbhnFzd2LbuLpRR_j61\
vvzAiDWKyvLYOAlkomZ6NXayxVmU3XLi-ZfleZaQ==",
        "db_port": "gAAAAABZ6-hyadloTFpJyIY9H6Ki4cikqab9GRP9EmjqXk--I6Nz3rd9mq\
Db_RPpzBaORVq1_XDzrKOlXozOq7n90Gsuukegbw=="
    }
}
