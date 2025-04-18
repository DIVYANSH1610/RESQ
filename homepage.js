// Hamburger Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('toggle');
});

// Explore Button Functionality
const exploreBtn = document.querySelector('.explore-btn');
exploreBtn.addEventListener('click', () => {
    // Simulate redirecting to an updates page
    alert('Redirecting to the latest disaster updates...');
    // You can replace the alert with a redirect:
    // window.location.href = 'updates.html';
});

// Info Cards Click Functionality
const cards = document.querySelectorAll('.card');
cards.forEach(card => {
    card.addEventListener('click', (e) => {
        // Prevent the "Get Help" button click from triggering the card click
        if (e.target.classList.contains('help-btn')) return;

        const info = card.getAttribute('data-info');
        alert(Details: ${info});
    });
});

// Get Help Button Functionality
const helpBtn = document.querySelector('.help-btn');
helpBtn.addEventListener('click', () => {
    alert('Contacting Emergency Services...\nCall: 911\nOr visit your nearest emergency center.');
});

// Simulate Dynamic Updates
const updateText = document.querySelector('#update-text');
const updates = [
    "Flood warning issued for City A. Evacuation in progress.",
    "Earthquake alert in Region B. Stay safe and follow guidelines.",
    "Hurricane approaching Coastal Area C. Prepare emergency kits."
];

let currentUpdateIndex = 0;

function displayNextUpdate() {
    updateText.textContent = updates[currentUpdateIndex];
    currentUpdateIndex = (currentUpdateIndex + 1) % updates.length;
}

// Display the first update immediately
displayNextUpdate();

// Rotate updates every 5 seconds
setInterval(displayNextUpdate, 5000);