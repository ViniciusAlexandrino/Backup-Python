import os 
import shutil
import datetime
import schedule
import time

source_dir  # Adicionar a pasta de origem do arquivo (colocar = "")
destination_dir # Adicionar o lugar para onde o arquivo irá (colocar = "")

# Função para copiar um diretório para outro local
def copy_folder_to_directory(source, dest):
  today = datetime.date.today()# Obtém a data atual
  dest_dir = os.path.join(dest, str(today)) # Cria um novo diretório de destino com a data atual

  try:
    shutil.copytree(source, dest_dir)# Tenta copiar o diretório-fonte para o diretório de destino
    print(f"Arquivo copiado para: {dest_dir}")# Mensagem de sucesso
  except FileExistsError:
    print(f"O arquivo já existe em: {dest}")# Se o diretório já existir, exibe uma mensagem indicando isso

# Agenda a execução da função 'copy_folder_to_directory' todos os dias às 17:07
# Passando a origem (source_dir) e destino (destination_dir) como parâmetros
schedule.every().day.at("17:07").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:# Loop para manter o programa em execução e verificar tarefas agendadas
  schedule.run_pending()# Executa qualquer tarefa agendada que esteja pendente
  time.sleep(60)  # Pausa por 60 segundos antes de verificar novamente por tarefas pendentes