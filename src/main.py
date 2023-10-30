import json
from fastapi import FastAPI, Request, Response
from datetime import datetime

app = FastAPI()

locacoes = []

@app.get("/")
def health_check():
    return {"status" : "ok"}

#Gabriel
@app.post("/locacoes")
async def criar_registro(request: Request):
    
    body = await request.body()
    body = dict(json.loads(body))
    
    for locacao in locacoes:
        if locacao.get("id_carro") == body.get("id_carro"):
            return {"mensagem": "Veiculo locado"}
    
    locacao = {
        "nome_cliente": body.get("nome_cliente"),
        "id_carro": body.get("id_carro"),
        "data_hora_saida": datetime.now()
    }

    locacoes.append(locacao)

    return locacao

#Fernando
@app.patch("/locacoes/{id_carro}/finalizar")
async def finalizar(id_carro: str, request: Request):
    # Recupera o body
    body = await request.body()
    # Converte para dictionary
    body = dict(json.loads(body))

    # Criamos uma variável de controle
    locacao_existe = None

    print(id_carro)
    for locacao in locacoes:
        # Se existir, atualiza a variável de controle e para o loop
        if (locacao.get("id_carro") == id_carro):
            locacao_existe = locacao
            break

    # Se existir um registro, vai retornar uma mensagem
    if (not locacao_existe):
        content = json.dumps({"mensagem": "Carro não encontrado"})
        return Response(content=content,
                        status_code=404,
                        media_type="application/json")

    indice = locacoes.index(locacao_existe)

    locacoes[indice]["data_hora_final_locacao"] = datetime.now()

    return locacoes[indice]

#Donovam
# DELETE /locacao/:id_carro
@app.delete("/locacao/{id_carro}")
def delete(id_carro: str):
    # Percorremos a lista procurando se existe uma locacao
    # com o mesmo id_carro
    for locacao in locacoes:
        # Se existir, atualiza a variável de controle e para o loop
        if (locacao.get("data_hora_saida") is not None):
            locacao_existe = locacao
            break

 # Se existir uma locação, vai retornar uma mensagem
    if (not locacao_existe):
        content = json.dumps({"mensagem": "locação não encontrada"})
        return Response(content=content,
                        status_code=404,
                        media_type="application/json")

    locacoes.remove(locacao_existe)

    Response(content=None,
             status_code=203,
             media_type="application/json")
