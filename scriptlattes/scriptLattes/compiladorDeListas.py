#!/usr/bin/python
# encoding: utf-8
#
#
#  scriptLattes
#  http://scriptlattes.sourceforge.net/
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#

import operator
import re
from scipy import sparse
from scriptLattes.util import merge_dols

class CompiladorDeListas:
    grupo = None
    matrizArtigoEmPeriodico = None
    matrizLivroPublicado = None
    matrizCapituloDeLivroPublicado = None
    matrizTextoEmJornalDeNoticia = None
    matrizTrabalhoCompletoEmCongresso = None
    matrizResumoExpandidoEmCongresso = None
    matrizResumoEmCongresso = None
    matrizArtigoAceito = None
    matrizApresentacaoDeTrabalho = None
    matrizOutroTipoDeProducaoBibliografica = None
    matrizSoftwareComPatente = None
    matrizSoftwareSemPatente = None
    matrizProdutoTecnologico = None
    matrizProcessoOuTecnica = None
    matrizTrabalhoTecnico = None
    matrizOutroTipoDeProducaoTecnica = None
    matrizProducaoArtistica = None

    matrizPatente = None
    matrizProgramaComputador = None
    matrizDesenhoIndustrial = None

    def __init__(self, grupo):
        self.grupo = grupo

        self.listaCompletaPB = {}
        self.listaCompletaPT = {}
        self.listaCompletaPR = {}
        self.listaCompletaPA = {}
        self.listaCompletaOA = {}
        self.listaCompletaOC = {}

        self.listaCompletaArtigoEmPeriodico = {}
        self.listaCompletaLivroPublicado = {}
        self.listaCompletaCapituloDeLivroPublicado = {}
        self.listaCompletaTextoEmJornalDeNoticia = {}
        self.listaCompletaTrabalhoCompletoEmCongresso = {}
        self.listaCompletaResumoExpandidoEmCongresso = {}
        self.listaCompletaResumoEmCongresso = {}
        self.listaCompletaArtigoAceito = {}
        self.listaCompletaApresentacaoDeTrabalho = {}
        self.listaCompletaOutroTipoDeProducaoBibliografica = {}

        self.listaCompletaSoftwareComPatente = {}
        self.listaCompletaSoftwareSemPatente = {}
        self.listaCompletaProdutoTecnologico = {}
        self.listaCompletaProcessoOuTecnica = {}
        self.listaCompletaTrabalhoTecnico = {}
        self.listaCompletaOutroTipoDeProducaoTecnica = {}

        self.listaCompletaPatente = {}
        self.listaCompletaProgramaComputador = {}
        self.listaCompletaDesenhoIndustrial = {}

        self.listaCompletaProducaoArtistica = {}

        self.listaCompletaOASupervisaoDePosDoutorado = {}
        self.listaCompletaOATeseDeDoutorado = {}
        self.listaCompletaOADissertacaoDeMestrado = {}
        self.listaCompletaOAMonografiaDeEspecializacao = {}
        self.listaCompletaOATCC = {}
        self.listaCompletaOAIniciacaoCientifica = {}
        self.listaCompletaOAOutroTipoDeOrientacao = {}

        self.listaCompletaOCSupervisaoDePosDoutorado = {}
        self.listaCompletaOCTeseDeDoutorado = {}
        self.listaCompletaOCDissertacaoDeMestrado = {}
        self.listaCompletaOCMonografiaDeEspecializacao = {}
        self.listaCompletaOCTCC = {}
        self.listaCompletaOCIniciacaoCientifica = {}
        self.listaCompletaOCOutroTipoDeOrientacao = {}

        self.listaCompletaPremioOuTitulo = {}
        self.listaCompletaProjetoDePesquisa = {}

        self.listaCompletaParticipacaoEmEvento = {}
        self.listaCompletaOrganizacaoDeEvento = {}


        # compilamos as producoes de todos os membros (separados por tipos)
        for membro in grupo.listaDeMembros:
            self.listaCompletaArtigoEmPeriodico = self.compilarLista(membro.listaArtigoEmPeriodico,
                                                                     self.listaCompletaArtigoEmPeriodico)
            self.listaCompletaLivroPublicado = self.compilarLista(membro.listaLivroPublicado,
                                                                  self.listaCompletaLivroPublicado)
            self.listaCompletaCapituloDeLivroPublicado = self.compilarLista(membro.listaCapituloDeLivroPublicado,
                                                                            self.listaCompletaCapituloDeLivroPublicado)
            self.listaCompletaTextoEmJornalDeNoticia = self.compilarLista(membro.listaTextoEmJornalDeNoticia,
                                                                          self.listaCompletaTextoEmJornalDeNoticia)
            self.listaCompletaTrabalhoCompletoEmCongresso = self.compilarLista(membro.listaTrabalhoCompletoEmCongresso,
                                                                               self.listaCompletaTrabalhoCompletoEmCongresso)
            self.listaCompletaResumoExpandidoEmCongresso = self.compilarLista(membro.listaResumoExpandidoEmCongresso,
                                                                              self.listaCompletaResumoExpandidoEmCongresso)
            self.listaCompletaResumoEmCongresso = self.compilarLista(membro.listaResumoEmCongresso,
                                                                     self.listaCompletaResumoEmCongresso)
            self.listaCompletaArtigoAceito = self.compilarLista(membro.listaArtigoAceito,
                                                                self.listaCompletaArtigoAceito)
            self.listaCompletaApresentacaoDeTrabalho = self.compilarLista(membro.listaApresentacaoDeTrabalho,
                                                                          self.listaCompletaApresentacaoDeTrabalho)
            self.listaCompletaOutroTipoDeProducaoBibliografica = self.compilarLista(
                membro.listaOutroTipoDeProducaoBibliografica, self.listaCompletaOutroTipoDeProducaoBibliografica)

            self.listaCompletaSoftwareComPatente = self.compilarLista(membro.listaSoftwareComPatente,
                                                                      self.listaCompletaSoftwareComPatente)
            self.listaCompletaSoftwareSemPatente = self.compilarLista(membro.listaSoftwareSemPatente,
                                                                      self.listaCompletaSoftwareSemPatente)
            self.listaCompletaProdutoTecnologico = self.compilarLista(membro.listaProdutoTecnologico,
                                                                      self.listaCompletaProdutoTecnologico)
            self.listaCompletaProcessoOuTecnica = self.compilarLista(membro.listaProcessoOuTecnica,
                                                                     self.listaCompletaProcessoOuTecnica)
            self.listaCompletaTrabalhoTecnico = self.compilarLista(membro.listaTrabalhoTecnico,
                                                                   self.listaCompletaTrabalhoTecnico)
            self.listaCompletaOutroTipoDeProducaoTecnica = self.compilarLista(membro.listaOutroTipoDeProducaoTecnica,
                                                                              self.listaCompletaOutroTipoDeProducaoTecnica)

            self.listaCompletaPatente = self.compilarLista(membro.listaPatente, self.listaCompletaPatente)
            self.listaCompletaProgramaComputador = self.compilarLista(membro.listaProgramaComputador,
                                                                      self.listaCompletaProgramaComputador)
            self.listaCompletaDesenhoIndustrial = self.compilarLista(membro.listaDesenhoIndustrial,
                                                                     self.listaCompletaDesenhoIndustrial)

            self.listaCompletaProducaoArtistica = self.compilarLista(membro.listaProducaoArtistica,
                                                                     self.listaCompletaProducaoArtistica)

            self.listaCompletaOASupervisaoDePosDoutorado = self.compilarLista(membro.listaOASupervisaoDePosDoutorado,
                                                                              self.listaCompletaOASupervisaoDePosDoutorado)
            self.listaCompletaOATeseDeDoutorado = self.compilarLista(membro.listaOATeseDeDoutorado,
                                                                     self.listaCompletaOATeseDeDoutorado)
            self.listaCompletaOADissertacaoDeMestrado = self.compilarLista(membro.listaOADissertacaoDeMestrado,
                                                                           self.listaCompletaOADissertacaoDeMestrado)
            self.listaCompletaOAMonografiaDeEspecializacao = self.compilarLista(
                membro.listaOAMonografiaDeEspecializacao, self.listaCompletaOAMonografiaDeEspecializacao)
            self.listaCompletaOATCC = self.compilarLista(membro.listaOATCC, self.listaCompletaOATCC)
            self.listaCompletaOAIniciacaoCientifica = self.compilarLista(membro.listaOAIniciacaoCientifica,
                                                                         self.listaCompletaOAIniciacaoCientifica)
            self.listaCompletaOAOutroTipoDeOrientacao = self.compilarLista(membro.listaOAOutroTipoDeOrientacao,
                                                                           self.listaCompletaOAOutroTipoDeOrientacao)

            self.listaCompletaOCSupervisaoDePosDoutorado = self.compilarLista(membro.listaOCSupervisaoDePosDoutorado,
                                                                              self.listaCompletaOCSupervisaoDePosDoutorado)
            self.listaCompletaOCTeseDeDoutorado = self.compilarLista(membro.listaOCTeseDeDoutorado,
                                                                     self.listaCompletaOCTeseDeDoutorado)
            self.listaCompletaOCDissertacaoDeMestrado = self.compilarLista(membro.listaOCDissertacaoDeMestrado,
                                                                           self.listaCompletaOCDissertacaoDeMestrado)
            self.listaCompletaOCMonografiaDeEspecializacao = self.compilarLista(
                membro.listaOCMonografiaDeEspecializacao, self.listaCompletaOCMonografiaDeEspecializacao)
            self.listaCompletaOCTCC = self.compilarLista(membro.listaOCTCC, self.listaCompletaOCTCC)
            self.listaCompletaOCIniciacaoCientifica = self.compilarLista(membro.listaOCIniciacaoCientifica,
                                                                         self.listaCompletaOCIniciacaoCientifica)
            self.listaCompletaOCOutroTipoDeOrientacao = self.compilarLista(membro.listaOCOutroTipoDeOrientacao,
                                                                           self.listaCompletaOCOutroTipoDeOrientacao)

            self.listaCompletaPremioOuTitulo = self.compilarLista(membro.listaPremioOuTitulo,
                                                                  self.listaCompletaPremioOuTitulo)
            # self.listaCompletaProjetoDePesquisa           = self.compilarListaDeProjetos(membro.listaProjetoDePesquisa, self.listaCompletaProjetoDePesquisa)
            self.listaCompletaProjetoDePesquisa = self.compilarLista(membro.listaProjetoDePesquisa,
                                                                     self.listaCompletaProjetoDePesquisa)

            self.listaCompletaParticipacaoEmEvento = self.compilarLista(membro.listaParticipacaoEmEvento,
                                                                        self.listaCompletaParticipacaoEmEvento)
            self.listaCompletaOrganizacaoDeEvento = self.compilarLista(membro.listaOrganizacaoDeEvento,
                                                                       self.listaCompletaOrganizacaoDeEvento)

        # ---------------------------------------------------------------------------
        # compilamos as producoes de todos os tipos
        if self.grupo.obterParametro('relatorio-incluir_artigo_em_periodico'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaArtigoEmPeriodico,
                                                                self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_livro_publicado'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaLivroPublicado, self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_capitulo_de_livro_publicado'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaCapituloDeLivroPublicado,
                                                                self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_texto_em_jornal_de_noticia'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaTextoEmJornalDeNoticia,
                                                                self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_trabalho_completo_em_congresso'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaTrabalhoCompletoEmCongresso,
                                                                self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_resumo_expandido_em_congresso'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaResumoExpandidoEmCongresso,
                                                                self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_resumo_em_congresso'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaResumoEmCongresso,
                                                                self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_artigo_aceito_para_publicacao'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaArtigoAceito, self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_apresentacao_de_trabalho'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaApresentacaoDeTrabalho,
                                                                self.listaCompletaPB)
        if self.grupo.obterParametro('relatorio-incluir_outro_tipo_de_producao_bibliografica'):
            self.listaCompletaPB = self.compilarListasCompletas(self.listaCompletaOutroTipoDeProducaoBibliografica,
                                                                self.listaCompletaPB)

        if self.grupo.obterParametro('relatorio-incluir_software_com_patente'):
            self.listaCompletaPT = self.compilarListasCompletas(self.listaCompletaSoftwareComPatente,
                                                                self.listaCompletaPT)
        if self.grupo.obterParametro('relatorio-incluir_software_sem_patente'):
            self.listaCompletaPT = self.compilarListasCompletas(self.listaCompletaSoftwareSemPatente,
                                                                self.listaCompletaPT)
        if self.grupo.obterParametro('relatorio-incluir_produto_tecnologico'):
            self.listaCompletaPT = self.compilarListasCompletas(self.listaCompletaProdutoTecnologico,
                                                                self.listaCompletaPT)
        if self.grupo.obterParametro('relatorio-incluir_processo_ou_tecnica'):
            self.listaCompletaPT = self.compilarListasCompletas(self.listaCompletaProcessoOuTecnica,
                                                                self.listaCompletaPT)
        if self.grupo.obterParametro('relatorio-incluir_trabalho_tecnico'):
            self.listaCompletaPT = self.compilarListasCompletas(self.listaCompletaTrabalhoTecnico, self.listaCompletaPT)
        if self.grupo.obterParametro('relatorio-incluir_outro_tipo_de_producao_tecnica'):
            self.listaCompletaPT = self.compilarListasCompletas(self.listaCompletaOutroTipoDeProducaoTecnica,
                                                                self.listaCompletaPT)

        if self.grupo.obterParametro('relatorio-incluir_patente'):
            self.listaCompletaPR = self.compilarListasCompletas(self.listaCompletaPatente, self.listaCompletaPR)
        if self.grupo.obterParametro('relatorio-incluir_programa_computador'):
            self.listaCompletaPR = self.compilarListasCompletas(self.listaCompletaProgramaComputador,
                                                                self.listaCompletaPR)
        if self.grupo.obterParametro('relatorio-incluir_desenho_industrial'):
            self.listaCompletaPR = self.compilarListasCompletas(self.listaCompletaDesenhoIndustrial,
                                                                self.listaCompletaPR)

        if self.grupo.obterParametro('relatorio-incluir_producao_artistica'):
            self.listaCompletaPA = self.compilarListasCompletas(self.listaCompletaProducaoArtistica,
                                                                self.listaCompletaPA)

        if self.grupo.obterParametro('relatorio-incluir_orientacao_em_andamento_pos_doutorado'):
            self.listaCompletaOA = self.compilarListasCompletas(self.listaCompletaOASupervisaoDePosDoutorado,
                                                                self.listaCompletaOA)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_em_andamento_doutorado'):
            self.listaCompletaOA = self.compilarListasCompletas(self.listaCompletaOATeseDeDoutorado,
                                                                self.listaCompletaOA)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_em_andamento_mestrado'):
            self.listaCompletaOA = self.compilarListasCompletas(self.listaCompletaOADissertacaoDeMestrado,
                                                                self.listaCompletaOA)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_em_andamento_monografia_de_especializacao'):
            self.listaCompletaOA = self.compilarListasCompletas(self.listaCompletaOAMonografiaDeEspecializacao,
                                                                self.listaCompletaOA)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_em_andamento_tcc'):
            self.listaCompletaOA = self.compilarListasCompletas(self.listaCompletaOATCC, self.listaCompletaOA)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_em_andamento_iniciacao_cientifica'):
            self.listaCompletaOA = self.compilarListasCompletas(self.listaCompletaOAIniciacaoCientifica,
                                                                self.listaCompletaOA)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_em_andamento_outro_tipo'):
            self.listaCompletaOA = self.compilarListasCompletas(self.listaCompletaOAOutroTipoDeOrientacao,
                                                                self.listaCompletaOA)

        if self.grupo.obterParametro('relatorio-incluir_orientacao_concluida_pos_doutorado'):
            self.listaCompletaOC = self.compilarListasCompletas(self.listaCompletaOCSupervisaoDePosDoutorado,
                                                                self.listaCompletaOC)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_concluida_doutorado'):
            self.listaCompletaOC = self.compilarListasCompletas(self.listaCompletaOCTeseDeDoutorado,
                                                                self.listaCompletaOC)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_concluida_mestrado'):
            self.listaCompletaOC = self.compilarListasCompletas(self.listaCompletaOCDissertacaoDeMestrado,
                                                                self.listaCompletaOC)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_concluida_monografia_de_especializacao'):
            self.listaCompletaOC = self.compilarListasCompletas(self.listaCompletaOCMonografiaDeEspecializacao,
                                                                self.listaCompletaOC)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_concluida_tcc'):
            self.listaCompletaOC = self.compilarListasCompletas(self.listaCompletaOCTCC, self.listaCompletaOC)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_concluida_iniciacao_cientifica'):
            self.listaCompletaOC = self.compilarListasCompletas(self.listaCompletaOCIniciacaoCientifica,
                                                                self.listaCompletaOC)
        if self.grupo.obterParametro('relatorio-incluir_orientacao_concluida_outro_tipo'):
            self.listaCompletaOC = self.compilarListasCompletas(self.listaCompletaOCOutroTipoDeOrientacao,
                                                                self.listaCompletaOC)

        for membro in grupo.listaDeMembros:
            if membro.idLattes == '0000000000000000':
                print ":: Processando coautor sem CV-Lattes" + membro.nomeInicial

                self.adicionarCoautorNaLista(self.listaCompletaArtigoEmPeriodico, membro)
                self.adicionarCoautorNaLista(self.listaCompletaArtigoEmPeriodico, membro)

                self.adicionarCoautorNaLista(self.listaCompletaLivroPublicado, membro)
                self.adicionarCoautorNaLista(self.listaCompletaCapituloDeLivroPublicado, membro)
                self.adicionarCoautorNaLista(self.listaCompletaTextoEmJornalDeNoticia, membro)
                self.adicionarCoautorNaLista(self.listaCompletaTrabalhoCompletoEmCongresso, membro)
                self.adicionarCoautorNaLista(self.listaCompletaResumoExpandidoEmCongresso, membro)
                self.adicionarCoautorNaLista(self.listaCompletaResumoEmCongresso, membro)
                self.adicionarCoautorNaLista(self.listaCompletaArtigoAceito, membro)
                self.adicionarCoautorNaLista(self.listaCompletaApresentacaoDeTrabalho, membro)
                self.adicionarCoautorNaLista(self.listaCompletaOutroTipoDeProducaoBibliografica, membro)

                self.adicionarCoautorNaLista(self.listaCompletaSoftwareComPatente, membro)
                self.adicionarCoautorNaLista(self.listaCompletaSoftwareSemPatente, membro)
                self.adicionarCoautorNaLista(self.listaCompletaProdutoTecnologico, membro)
                self.adicionarCoautorNaLista(self.listaCompletaProcessoOuTecnica, membro)
                self.adicionarCoautorNaLista(self.listaCompletaTrabalhoTecnico, membro)
                self.adicionarCoautorNaLista(self.listaCompletaOutroTipoDeProducaoTecnica, membro)

                self.adicionarCoautorNaLista(self.listaCompletaPatente, membro)
                self.adicionarCoautorNaLista(self.listaCompletaProgramaComputador, membro)
                self.adicionarCoautorNaLista(self.listaCompletaDesenhoIndustrial, membro)

                self.adicionarCoautorNaLista(self.listaCompletaProducaoArtistica, membro)


    def adicionarCoautorNaLista(self, listaCompleta, membro):
        keys = listaCompleta.keys()
        for ano in keys:
            for pub in listaCompleta[ano]:
                if self.procuraNomeEmPublicacao(membro.nomeInicial, pub.autores):
                    pub.idMembro.add(membro.idMembro)
                    # print ">>>" + membro.nomeInicial
                    #print ">>>" + pub.autores


    def procuraNomeEmPublicacao(self, nomesAbreviados, nomesDosCoautores):
        nomesAbreviados = nomesAbreviados.lower()
        nomesDosCoautores = nomesDosCoautores.lower()

        nomesAbreviados = nomesAbreviados.replace(".", " ")
        nomesDosCoautores = nomesDosCoautores.replace(".", " ")
        nomesDosCoautores = nomesDosCoautores.replace(",", " ")
        nomesAbreviados = re.sub('\s+', ' ', nomesAbreviados).strip()
        nomesDosCoautores = re.sub('\s+', ' ', nomesDosCoautores).strip()

        listaNomesAbreviados = nomesAbreviados.split(";")
        listaNomesDosCoautores = nomesDosCoautores.split(";")

        for abrev1 in listaNomesAbreviados:
            abrev1 = abrev1.strip()
            for abrev2 in listaNomesDosCoautores:
                abrev2 = abrev2.strip()
                if abrev1 == abrev2 and len(abrev1) > 0 and len(abrev2) > 0:
                    return True
        return False


    def compilarLista(self, listaDoMembro, listaCompleta):
        for pub in listaDoMembro:  # adicionar 'pub'  em  'listaCompleta'
            if pub == None or listaCompleta.get(pub.ano) == None:  # Se o ano nao existe no listaCompleta (lista total)
                listaCompleta[pub.ano] = []  # criamos uma nova entrada vazia
                listaCompleta[pub.ano].append(pub)
            else:
                inserir = 1
                for i in range(0, len(listaCompleta[pub.ano])):
                    item = pub.compararCom(listaCompleta[pub.ano][i])  # comparamos: pub com listaCompleta[pub.ano][i]
                    if not item == None:  # sao similares
                        print "\n[AVISO] PRODUÇÕES SIMILARES",
                        print pub,
                        print listaCompleta[pub.ano][i]
                        # print "Membro " + str(pub.idMembro) + ": " + pub.titulo.encode('utf8')
                        # print "Membro " + str(listaCompleta[pub.ano][i].idMembro) + ": " + listaCompleta[pub.ano][i].titulo.encode('utf8')

                        listaCompleta[pub.ano][i] = item
                        inserir = 0
                        break
                if inserir:  # se pub for difererente a todos os elementos do listaCompleta
                    listaCompleta[pub.ano].append(pub)
        return listaCompleta

    # Para projetos não é feita a busca de projetos similares (NÃO MAIS UTILIZADA)
    def compilarListaDeProjetos(self, listaDoMembro, listaCompleta):
        for pub in listaDoMembro:  # adicionar 'pub'  em  'listaCompleta'
            if listaCompleta.get(pub.anoInicio) == None:
                listaCompleta[pub.anoInicio] = []
            listaCompleta[pub.anoInicio].append(pub)
        return listaCompleta

    def compilarListasCompletas(self, listaCompleta, listaTotal):
        keys = listaCompleta.keys()
        for ano in keys:
            if listaTotal.get(ano) == None:
                listaTotal[ano] = []
            listaTotal[ano].extend(listaCompleta[ano])
        return listaTotal


    def criarMatrizesDeColaboracao(self):
        if self.grupo.obterParametro('grafo-incluir_artigo_em_periodico'):
            self.matrizesArtigoEmPeriodico = self.criarMatrizes(self.listaCompletaArtigoEmPeriodico)
        if self.grupo.obterParametro('grafo-incluir_livro_publicado'):
            self.matrizesLivroPublicado = self.criarMatrizes(self.listaCompletaLivroPublicado)
        if self.grupo.obterParametro('grafo-incluir_capitulo_de_livro_publicado'):
            self.matrizesCapituloDeLivroPublicado = self.criarMatrizes(self.listaCompletaCapituloDeLivroPublicado)
        if self.grupo.obterParametro('grafo-incluir_texto_em_jornal_de_noticia'):
            self.matrizesTextoEmJornalDeNoticia = self.criarMatrizes(self.listaCompletaTextoEmJornalDeNoticia)
        if self.grupo.obterParametro('grafo-incluir_trabalho_completo_em_congresso'):
            self.matrizesTrabalhoCompletoEmCongresso = self.criarMatrizes(self.listaCompletaTrabalhoCompletoEmCongresso)
        if self.grupo.obterParametro('grafo-incluir_resumo_expandido_em_congresso'):
            self.matrizesResumoExpandidoEmCongresso = self.criarMatrizes(self.listaCompletaResumoExpandidoEmCongresso)
        if self.grupo.obterParametro('grafo-incluir_resumo_em_congresso'):
            self.matrizesResumoEmCongresso = self.criarMatrizes(self.listaCompletaResumoEmCongresso)
        if self.grupo.obterParametro('grafo-incluir_artigo_aceito_para_publicacao'):
            self.matrizesArtigoAceito = self.criarMatrizes(self.listaCompletaArtigoAceito)
        if self.grupo.obterParametro('grafo-incluir_apresentacao_de_trabalho'):
            self.matrizesApresentacaoDeTrabalho = self.criarMatrizes(self.listaCompletaApresentacaoDeTrabalho)
        if self.grupo.obterParametro('grafo-incluir_outro_tipo_de_producao_bibliografica'):
            self.matrizesOutroTipoDeProducaoBibliografica = self.criarMatrizes(self.listaCompletaOutroTipoDeProducaoBibliografica)

        if self.grupo.obterParametro('grafo-incluir_software_com_patente'):
            self.matrizesSoftwareComPatente = self.criarMatrizes(self.listaCompletaSoftwareComPatente)
        if self.grupo.obterParametro('grafo-incluir_software_sem_patente'):
            self.matrizesSoftwareSemPatente = self.criarMatrizes(self.listaCompletaSoftwareSemPatente)
        if self.grupo.obterParametro('grafo-incluir_produto_tecnologico'):
            self.matrizesProdutoTecnologico = self.criarMatrizes(self.listaCompletaProdutoTecnologico)
        if self.grupo.obterParametro('grafo-incluir_processo_ou_tecnica'):
            self.matrizesProcessoOuTecnica = self.criarMatrizes(self.listaCompletaProcessoOuTecnica)
        if self.grupo.obterParametro('grafo-incluir_trabalho_tecnico'):
            self.matrizesTrabalhoTecnico = self.criarMatrizes(self.listaCompletaTrabalhoTecnico)
        if self.grupo.obterParametro('grafo-incluir_outro_tipo_de_producao_tecnica'):
            self.matrizesOutroTipoDeProducaoTecnica = self.criarMatrizes(self.listaCompletaOutroTipoDeProducaoTecnica)

        if self.grupo.obterParametro('grafo-incluir_patente'):
            self.matrizesPatente = self.criarMatrizes(self.listaCompletaPatente)
        if self.grupo.obterParametro('grafo-incluir_programa_computador'):
            self.matrizesProgramaComputador = self.criarMatrizes(self.listaCompletaProgramaComputador)
        if self.grupo.obterParametro('grafo-incluir_desenho_industrial'):
            self.matrizesDesenhoIndustrial = self.criarMatrizes(self.listaCompletaDesenhoIndustrial)

        if self.grupo.obterParametro('grafo-incluir_producao_artistica'):
            self.matrizesProducaoArtistica = self.criarMatrizes(self.listaCompletaProducaoArtistica)


        # Criamos as matrizes de:
        #  - (1) adjacência
        #  - (2) frequencia

    def criarMatrizes(self, listaCompleta):
        # matriz1 = numpy.zeros((self.grupo.numeroDeMembros(), self.grupo.numeroDeMembros()), dtype=numpy.int32)
        # matriz2 = numpy.zeros((self.grupo.numeroDeMembros(), self.grupo.numeroDeMembros()), dtype=numpy.float32)
        matriz1 = sparse.lil_matrix((self.grupo.numeroDeMembros(), self.grupo.numeroDeMembros()))
        matriz2 = sparse.lil_matrix((self.grupo.numeroDeMembros(), self.grupo.numeroDeMembros()))

        # armazenamos a lista de itens associadas a cada colaboracao endogena
        listaDeColaboracoes = list([])
        for i in range(0, self.grupo.numeroDeMembros()):
            listaDeColaboracoes.append( dict([]) )

        keys = listaCompleta.keys()
        keys.sort(reverse=True)
        for k in keys:
            for pub in listaCompleta[k]:

                numeroDeCoAutores = len(pub.idMembro)
                if numeroDeCoAutores > 1:
                    # Para todos os co-autores da publicacao:
                    # (1) atualizamos o contador de colaboracao (adjacencia)
                    # (2) incrementamos a 'frequencia' de colaboracao
                    combinacoes = self.calcularCombinacoes(pub.idMembro)
                    for c in combinacoes:
                        matriz1[c[0], c[1]] += 1
                        matriz1[c[1], c[0]] += 1
                        matriz2[c[0], c[1]] += 1.0 / (numeroDeCoAutores - 1)
                        matriz2[c[1], c[0]] += 1.0 / (numeroDeCoAutores - 1)
                        
                        if not c[0] in listaDeColaboracoes[c[1]]:
                            listaDeColaboracoes[c[1]][ c[0] ] = list([])
                        if not c[1] in listaDeColaboracoes[c[0]]:
                            listaDeColaboracoes[c[0]][ c[1] ] = list([])

                        listaDeColaboracoes[c[0]][ c[1] ].append(pub)
                        listaDeColaboracoes[c[1]][ c[0] ].append(pub)

        return [matriz1, matriz2, listaDeColaboracoes]


    # combinacoes 2 a 2 de todos os co-autores da publicação
    # exemplo:
    # lista = [0, 3, 1]
    # combinacoes = [[0,3], [0,1], [3,1]]
    def calcularCombinacoes(self, conjunto):
        lista = list(conjunto)
        combinacoes = []
        for i in range(0, len(lista) - 1):
            for j in range(i + 1, len(lista)):
                combinacoes.append([lista[i], lista[j]])
        return combinacoes


    def intercalar_colaboracoes(self, lista1, lista2):
        for i in range(0, self.grupo.numeroDeMembros()):
            lista1[i] = merge_dols( lista1[i], lista2[i] )
        return lista1


    def uniaoDeMatrizesDeColaboracao(self):
        ##matriz1 = numpy.zeros((self.grupo.numeroDeMembros(), self.grupo.numeroDeMembros()), dtype=numpy.int32)
        ##matriz2 = numpy.zeros((self.grupo.numeroDeMembros(), self.grupo.numeroDeMembros()), dtype=numpy.float32)
        matriz1 = sparse.lil_matrix((self.grupo.numeroDeMembros(), self.grupo.numeroDeMembros()))
        matriz2 = sparse.lil_matrix((self.grupo.numeroDeMembros(), self.grupo.numeroDeMembros()))
        colaboracoes = []
        for i in range(0, self.grupo.numeroDeMembros()):
            colaboracoes.append([])

        if self.grupo.obterParametro('grafo-incluir_artigo_em_periodico'):
            matriz1 += self.matrizesArtigoEmPeriodico[0]
            matriz2 += self.matrizesArtigoEmPeriodico[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesArtigoEmPeriodico[2] )
        if self.grupo.obterParametro('grafo-incluir_livro_publicado'):
            matriz1 += self.matrizesLivroPublicado[0]
            matriz2 += self.matrizesLivroPublicado[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesLivroPublicado[2] )
        if self.grupo.obterParametro('grafo-incluir_capitulo_de_livro_publicado'):
            matriz1 += self.matrizesCapituloDeLivroPublicado[0]
            matriz2 += self.matrizesCapituloDeLivroPublicado[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesCapituloDeLivroPublicado[2] )
        if self.grupo.obterParametro('grafo-incluir_texto_em_jornal_de_noticia'):
            matriz1 += self.matrizesTextoEmJornalDeNoticia[0]
            matriz2 += self.matrizesTextoEmJornalDeNoticia[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesTextoEmJornalDeNoticia[2] )
        if self.grupo.obterParametro('grafo-incluir_trabalho_completo_em_congresso'):
            matriz1 += self.matrizesTrabalhoCompletoEmCongresso[0]
            matriz2 += self.matrizesTrabalhoCompletoEmCongresso[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesTrabalhoCompletoEmCongresso[2] )
        if self.grupo.obterParametro('grafo-incluir_resumo_expandido_em_congresso'):
            matriz1 += self.matrizesResumoExpandidoEmCongresso[0]
            matriz2 += self.matrizesResumoExpandidoEmCongresso[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesResumoExpandidoEmCongresso[2] )
        if self.grupo.obterParametro('grafo-incluir_resumo_em_congresso'):
            matriz1 += self.matrizesResumoEmCongresso[0]
            matriz2 += self.matrizesResumoEmCongresso[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesResumoEmCongresso[2] )
        if self.grupo.obterParametro('grafo-incluir_artigo_aceito_para_publicacao'):
            matriz1 += self.matrizesArtigoAceito[0]
            matriz2 += self.matrizesArtigoAceito[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesArtigoAceito[2] )
        if self.grupo.obterParametro('grafo-incluir_apresentacao_de_trabalho'):
            matriz1 += self.matrizesApresentacaoDeTrabalho[0]
            matriz2 += self.matrizesApresentacaoDeTrabalho[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesApresentacaoDeTrabalho[2] )
        if self.grupo.obterParametro('grafo-incluir_outro_tipo_de_producao_bibliografica'):
            matriz1 += self.matrizesOutroTipoDeProducaoBibliografica[0]
            matriz2 += self.matrizesOutroTipoDeProducaoBibliografica[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesOutroTipoDeProducaoBibliografica[2] )

        if self.grupo.obterParametro('grafo-incluir_software_com_patente'):
            matriz1 += self.matrizesSoftwareComPatente[0]
            matriz2 += self.matrizesSoftwareComPatente[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesSoftwareComPatente[2] )
        if self.grupo.obterParametro('grafo-incluir_software_sem_patente'):
            matriz1 += self.matrizesSoftwareSemPatente[0]
            matriz2 += self.matrizesSoftwareSemPatente[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesSoftwareSemPatente[2] )
        if self.grupo.obterParametro('grafo-incluir_produto_tecnologico'):
            matriz1 += self.matrizesProdutoTecnologico[0]
            matriz2 += self.matrizesProdutoTecnologico[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesProdutoTecnologico[2] )
        if self.grupo.obterParametro('grafo-incluir_processo_ou_tecnica'):
            matriz1 += self.matrizesProcessoOuTecnica[0]
            matriz2 += self.matrizesProcessoOuTecnica[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesProcessoOuTecnica[2] )
        if self.grupo.obterParametro('grafo-incluir_trabalho_tecnico'):
            matriz1 += self.matrizesTrabalhoTecnico[0]
            matriz2 += self.matrizesTrabalhoTecnico[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesTrabalhoTecnico[2] )
        if self.grupo.obterParametro('grafo-incluir_outro_tipo_de_producao_tecnica'):
            matriz1 += self.matrizesOutroTipoDeProducaoTecnica[0]
            matriz2 += self.matrizesOutroTipoDeProducaoTecnica[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesOutroTipoDeProducaoTecnica[2] )

        if self.grupo.obterParametro('grafo-incluir_patente'):
            matriz1 += self.matrizesPatente[0]
            matriz2 += self.matrizesPatente[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesPatente[2] )

        if self.grupo.obterParametro('grafo-incluir_programa_computador'):
            matriz1 += self.matrizesProgramaComputador[0]
            matriz2 += self.matrizesProgramaComputador[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesProgramaComputador[2] )

        if self.grupo.obterParametro('grafo-incluir_desenho_industrial'):
            matriz1 += self.matrizesDesenhoIndustrial[0]
            matriz2 += self.matrizesDesenhoIndustrial[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesDesenhoIndustrial[2] )

        if self.grupo.obterParametro('grafo-incluir_producao_artistica'):
            matriz1 += self.matrizesProducaoArtistica[0]
            matriz2 += self.matrizesProducaoArtistica[1]
            colaboracoes = self.intercalar_colaboracoes( colaboracoes, self.matrizesProducaoArtistica[2] )

        return [matriz1, matriz2, colaboracoes]


    def imprimirMatrizesDeFrequencia(self):
        print "\n[LISTA DE MATRIZES DE FREQUENCIA]"
        print "\nArtigo em periodico"
        print self.matrizArtigoEmPeriodico
        print "\nLivro publicado"
        print self.matrizLivroPublicado
        print "\nCapitulo de livro publicado"
        print self.matrizCapituloDeLivroPublicado
        print "\nTexto em jornal de noticia"
        print self.matrizTextoEmJornalDeNoticia
        print "\nTrabalho completo em congresso"
        print self.matrizTrabalhoCompletoEmCongresso
        print "\nResumo expandido em congresso"
        print self.matrizResumoExpandidoEmCongresso
        print "\nResumo em congresso"
        print self.matrizResumoEmCongresso
        print "\nArtigo aceito"
        print self.matrizArtigoAceito
        print "\nApresentacao de trabalho"
        print self.matrizApresentacaoDeTrabalho
        print "\nOutro tipo de producao bibliografica"
        print self.matrizOutroTipoDeProducaoBibliografica
        print "\nSoftware com patente"
        print self.matrizSoftwareComPatente
        print "\nSoftware sem patente"
        print self.matrizSoftwareSemPatente
        print "\nProduto tecnologico"
        print self.matrizProdutoTecnologico
        print "\nProcesso ou tecnica"
        print self.matrizProcessoOuTecnica
        print "\nTrabalho tecnico"
        print self.matrizTrabalhoTecnico
        print "\nOutro tipo de producao tecnica"
        print self.matrizOutroTipoDeProducaoTecnica

        print "\nPatente"
        print self.matrizPatente
        print "\nPrograma de computador"
        print self.matrizProgramaComputador
        print "\nDesenho industrial"
        print self.matrizDesenhoIndustrial

        print "\nProducao artistica"
        print self.matrizProducaoArtistica


    def imprimirListasCompletas(self):
        print "\n\n[LISTA COMPILADA DE PRODUÇÕES]"

        print "\nArtigo em periodico"
        self.imprimirListaProducoes(self.listaCompletaArtigoEmPeriodico)
        print "\nLivro publicado"
        self.imprimirListaProducoes(self.listaCompletaLivroPublicado)
        print "\nCapitulo de livro publicado"
        self.imprimirListaProducoes(self.listaCompletaCapituloDeLivroPublicado)
        print "\nTexto em jornal de noticia"
        self.imprimirListaProducoes(self.listaCompletaTextoEmJornalDeNoticia)
        print "\nTrabalho completo em congresso"
        self.imprimirListaProducoes(self.listaCompletaTrabalhoCompletoEmCongresso)
        print "\nResumo expandido em congresso"
        self.imprimirListaProducoes(self.listaCompletaResumoExpandidoEmCongresso)
        print "\nResumo em congresso"
        self.imprimirListaProducoes(self.listaCompletaResumoEmCongresso)
        print "\nArtigo aceito"
        self.imprimirListaProducoes(self.listaCompletaArtigoAceito)
        print "\nApresentacao de trabalho"
        self.imprimirListaProducoes(self.listaCompletaApresentacaoDeTrabalho)
        print "\nOutro tipo de producao bibliografica"
        self.imprimirListaProducoes(self.listaCompletaOutroTipoDeProducaoBibliografica)
        print "\nTOTAL DE PB"
        self.imprimirListaProducoes(self.listaCompletaPB)

        print "\nSoftware com patente"
        self.imprimirListaProducoes(self.listaCompletaSoftwareComPatente)
        print "\nSoftware sem patente"
        self.imprimirListaProducoes(self.listaCompletaSoftwareSemPatente)
        print "\nProduto tecnologico"
        self.imprimirListaProducoes(self.listaCompletaProdutoTecnologico)
        print "\nProcesso ou tecnica"
        self.imprimirListaProducoes(self.listaCompletaProcessoOuTecnica)
        print "\nTrabalho tecnico"
        self.imprimirListaProducoes(self.listaCompletaTrabalhoTecnico)
        print "\nOutro tipo de producao tecnica"
        self.imprimirListaProducoes(self.listaCompletaOutroTipoDeProducaoTecnica)
        print "\nTOTAL DE PT"
        self.imprimirListaProducoes(self.listaCompletaPT)

        print "\nPatente"
        self.imprimirListaProducoes(self.listaCompletaPatente)
        print "\nPrograma de computador"
        self.imprimirListaProducoes(self.listaCompletaProgramaComputador)
        print "\nDesenho industrial"
        self.imprimirListaProducoes(self.listaCompletaDesenhoIndustrial)
        print "\nTOTAL DE PR"
        self.imprimirListaProducoes(self.listaCompletaPR)

        print "\nProducao artistica"
        self.imprimirListaProducoes(self.listaCompletaProducaoArtistica)
        print "\nTOTAL DE PA"
        self.imprimirListaProducoes(self.listaCompletaPA)

        print "\n\n[LISTA COMPILADA DE ORIENTAÇÕES]"
        print "\nOA - Pos doutorado"
        self.imprimirListaOrientacoes(self.listaCompletaOASupervisaoDePosDoutorado)
        print "\nOA - Doutorado"
        self.imprimirListaOrientacoes(self.listaCompletaOATeseDeDoutorado)
        print "\nOA - Mestrado"
        self.imprimirListaOrientacoes(self.listaCompletaOADissertacaoDeMestrado)
        print "\nOA - Monografia de especializacao"
        self.imprimirListaOrientacoes(self.listaCompletaOAMonografiaDeEspecializacao)
        print "\nOA - TCC"
        self.imprimirListaOrientacoes(self.listaCompletaOATCC)
        print "\nOA - Iniciacao cientifica"
        self.imprimirListaOrientacoes(self.listaCompletaOAIniciacaoCientifica)
        print "\nOA - Outro tipo de orientacao"
        self.imprimirListaOrientacoes(self.listaCompletaOAOutroTipoDeOrientacao)
        print "\nTOTAL DE OA"
        self.imprimirListaOrientacoes(self.listaCompletaOA)

        print "\nOC - Pos doutorado"
        self.imprimirListaOrientacoes(self.listaCompletaOCSupervisaoDePosDoutorado)
        print "\nOC - Doutorado"
        self.imprimirListaOrientacoes(self.listaCompletaOCTeseDeDoutorado)
        print "\nOC - Mestrado"
        self.imprimirListaOrientacoes(self.listaCompletaOCDissertacaoDeMestrado)
        print "\nOC - Monografia de especializacao"
        self.imprimirListaOrientacoes(self.listaCompletaOCMonografiaDeEspecializacao)
        print "\nOC - TCC"
        self.imprimirListaOrientacoes(self.listaCompletaOCTCC)
        print "\nOC - Iniciacao cientifica"
        self.imprimirListaOrientacoes(self.listaCompletaOCIniciacaoCientifica)
        print "\nOC - Outro tipo de orientacao"
        self.imprimirListaOrientacoes(self.listaCompletaOCOutroTipoDeOrientacao)
        print "\nTOTAL DE OC"
        self.imprimirListaOrientacoes(self.listaCompletaOC)

        print "\n[LISTA COMPILADA DE PROJETOS]"
        self.imprimirListaProjetos(self.listaCompletaProjetoDePesquisa)

        print "\n[LISTA COMPILADA DE PREMIOS]"
        self.imprimirListaPremios(self.listaCompletaPremioOuTitulo)

        print "\n[LISTA COMPILADA DE PARTICIPACAO EM EVENTOS] ..."
        print "\n[LISTA COMPILADA DE ORGANIZACAO DE EVENTOS] ..."


    def imprimirListaProducoes(self, listaCompleta):
        print "---------------------------------------------------------------------------"
        keys = listaCompleta.keys()
        keys.sort(reverse=True)
        for k in keys:
            print k
            listaCompleta[k].sort(key=operator.attrgetter('autores'))

            for pub in listaCompleta[k]:
                print "--- " + str(pub.idMembro)
                print "--- " + pub.autores.encode('utf8')
                print "--- " + pub.titulo.encode('utf8') + "\n"


    def imprimirListaOrientacoes(self, listaCompleta):
        print "---------------------------------------------------------------------------"
        keys = listaCompleta.keys()
        keys.sort(reverse=True)
        for k in keys:
            print k
            listaCompleta[k].sort(key=operator.attrgetter('nome'))

            for pub in listaCompleta[k]:
                print "--- " + str(pub.idMembro)
                print "--- " + pub.nome.encode('utf8')
                print "--- " + pub.tituloDoTrabalho.encode('utf8') + "\n"


    def imprimirListaProjetos(self, listaCompleta):
        print "---------------------------------------------------------------------------"
        keys = listaCompleta.keys()
        keys.sort(reverse=True)
        for k in keys:
            print k
            listaCompleta[k].sort(key=operator.attrgetter('nome'))

            for pub in listaCompleta[k]:
                print "--- " + str(pub.idMembro)
                print "--- " + pub.nome.encode('utf8')
                print "--- " + pub.cargo.encode('utf8') + "\n"


    def imprimirListaPremios(self, listaCompleta):
        print "---------------------------------------------------------------------------"
        keys = listaCompleta.keys()
        keys.sort(reverse=True)
        for k in keys:
            print k
            listaCompleta[k].sort(key=operator.attrgetter('descricao'))

            for pub in listaCompleta[k]:
                print "--- " + str(pub.idMembro)
                print "--- " + pub.descricao.encode('utf8') + "\n"

