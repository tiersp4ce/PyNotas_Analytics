# 🔍 PyNotas_Analytics

### Motor de Busca e Processamento de Itens em Notas Fiscais (NFe)

O **PyNotas_Analytics** é uma ferramenta robusta desenvolvida em Python para automatizar a extração, organização e consulta de dados contidos em arquivos XML de Notas Fiscais Eletrônicas. O projeto resolve a complexidade de buscar itens manualmente em grandes volumes de arquivos fiscais, permitindo filtros instantâneos por múltiplos critérios.

---

## 🚀 Funcionalidades Técnicas

O sistema foi arquitetado com foco em precisão e performance:

* **Parsing Inteligente de XML:** Utiliza a biblioteca `xml.etree.ElementTree` para navegar em estruturas complexas de NFe.
* **Limpeza de Namespaces:** Implementação de um método interno para tratar e remover namespaces automáticos do XML, garantindo que as tags de dados (como `<xProd>`, `<nNF>`, `<dhEmi>`) sejam localizadas sem erros.
* **Indexação e Metadados:** Extrai e organiza informações cruciais:
    * 📦 Nome do Produto
    * 🏢 Nome/Fantasia do Fornecedor
    * 📄 Número da Nota Fiscal
    * 🔑 Chave de Acesso (44 dígitos)
    * 📅 Data de Emissão (com ordenação automática)
* **Motor de Busca Dinâmica:** Sistema de busca que ignora diferenças entre maiúsculas e minúsculas (*case-insensitive*) para encontrar produtos através de termos parciais.

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.x
* **Processamento XML:** ElementTree
* **Gerenciamento de Arquivos:** OS (para leitura em lote e criação automatizada de diretórios)
* **Ambiente:** Desenvolvido e otimizado para sistemas Linux.

---

## 💻 Exemplo de Implementação (Lógica de Busca)

A filtragem dos dados é realizada de forma eficiente através de *list comprehension*, permitindo consultas rápidas mesmo em catálogos extensos:

```python
def buscar(self, termo):
    """Retorna uma lista de produtos que correspondem ao termo."""
    return [p for p in self.catalogo if termo.lower() in p['produto'].lower()]
