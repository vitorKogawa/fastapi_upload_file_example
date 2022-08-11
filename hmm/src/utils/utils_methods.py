import datetime


# formata as contas para o padrão de dicionários
def normaliza_data(data):
    return {
        "conta_cloud": data[0],
        "codigo": data[1],
        "data": data[2],
        "valor": data[3],
    }


# agrupa os registros da base de dados por numero de contas
def group_contas(data):
    response = {}
    categorias = ["realizado", "planejado", "orcado"]

    for categoria in categorias:
        for item in data[categoria]:
            f_item = normaliza_data(item)
            if "conta_cloud" in f_item:
                numero_conta = f_item["conta_cloud"]
                if str(numero_conta) not in response:
                    response[str(numero_conta)] = {
                        "realizado": [],
                        "planejado": [],
                        "orcado": [],
                    }

                response[str(numero_conta)][categoria].append(f_item)

    return response


# formata o dicionário utilizado em 'insert_empty_values'
def dict_factory(data_dict):
    return {
        "conta_cloud": data_dict["conta_cloud"],
        "codigo": 0,
        "data": data_dict["data"],
        "valor": "0.00",
    }


# insere valores fictícios para que o frontend sempre receba 12 registros nas categorias realizado, planejado e orcado
def insert_empty_values(data: dict, by_contas: bool):
    categorias = ["realizado", "planejado", "orcado"]
    if not by_contas:
        for categoria in categorias:
            if not data[categoria]:
                ano = int(datetime.datetime.now().strftime("%Y"))
                mes = int(datetime.datetime.now().strftime("%m"))

                for i in range(12):
                    if (mes + i) > 12:
                        ano += 1
                        mes = 1
                        for j in range(0, (12 - i)):
                            new_item = {
                                "conta_cloud": 0,
                                "codigo": 0,
                                "data": f"{ano}-0{mes + (j)}-01"
                                if (mes + j) <= 9
                                else f"{ano}-{mes + (j)}-01",
                                "valor": 0.00,
                            }

                            data[categoria].append(new_item)
                        break

                    new_item = {
                        "conta_cloud": 0,
                        "codigo": 0,
                        "data": f"{ano}-0{mes + (i)}-01"
                        if (mes + i) <= 9
                        else f"{ano}-{mes + (i)}-01",
                        "valor": 0.00,
                    }

                    data[categoria].append(new_item)

            else:
                qtd = 12 - len(data[categoria])
                ultimo_registro = data[categoria][-1]
                ano = int(ultimo_registro["data"].strftime("%Y"))
                mes = int(ultimo_registro["data"].strftime("%m"))

                for i in range(qtd):
                    if (mes + (i + 1)) > 12:
                        ano += 1
                        mes = 1
                        for j in range(0, (qtd - i)):
                            new_item = {
                                "conta_cloud": 0,
                                "codigo": 0,
                                "data": f"{ano}-0{mes + (j)}-01"
                                if (mes + j) <= 9
                                else f"{ano}-{mes + (j)}-01",
                                "valor": 0.00,
                            }

                            data[categoria].append(new_item)
                        break

                    new_item = {
                        "conta_cloud": 0,
                        "codigo": 0,
                        "data": f"{ano}-0{mes + (i)}-01"
                        if (mes + i) <= 9
                        else f"{ano}-{mes + (i)}-01",
                        "valor": 0.00,
                    }

                    data[categoria].append(new_item)
    else:
        for categoria in categorias:
            for numero_conta in data.keys():
                if not data[numero_conta][categoria]:
                    ano = int(datetime.datetime.now().strftime("%Y"))
                    mes = int(datetime.datetime.now().strftime("%m"))

                    for i in range(12):
                        if (mes + i) > 12:
                            ano += 1
                            mes = 1
                            for j in range(0, (12 - i)):
                                new_item = {
                                    "conta_cloud": numero_conta,
                                    "codigo": 0,
                                    "data": f"{ano}-0{mes + (j)}-01"
                                    if (mes + j) <= 9
                                    else f"{ano}-{mes + (j)}-01",
                                    "valor": 0.00,
                                }

                                data[numero_conta][categoria].append(new_item)
                            break

                        new_item = {
                            "conta_cloud": numero_conta,
                            "codigo": 0,
                            "data": f"{ano}-0{mes + (i)}-01"
                            if (mes + i) <= 9
                            else f"{ano}-{mes + (i)}-01",
                            "valor": 0.00,
                        }

                        data[numero_conta][categoria].append(new_item)

                else:
                    qtd = 12 - len(data[numero_conta][categoria])
                    ultimo_registro = data[numero_conta][categoria][-1]
                    ano = int(ultimo_registro["data"].strftime("%Y"))
                    mes = int(ultimo_registro["data"].strftime("%m"))

                    for i in range(qtd):
                        if (mes + (i + 1)) > 12:
                            ano += 1
                            mes = 1
                            for j in range(0, (qtd - i)):
                                new_item = {
                                    "conta_cloud": numero_conta,
                                    "codigo": 0,
                                    "data": f"{ano}-0{mes + (j)}-01"
                                    if (mes + j) <= 9
                                    else f"{ano}-{mes + (j)}-01",
                                    "valor": 0.00,
                                }

                                data[numero_conta][categoria].append(new_item)
                            break

                        new_item = {
                            "conta_cloud": numero_conta,
                            "codigo": 0,
                            "data": f"{ano}-0{mes + (i)}-01"
                            if (mes + i) <= 9
                            else f"{ano}-{mes + (i)}-01",
                            "valor": 0.00,
                        }

                        data[numero_conta][categoria].append(new_item)
    return data


# deleta os itens ficticios
def del_item(vetor, itens):
    for index in sorted(itens, reverse=True):
        del vetor[index]

    return vetor


# identifica os registros ficticios
def clean_input_data(data: dict, by_contas: bool):
    if not by_contas:
        print(data)
        categorias = ["realizado", "planejado", "orcado"]
        indexes = {"realizado": [], "planejado": [], "orcado": []}
        for cat in categorias:
            for item in data[cat]:
                membro_cat = data[cat].index(item)
                if item["codigo"] == 0 and item["valor"] == 0.00:
                    indexes[cat].append(membro_cat)

        for cat in categorias:
            data[cat] = del_item(data[cat], indexes[cat])
            
    else:
        
        categorias = ["realizado", "planejado", "orcado"]
        indexes = {"realizado": [], "planejado": [], "orcado": []}
        for cat in categorias:
            for numero_conta in data.keys():
                clean_input_data(data[numero_conta], by_contas=False)

    print(data)
    return data
