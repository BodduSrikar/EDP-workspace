document.getElementById('checkBtn').addEventListener('click', async() => {
    const textInput = document.getElementById('newsInput').value;
    const resultDiv = document.getElementById('result');

    if (!textInput.trim()) {
        resultDiv.innerHTML = "<span style='color: #dc3545;'>Please enter some news text to analyze.</span>";
        return;
    }

    resultDiv.innerHTML = "⏳ <i>Analyzing news text...</i>";

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: textInput })
        });

        const data = await response.json();

        if (data.result) {
            if (data.result === "REAL") {
                resultDiv.innerHTML = `<div class="alert real">✅ Article Class: REAL NEWS</div>`;
            } else {
                resultDiv.innerHTML = `<div class="alert fake">🚨 Article Class: FAKE NEWS</div>`;
            }
        } else {
            resultDiv.innerHTML = "<span style='color: #dc3545;'>Error processing request.</span>";
        }
    } catch (error) {
        resultDiv.innerHTML = "<span style='color: #dc3545;'>❌ Error: Flask server is offline! Start <code>app.py</code> first.</span>";
    }
});