document.getElementById("advancedForm").addEventListener("submit", function (e) {
    const age = document.getElementById("age").value;

    if (age < 18 || age > 100) {
        e.preventDefault();
        alert("Por favor, ingresa una edad válida (18-100 años).");
    }
});
