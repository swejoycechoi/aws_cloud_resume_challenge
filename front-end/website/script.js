function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}

const apiUrl = 'https://0ootsin9k1.execute-api.us-west-1.amazonaws.com/prod/visitor-counter';

async function getVisitorCount() {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse JSON response
        const data = await response.json();
        console.log('API Response:', data); // Debugging: Should log { visitor_count: 60 }

        // Extract visitor count and display it
        const visitorCount = data.visitor_count; // Ensure key matches exactly
        document.getElementById('visitor-count').textContent = visitorCount;

    } catch (error) {
        console.error('Failed to fetch visitor count:', error);
        document.getElementById('visitor-count').textContent = 'Error';
    }
}

window.addEventListener('DOMContentLoaded', getVisitorCount);