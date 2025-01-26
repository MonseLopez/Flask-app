document.getElementById("advancedForm").addEventListener("submit", function (e) {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const age = document.getElementById("age").value;
    const password = document.getElementById("password").value;

    if (!name || !email || !age || !password) {
        e.preventDefault();
        alert("Todos los campos son obligatorios.");
    } else if (age < 18 || age > 100) {
        e.preventDefault();
        alert("Por favor, ingresa una edad válida (18-100 años).");
    }
});
