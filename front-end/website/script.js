function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}

document.addEventListener("DOMContentLoaded", () => {
    const visitorCountSpan = document.getElementById("visitor-count");

    fetch("https://0ootsin9k1.execute-api.us-west-1.amazonaws.com/prod")
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            // Assuming the API response has a field "count"
            visitorCountSpan.textContent = data.count;
        })
        .catch((error) => {
            console.error("Failed to fetch visitor count:", error);
            visitorCountSpan.textContent = "Error!";
        });
});