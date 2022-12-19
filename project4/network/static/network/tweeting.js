


document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(function(button) {
        button.onclick = function() {
            console.log(button.dataset.id);
            let twt = button.dataset.id
            console.log(twt)
            fetch('like', {
                method: 'POST',
                body: JSON.stringify({
                    tweet_id: twt
                })
              })
              .then(response => response.json())
              .then(result => {
                  // Print result
                  console.log(result);
              })
              button.disabled=True;

        }
    });
 });

function editbutton() {
    // TODO
    console.log('edit button activated!')
}