function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}

document.addEventListener("DOMContentLoaded", () => {
    const visitorCountSpan = document.getElementById("visitor-counter");

    fetch("https://0ootsin9k1.execute-api.us-west-1.amazonaws.com/prod/visitor-counter", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            // Assuming the API response has a field "visitor_count"
            visitorCountSpan.textContent = `Visitor Count: ${data.visitor_count}`;
        })
        .catch((error) => {
            console.error("Failed to fetch visitor count:", error);
            visitorCountSpan.textContent = "Error!";
        });
});