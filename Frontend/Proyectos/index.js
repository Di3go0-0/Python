document.querySelector('.button').addEventListener('click', function() {
    var red = Math.floor(Math.random() * 256);
    var green = Math.floor(Math.random() * 256);
    var blue = Math.floor(Math.random() * 256);
    document.querySelector('.principal').style.backgroundColor = 'rgb(' + red + ',' + green + ',' + blue + ')';
});

document.querySelector('.button').addEventListener('hover', function() {
    document.querySelector('.button').style.background = 'black';
})