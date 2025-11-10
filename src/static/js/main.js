// main.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("moodForm");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const sentenceInput = document.getElementById("sentenceInput").value;

        fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ sentence: sentenceInput })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = "Predicted Mood: " + data.prediction;
        })
        .catch(error => {
            console.error("Error:", error);
            resultDiv.innerHTML = "An error occurred. Please try again.";
        });
    });
});