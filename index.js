const num1Input = document.getElementById('num1'),
      num2Input = document.getElementById('num2'),
      parrafo = document.getElementById('result'),
      acept = document.getElementById('acept');

// El método correcto es addEventListener y se aplica directamente al botón.
acept.addEventListener('click', function(){

    // Obtenemos el valor de los inputs DENTRO de la función, cuando el usuario hace clic.
    const a = parseInt(num1Input.value);
    const b = parseInt(num2Input.value);

    if (!isNaN(a) && !isNaN(b)) {
        const mtpc = a * b;
        parrafo.innerText = "El resultado es: " + mtpc;
    } else {
        parrafo.innerText = "Por favor, ingrese números válidos.";
    }
});
