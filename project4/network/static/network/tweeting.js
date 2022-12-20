


document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('button').forEach(function(button) {
        button.onclick = function() {

            let twt = button.dataset.id

            fetch('like', {
                method: 'POST',
                body: JSON.stringify({
                    tweet_id: twt,
                    like_count: this.dataset.likes
                })
              })
              .then(response => response.json())
              .then(result => {
                  // Print result
                  console.log(result);
                  console.log(result['likes'])
                  let like_count = parseInt(result['likes'])
                  console.log(like_count)
                  
                let address = `#container-${this.dataset.id}`;
  
                if (like_count == 1) {
                    document.querySelector(address).innerHTML= like_count +' Like';
                } else {
                    document.querySelector(address).innerHTML= like_count +' Likes';
                }
                document.querySelector(`#${this.id}`).innerText = 'Liked';
              })
            
              


        }
    });
 });

function editbutton() {
    // TODO
    console.log('edit button activated!')
}