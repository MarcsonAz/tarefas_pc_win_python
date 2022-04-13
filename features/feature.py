import os
import re

REGEX_DATE = ".\d{8}"
PATTERN = re.compile(REGEX_DATE, re.IGNORECASE)

def renomear_arquivo(caminho,res):
    # aplicar o rename nos arquivos com data

    # chamar remover_data para novo nome
    for file in res:
            
        old_name = os.path.join(caminho,file)
        new_name = re.sub(PATTERN,"",os.path.join(caminho,file))
        
        # enclosing inside try-except
        try:
            os.rename(old_name, new_name)
        except FileExistsError:
            print("File already Exists")
            print("Removing existing file")
            # skip the below code
            # if you don't' want to forcefully rename
            os.remove(new_name)
            # rename it
            os.rename(old_name, new_name)
            print('Done renaming a file')


def listar_com_data(caminho):
    res = []

    for file in os.listdir(caminho):
        if PATTERN.search(file):
            print(file)
            res.append(file)
    return(res)



def definir_dir():
    DIR = "S:\\05 - Projetos\\05.04_Bases Desindentificadas\\METADADOS"
    IN_METADADOS = 0
    
    IN_METADADOS = int( input("DENTRO DA PASTA: "+ DIR + " ? \nDigite 1 para sim ou 0 para não \n"))

    #print(IN_METADADOS)
    
    if(IN_METADADOS):
        print("Mostrar arquivos em: "+DIR+" \n")

        for file in os.listdir(DIR):
            print(file)

        pasta = input("DIGITE NOME DA PASTA OU PRESSIONE ENTER PARA MANTER NESTE DIRETORIO:")
        #print(pasta)

        if(len(pasta) > 0):
            caminho = DIR + "\\" + pasta
        else:
            caminho = DIR
    else:
        caminho = input("DIGITE CAMINHO COMPLETO")
    print(caminho)
    
    return(caminho)