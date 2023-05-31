from collections import namedtuple


class ParametrizationRegistrationUser:
    name_user_incorrect = namedtuple(
        'data_tuple',
        'name first_name last_name password password_confirm',
    )
    password_error = namedtuple(
        'data_tuple',
        'name password password_confirm check',
    )
    telephone_error = namedtuple(
        'data_tuple',
        'name telephone password password_confirm check',
    )
    password_confirm_error = namedtuple(
        'data_tuple',
        'name password password_confirm check',
    )

    user_name_incorrect = [
        name_user_incorrect(
            name='incorrect first_name',
            first_name='1234',
            last_name='asdf',
            password=1234,
            password_confirm=1234,
        ),
        name_user_incorrect(
            name='incorrect last_name',
            first_name='asdf',
            last_name='1234',
            password=1234,
            password_confirm=1234,
        ),
    ]
    input_data_errors_password = [
        password_error(
            name='empty password and filled in confirm password',
            password='',
            password_confirm=1234,
            check='Password must be between 4 and 20 characters!',
        ),
        password_error(
            name='space password and password confirm',
            password=' ',
            password_confirm=' ',
            check='Password must be between 4 and 20 characters!',
        ),
    ]
    input_data_errors_telephone = [
        telephone_error(
            name='phone 1 character',
            telephone=1,
            password=1234,
            password_confirm=1234,
            check='Telephone must be between 3 and 32 characters!',
        ),
        telephone_error(
            name='phone 2 character',
            telephone=12,
            password=1234,
            password_confirm=1234,
            check='Telephone must be between 3 and 32 characters!',
        ),
    ]
    input_data_errors_password_confirm = [
        password_confirm_error(
            name='confirm password is less than password',
            password=1234,
            password_confirm=123,
            check='Password confirmation does not match password!',
        ),
        password_confirm_error(
            name='confirm password is more than password',
            password=1234,
            password_confirm='12345',
            check='Password confirmation does not match password!',
        ),
        password_confirm_error(
            name='confirm password has spaces around it',
            password=1234,
            password_confirm=' 1234 ',
            check='Password confirmation does not match password!',
        ),
    ]
