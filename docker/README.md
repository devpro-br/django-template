# Pasta de Arquivos docker

Nessa pasta está o arquivo docker-compose.yml. 

Ele possui um postgres para execução do ambiente local. Por padrão ele roda com configurações padrão da imagem do Posgres:
Usuário e senha: postgres
Porta: 5432

Para rodar, navegue até o diretório docker e rode o comando:

```bash
docker compose up -d
```

Por padrão ao rodar em ambiente local também está sendo usado o nginx rodando na porta 80.
Ele funciona como proxy reverso para a aplicação Django rodando na porta 8000.
E também serve os estático gerados pelo Django se não tiver um bucket definido.