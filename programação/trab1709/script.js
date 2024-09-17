// script.js
document.getElementById('contactForm').addEventListener('submit', function(event) {
    const name = document.getElementById('name').value;
    const message = document.getElementById('message').value;
    const date = document.getElementById('date').value;
    const number = document.getElementById('number').value;
    const terms = document.getElementById('terms').checked;
    const contactPreferences = document.querySelectorAll('input[name="contactPreference"]:checked');
    
    if (!name || !message || !date || !number || !terms || contactPreferences.length === 0) {
        event.preventDefault();
        alert('Por favor, preencha todos os campos, aceite os termos de uso e selecione pelo menos uma forma de contato.');
    }
});
