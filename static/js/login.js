function login() {
    showLoadingState('loginForm');
    var loginForm = $('#loginForm');
    var email = loginForm.find('#email').val();
    var password = loginForm.find('#password').val();
    if (email.length == 0 || password.length == 0) {
        loginForm.find('#email-error').removeClass('element-hide');
        loginForm.find('#password-error').removeClass('element-hide');
        showLoadedState('loginForm');
    } else {
        $.post(API_URL + 'login/', loginForm.serialize())
            .done(function (response) {
                if (response.success == true) {
                    if (response.redirect) {
                        window.location.href = response.redirect;
                    }
                } else if (response.success == false) {
                    loginForm.find('#password-form-error').removeClass('element-hide').text(response.errorMsg)
                }
                showLoadedState('loginForm');
            })
    }
}