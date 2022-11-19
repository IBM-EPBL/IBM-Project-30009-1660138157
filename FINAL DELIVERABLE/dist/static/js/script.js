
const form = document.getElementById('form');
const name = document.getElementById('name');
const email = document.getElementById('email');
const password = document.getElementById('password');
const confirm = document.getElementById('confirm');
const phoneno = document.getElementById('phoneno');
const dob = document.getElementById('dob');

form.addEventListener('submit', e => {
    // e.preventDefault();

    checkInputs();
});

function checkInputs() {
    // trim to remove the whitespaces
    const nameValue = name.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const confirmValue = confirm.value.trim();
    const phonenoValue = confirm.value.trim();
    const DobValue = dob.value.trim();

    if (nameValue === '') {
        setErrorFor(name, 'Please enter your name');
        return false;
    } else {
        setSuccessFor(name);
    }

    if (emailValue === '') {
        setErrorFor(email, 'Please enter your email');
        return false;
    } else if (!isEmail(emailValue)) {
        setErrorFor(email, 'Email not valid');
        return false;
    } else {
        setSuccessFor(email);
    }

    if (passwordValue === '') {
        setErrorFor(password, 'Please enter password');
        return false;
    } else if (!isPassword(passwordValue)) {
        setErrorFor(password, 'atleast one number, one uppercase, lowercase letter, and atleast 8 character');
        return false;
    } else {
        setSuccessFor(password);
    }

    if (confirmValue === '') {
        setErrorFor(confirm, 'Please re-enter password');
        return false;
    } else if (!isConfirm(confirmValue)) {
        setErrorFor(confirm, 'Invalid password');
    } else if (passwordValue !== confirmValue) {
        setErrorFor(confirm, 'Passwords does not match');
        return false;
    } else {
        setSuccessFor(confirm);
    }

    if (phonenoValue === '') {
        setErrorFor(phoneno, 'Please enter mobile number');
        return false;
    }
    else {
        setSuccessFor(phoneno);
    }
    if (DobValue === '') {
        setErrorFor(dob, 'Please enter your dob');
        return false;
    } else if (DobValue < 18) {
        setErrorFor(dob, 'Your age is not allowed');
        return false;

    } else {
        setSuccessFor(dob);
    }

    return true;
}

function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    formControl.className = 'form-control error';
    small.innerText = message;
}

function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
}

function isEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

function isPassword(password) {
    return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/.test(password);
}

function isConfirm(confirm) {
    return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/.test(password) == / ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/.test(password);

}

function isDob(dob) {


    str = str.split("-");
    var dd = str[0];
    var mm = str[1];
    var yy = str[2];
    // Current date calculation
    var d = new Date();
    var ds = d.getDate();
    var ms = d.getMonth();
    var ys = d.getFullYear();
    // convert 18years as days from current date
    var days = ((18 * 12) * 30) + (ms * 30) + ds;
    // convert days from input value
    var age = (((ys - yy) * 12) * 30) + ((12 - mm) * 30) + parseInt(30 - dd);
    return age.test(dob);


}

