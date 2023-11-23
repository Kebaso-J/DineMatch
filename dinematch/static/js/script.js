// script.js

// Sample user data (replace this with your actual user data)
const users = [
    { username: 'user1', password: 'password1', name: 'User1' },
    { username: 'user2', password: 'password2', name: 'User2' },
    // Add more users...
];

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Find the user with the provided username
    const user = users.find(u => u.username === username);

    if (user && user.password === password) {
        // Authentication successful
        alert('Login successful!');
        // Redirect to the profile page
        window.location.href = 'profile.html';
    } else {
        // Authentication failed
        alert('Invalid username or password. Please try again.');
    }
}
