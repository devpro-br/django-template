# Backend Django

Nessa pasta se encontram os arquivos de backend do projeto Django.

Será usado o Poetry  como gestor pacotes.

Por isso, para instalar o projeto com as dependência de desenvolvimento, dentro das pasta backend rode

```bash
poetry install --with dev
```

Para rodar seu servidor Django ative o ambiente virtual:

```bash
poetry shell
```

Então rode

```bash
python manage.py runserver
```

## Padrão de código
Para o backend esse projeto usa o flake8, com as seguintes customizações

Tamanho de linha pode ter até 120 caracteres. Para ver o relatório do linter rode:


```bash
flake8 .
```

