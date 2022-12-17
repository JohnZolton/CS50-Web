document.addEventListener('DOMContentLoaded', function() {


  // By default, load the inbox
  load_mailbox('inbox');
  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('form').onsubmit = sendmail;
});

function compose_email() {
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#spec-email').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';  
};

function sendmail() {
    let recipient = document.querySelector('#compose-recipients').value;
    let subj = document.querySelector('#compose-subject').value;
    let mailbody = document.querySelector('#compose-body').value;

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: recipient,
          subject: subj,
          body: mailbody
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    })
    .then(()=>load_mailbox('sent'));
    return false;
  }
;

function getmail(mailbox) {
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print emails
    console.log(emails);
    
    // ... do something else with emails ...
    emails.forEach(element => showmail(element));
})
};

function showmail(item) {
  const element = document.createElement('div');
  element.innerHTML = `<div style='font-weight:bold; margin-left:10px;'>${item.sender}</div> <div style='text-align:left; margin-left:20px;'>${item.subject}</div>  <div style='text-align:right; opacity:70%; margin-right: 10px'>${item.timestamp}</div>`;
  if (item.read === true){
    element.style.background = 'rgb(180, 180, 180)'
  };
  if (item.sender === document.querySelector('#cur-user').innerHTML){
    element.style.background = 'white'
  };
  element.id = 'mailbox'
  console.log(document.querySelector('#cur-user').innerHTML);
  element.addEventListener('click', function() {
    getthatmail(item.id);
    console.log(item.id);
  });
  document.querySelector('#emails-view').append(element);
};

function getthatmail(item) {
  fetch(`/emails/${item}`)
  .then(response => response.json())
  .then(email => {
    // Print emails
    console.log(email);

    // need to wipe display clean and show email
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#spec-email').style.display = 'block';
    document.querySelector('#spec-email').value = item
    document.querySelector('#heading').innerHTML = `<strong>Subject: </strong>${email.subject}`;
    document.querySelector('#body').innerHTML = `${email.body}`;
    document.querySelector('#reciever').innerHTML = `<strong>From: </strong>${email.sender}`;
    document.querySelector('#sender').innerHTML = `<strong>To: </strong>${email.recipients}`;
    document.querySelector('#timestamp').innerHTML = `<strong>Timestamp: </strong>${email.timestamp}`;
    document.querySelector('#archive-btn').addEventListener('click', send_archive);
    document.querySelector('#reply-btn').addEventListener('click', () => reply_mail(email));
    if (email.archived===false){
      document.querySelector('#archive-btn').innerHTML = 'Archive'
    } else {
      document.querySelector('#archive-btn').innerHTML = 'Remove from Archive'
    };
  })
  fetch(`/emails/${item}`, {
    method: 'PUT',
    body: JSON.stringify({
        read: true
    })
  });
};

function reply_mail(email) {
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#spec-email').style.display = 'none';
  console.log(email)
  document.querySelector('#compose-recipients').value = email.sender;
  document.querySelector('#compose-subject').value = email.subject;
  document.querySelector('#compose-body').value = '';  
};

function send_archive() {
  const item = document.querySelector('#spec-email').value;
  fetch(`/emails/${item}`)
  .then(response => response.json())
  .then(email => {
    if (email.archived === false){
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: true
        })
      });
      document.querySelector('#archive-btn').innerHTML = 'Remove from Archive'
      alert(`Added to Archived`)
    } else {
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: false
        })
      });
      document.querySelector('#archive-btn').innerHTML = 'Archive'
      alert(`Removed from Archived`)
  };  
})
  load_mailbox('inbox')
};
  
function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#spec-email').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  getmail(mailbox);
}