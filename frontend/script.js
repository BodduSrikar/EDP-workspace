const checkBtn = document.getElementById('checkBtn');
const clearBtn = document.getElementById('clearBtn');
const newsInput = document.getElementById('newsInput');
const resultDiv = document.getElementById('result');

checkBtn.addEventListener('click', async() => {
    const text = newsInput.value.trim();

    if (!text) {
        resultDiv.innerHTML = `<div class="card uncertain">⚠️ Please enter news text to analyze.</div>`;
        return;
    }

    resultDiv.innerHTML = `<p style="text-align: center; color: #7f8c8d;">⏳ <i>Analyzing text through ML model...</i></p>`;

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        if (data.result === 'REAL') {
            resultDiv.innerHTML = `
                <div class="card real">
                    <div class="card-title">✅ Prediction: REAL NEWS</div>
                    <div>Model Confidence: <strong>${data.confidence}%</strong></div>
                    <div class="progress-container">
                        <div class="progress-bar real" style="width: ${data.confidence}%"></div>
                    </div>
                </div>
            `;
        } else if (data.result === 'FAKE') {
            resultDiv.innerHTML = `
                <div class="card fake">
                    <div class="card-title">🚨 Prediction: FAKE NEWS</div>
                    <div>Model Confidence: <strong>${data.confidence}%</strong></div>
                    <div class="progress-container">
                        <div class="progress-bar fake" style="width: ${data.confidence}%"></div>
                    </div>
                </div>
            `;
        } else {
            resultDiv.innerHTML = `
                <div class="card uncertain">
                    <div class="card-title">⚠️ Result: ${data.result}</div>
                    <div style="font-size: 13px; margin-top: 4px;">${data.message || 'Low confidence in input features.'}</div>
                </div>
            `;
        }
    } catch (error) {
        resultDiv.innerHTML = `<div class="card fake">❌ Error connecting to Flask backend. Ensure server is active.</div>`;
    }
});

clearBtn.addEventListener('click', () => {
    newsInput.value = '';
    resultDiv.innerHTML = '';
    newsInput.focus();
});