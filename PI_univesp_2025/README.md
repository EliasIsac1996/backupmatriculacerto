# Projeto Integrador Grupo 010 - UNIVESP 2025 (Django com MySQL)

Este projeto utiliza **Django** (qualquer versão 5.x é compatível) e **MySQL** como banco de dados.


## ✅ Requisitos
```
Antes de iniciar, certifique-se de ter os seguintes pacotes instalados no seu ambiente:

- Python 3.10+ (ou compatível com Django 5)
- MySQL Server
- Virtualenv (opcional, mas recomendado)

```

## 📦 Dependências Python

### 1. Criação e ativação do ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 2. Instalação das dependências:

Instale todas as dependências com:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` já contém as bibliotecas necessárias para rodar o projeto:

- **Django 5.2** ou superior
- **mysqlclient** para conexão com o MySQL

---

## 🗄️ Configuração do Banco de Dados

Este projeto utiliza um banco de dados **MySQL**. Para configurá-lo corretamente, siga os passos abaixo:

### 1. Criar o banco de dados:

Acesse o MySQL e crie o banco de dados:

```sql
CREATE DATABASE pi_univesp;
```

### 2. Criar o usuário no MySQL:

Crie um usuário com a senha usada no `settings.py`:

```sql
CREATE USER 'pi'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON pi_univesp.* TO 'pi'@'localhost';
FLUSH PRIVILEGES;
```

### 3. Migrar o Banco de dados:
Faça as migrações do banco de dados padrão do Django para o MySQL:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Importar o backup:

Navegue até o diretório fora da pasta do projeto, onde está o arquivo `bkp.sql`, e importe o banco:

```bash
mysql -u pi -p pi_univesp < bkp.sql
```

Quando pedir a senha, digite: `1234`
(Observação: Em caso de atualização, caso ocorra um erro de importação devido a tabelas já criadas, remova o banco anterior e importe a nova versão.

```sql
DROP DATABASE pi_univesp;
CREATE DATABASE pi_univesp;
EXIT;
```
```bash
mysql -u pi -p pi_univesp < bkp.sql
```
---

## 🚀 Rodando o Projeto

Depois de configurar o banco de dados e as dependências, você pode rodar o servidor de desenvolvimento do Django com o seguinte comando:

```bash
python manage.py runserver
```

Acesse o navegador em:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 Informações Adicionais

- O login de usuários utiliza a autenticação padrão do Django.
- Para acessar a área de administração (`/admin`), crie um superusuário (opcional):

```bash
python manage.py createsuperuser
```

---

## ⚠️ Observações
- Certifique-se de que o banco de dados MySQL está em funcionamento antes de rodar o projeto.
- O arquivo `bkp.sql` deve estar no diretório correto para ser importado com sucesso.
