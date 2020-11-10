# Projeto Koper Routes

API para calculo do trajeto de menor custo  baseado em uma malha logistica de referencia, na perfomance estimada do 
veiculo e no custo estipulado do combustivel. O processo utiliza o algoritmo de Djikstra para efetuar o referido calculo.
---

## Requisitos
- Python 3.6+
- VirtualEnv

## Clonar projeto
```bash
git clone https://github.com/LePiN/desafio-koper.git
```

## Criar ambiente virtual

### Ambiente Linux

Criar virtualenv dentro do projeto:
```
virtualenv -p /usr/bin/python3.6 .venv
```

Ativar virtualenv:
```
source .venv/bin/activate
```

### Ambiente Windows

Criar diretório da virtualenv dentro do projeto:
```
mkdir .venv
```

Criar virtualenv:
```
virtualenv.exe .venv
```

Ativar virtualenv:
```
.venv\Scripts\activate
```

## Instalar as dependências do projeto
```
pip install --upgrade pip
pip install -r requirements.txt
```


## Teste do projeto

Efetuar teste unitários:
```
pytest test\ -v
```

Efetuar teste de convenção de código:
```
black api/
make code-convention
flake8 --exclude=.venv --max-line-length=120
```

Limpar os dados gerados pelos testes:
```
@find . -name '*.pyc' -exec rm -rf {} \;
@find . -name '__pycache__' -exec rm -rf {} \;
@find . -name 'Thumbs.db' -exec rm -rf {} \;
@find . -name '*~' -exec rm -rf {} \;
rm -rf .cache
rm -rf build
rm -rf dist
rm -rf *.egg-info
rm -rf htmlcov
rm -rf .tox/
rm -rf docs/_build
```

## Executando

Criar banco de dados (rodar uma vez antes de criar o servidor)
```bash
flask create-db
```

Caso queira popular o banco com valores simulados (rodar uma vez antes de criar o servidor):
```bash
flask populate-db
```

Iniciar o servidor para uso:
```bash
flask run
```

Acesse:

- Website: http://localhost:5000/
- SERVIÇOS DISPONÍVEIS:
    - BUSCAR MAPA LOGISTICO PERSISTIDO:
        - http://127.0.0.1:5000/find-map/<string: name_map>/
    - PERSISTIR NOVO MAPA LOGISTICO:
        - http://127.0.0.1:5000/add-map/
            - Body (estrutura)
            ````bash
            {
              "map_name": "string",
              "map_file": [list
                [list],  
                ["string", "string",float],
                [...],      
              ]
            }
            ````
            - Body (exemplo)
                ```json
                {
                  "map_name":"Koper MOCK network",
                  "map_file":[
                    ["A", "B", 10.0],  
                    ["B", "C", 25.0],
                    ["C", "D", 30.0],
                    ["D", "E", 30.0],        
                    ["A", "C", 50.0],
                    ["B", "D", 15.0],
                    ["C", "E", 45.0],               
                    ["B", "E", 50.0],
                    ["A", "D", 90.0]        
                  ]
                }
                ```
    - REMOVER MAPA LOGISTICO PERSISTIDO:
        - http://127.0.0.1:5000/delete-map/<string: name_map>/
    - BUSCAR MELHOR ROTA:
        - http://127.0.0.1:5000/find-best-track/<string: name_map>/
        - Body (estrutura)
            ```bash
            {
              "map_name":"string",
              "start_point":"string",
              "destination_point":"string",
              "vehicle_performance":float,
              "fuel_cost":float 
            }
            ````
        - Body (example)
            ```json
            {
              "map_name":"Koper MOCK network",
              "start_point":"A",
              "destination_point":"D",
              "vehicle_performance":10.0,
              "fuel_cost":2.5 
            }
            ```
        - Result
            ```json
            {
              "map_name": "Koper MOCK network",
              "start_point": "A",
              "destination_point": "D",
              "vehicle_perfomance": 10.0,
              "fuel_cost": 2.5,
              "best_track": [
                "A",
                "B",
                "D"
              ],
              "best_track_distance": 25.0,
              "best_track_cost": 6.25
            }
            ```
    - BUSCAR MELHOR ROTA (CONFIRMAÇÃO POR OUTRO ALGORITMO):
        - http://127.0.0.1:5000/find-best-track/<string: name_map>/
        - Body (estrutura)
            ```bash
            {
              "map_name":"string",
              "start_point":"string",
              "destination_point":"string",
              "vehicle_performance":float,
              "fuel_cost":float 
            }
            ````
        - Body (example)
            ```json
            {
              "map_name":"Koper MOCK network",
              "start_point":"A",
              "destination_point":"D",
              "vehicle_performance":10.0,
              "fuel_cost":2.5 
            }
            ```
        - Result
            ```json
            {
              "map_name": "Koper MOCK network",
              "start_point": "A",
              "destination_point": "D",
              "vehicle_perfomance": 10.0,
              "fuel_cost": 2.5,
              "best_track": [
                "A",
                "B",
                "D"
              ],
              "best_track_distance": 25.0,
              "best_track_cost": 6.25
            }
            ```

## Construído com:
- Python3
- Flask
- Networkx
- TOML


## Observação:
- O algoritmo de confirmação referenciado encontra-se em https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python.

## Autor
- Leandro Pieper Nues - lpnunes@gmail.com - https://www.linkedin.com/in/leandro-pieper-nunes/