const num1Input = document.getElementById('num1'),
      num2Input = document.getElementById('num2'),
      operationSelect = document.getElementById('operation'),
      parrafo = document.getElementById('result'),
      acept = document.getElementById('acept');

acept.addEventListener('click', async function(){

    // 1. Obtenemos los valores de los inputs y el select.
    const a = parseInt(num1Input.value);
    const b = parseInt(num2Input.value);
    const operation = operationSelect.value;

    if (!isNaN(a) && !isNaN(b)) {
        // 2. Preparamos los datos para enviar al servidor.
        const data = {
            operation: operation,
            x: a,
            y: b
        };

        try {
            // 3. Usamos fetch para enviar los datos a la API de Python.
            const response = await fetch('http://127.0.0.1:5000/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            const resultData = await response.json();
            parrafo.innerText = "El resultado es: " + resultData.result;
        } catch (error) {
            parrafo.innerText = "Error al conectar con el servidor.";
            console.error('Error:', error);
        }
    } else {
        parrafo.innerText = "Por favor, ingrese números válidos.";
    }
});
