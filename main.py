
import features.feature as ft

caminho = ft.definir_dir()

try:
    arquivos = ft.listar_com_data(caminho)
    OK = input("Confirmar a remocao de datas dos arquivos listados? \n0 para cancelar operação")
    if(OK == "0" ):
        print("Operação cancelada! \nFim do programa")
    else:
        ft.renomear_arquivo(caminho,arquivos)
        print("Operação finalizada!")
except FileExistsError:
    print("File error!")


# confirmar diretório
# pegar todos com data
# mostrar os identificados com data
# pedir confirmacao
# limpar as datas
# informar que todos foram renomeados



