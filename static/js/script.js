function validarFormulario() {
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let birthdate = document.getElementById("birthdate").value.trim();
    let gender = document.getElementById("gender").value.trim();

    if (!name || !email || !birthdate || !gender) {
        alert("Todos los campos son obligatorios.");
        return false;
    }

    return true;
}