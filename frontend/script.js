document.getElementById('checkBtn').addEventListener('click', () => {
    const text = document.getElementById('newsInput').value;
    const resultDiv = document.getElementById('result');
    
    if (!text.trim()) {
        resultDiv.textContent = "Please enter some text to analyze.";
        return;
    }
    
    resultDiv.textContent = "Analyzing news text...";
});