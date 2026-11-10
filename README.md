# Analisador de Senhas (v1)

> Versão 1, desenvolvida no início dos meus estudos em Python. As melhorias estão planejadas para as próximas versões (veja o roadmap).

Script em Python que avalia a força de uma senha por regras simples e explica o motivo de cada penalidade. Faz parte dos meus estudos de segurança defensiva: entender o que torna uma credencial fraca é o primeiro passo para impedir que ela seja usada.

## Como funciona

A senha começa com 0 ponto. Cada critério soma ou subtrai:

| Critério | Atende | Não atende |
|---|---|---|
| Tamanho de pelo menos 8 caracteres | +1 | -1 |
| Contém número | +1 | -1 |
| Contém letra maiúscula | +1 | -1 |
| Contém símbolo (`!@#$%^&*()_+-=`) | +1 | -1 |
| Caracteres iguais adjacentes (ex.: `aa`) | | -1 |
| Sequência numérica crescente (ex.: `123`) | | -1 |

Classificação final (pontuação máxima: 4):

- **0 ou menos:** senha fraca
- **1 a 2:** senha média
- **3 ou mais:** senha forte

Além da classificação, o programa lista os motivos que reduziram a pontuação.

## Exemplo de uso

```
Digite a senha: senha1234
Senha fraca
Motivos:
Sem letra maiúscula
Sem símbolo
Tem sequência
```

Resultados de alguns testes:

| Senha | Pontos | Classificação | Motivos |
|---|---|---|---|
| `abc` | -4 | fraca | muito curta, sem número, sem maiúscula, sem símbolo |
| `senha1234` | -1 | fraca | sem maiúscula, sem símbolo, sequência |
| `Xk9#mP2$vL` | 4 | forte | nenhum |

## Limitações conhecidas

Esta primeira versão é um avaliador baseado em regras, e as regras têm pontos cegos que documentei de propósito e que guiam as próximas versões:

1. **Não consulta senhas comuns.** `Senha123!` e `Password1!` recebem 3 pontos e são classificadas como fortes, embora estejam entre os padrões mais previsíveis. Cumprir as regras de composição não significa que a senha seja difícil de adivinhar.
2. **O tamanho não escala a pontuação.** Uma frase longa como `correto cavalo bateria grampo` recebe -3 (fraca) por não ter número, maiúscula nem símbolo, apesar de ser bem mais difícil de quebrar que `Xk9#mP2$vL`.
3. **A detecção de sequências é limitada.** Pega apenas dígitos crescentes (`123`), e não `321`, `abc` nem padrões de teclado como `qwerty`.
4. **A regra de repetição é rígida.** Qualquer par de caracteres iguais seguidos (como o `ss` de `Password`) já penaliza.
5. **Conjunto fixo de símbolos.** Só os caracteres listados na tabela contam como símbolo.

## Roadmap (próximas versões)

- Comparar a senha com uma lista de senhas vazadas ou comuns antes de classificar.
- Trocar a pontuação fixa por uma estimativa de entropia, de modo que o comprimento pese mais.
- Detectar mais padrões: sequências alfabéticas e decrescentes, teclado e datas.

## Projetos relacionados

- [password-attack-simulator](https://github.com/Charlys-teixeira/password-attack-simulator): simulador de ataques de wordlist e brute force, que mostra na prática o tempo de quebra de cada tipo de senha.
- [Detector_de_Login_Suspeito](https://github.com/Charlys-teixeira/Detector_de_Login_Suspeito): identificação de brute force e credential stuffing em tentativas de login.

## Tecnologias

- Python (somente biblioteca padrão)
