function login_check() {
    var elements = document.getElementsByClassName('input100')
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].getAttribute('value') === '') {
            if (elements[i].className.match('has-value')) {
                elements[i].classList.remove('has-val')
            }
        }
        else {
            if (!elements[i].className.match('has-val')) {
                elements[i].classList.add('has-val')
            }
        }
    }
}
login_check();