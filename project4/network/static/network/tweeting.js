document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(function(button) {
        button.onclick = function() {
            let csrf = getcookie('csrftoken');
            let tweet = button.dataset.id

            if (this.dataset.type === 'like') {
                fetch('like', {
                    method: 'POST',
                    headers:{'X-CSRFToken': csrf},
                    body: JSON.stringify({
                        tweet_id: tweet,
                        like_count: this.dataset.likes
                    })
                  })
                  .then(response => response.json())
                  .then(result => {
                    let like_count = parseInt(result['likes'])
                    let address = `#container-${this.dataset.id}`;
      
                    if (like_count == 1) {
                        document.querySelector(address).innerHTML= like_count +' Like';
                    } else {
                        document.querySelector(address).innerHTML= like_count +' Likes';
                    }
                    
                    document.querySelector(`#${this.id}`).innerText = 'Liked';
                    this.dataset.type = 'unlike'
                  })}

            if (this.dataset.type === 'unlike') {
                fetch('unlike', {
                    method: 'POST',
                    headers:{'X-CSRFToken': csrf},
                    body: JSON.stringify({
                        tweet_id: tweet,
                        like_count: this.dataset.likes})
                    })
                    .then(response => response.json())
                    .then(result => {
                    let like_count = parseInt(result['likes'])
                    let address = `#container-${this.dataset.id}`;
        
                    if (like_count == 1) {
                        document.querySelector(address).innerHTML= like_count +' Like';
                    } else {
                        document.querySelector(address).innerHTML= like_count +' Likes';
                    }

                    document.querySelector(`#${this.id}`).innerText = 'Like';
                    this.dataset.type = 'like'
                    })}

            if (this.dataset.type === 'save'){
                let area_address = `#text-${this.id}`
                let tweet_body = document.querySelector(area_address).value;

                fetch('edit',{
                    method:'POST',
                    headers:{'X-CSRFToken': csrf},
                    body: JSON.stringify({
                        tweet_id: tweet,
                        body: tweet_body})
                    })
                    .then(response => response.json())
                    .then(result => {
                        let newbody = result['tweet_body']
                        document.querySelector(`#${this.id}`).innerHTML= 'Edit'
                        this.dataset.type = 'edit';
                        document.querySelector(`#body-${this.dataset.id}`).innerHTML = newbody;
                })
            }
            if (this.dataset.type === 'edit'){
                let address = `#body-${this.dataset.id}`
                let tweet_body = document.querySelector(address).innerHTML;
                this.dataset.type = 'save'
                document.querySelector(`#${this.id}`).innerText = 'Save';
                document.querySelector(address).innerHTML=  `<textarea class='editbox' id='text-${this.id}' maxlength="140" rows="4">${tweet_body}</textarea>`;
            }

            if (this.dataset.type === 'unfollow') {
                fetch('unfollow',{
                    method:'POST',
                    headers:{'X-CSRFToken': csrf},
                    body: JSON.stringify({
                        acc_to_follow: this.dataset.account
                    })
                    })
                    .then(response => response.json())
                    .then(result => {
                        this.dataset.type='follow'
                        document.querySelector(`#${this.id}`).innerHTML = 'Follow'
                        if (result.followers === 1) {
                            document.querySelector('#follower_count').innerText = `${result.followers} Follower`
                        } else {
                            document.querySelector('#follower_count').innerText = `${result.followers} Followers`
                        }
                })}

            if (this.dataset.type === 'follow') {
                fetch('follow',{
                    method:'POST',
                    headers:{'X-CSRFToken': csrf},
                    body: JSON.stringify({
                        acc_to_follow: this.dataset.account
                    })
                    })
                    .then(response => response.json())
                    .then(result => {
                        this.dataset.type='unfollow';
                        document.querySelector(`#${this.id}`).innerHTML = 'Unfollow'
                        if (result.followers === 1) {
                            document.querySelector('#follower_count').innerText = `${result.followers} Follower`
                        } else {
                            document.querySelector('#follower_count').innerText = `${result.followers} Followers`
                        }
                })}
        }
    });
 });


 function getcookie(name) {
    let cookievalue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookievalue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookievalue;
}