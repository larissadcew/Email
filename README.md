# 📧 Email - Cliente de Email Baseado na Web

<a href="https://www.youtube.com/watch?v=wC25I3LW3w8" target="_blank">Ver demonstração ao vivo</a>

O projeto Email é uma aplicação web que simula as funcionalidades básicas de um cliente de email. Desenvolvido com Django e JavaScript, permite que os usuários enviem, recebam e gerenciem emails através de uma interface interativa e responsiva. O Django gerencia o banco de dados e a lógica do servidor, enquanto o JavaScript manipula a interface do usuário e as requisições assíncronas para o servidor.

![image](image/image.png)

## 🔍 O Que Este Projeto Faz?

### Funcionalidades Principais:

- Gerenciamento de Caixa de Entrada: Visualize todos os emails recebidos, com status de lido/não lido. 📨
- Rastreamento de Enviados: Acesse os emails enviados pelo usuário. ✉️
- Funcionalidade de Arquivamento: Arquive e desarquive emails para manter a caixa de entrada organizada. 📂
- Composição de Email: Crie e envie emails com facilidade. ✍️
- Atualizações Dinâmicas: Interações suaves graças ao JavaScript. ⚡

### 📁 Arquivos Importantes

### O arquivo models.py define os modelos de dados da aplicação, incluindo:
## models.py
O arquivo models.py define os modelos de dados da aplicação, incluindo:

1. User: Um modelo de usuário personalizado que estende o modelo padrão do Django.
2. Email: Um modelo que representa um e-mail enviado entre usuários, contendo campos como remetente, destinatários, assunto, corpo, data/hora e status de leitura/arquivamento.

## inbox.js
O arquivo inbox.js contém a lógica do frontend, que interage com a interface do usuário e o backend. Aqui estão algumas das principais funcionalidades:

1. Manipulação de Eventos: O JavaScript aguarda o carregamento completo do DOM e adiciona ouvintes de eventos a botões para alternar entre diferentes visualizações (caixa de entrada, enviados, arquivados, composição de e-mail).

2. Requisições Assíncronas: Utiliza a API Fetch para enviar e receber dados do servidor:

3. Carregar E-mails: A função get_mail(mailbox) faz uma requisição para obter e-mails de uma caixa de correio específica e exibi-los na interface.

4. Visualizar E-mail: A função view_email(id) busca os detalhes de um e-mail específico e o exibe, além de marcar o e-mail como lido.

5. Enviar E-mail: A função Sending_mail(event) coleta os dados do formulário de composição e os envia para o servidor via POST.

 6. Atualização do Estado: Funções como archived(id) e unarchiveEmail(id) enviam requisições PUT para atualizar o estado de arquivamento de um e-mail.

### 🛠️ Instruções para Execução

# Executar testes:
```bash
python manage.py test
```

# Instalar dependências
```
pip install -r requirements.txt
```
# Fazer migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```
# Executar o servidor
```bash
python manage.py runserver
```

