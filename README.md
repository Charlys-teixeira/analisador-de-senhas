# Analisador de Força de Senhas (v1)

## Sobre o Projeto
Script em Python que avalia a força de uma senha por regras simples e explica o motivo de cada penalidade. Desenvolvido no início dos meus estudos de segurança defensiva: entender o que torna uma credencial fraca é o primeiro passo para impedir que ela seja usada no mundo real.

## Como Funciona
A senha começa com 0 ponto. Cada critério soma ou subtrai da pontuação final:

| Critério | Atende | Não atende |
| :--- | :---: | :---: |
| Tamanho (mínimo de 8 caracteres) | +1 | -1 |
| Contém número | +1 | -1 |
| Contém letra maiúscula | +1 | -1 |
| Contém símbolo (`!@#$%^&*()_+-=`) | +1 | -1 |
| Caracteres iguais adjacentes (ex.: `aa`) | - | -1 |
| Sequência numérica crescente (ex.: `123`) | - | -1 |

**Classificação Final (Pontuação máxima: 4)**
- **0 ou menos:** Senha fraca
- **1 a 2:** Senha média
- **3 ou mais:** Senha forte

Além da classificação, o programa lista exatamente os motivos que reduziram a pontuação para o usuário.

## Exemplo de Uso
```text
Digite a senha: senha1234
Senha fraca
Motivos:
Sem letra maiúscula
Sem símbolo
Tem sequência
