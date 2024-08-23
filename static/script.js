document.getElementById('content-form').addEventListener('submit', async function(e) {
    e.preventDefault();  // Prevent the default form submission

    // Get the form data
    const author = document.getElementById('author').value;
    const content = document.getElementById('content').value;

    // Send the data to the server
    const response = await fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ author, content })
    });

    // Parse the JSON response
    const data = await response.json();

    // Display the response
    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = `<strong>Response:</strong> ${data.message}<br><pre>${JSON.stringify(data.block, null, 2)}</pre>`;
    responseDiv.style.display = 'block';
});
