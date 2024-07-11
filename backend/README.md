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

# Usuário padrão

Nesse projeto o usuário foi customizado. Ele não tem username nem last_name como o usuário padrão do Django.
Ele usa o login como identificador único. O usuário se encontra na app base para que você pode acrescentar acampos de 
acordo com sua necessidade.

