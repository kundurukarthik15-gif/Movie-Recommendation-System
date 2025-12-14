const API_URL = "http://127.0.0.1:5000";

async function getRecommendations() {
    const movie = document.getElementById("movieInput").value.trim();

    if (!movie) {
        alert("Please enter a movie name");
        return;
    }

    const res = await fetch(`${API_URL}/recommend`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ movie })
    });

    const data = await res.json();
    const list = document.getElementById("results");
    list.innerHTML = "";

    if (data.length === 0) {
        list.innerHTML = "<li>❌ Movie not found</li>";
        return;
    }

    data.forEach(m => {
        const li = document.createElement("li");
        li.textContent = m;
        list.appendChild(li);
    });
}
