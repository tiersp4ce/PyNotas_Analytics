# 🔍 PyNotas_Analytics

### Motor de Busca e Filtragem Inteligente para Itens em Notas Fiscais

O **PyNotas_Analytics** é uma ferramenta desenvolvida em Python para automatizar a localização e organização de itens em Notas Fiscais (NFs). O projeto resolve a dificuldade de busca manual em grandes volumes de dados fiscais, permitindo consultas granulares e instantâneas.

---

## 🚀 Funcionalidades Principais

O sistema foi projetado para oferecer precisão na recuperação de dados através de múltiplos filtros:

* **Busca por Nome (Partial Match):** Filtra produtos que contenham o termo digitado, facilitando a busca mesmo sem o nome completo do item.
* **Filtro por Código da NF:** Isola rapidamente todos os produtos vinculados a um número específico de nota fiscal.
* **Filtro por Data:** Permite restringir a busca a períodos específicos de emissão para controle de estoque ou financeiro.
* **Extração de Dados (ETL):** Processa e limpa informações brutas de arquivos fiscais para consulta dinâmica.



---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem Principal:** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* **Manipulação de Dados:** **Pandas** (utilizado para a lógica de filtros e tratamento de DataFrames).
* **Ambiente de Desenvolvimento:** **Linux (Arch Linux / Nobara OS)**.

---

## 💻 Exemplo de Implementação (Lógica de Busca)

Abaixo, um exemplo de como a filtragem é aplicada utilizando a performance do Pandas:

```python
# Lógica central de filtragem do projeto
resultado = df[
    (df['produto'].str.contains(termo_busca, case=False)) & 
    (df['codigo_nf'] == codigo_digitado) &
    (df['data'] == data_selecionada)
]
