
import threading
from time import sleep

datashows = [
    {"id": 1, "reservas": []},
    {"id": 2, "reservas": []},
    {"id": 3, "reservas": []}
]

# Lock para sincronização
lock = threading.Lock()

# Função para verificar disponibilidade de um datashow
def disponivel(datashow, dia, hora_inicio, hora_fim):
    for reserva in datashow["reservas"]:
        if reserva["dia"] == dia and not (hora_fim <= reserva["hora_inicio"] or hora_inicio >= reserva["hora_fim"]):
            return False
    return True

# Função para reservar um datashow
def reservar_datashow(datashow_id, dia, hora_inicio, hora_fim):
    with lock:  # Garante que apenas uma thread acesse os datashows por vez
        for datashow in datashows:
            if datashow["id"] == datashow_id:
                if disponivel(datashow, dia, hora_inicio, hora_fim):
                    datashow["reservas"].append({"dia": dia, "hora_inicio": hora_inicio, "hora_fim": hora_fim})
                    print(f"Datashow {datashow_id} reservado para {dia} das {hora_inicio} às {hora_fim}.")
                else:
                    print(f"Datashow {datashow_id} não está disponível para {dia} das {hora_inicio} às {hora_fim}.")
# caso já esteja reservado ele informa que não esta disponível
def usuario(nome, datashow_id, dia, hora_inicio, hora_fim):
    print(f"Usuário {nome} tentando reservar datashow {datashow_id}...")
    reservar_datashow(datashow_id, dia, hora_inicio, hora_fim)
    sleep(1)

# Criando threads para múltiplos usuários
threads = [
    threading.Thread(target=usuario, args=("Alice", 1, "segunda", 10, 12)),
    threading.Thread(target=usuario, args=("Bob", 1, "segunda", 11, 13)),
    threading.Thread(target=usuario, args=("Carol", 2, "terça", 14, 16)),
    threading.Thread(target=usuario, args=("Dave", 1, "segunda", 9, 11)),
    threading.Thread(target=usuario, args=("Eve", 3, "quarta", 15, 17))
]

# Iniciando as threads
for t in threads:
    t.start()

# Esperando todas as threads terminarem
for t in threads:
    t.join()

# Mostrando as Reservas
print("\nEstado final dos datashows:")
for datashow in datashows:
    print(f"Datashow {datashow['id']} - Reservas: {datashow['reservas']}")
