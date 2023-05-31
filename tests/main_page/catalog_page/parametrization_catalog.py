from collections import namedtuple


class ParametrizationCatalog:
    data_catalog = namedtuple('data_tuple', 'name url')
    search_data = [
        data_catalog(name='Mice and Trackballs', url="/mouse"),
        data_catalog(name='Printers', url="/printer"),
        data_catalog(name='Scanners', url="/scanner"),
    ]
