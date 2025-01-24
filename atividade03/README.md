
## Objetivo
- Permitir múltiplas solicitações simultâneas de reservas para datashows.
- Garantir que não ocorram conflitos de horário nas reservas.
- Usar **threads** para simular concorrência e **locks** para sincronizar acessos.

## Estrutura do Código

### Componentes Principais

1. **Lista de Datashows**
   - Cada datashow é representado como um dicionário com:
     - `id`: Identificador único do datashow.
     - `reservas`: Lista de reservas feitas para o datashow.

2. **Funções**
   - `disponivel(datashow, dia, hora_inicio, hora_fim)`:
     - Verifica se um datashow está disponível no horário solicitado.
   - `reservar_datashow(datashow_id, dia, hora_inicio, hora_fim)`:
     - Faz a reserva de um datashow, garantindo que não haja conflitos.
   - `usuario(nome, datashow_id, dia, hora_inicio, hora_fim)`:
     - Simula um usuário tentando fazer uma reserva.

3. **Threads**
   - Cada thread representa um usuário tentando reservar um datashow.
   - O acesso à lista de datashows é sincronizado usando `threading.Lock`.

## Como Executar

1. Certifique-se de ter Python 3 instalado.
2. Salve o código em um arquivo chamado `datashow_threading.py`.
3. Execute o arquivo no terminal:
   ```bash
   python datashow_threading.py
   ```

## Exemplo de Saída

Quando o programa é executado, múltiplos usuários tentarão reservar datashows simultaneamente. A saída mostrará quais reservas foram bem-sucedidas e quais falharam devido a conflitos de horário.

Exemplo:
```
Usuário Alice tentando reservar datashow 1...
Datashow 1 reservado para segunda das 10 às 12.
Usuário Bob tentando reservar datashow 1...
Datashow 1 não está disponível para segunda das 11 às 13.
Usuário Carol tentando reservar datashow 2...
Datashow 2 reservado para terça das 14 às 16.
Usuário Dave tentando reservar datashow 1...
Datashow 1 reservado para segunda das 9 às 11.
Usuário Eve tentando reservar datashow 3...
Datashow 3 reservado para quarta das 15 às 17.

Estado final dos datashows:
Datashow 1 - Reservas: [{'dia': 'segunda', 'hora_inicio': 10, 'hora_fim': 12}, {'dia': 'segunda', 'hora_inicio': 9, 'hora_fim': 11}]
Datashow 2 - Reservas: [{'dia': 'terça', 'hora_inicio': 14, 'hora_fim': 16}]
Datashow 3 - Reservas: [{'dia': 'quarta', 'hora_inicio': 15, 'hora_fim': 17}]
```

## Funcionalidades de Concorrência
- **Threads**: Cada usuário é representado por uma thread que tenta fazer uma reserva.
- **Lock**: O `threading.Lock` é usado para evitar que múltiplas threads modifiquem a lista de datashows ao mesmo tempo, prevenindo conflitos.

## Branches
- Implementação inicial: `feature/atividade-01-20242`
- Correções: `bugfix/atividade-01-20242`(Se necessãrio)

---

