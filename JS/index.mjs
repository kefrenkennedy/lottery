// A função recebe um array de arrays como parâmetro
function getRank(arrays) {
  // Conta as frequências de cada número nos arrays
  const frequencies = countFrequencies(arrays);

  // Classifica as frequências em ordem decrescente
  const sortedFrequencies = sortFrequencies(frequencies);

  // Mapeia as frequências classificadas para o formato de ranking desejado
  const rankedFrequencies = mapFrequenciesToRank(sortedFrequencies);

  // Retorna o resultado final, um array de strings no formato "numero: frequencia vezes"
  return rankedFrequencies;
}

// Função auxiliar para contar as frequências de cada número nos arrays
function countFrequencies(arrays) {
  const count = {}; // Cria um objeto vazio para armazenar as frequências
  arrays.forEach((array) => {
    array.forEach((num) => {
      count[num] = (count[num] || 0) + 1; // Adiciona 1 à contagem do número atual
    });
  });
  return count; // Retorna o objeto com as frequências
}

// Função auxiliar para classificar as frequências em ordem decrescente
function sortFrequencies(frequencies) {
  const entries = Object.entries(frequencies); // Converte o objeto de frequências em um array de arrays
  return entries.sort((a, b) => b[1] - a[1]); // Classifica o array de arrays com base na frequência
}

// Função auxiliar para mapear as frequências classificadas para o formato de ranking desejado
function mapFrequenciesToRank(frequencies) {
  return frequencies.map((entry) => `${entry[0]}: ${entry[1]} vezes`); // Converte cada entrada em uma string no formato "numero: frequencia vezes"
}

function verificaListas(listaPrincipal, listaVerificada) {
  const listaVerificadaNums = listaVerificada.map(Number);
  for (const lista of listaPrincipal) {
    if (lista.every((num, i) => num === listaVerificadaNums[i])) {
      return "Esse jogo já ocorreu.";
    }
  }
  return "Esse jogo nunca ocorreu.";
}
