// Aguarda o carregamento completo do DOM antes de executar o código
document.addEventListener('DOMContentLoaded', function() {

  // Usa botões para alternar entre as visualizações
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Se o email for enviado, chama a função Sending_mail
  document.querySelector('#compose-form').addEventListener('submit', Sending_mail);

  // Por padrão, carrega a caixa de entrada
  load_mailbox('inbox');
});


// Função para limpar a visualização do corpo do email
function clear_body(){

  // Esconde as visualizações de emails e de composição
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

}

// Função para exibir o formulário de composição de email com dados preenchidos
function entry(recipients, subject, timestamp){

  // Exibir o formulário de composição de e-mail
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';

  // Limpar os campos do formulário
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // Preencher os campos do formulário com os dados fornecidos
  document.querySelector('#compose-recipients').value = recipients;
  document.querySelector('#compose-subject').value = subject;
  document.querySelector('#compose-body').value = timestamp;

}


// Função para arquivar um email
function archived(id){

  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: true
    })
  })

  // Limpa a visualização do corpo do email
  clear_body();
}

// Função para desarquivar um email
function unarchiveEmail(id){

  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: false
    })
  })  

  // Limpa a visualização do corpo do email
  clear_body();

}

// Função para visualizar um email
function view_email(id){
  
  // Limpa toda a página
  clear_body();

  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Imprime o email no console
      console.log(email);

      // Cria um novo div para exibir o email
      displaydiv = document.createElement('div');

      // Marca o email como lido
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
          read: true
        })
      })

      displaydiv.style.margin = '2px';

      const isArchived  = email.archived;
      const isArchivedLabel = isArchived ? 'Unarchive' : 'Archive';

      displaydiv.innerHTML = `
      <p>From: ${email.sender}</p>
      <p>To: ${email.recipients}</p>
      <p>Subject: ${email.subject}</p>
      <p>Timestamp: ${email.timestamp}</p>
      <button class="btn btn-danger" id="entry">Entry</button>
      <button class="btn btn-primary" id="Archived">${isArchivedLabel}</button>
      </br>
      <hr>
      <p>Timestamp: ${email.body}</p>
      `

      // Adiciona o div criado à visualização de emails
      document.querySelector('#emails-view').innerHTML = '';
      document.querySelector('#emails-view').append(displaydiv);
      document.querySelector('#emails-view').style.display = 'block';

      // Adiciona evento de clique ao botão #entry
      document.querySelector('#entry').addEventListener('click', () => {
        // Passa os parâmetros para a função entry
        entry(email.recipients, email.sender, email.subject, email.timestamp);
      });

      // Adiciona evento de clique ao botão #Archived
      document.querySelector('#Archived').addEventListener('click', () => {
        if(email.archived){
          unarchiveEmail(email.id);
        } else {
          archived(email.id);
        }
      });
  });
}

// function to get mail
function get_mail(mailbox){

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);

      // iterate over each email
      emails.forEach(email => {

        // create new div to display mail
        const mailDiv = document.createElement('div');
        mailDiv.classList.add('email');

        // set background color based on read status
        if(email.read){
          mailDiv.style.backgroundColor = '#FAFAFA';
        }else{
          mailDiv.style.backgroundColor = '#ffffff';
        }

        // add border and padding
        mailDiv.style.border = '1px solid #ccc';
        mailDiv.style.padding = '10px';
        mailDiv.style.marginBottom = '10px';
        mailDiv.style.border = '1px solid black';
    

        // set content of email div
        mailDiv.innerHTML = `
          <p style="font-weight: bold;">From: ${email.sender}</p>
          <p style="margin-bottom: 5px;">Subject: ${email.subject}</p>
          <p style="margin-bottom: 5px;">Timestamp: ${email.timestamp}</p>
          `;

       // add click event listener to view email details
       mailDiv.addEventListener('click', () => {
        view_email(email.id);
      });
      
      // append email div to emails-view
      document.querySelector('#emails-view').append(mailDiv);

      });
  });

}

// Função para exibir a visualização de composição de email e esconder outras visualizações
function compose_email() {

  // Mostrar a visualização de composição e esconder outras visualizações
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Limpar os campos de composição
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

// Função para carregar a caixa de correio
function load_mailbox(mailbox) {
  
  // Mostrar a caixa de correio e esconder outras visualizações
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Mostrar o nome da caixa de correio
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Aqui temos acesso a todos os mailbox
  get_mail(mailbox);
}

// Função para enviar email
function Sending_mail(event){

  event.preventDefault();

  // Pegando os valores dos campos de composição
  recipients = document.querySelector('#compose-recipients').value;
  subject = document.querySelector('#compose-subject').value;
  body = document.querySelector('#compose-body').value;

  // Enviando o email
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Imprimir o resultado
      console.log(result);
  });

  // Por padrão, carregar a caixa de entrada
  load_mailbox('inbox');
}
