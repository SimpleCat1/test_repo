from collections import namedtuple


class ParametrizationAdminAuthorization:
    data_authorization_incorrect = namedtuple('data_tuple', 'name username password')
    input_data = [
        data_authorization_incorrect(
            name='input username="1" password="1"',
            username='1',
            password='1',
        ),
        data_authorization_incorrect(
            name='input username=" " password=" "',
            username=' ',
            password=' ',
        ),
        data_authorization_incorrect(
            name='input username="" password=""',
            username='',
            password='',
        ),
        data_authorization_incorrect(
            name='input username="1" password=" "',
            username='1',
            password='',
        ),
        data_authorization_incorrect(
            name='input username="" password="1"',
            username='',
            password='1',
        ),
    ]
