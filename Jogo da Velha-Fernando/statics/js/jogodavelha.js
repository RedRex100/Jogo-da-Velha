let contador = 0;
let tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];

function jogodavelha(valor, imgElement) {
    // Atualiza o valor exibido

    // Ajuste no cálculo da linha e coluna (base 0)
    let linha = Math.floor((valor - 1) / 3);  // Linha ajustada para base 0
    let coluna = (valor - 1) % 3;  // Coluna ajustada para base 0

    // Verifica se o espaço está vazio e se a jogada é válida
    if (tabuleiro[linha][coluna] === 0) {
        if (contador % 2 === 0) {
            imgElement.src = "../imagens/x.png"; // Jogador 1 (X)
            tabuleiro[linha][coluna] = 1;  // Marca o tabuleiro com 1 para jogador 1
        } else {
            imgElement.src = "../imagens/o.png"; // Jogador 2 (O)
            tabuleiro[linha][coluna] = 2;  // Marca o tabuleiro com 2 para jogador 2
        }
        contador++; // Alterna entre os jogadores

        // Verificar vitória
        if (verificarVitoria(1)) {
            console.log('Vitória do jogador 1!');
            document.getElementById('valor').innerText = 'Vitória do jogador 1!';
            return;
        }
        if (verificarVitoria(2)) {
            console.log('Vitória do jogador 2!');
            document.getElementById('valor').innerText = 'Vitória do jogador 2!';
            return;
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
