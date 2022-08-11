import datetime
from decimal import Decimal
from unittest import result
from src.utils.utils_methods import (
    del_item,
    dict_factory,
    group_contas,
    normaliza_data,
    insert_empty_values,
    del_item,
    clean_input_data,
)


def test_normaliza_data():
    payload = (1, 1, "2021-01-01", 15.56)
    result = normaliza_data(payload)

    assert type(result) is dict


def test_dict_dactory():
    data = {
        "conta_cloud": 1,
        "data": "2021-01-01",
    }

    result = dict_factory(data)
    assert type(result) == dict


def test_group_contas():
    payload = {
        "realizado": [],
        "planejado": [
            (1, 3, datetime.datetime(2022, 10, 1, 0, 0), Decimal("36.00")),
            (1, 2, datetime.datetime(2022, 9, 1, 0, 0), Decimal("26.00")),
            (1, 1, datetime.datetime(2022, 8, 1, 0, 0), Decimal("16.00")),
            (1, 19, datetime.datetime(2022, 8, 1, 0, 0), Decimal("10.00")),
            (2, 20, datetime.datetime(2023, 2, 1, 0, 0), Decimal("20.00")),
            (2, 4, datetime.datetime(2022, 8, 1, 0, 0), Decimal("46.00")),
            (2, 5, datetime.datetime(2022, 8, 1, 0, 0), Decimal("56.00")),
            (2, 6, datetime.datetime(2022, 8, 1, 0, 0), Decimal("76.00")),
        ],
        "orcado": [],
    }

    expected = {
        "1": {
            "realizado": [],
            "planejado": [
                {
                    "conta_cloud": 1,
                    "codigo": 3,
                    "data": datetime.datetime(2022, 10, 1, 0, 0),
                    "valor": Decimal("36.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 2,
                    "data": datetime.datetime(2022, 9, 1, 0, 0),
                    "valor": Decimal("26.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 1,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("16.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 19,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("10.00"),
                },
            ],
            "orcado": [],
        },
        "2": {
            "realizado": [],
            "planejado": [
                {
                    "conta_cloud": 2,
                    "codigo": 20,
                    "data": datetime.datetime(2023, 2, 1, 0, 0),
                    "valor": Decimal("20.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 4,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("46.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 5,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("56.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 6,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("76.00"),
                },
            ],
            "orcado": [],
        },
    }

    result = group_contas(payload)

    assert result == expected


def test_insert_empty_values_by_contas_false():
    payload = {
        "realizado": [],
        "planejado": [
            {
                "conta_cloud": 2,
                "codigo": 20,
                "data": datetime.datetime(2023, 2, 1, 0, 0),
                "valor": Decimal("20.00"),
            },
            {
                "conta_cloud": 1,
                "codigo": 3,
                "data": datetime.datetime(2022, 10, 1, 0, 0),
                "valor": Decimal("36.00"),
            },
            {
                "conta_cloud": 1,
                "codigo": 2,
                "data": datetime.datetime(2022, 9, 1, 0, 0),
                "valor": Decimal("26.00"),
            },
            {
                "conta_cloud": 1,
                "codigo": 1,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("16.00"),
            },
            {
                "conta_cloud": 2,
                "codigo": 4,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("46.00"),
            },
            {
                "conta_cloud": 2,
                "codigo": 5,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("56.00"),
            },
            {
                "conta_cloud": 2,
                "codigo": 6,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("76.00"),
            },
            {
                "conta_cloud": 1,
                "codigo": 19,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("10.00"),
            },
        ],
        "orcado": [],
    }
    expected = {
        "realizado": [
            {"conta_cloud": 0, "codigo": 0, "data": "2022-08-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-09-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-10-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-11-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-12-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-01-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-02-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-03-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-04-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-05-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-06-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-07-01", "valor": 0.0},
        ],
        "planejado": [
            {
                "conta_cloud": 2,
                "codigo": 20,
                "data": datetime.datetime(2023, 2, 1, 0, 0),
                "valor": Decimal("20.00"),
            },
            {
                "conta_cloud": 1,
                "codigo": 3,
                "data": datetime.datetime(2022, 10, 1, 0, 0),
                "valor": Decimal("36.00"),
            },
            {
                "conta_cloud": 1,
                "codigo": 2,
                "data": datetime.datetime(2022, 9, 1, 0, 0),
                "valor": Decimal("26.00"),
            },
            {
                "conta_cloud": 1,
                "codigo": 1,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("16.00"),
            },
            {
                "conta_cloud": 2,
                "codigo": 4,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("46.00"),
            },
            {
                "conta_cloud": 2,
                "codigo": 5,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("56.00"),
            },
            {
                "conta_cloud": 2,
                "codigo": 6,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("76.00"),
            },
            {
                "conta_cloud": 1,
                "codigo": 19,
                "data": datetime.datetime(2022, 8, 1, 0, 0),
                "valor": Decimal("10.00"),
            },
            {"conta_cloud": 0, "codigo": 0, "data": "2022-08-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-09-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-10-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-11-01", "valor": 0.0},
        ],
        "orcado": [
            {"conta_cloud": 0, "codigo": 0, "data": "2022-08-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-09-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-10-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-11-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-12-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-01-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-02-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-03-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-04-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-05-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-06-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-07-01", "valor": 0.0},
        ],
    }
    result = insert_empty_values(payload, by_contas=False)

    assert result == expected


def test_insert_empty_values_by_contas_true():
    payload = {
        "1": {
            "realizado": [],
            "planejado": [
                {
                    "conta_cloud": 1,
                    "codigo": 3,
                    "data": datetime.datetime(2022, 10, 1, 0, 0),
                    "valor": Decimal("36.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 2,
                    "data": datetime.datetime(2022, 9, 1, 0, 0),
                    "valor": Decimal("26.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 1,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("16.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 19,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("10.00"),
                },
            ],
            "orcado": [],
        },
        "2": {
            "realizado": [],
            "planejado": [
                {
                    "conta_cloud": 2,
                    "codigo": 20,
                    "data": datetime.datetime(2023, 2, 1, 0, 0),
                    "valor": Decimal("20.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 4,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("46.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 5,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("56.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 6,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("76.00"),
                },
            ],
            "orcado": [],
        },
    }
    expected = {
        "1": {
            "realizado": [
                {"conta_cloud": "1", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-12-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-05-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-06-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-07-01", "valor": 0.0},
            ],
            "planejado": [
                {
                    "conta_cloud": 1,
                    "codigo": 3,
                    "data": datetime.datetime(2022, 10, 1, 0, 0),
                    "valor": Decimal("36.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 2,
                    "data": datetime.datetime(2022, 9, 1, 0, 0),
                    "valor": Decimal("26.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 1,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("16.00"),
                },
                {
                    "conta_cloud": 1,
                    "codigo": 19,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("10.00"),
                },
                {"conta_cloud": "1", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
            ],
            "orcado": [
                {"conta_cloud": "1", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-12-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-05-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-06-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-07-01", "valor": 0.0},
            ],
        },
        "2": {
            "realizado": [
                {"conta_cloud": "2", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-12-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-05-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-06-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-07-01", "valor": 0.0},
            ],
            "planejado": [
                {
                    "conta_cloud": 2,
                    "codigo": 20,
                    "data": datetime.datetime(2023, 2, 1, 0, 0),
                    "valor": Decimal("20.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 4,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("46.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 5,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("56.00"),
                },
                {
                    "conta_cloud": 2,
                    "codigo": 6,
                    "data": datetime.datetime(2022, 8, 1, 0, 0),
                    "valor": Decimal("76.00"),
                },
                {"conta_cloud": "2", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
            ],
            "orcado": [
                {"conta_cloud": "2", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-12-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-05-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-06-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-07-01", "valor": 0.0},
            ],
        },
    }
    result = insert_empty_values(payload, by_contas=True)

    assert result == expected


def test_del_item():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    itens = [0, 6, 9]

    expected = [2, 3, 4, 5, 6, 8, 9]
    result = del_item(vetor, itens)

    assert result == expected


def test_clean_input_data_by_contas_false():
    payload = {
        "realizado": [
            {"conta_cloud": 0, "codigo": 0, "data": "2022-08-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-09-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-10-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-11-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-12-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-01-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-02-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-03-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-04-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-05-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-06-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-07-01", "valor": 0.0},
        ],
        "planejado": [
            {
                "conta_cloud": 2,
                "codigo": 20,
                "data": "2023-02-01 00:00:00",
                "valor": "20.00",
            },
            {
                "conta_cloud": 1,
                "codigo": 3,
                "data": "2022-10-01 00:00:00",
                "valor": "36.00",
            },
            {
                "conta_cloud": 1,
                "codigo": 2,
                "data": "2022-09-01 00:00:00",
                "valor": "26.00",
            },
            {
                "conta_cloud": 1,
                "codigo": 1,
                "data": "2022-08-01 00:00:00",
                "valor": "16.00",
            },
            {
                "conta_cloud": 2,
                "codigo": 4,
                "data": "2022-08-01 00:00:00",
                "valor": "46.00",
            },
            {
                "conta_cloud": 2,
                "codigo": 5,
                "data": "2022-08-01 00:00:00",
                "valor": "56.00",
            },
            {
                "conta_cloud": 2,
                "codigo": 6,
                "data": "2022-08-01 00:00:00",
                "valor": "76.00",
            },
            {
                "conta_cloud": 1,
                "codigo": 19,
                "data": "2022-08-01 00:00:00",
                "valor": "10.00",
            },
            {"conta_cloud": 0, "codigo": 0, "data": "2022-08-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-09-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-10-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-11-01", "valor": 0.0},
        ],
        "orcado": [
            {"conta_cloud": 0, "codigo": 0, "data": "2022-08-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-09-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-10-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-11-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2022-12-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-01-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-02-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-03-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-04-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-05-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-06-01", "valor": 0.0},
            {"conta_cloud": 0, "codigo": 0, "data": "2023-07-01", "valor": 0.0},
        ],
    }

    expected = {
        "realizado": [],
        "planejado": [
            {
                "conta_cloud": 2,
                "codigo": 20,
                "data": "2023-02-01 00:00:00",
                "valor": "20.00",
            },
            {
                "conta_cloud": 1,
                "codigo": 3,
                "data": "2022-10-01 00:00:00",
                "valor": "36.00",
            },
            {
                "conta_cloud": 1,
                "codigo": 2,
                "data": "2022-09-01 00:00:00",
                "valor": "26.00",
            },
            {
                "conta_cloud": 1,
                "codigo": 1,
                "data": "2022-08-01 00:00:00",
                "valor": "16.00",
            },
            {
                "conta_cloud": 2,
                "codigo": 4,
                "data": "2022-08-01 00:00:00",
                "valor": "46.00",
            },
            {
                "conta_cloud": 2,
                "codigo": 5,
                "data": "2022-08-01 00:00:00",
                "valor": "56.00",
            },
            {
                "conta_cloud": 2,
                "codigo": 6,
                "data": "2022-08-01 00:00:00",
                "valor": "76.00",
            },
            {
                "conta_cloud": 1,
                "codigo": 19,
                "data": "2022-08-01 00:00:00",
                "valor": "10.00",
            },
        ],
        "orcado": [],
    }

    result = clean_input_data(payload, by_contas=False)

    assert result == expected


def test_clean_input_data_by_contas_true():
    payload = {
        "1": {
            "realizado": [
                {"conta_cloud": "1", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-12-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-05-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-06-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-07-01", "valor": 0.0},
            ],
            "planejado": [
                {
                    "conta_cloud": 1,
                    "codigo": 3,
                    "data": "2022-10-01 00:00:00",
                    "valor": "36.00",
                },
                {
                    "conta_cloud": 1,
                    "codigo": 2,
                    "data": "2022-09-01 00:00:00",
                    "valor": "26.00",
                },
                {
                    "conta_cloud": 1,
                    "codigo": 1,
                    "data": "2022-08-01 00:00:00",
                    "valor": "16.00",
                },
                {
                    "conta_cloud": 1,
                    "codigo": 19,
                    "data": "2022-08-01 00:00:00",
                    "valor": "10.00",
                },
                {"conta_cloud": "1", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
            ],
            "orcado": [
                {"conta_cloud": "1", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2022-12-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-05-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-06-01", "valor": 0.0},
                {"conta_cloud": "1", "codigo": 0, "data": "2023-07-01", "valor": 0.0},
            ],
        },
        "2": {
            "realizado": [
                {"conta_cloud": "2", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-12-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-05-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-06-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-07-01", "valor": 0.0},
            ],
            "planejado": [
                {
                    "conta_cloud": 2,
                    "codigo": 20,
                    "data": "2023-02-01 00:00:00",
                    "valor": "20.00",
                },
                {
                    "conta_cloud": 2,
                    "codigo": 4,
                    "data": "2022-08-01 00:00:00",
                    "valor": "46.00",
                },
                {
                    "conta_cloud": 2,
                    "codigo": 5,
                    "data": "2022-08-01 00:00:00",
                    "valor": "56.00",
                },
                {
                    "conta_cloud": 2,
                    "codigo": 6,
                    "data": "2022-08-01 00:00:00",
                    "valor": "76.00",
                },
                {"conta_cloud": "2", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
            ],
            "orcado": [
                {"conta_cloud": "2", "codigo": 0, "data": "2022-08-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-09-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-10-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-11-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2022-12-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-01-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-02-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-03-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-04-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-05-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-06-01", "valor": 0.0},
                {"conta_cloud": "2", "codigo": 0, "data": "2023-07-01", "valor": 0.0},
            ],
        },
    }

    expected = {
        "1": {
            "realizado": [],
            "planejado": [
                {
                    "conta_cloud": 1,
                    "codigo": 3,
                    "data": "2022-10-01 00:00:00",
                    "valor": "36.00",
                },
                {
                    "conta_cloud": 1,
                    "codigo": 2,
                    "data": "2022-09-01 00:00:00",
                    "valor": "26.00",
                },
                {
                    "conta_cloud": 1,
                    "codigo": 1,
                    "data": "2022-08-01 00:00:00",
                    "valor": "16.00",
                },
                {
                    "conta_cloud": 1,
                    "codigo": 19,
                    "data": "2022-08-01 00:00:00",
                    "valor": "10.00",
                },
            ],
            "orcado": [],
        },
        "2": {
            "realizado": [],
            "planejado": [
                {
                    "conta_cloud": 2,
                    "codigo": 20,
                    "data": "2023-02-01 00:00:00",
                    "valor": "20.00",
                },
                {
                    "conta_cloud": 2,
                    "codigo": 4,
                    "data": "2022-08-01 00:00:00",
                    "valor": "46.00",
                },
                {
                    "conta_cloud": 2,
                    "codigo": 5,
                    "data": "2022-08-01 00:00:00",
                    "valor": "56.00",
                },
                {
                    "conta_cloud": 2,
                    "codigo": 6,
                    "data": "2022-08-01 00:00:00",
                    "valor": "76.00",
                },
            ],
            "orcado": [],
        },
    }

    result = clean_input_data(payload, by_contas=True)

    assert result == expected
