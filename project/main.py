# A tela toda é considerada uma coluna, oq tem dentro são listas = []

import PySimpleGUI as sg
from cotacao import pegar_cotacoes

layout = [
    [sg.Text("Pegar cotação da moeda ")],
    [sg.InputText(key="nome_cotacao")],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_cotacao")],
]

janela = sg.Window("Sistema de cotação de moedas", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
         break
    if evento == "Pegar Cotação":
         #pegando um valor de um input
         codigo_cotacao = valores["nome_cotacao"]
         #codcotacao
         cotacao = pegar_cotacoes(codigo_cotacao)
         #edição de um valor
         janela["texto_cotacao"].update(f"A cotação do {codigo_cotacao} é de R${cotacao}")


janela.close()