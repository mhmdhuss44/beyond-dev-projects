document.getElementById("registrationForm").addEventListener("submit", function (event) {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const passwordError = document.getElementById("passwordError");
    const confirmPasswordError = document.getElementById("confirmPasswordError");

    if (password.length < 8) {
        passwordError.textContent = "Password must be at least 8 characters long.";
        event.preventDefault();
    } else {
        passwordError.textContent = "";
    }

    if (password !== confirmPassword) {
        confirmPasswordError.textContent = "Passwords do not match.";
        event.preventDefault();
    } else {
        confirmPasswordError.textContent = "";
    }
});
