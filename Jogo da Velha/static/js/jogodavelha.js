let contador = 0;
let valor1 = 0;
let tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];

function jogodavelha(valor, imgElement) {
    // Atualiza o valor exibido

    // Ajuste no cálculo da linha e coluna (base 0)
    let linha = Math.floor((valor - 1) / 3);  // Linha ajustada para base 0
    let coluna = (valor - 1) % 3;  // Coluna ajustada para base 0

    // Verifica se o espaço está vazio e se a jogada é válida
    if (tabuleiro[linha][coluna] === 0) {
        if (contador % 2 === 0) {
            imgElement.src = "../static/imagens/X.png"; // Jogador 1 (X)
            tabuleiro[linha][coluna] = 1;  // Marca o tabuleiro com 1 para jogador 1
        } else {
            imgElement.src = "../static/imagens/O.png"; // Jogador 2 (O)
            tabuleiro[linha][coluna] = 2;  // Marca o tabuleiro com 2 para jogador 2
        }
        contador++; // Alterna entre os jogadores

        // Verificar vitória
        if (verificarVitoria(1)) {
            console.log('Vitória do jogador 1!');
            valor1 = 1;
            document.getElementById('valor').innerText = 'Vitória do jogador 1!';
            enviarValorParaJogo(); // Envia o resultado do jogo imediatamente
            return;
        }
        if (verificarVitoria(2)) {
            console.log('Vitória do jogador 2!');
            valor1 = 2;
            document.getElementById('valor').innerText = 'Vitória do jogador 2!';
            enviarValorParaJogo(); // Envia o resultado do jogo imediatamente
            return;
        }

        // Verificar empate (Velha)
        if (verificarEmpate()) {
            console.log('Velha!');
            valor1 = 0;
            document.getElementById('valor').innerText = 'Velha!';
            enviarValorParaJogo(); // Envia o empate imediatamente
        }
    }

    console.log(tabuleiro); // Para exibir o estado atual do tabuleiro
}

// Função para verificar se houve vitória de um jogador (1 ou 2)
function verificarVitoria(jogador) {
    // Verifica linhas e colunas
    for (let i = 0; i < 3; i++) {
        if (tabuleiro[i][0] === jogador && tabuleiro[i][1] === jogador && tabuleiro[i][2] === jogador) {
            return true;  // Vitória na linha i
        }
        if (tabuleiro[0][i] === jogador && tabuleiro[1][i] === jogador && tabuleiro[2][i] === jogador) {
            return true;  // Vitória na coluna i
        }
    }

    // Verifica diagonais
    if (tabuleiro[0][0] === jogador && tabuleiro[1][1] === jogador && tabuleiro[2][2] === jogador) {
        return true;  // Vitória na diagonal principal
    }
    if (tabuleiro[0][2] === jogador && tabuleiro[1][1] === jogador && tabuleiro[2][0] === jogador) {
        return true;  // Vitória na diagonal secundária
    }

    return false; // Nenhuma vitória
}

// Função para verificar se houve empate (Velha)
function verificarEmpate() {
    // Verifica se o tabuleiro está cheio e não houve vitória
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (tabuleiro[i][j] === 0) {
                return false; // Ainda há espaços vazios, não é empate
            }
        }
    }
    return true; // O tabuleiro está cheio e não houve vencedor
}

// Envia o resultado do jogo para o servidor
function enviarValorParaJogo() {
    let valor = valor1; // Obter o valor do resultado do jogo

    if (valor === 0) {
        alert('Por favor, espere o jogo terminar!');
        return;
    }

    // Criar um objeto JSON com o valor
    const data = { valor: valor === 1 ? 'Vitória do jogador 1!' : 'Vitória do jogador 2!' };

    // Enviar o JSON para a rota '/jogo' via POST
    fetch('/jogo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',  // Indica que o conteúdo da requisição é JSON
        },
        body: JSON.stringify(data)  // Converte o objeto JavaScript para uma string JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na resposta da rede: ' + response.statusText);
        }
        return response.json();  // Converte a resposta para JSON
    })
    .then(data => {
        console.log('Resposta recebida do servidor:', data);
        alert(data.message); // Exibe a mensagem retornada pelo servidor
    })
    .catch((error) => {
        console.error('Erro:', error);
    });
}
