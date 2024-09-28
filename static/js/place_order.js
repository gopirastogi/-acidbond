document.getElementById('orderBtn').addEventListener('click', function() {
    document.getElementById('orderPopup').style.display = 'block';
});

document.getElementById('closeBtn').addEventListener('click', function() {
    document.getElementById('orderPopup').style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('orderPopup')) {
        document.getElementById('orderPopup').style.display = 'none';
    }
});

document.getElementById('orderForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Order submitted successfully!');
    document.getElementById('orderPopup').style.display = 'none';
});