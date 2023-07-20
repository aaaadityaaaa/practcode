// // on logindata submite
console.log("login js linked...")
$(document).on('submit', '#post-userlogin_form', function (e) {
    e.preventDefault();
    
    // Downloader_section.innerHTML=containt_text;

    $.ajax({
        type: 'POST',
        url:'/Authlogin/',
        data: {
            username: $('#username').val(),
            password: $('#password').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            document.getElementById('loginmsg').innerText=data['message']
            if(data['error']){
                document.getElementById('loginmsg').style.display="block"
                document.getElementById('loginmsg').style.color="red"
                document.getElementById('loginmsg').style.border="1px solid red"
                document.getElementById('loginmsg').style.backgroundColor= "rgba(252, 189, 189, 0.5)"
            }else{
                console.log("success !",data['message'])
                document.getElementById('loginmsg').style.display="block"
                document.getElementById('loginmsg').style.color="green"
                document.getElementById('loginmsg').style.border="1px solid greenyellow"
                document.getElementById('loginmsg').style.backgroundColor= "rgba(189, 252, 189, 0.5)"
            }
            


        }
    })
})

