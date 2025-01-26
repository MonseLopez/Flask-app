document.getElementById("exampleForm").addEventListener("submit", function (event) {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;

    if (!name || !age) {
        event.preventDefault();
        alert("Por favor, llena todos los campos.");
    } else if (age < 1 || age > 120) {
        event.preventDefault();
        alert("Por favor, ingresa una edad válida.");
    }
});
