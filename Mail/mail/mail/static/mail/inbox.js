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
    load_mailbox('sent')
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
  element.innerHTML = `<strong>${item.subject}</strong>, from ${item.sender}, to ${item.recipients} at ${item.timestamp}`;
  if (item.read === true){
    element.style.background = 'grey'
  };
  element.style.border = '2px solid black'
  element.style.margin = '10px'
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
    document.querySelector('#heading').innerHTML = email.subject;
    document.querySelector('#body').innerHTML = email.body;
    document.querySelector('#sender').innerHTML = email.sender;
    document.querySelector('#timestamp').innerHTML = email.timestamp;
  })
  fetch(`/emails/${item}`, {
    method: 'PUT',
    body: JSON.stringify({
        read: true
    })
  });
  document.querySelector('#archive-btn').addEventListener('click', send_archive());
};

function send_archive() {
  item = document.querySelector('#spec-email').value;
  fetch(`/emails/${item}`)
  .then(response => response.json())
  .then(email => {
    if (email.archived === true){
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: true
        })
      });
      alert(`Added to Archived`)
    } else {
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: false
        })
      });
      alert(`Removed from Archived`)
  };

  
})};
  
function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#spec-email').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  getmail(mailbox);
}