# Projeto Koper Routes

API para cálculo do trajeto menos custoso baseada em malhas logísticas
---

## Clone

```bash
git clone 
```

## ou faça o download

https://
ou

```bash
wget https://
```

## Ambiente

Python 3.6+
Ative a sua virtualenv

```bash
pip install -r requirements.txt
```

## Testando

```bash
pytest api-best-track/tests
```

## Executando

```bash
flask create-db  # rodar uma vez
flask populate-db # rodar uma vez
flask run
```

Acesse:

- Website: http://localhost:5000
- API GET:
  - https://localhost:5000/api/calculate-track/map/


## Structure

```bash
.

```