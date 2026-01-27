import os
import xml.etree.ElementTree as ET

class ProcessadorNotas:
    def __init__(self, pasta_notas='notas_fiscais'):
        self.pasta_notas = pasta_notas
        self.catalogo = [] 

    def _limpar_namespace(self, elemento):
        """Método interno para limpar o namespace do XML."""
        for elem in elemento.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]

    def carregar_dados(self):
        """Lê os XMLs e preenche o self.catalogo."""
        print(f"--- Carregando dados de: {self.pasta_notas} ---\n")
        
        if not os.path.exists(self.pasta_notas):
            os.makedirs(self.pasta_notas)
            print(f"Pasta '{self.pasta_notas}' criada. Coloque os arquivos lá.")
            return

        arquivos = [f for f in os.listdir(self.pasta_notas) if f.endswith('.xml')]

        for arquivo in arquivos:
            caminho_completo = os.path.join(self.pasta_notas, arquivo)
            try:
                self._processar_arquivo_individual(caminho_completo, arquivo)
            except Exception as e:
                print(f"Erro ao ler {arquivo}: {e}")

        # ORDENAÇÃO POR DATA

        self.catalogo.sort(key=lambda x: x['data'], reverse=False)

    def _processar_arquivo_individual(self, caminho, nome_arquivo):
        tree = ET.parse(caminho)
        root = tree.getroot()
        self._limpar_namespace(root)
        
        # 1. Dados da Nota
        try:
            numero_nota = root.find('.//ide/nNF').text
            data_emissao = root.find('.//ide/dhEmi').text[:10]
        except:
            numero_nota = "Desconhecido"
            data_emissao = "-"

        # 2. Chave de Acesso
        try:
            chave = root.find('.//protNFe/infProt/chNFe').text
        except:
            try:
                inf_nfe = root.find('.//infNFe')
                chave = inf_nfe.attrib.get('Id')[3:] 
            except:
                chave = "Chave não encontrada"

        # 3. Fornecedor
        try:
            fornecedor = root.find('.//emit/xFant').text
            if not fornecedor:
                fornecedor = root.find('.//emit/xNome').text
        except:
            try:
                fornecedor = root.find('.//emit/xNome').text
            except:
                fornecedor = "Fornecedor Desconhecido"

        # 4. Produtos
        itens = root.findall('.//det')
        for item in itens:
            produto_nome = item.find('.//xProd')
            if produto_nome is not None:
                self.catalogo.append({
                    'produto': produto_nome.text,
                    'nota': numero_nota,
                    'arquivo': nome_arquivo,
                    'data': data_emissao,
                    'fornecedor': fornecedor,
                    'chave': chave
                })
        
        print(f"Arquivo carregado: {nome_arquivo} ({len(itens)} itens)")

    def buscar(self, termo):
        """Retorna uma lista de produtos que correspondem ao termo."""
        return [p for p in self.catalogo if termo.lower() in p['produto'].lower()]
