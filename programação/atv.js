// Seleciona os elementos do formulário
const leituraAnterior = document.getElementById('leitura_anterior');
const leituraAtual = document.getElementById('leitura_atual');
const baixaRenda = document.getElementById('baixa_renda');
const calcular = document.getElementById('calcular');
const resultado = document.getElementById('resultado');

// Função para calcular o consumo
function calcularConsumo() {
 const consumo = leituraAtual.value - leituraAnterior.value;
 const valorKw = baixaRenda.checked ? 0.41 : 0.76;
 const valorAPagar = consumo * valorKw;
 resultado.innerText = `Consumo: ${consumo} Kw\nValor a pagar: R$ ${valorAPagar.toFixed(2)}`;
}

// Adiciona evento de click ao botão calcular
calcular.addEventListener('click', (e) => {
 e.preventDefault();
 calcularConsumo();
});