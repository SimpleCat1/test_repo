from collections import namedtuple


class ParametrizationCardProduct:
    data_count_product = namedtuple('data_tuple', 'name count_product check')
    input_data = [
        data_count_product(name='add product count: 1', count_product=1, check=1),
        data_count_product(name='add product count: 2', count_product=2, check=3),
        data_count_product(name='add product count: 10', count_product=10, check=13),
        data_count_product(name='add product count: -10', count_product=-10, check=3),
        data_count_product(name='add product count: 1.1', count_product='1.1', check=3),
        data_count_product(name='add product count: 1,1', count_product='1,1', check=3),
        data_count_product(name='add product count: 0.1', count_product='0.1', check=3),
        data_count_product(name='add product count: 0', count_product=0, check=3),
        data_count_product(name='add product count: -0', count_product=-0, check=3),
        data_count_product(name='add product count: -3', count_product=-3, check=0),
        data_count_product(name='add product count: -1', count_product=-1, check=0),
        data_count_product(name='add product count: -0.1', count_product='-0.1', check=0),
        data_count_product(name='add product count: asdf', count_product='asdf', check=0),
        data_count_product(name='add product count: asdf1', count_product='asdf', check=0),
        data_count_product(name='add product count: probel1probel', count_product=' 1 ', check=1),
    ]