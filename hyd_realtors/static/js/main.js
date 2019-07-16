const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function () {
    $('#message').fadeout('slow');
}, 3000);