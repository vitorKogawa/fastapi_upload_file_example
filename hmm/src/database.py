from peewee import (
    MySQLDatabase,
    Model,
    CharField,
    IntegerField,
    ForeignKeyField,
    DateTimeField,
    DecimalField,
)

PORT = 3306
DBNAME = "ctcloud"
HOSTNAME = "localhost"
USERNAME = "kogawav"
PASSWORD = "basket4433"

db = MySQLDatabase(
    host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, database=DBNAME
)


class UnknownField(object):
    def __init__(self, *_, **__):
        pass


class BaseModel(Model):
    class Meta:
        database = db


class ContaCloud(BaseModel):
    numero_conta = IntegerField(column_name="NUMERO_CONTA", primary_key=True)
    nome_conta = CharField(column_name="NOME_CONTA", null=True)

    class Meta:
        table_name = "conta_publica"


class CustoRealizadoModel(BaseModel):
    codigo = IntegerField(column_name="ID", primary_key=True)
    valor = DecimalField(column_name="VALOR_CT", null=True)
    data = DateTimeField(column_name="DATA_CT", null=True)
    numero_conta = ForeignKeyField(
        column_name="NUMERO_CONTA", field="numero_conta", model=ContaCloud, null=True
    )

    class Meta:
        table_name = "custo_realizado"


class CustoPlanejadoModel(BaseModel):
    codigo = IntegerField(column_name="ID", primary_key=True)
    valor = DecimalField(column_name="VALOR_CP", null=True)
    data = DateTimeField(column_name="DATA_CP", null=True)
    numero_conta = ForeignKeyField(
        column_name="NUMERO_CONTA", field="numero_conta", model=ContaCloud, null=True
    )

    class Meta:
        table_name = "custo_planejado"


class CustoOrcamentoModel(BaseModel):
    codigo = IntegerField(column_name="ID", primary_key=True)
    valor = DecimalField(column_name="VALOR_CO", null=True)
    data = DateTimeField(column_name="VALOR_CO", null=True)
    numero_conta = ForeignKeyField(
        column_name="NUMERO_CONTA", field="numero_conta", model=ContaCloud, null=True
    )

    class Meta:
        table_name = "custo_orcado"
