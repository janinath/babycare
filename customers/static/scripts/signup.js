function validateForm() {
    // Reset error messages and styles
    document.getElementById('nameerror').innerText = '';
    document.getElementById('emailerror').innerText = '';
    document.getElementById('moberror').innerText = '';
    document.getElementById('pswd1error').innerText = '';
    document.getElementById('pswd2error').innerText = '';

    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var mobile = document.getElementById('mobile').value;
    var password1 = document.getElementById('pswd1').value;
    var password2 = document.getElementById('pswd2').value;

    var isValid = true;

    if (name.trim() === '') {
      document.getElementById('nameerror').innerText = 'Please enter your name';
      document.getElementById('nameerror').style.color='red'

      isValid = false;
    }

    if (email.trim() === '') {
      document.getElementById('emailerror').innerText = 'Please enter your email';
      document.getElementById('emailerror').style.color='red'

      isValid = false;
    }

    if (mobile.trim()==''){
        document.getElementById('moberror').innerText = 'Please enter your mobile';
        document.getElementById('moberror').style.color='red'
        isValid = false;
    }
    // Mobile number validation can be added if needed

    if (password1.trim() === '') {
      document.getElementById('pswd1error').innerText = 'Please enter a password';
      document.getElementById('pswd1error').style.color='red'
      isValid = false;
    }

    if (password2.trim() === '') {
      document.getElementById('pswd2error').innerText = 'Please repeat the password';
      document.getElementById('pswd2error').style.color='red'
      isValid = false;
    }

    if (password1 !== password2) {
      document.getElementById('pswd2error').innerText = 'Passwords do not match';
      document.getElementById('pswd2error').style.color='red'
      isValid = false;
    }

    return isValid;
  }
