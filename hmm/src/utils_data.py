import datetime
from database import db, Model
from database import CustoOrcamentoModel, CustoPlanejadoModel, CustoRealizadoModel
from utils.utils_methods import normaliza_data
from queries import (
    realizado_join_cc_without_account_number,
    planejado_join_cc_without_account_number,
    orcado_join_cc_without_account_number,
    realizado_join_cc_with_account_number,
    planejado_join_cc_with_account_number,
    orcado_join_cc_with_account_number,
    select_item_realizado,
    select_item_planejado,
    select_item_orcado,
)

# pega o primeiro dia do mês corrente
def first_day_of_current_month():
    today = datetime.datetime.now()
    return f'{today.strftime("%Y")}-{today.strftime("%m")}-01'


# pega todos os registros da tabela de realizado
def get_most_recent_realizado():
    data = db.execute_sql(
        realizado_join_cc_without_account_number, [first_day_of_current_month()]
    )

    data = [normaliza_data(item) for item in data]

    return list(data)


# pega todos os registros mais recentes da tabela de planejado
def get_most_recent_planejado():
    data = db.execute_sql(
        planejado_join_cc_without_account_number, [first_day_of_current_month()]
    )

    data = [normaliza_data(item) for item in data]

    return list(data)


# pega todos os registros mais recentes da tabela de orcado
def get_most_recent_orcado():
    data = db.execute_sql(
        orcado_join_cc_without_account_number, [first_day_of_current_month()]
    )

    data = [normaliza_data(item) for item in data]

    return list(data)


# pega todos os registro da tabela de realizado pelo número da conta
def get_most_recent_realizado_by_account(conta: int):
    data = db.execute_sql(
        realizado_join_cc_with_account_number, [conta, first_day_of_current_month()]
    )
    return list(data)


# pega todos os registros da tabela de planejado pelo número da conta
def get_most_recent_planejado_by_account(conta: int):
    data = db.execute_sql(
        planejado_join_cc_with_account_number, [conta, first_day_of_current_month()]
    )
    return list(data)


# pega todos os registros da tabela de orcado pelo número da conta
def get_most_recent_orcado_by_account(conta: int):
    data = db.execute_sql(
        orcado_join_cc_with_account_number, [conta, first_day_of_current_month()]
    )
    return list(data)


# verifica se um item existe na base de dados
def item_exists(data: dict, model: Model):
    if model is CustoRealizadoModel:
        query = db.execute_sql(
            select_item_realizado, [data["conta_cloud"], data["codigo"]]
        )
        return True if len(list(query)) > 0 else False

    elif model is CustoPlanejadoModel:
        query = db.execute_sql(
            select_item_planejado, [data["conta_cloud"], data["codigo"]]
        )
        return True if len(list(query)) > 0 else False

    elif model is CustoOrcamentoModel:
        query = db.execute_sql(
            select_item_orcado, [data["conta_cloud"], data["codigo"]]
        )
        return True if len(list(query)) > 0 else False


def update_bd(model: Model, data):
    update_query = model.update(
        {model.valor: data["valor"], model.data: data["data"]}
    ).where(model.numero_conta == data["conta_cloud"], model.codigo == data["codigo"])
    print(update_query.execute())
    if update_query.execute() <= 0:
        return False
    else:
        return True


def insert_bd(model: Model, data):
    insert_query = model(
        numero_conta=data["conta_cloud"], data=data["data"], valor=data["valor"]
    )
    if insert_query.save() <= 0:
        return False
    else:
        return True
