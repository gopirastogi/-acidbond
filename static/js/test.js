document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Dummy check for demonstration
    if (username === 'admin' && password === 'password') {
        // Successful login
        alert('Login successful!');
        // Redirect or do something after successful login
    } else {
        // Failed login
        document.getElementById('error-msg').textContent = 'Invalid username or password. Please try again.';
    }
});