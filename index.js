const num1 = document.getElementById('num1').value,
      num2 = document.getElementById('num2').value,
      parrafo = document.getElementById('result'),
     acept = document.getElementById('acept');

    acept.document.geteventListener('click', function(){

        const a = parseInt(num1);
        const b = parseInt(num2);

        if (!isNaN(a) && !isNaN(b)) {
            const mtpc = a * b;
            parrafo.innerText = "El resultado es: " + mtpc;
        } else {
            parrafo.innerText = "Por favor, ingrese números válidos.";
        }
    });

