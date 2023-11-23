// Sample user data (replace this with your actual user data)
const users = [
    { id: 1, name: 'User1', age: 25, hobbies: ['cooking', 'reading'], diningPreferences: ['Italian', 'Vegetarian'], availability: 'Weekends' },
    { id: 2, name: 'User2', age: 30, hobbies: ['traveling', 'painting'], diningPreferences: ['Mexican', 'Seafood'], availability: 'Evenings' },
    // Add more users...
];

// Function to find matches based on user preferences
function findMatches(currentUser) {
    const matches = [];

    for (const user of users) {
        // Exclude the current user from the list of potential matches
        if (user.id !== currentUser.id) {
            // Compare prfile features ie the interests, age, dining preferences, and availability
            const commonHobbies = user.hobbies.filter(hobby => currentUser.hobbies.includes(hobby));
            const commonPreferences = user.diningPreferences.filter(preference => currentUser.diningPreferences.includes(preference));

            // Adjusting the weights based on the importance of the factors
            const ageDifference = Math.abs(user.age - currentUser.age);
            const commonHobbiesWeight = commonHobbies.length;
            const commonPreferencesWeight = commonPreferences.length;

            // TODO: 
            // Customize the algorithm further based on the other features that will arise as we develop it
            const matchScore = ageDifference + commonHobbiesWeight + commonPreferencesWeight;

            // Consider a match if the score is below a certain threshold
            if (matchScore < 5) {
                matches.push({ user, matchScore });
            }
        }
    }

    // Sort matches by score 
    // (I have opted for ascending order)
    matches.sort((a, b) => a.matchScore - b.matchScore);

    // Return the top matches
    return matches.map(match => match.user);
}

// Example usage
const currentUser = users[0]; // Replace this with the logged-in user
const potentialMatches = findMatches(currentUser);
console.log('Potential Matches:', potentialMatches);
