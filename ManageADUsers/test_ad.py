import ssl

from ldap3 import Server, Connection, SUBTREE, Tls, MODIFY_REPLACE

OBJECT_CLASS = ['person', 'user']
LDAP_HOST = 'corp.tass.ru'
'''LDAP_HOST = 'ldaps01.tass.ru'''''
LDAP_USER = 'corp\\sccm_sd_service'
LDAP_PASSWORD = 'ru8akUhU'
LDAP_BASE_DN = 'DC=corp,DC=tass,DC=ru'
search_filter = "(|(samaccountname={0}*)(name=*{0}*))"

tls_configuration = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1_2)


def find_ad_users(username):
    with ldap_connection() as c:
        c.search(search_base=LDAP_BASE_DN,
                 search_filter=search_filter.format(username),
                 search_scope=SUBTREE,
                 attributes={'name', 'TASS-1C-DepartmentPath'},
                 get_operational_attributes=True)

    entries = c.entries

    return entries


def create_ad_user(username, forename, surname, new_password):
    with ldap_connection() as c:
        attributes = get_attributes(username, forename, surname)
        user_dn = get_dn(username)
        result = c.add(dn=user_dn,
                       object_class=OBJECT_CLASS,
                       attributes=attributes)
        if not result:
            msg = "ERROR: User '{0}' was not created: {1}".format(
                username, c.result.get("description"))
            raise Exception(msg)

        # unlock and set password
        c.extend.microsoft.unlock_account(user=user_dn)
        c.extend.microsoft.modify_password(user=user_dn,
                                           new_password=new_password,
                                           old_password=None)
        # Enable account - must happen after user password is set
        enable_account = {"userAccountControl": (MODIFY_REPLACE, [512])}
        c.modify(user_dn, changes=enable_account)

        # Add groups
        c.extend.microsoft.add_members_to_groups([user_dn], get_groups())


def ldap_connection():
    server = ldap_server()
    return Connection(server, user=LDAP_USER,
                      password=LDAP_PASSWORD,
                      auto_bind=True)


def ldap_server():
    return Server(LDAP_HOST, use_ssl=False, tls=tls_configuration)


def get_dn(username):
    return "CN={0},OU=Test Accounts,OU=User Accounts," \
           "OU=Accounts,DC=test,DC=core,DC=bogus,DC=org,DC=uk".format(username)


def get_attributes(username, forename, surname):
    return {
        "displayName": username,
        "sAMAccountName": username,
        "userPrincipalName": "{0}@test.core.bogus.org.uk".format(username),
        "name": username,
        "givenName": forename,
        "sn": surname
    }


def get_groups():
    postfix = ',OU=MyService,OU=My Groups,DC=test,DC=core,DC=bogus,DC=org,DC=uk'
    return [
        ('CN=ROLE_A%s' % postfix)
    ]


search = find_ad_users('myltsev_a')

