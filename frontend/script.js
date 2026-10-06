const API_URL = `http://${window.location.hostname}:8000/message`;

async function loadMessage() {
    const element = document.getElementById("message");
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }
        const data = await response.json();
        element.textContent = data.message;
    } catch (error) {
        element.textContent = "Unable to reach the API";
        element.classList.add("error");
        console.error(error);
    }
}

loadMessage();