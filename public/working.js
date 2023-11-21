
// Function to fetch user data from the server
async function fetchUserData() {
    try {
        const response = await fetch('https://your-api-endpoint.com/users');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching user data:', error);
        return [];
    }
}

// Function to process user data and update the profile page
async function updateUserProfile() {
    // Fetch user data from the server
    const users = await fetchUserData();

    // Assuming there is a logged-in user, you can get their ID or other identifier
    const loggedInUserId = 1; // Replace with the actual logged-in user's ID

    // Find the logged-in user in the fetched data
    const loggedInUser = users.find(user => user.id === loggedInUserId);

    if (loggedInUser) {
        // Update profile page with user information
        document.getElementById("user-name").innerText = loggedInUser.name;
        document.getElementById("username-label").innerText = `Username: ${loggedInUser.username}`;
        document.getElementById("age-label").innerText = `Age: ${loggedInUser.age}`;
        document.getElementById("gender-label").innerText = `Gender: ${loggedInUser.gender}`;
        document.getElementById("hobbies-label").innerText = `Hobbies: ${loggedInUser.hobbies.join(', ')}`;
        document.getElementById("dining-label").innerText = `Dining Preferences: ${loggedInUser.diningPreferences.join(', ')}`;
    } else {
        console.error('Logged-in user not found');
    }
}

// Call the function to update the user profile when the page loads
updateUserProfile();
