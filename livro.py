from datetime import datetime, timedelta
pag_atual = int(input("Informe a ultima pagina lida: "))
pag_total = int(input("Informe a quantidade de paginas no livro: "))
pag_dia = int(input("Informe a quantidade de paginas lidas por dia em média: "))
prazo = int(input("Deseja determinar uma data para a finalização do livro? Se sim digite 1, se não digite 0: "))

while(pag_atual > pag_total):
    pag_atual = int(input("Informe a ultima pagina lida correta: "))
    pag_total = int(input("Informe a quantidade de paginas correta: "))


pag_rest = pag_total - pag_atual
porcentagem = (pag_atual * 100) / pag_total
dias_rest = pag_rest/pag_dia

data_atual = datetime.today()
data_atual2 = data_atual + timedelta(days=dias_rest)
data_atual2str = '{}/{}/{}'.format(data_atual2.day, data_atual2.month, data_atual2.year)

if(prazo == 1):
    data_prazo = input("Informe a data desejada no esquema dia/mes/ano.. Exemplo: 02/04/2025: ")
    data_prazo = datetime.strptime(data_prazo.strip(), "%d/%m/%Y")
    while(data_prazo < data_atual):
        data_prazo = input("Informe a data correta no esquema dia/mes/ano: ")
        data_prazo = datetime.strptime(data_prazo.strip(), "%d/%m/%Y")

    dias_ate = (data_prazo - data_atual).days + 2
    dias_ate2 =  dias_ate
    pag_recomendadas = pag_rest/dias_ate
    
    print(f"O número de paginas recomendadas é de: {round(pag_recomendadas, 2)} por dia")
    print(f"Dias restantes até o prazo: {dias_ate}")
print(f"O número de paginas restantes é de: {pag_rest}")
print(f"{round(porcentagem, 2)}% do livro concluído")
if(prazo == 0):
    print(f"Faltam em média {round(dias_rest + 1, 0)} dias para finalizar o livro, finalizando no dia: {data_atual2str}")
