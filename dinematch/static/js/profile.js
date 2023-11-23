
// Sample user details (replace this with actual user data)
const currentUser = {
    name: "Jack Brian",
    username: "jack",
    age: 25,
    gender: "Male",
    hobbies: ["Cooking", "Reading"],
    diningPreferences: "Vegetarian"
};

// Set user information on the profile page
document.getElementById("user-name").innerText = currentUser.name;
document.getElementById("username-label").innerText += currentUser.username;
document.getElementById("age-label").innerText += currentUser.age;
document.getElementById("gender-label").innerText += currentUser.gender;
document.getElementById("hobbies-label").innerText += currentUser.hobbies.join(", ");
document.getElementById("dining-label").innerText += currentUser.diningPreferences;
