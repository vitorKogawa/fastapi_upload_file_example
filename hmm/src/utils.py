import json
from database import CustoOrcamentoModel, CustoPlanejadoModel, CustoRealizadoModel
from utils_data import item_exists, update_bd, insert_bd
from utils_data import (
    get_most_recent_orcado,
    get_most_recent_planejado,
    get_most_recent_realizado,
    get_most_recent_planejado_by_account,
    get_most_recent_realizado_by_account,
    get_most_recent_orcado_by_account,
)
from utils.utils_methods import group_contas, insert_empty_values, clean_input_data

# seleciona todos os registros mais recentes de realizado, planejado e orcado independentemente das contas
def get_most_recent_data():
    realizado = get_most_recent_realizado()
    planejado = get_most_recent_planejado()
    orcado = get_most_recent_orcado()

    response = insert_empty_values(
        {
            "realizado": realizado,
            "planejado": planejado,
            "orcado": orcado,
        },
        by_contas=False,
    )

    return response


# selecionar todos os registros mais recentes de realizado, planejado e orcado conforme os número de conta informados
def get_most_recent_data_by_account(contas: list):
    realizado = []
    planejado = []
    orcado = []
    for conta in contas:
        realizado.extend(get_most_recent_realizado_by_account(conta))
        planejado.extend(get_most_recent_planejado_by_account(conta))
        orcado.extend(get_most_recent_orcado_by_account(conta))

    response = insert_empty_values(
        group_contas(
            {"realizado": realizado, "planejado": planejado, "orcado": orcado}
        ),
        by_contas=True,
    )

    return response


# all_contas = json.dumps(get_most_recent_data(), default=str)
by_numero_contas = json.dumps(get_most_recent_data_by_account([1, 2]), default=str)
print(json.loads(by_numero_contas))


# print("Todas as contas.")
# print(all_contas)
# print()
# print("Contas limpas")
# print(clean_input_data(json.loads(all_contas), by_contas=False))

# print()
# print()
# print()


# def check_data_from_front(data: dict, by_contas: bool):
#     categorias = {
#         "realizado": CustoRealizadoModel,
#         "planejado": CustoPlanejadoModel,
#         "orcado": CustoOrcamentoModel,
#     }
#     if not by_contas:
#         pass
#     else:
#         for categoria, model in categorias.items():
#             for numero_conta in data.keys():
#                 for item in data[numero_conta][categoria]:
#                     if item_exists(item, model):
#                         update_bd(model, item)
#                     else:
#                         insert_bd(model, item)


# check_data_from_front(clean_request, by_contas=True)

# print("Determinadas contas.")
# print(by_numero_contas)
# print()
# print("Contas limpas")
# print(clean_input_data(json.loads(by_numero_contas), by_contas=True))
