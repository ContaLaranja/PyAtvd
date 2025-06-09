# Sistema de Gerenciamento de Estoque

## Visão Geral
Este projeto é um Sistema de Gerenciamento de Estoque projetado para ajudar os usuários a gerenciar seus estoques de forma eficiente. Ele permite adicionar, listar, alterar e excluir itens do estoque por meio de uma interface amigável.

## Estrutura do Projeto
O projeto consiste nos seguintes arquivos:

- **Sistema_Estoque.py**: Este arquivo contém o menu principal do sistema de estoque. Ele importa o módulo `negocios_crud` e fornece opções para adicionar, listar, alterar e excluir itens no estoque.

- **interface.py**: Este arquivo é a interface gráfica atualizada para o sistema de estoque. Ele inclui elementos visuais como rótulos, botões e campos de entrada para suportar as funcionalidades do módulo `negocios_crud`. A interface está projetada, mas ainda não está conectada às funções de backend ou ao arquivo de dados de texto.

- **negocios_crud.py**: Este arquivo contém funções para gerenciar o estoque, incluindo adicionar, listar, alterar e excluir itens. Cada função interage com o arquivo `estoque.txt` para realizar as respectivas operações.

- **estoque.txt**: Este arquivo serve como armazenamento para os itens do estoque, formatados como valores separados por vírgulas. Atualmente, está preenchido com dados de exemplo.

## Uso
1. Execute o arquivo `Sistema_Estoque.py` para acessar o menu principal do sistema de estoque.
2. Siga as instruções para adicionar, listar, alterar ou excluir itens no estoque.
3. Use o arquivo `interface.py` para uma interface gráfica que suporta essas funcionalidades (atualmente não conectada ao backend).

## Melhorias Futuras
- Conectar a interface gráfica às funções de backend no arquivo `negocios_crud.py`.
- Implementar funcionalidades adicionais, como busca e validação de dados.
- Melhorar a interface do usuário para maior usabilidade e estética.
