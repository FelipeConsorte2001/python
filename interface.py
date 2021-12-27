import requests
from  tkinter import *



def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacao['text'] = texto


janela = Tk()
janela.geometry('350x250')
janela.title('Cotação atual das Moedas')
texto_orientacao = Label(janela, text="Click no botão para ver as cotações")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Buscar cotações do Euro, dollar,BTC', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacao = Label(janela, text='Cotação')
texto_cotacao.grid(column=0, row=2, padx=10, pady=10)
janela.mainloop()
