function signUp() {
    showLoadingState('signUpForm');
    isValid = true;
    var signUpModal = $('#signUpForm');
    // take the values from form input
    email = signUpModal.find('#email').val();
    password = signUpModal.find('#password').val();
    cpassword = signUpModal.find('#cpassword').val();

    // Validate email format
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    eres = re.test(email.toLowerCase());
    if (eres) {
        signUpModal.find('#email-error').addClass('element-hide');
    } else {
        signUpModal.find('#email-error').removeClass('element-hide');
        isValid = false;
    }

    // Validate password and confirm password
    isPasswordCorrect = password.localeCompare(cpassword);
    if (isPasswordCorrect == 1 || isPasswordCorrect == -1 || password.length == 0 || cpassword.length == 0) {
        signUpModal.find('#password-error').removeClass('element-hide');
        isValid = false;
    } else {
        signUpModal.find('#password-error').addClass('element-hide');
    }

    // Submit form if all validation are true
    if (isValid) {
        $.post(API_URL + 'signup/', signUpModal.serialize())
            .done(function (response) {
                var successResSpan = signUpModal.find('#success-msg');
                var emailResSpan = signUpModal.find('#email-success');
                if (response.success == true) {
                    if (response.redirect) {
                        window.location.href = response.redirect;
                    }
                    emailResSpan.addClass('element-hide');
                    successResSpan.removeClass('element-hide').text(response.successMsg);
                } else {
                    successResSpan.addClass('element-hide');
                    emailResSpan.removeClass('element-hide').text(response.errorMsg)
                }
                showLoadedState('signUpForm');
            }).fail(function (error) {
                signUpModal.find('#success-msg').addClass('element-hide');
                signUpModal.find('#email-success').removeClass('element-hide').text('Email already exists');
            showLoadedState('signUpForm');
        });
    } else {
        showLoadedState('signUpForm');
        console.log('something wrong')
    }
}

function passwordToggle() {
    var passwordElement = $('#signupModal #password');
    if (passwordElement.attr('type') === 'password') {
        passwordElement.attr('type', 'text');
    } else {
        passwordElement.attr('type', 'password')
    }
}