#!/usr/bin/python
# encoding: utf-8
# filename: apresentacaoDeTrabalho.py
#
#  scriptLattes V8
#  Copyright 2005-2013: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
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


import re

from scriptLattes.util import similaridade_entre_cadeias


class ApresentacaoDeTrabalho:
	item = None # dado bruto
	idMembro = None

	relevante = None
	autores = None
	titulo = None
	ano = None
	natureza = None # tipo de apresentacao
	chave = None


	def __init__(self, idMembro, partesDoItem='', relevante=''):
		self.idMembro = set([])
		self.idMembro.add(idMembro)

		if not partesDoItem=='': 
			# partesDoItem[0]: Numero (NAO USADO)
			# partesDoItem[1]: Descricao do livro (DADO BRUTO)

			self.relevante = relevante
			self.item = partesDoItem[1]

			# Dividir o item na suas partes constituintes
			if " . " in self.item:
				partes = self.item.partition(" . ")
			else:
				partes = self.item.partition(".. ")

			self.autores = partes[0].strip()
			partes = partes[2]

			aux = re.findall(u' \((.*?)\)', partes)
			if len(aux)>0:
				self.natureza = aux[-1]
				partes = partes.rpartition(" (")
				partes = partes[0]
			else:
				self.natureza = ''
	
			aux = re.findall(u'. ((?:19|20)\d\d)\\b', partes)
			if len(aux)>0:
				self.ano = aux[-1] #.strip().rstrip(".").rstrip(",")
				partes = partes.rpartition(". ")
				partes = partes[0]
			else:
				self.ano = ''
	
			self.titulo = partes.strip().rstrip(".")
			self.chave = self.autores # chave de comparação entre os objetos

		else:
			self.relevante = ''
			self.autores = ''
			self.titulo = ''
			self.ano = ''
			self.natureza = ''


	def compararCom(self, objeto):
		if self.idMembro.isdisjoint(objeto.idMembro) and similaridade_entre_cadeias(self.titulo, objeto.titulo):
			# Os IDs dos membros são agrupados. 
			# Essa parte é importante para a criação do GRAFO de colaborações
			self.idMembro.update(objeto.idMembro)

			if len(self.autores)<len(objeto.autores):
				self.autores = objeto.autores

			if len(self.titulo)<len(objeto.titulo):
				self.titulo = objeto.titulo

			if len(self.natureza)<len(objeto.natureza):
				self.natureza = objeto.natureza

			return self
		else: # nao similares
			return None


	def html(self, listaDeMembros):
		s = self.autores + '. <b>' + self.titulo + '</b>. ' 
		s+= str(self.ano) + '. '  if str(self.ano).isdigit() else '. '
		s+= self.natureza        if not self.natureza=='' else ''

 		# s+= menuHTMLdeBuscaPB(self.titulo)
		return s


	# ------------------------------------------------------------------------ #
	def __str__(self):
		s  = "\n[APRESENTACAO DE TRABALHO] \n"
		s += "+ID-MEMBRO   : " + str(self.idMembro) + "\n"
		s += "+RELEVANTE   : " + str(self.relevante) + "\n"
		s += "+AUTORES     : " + self.autores.encode('utf8','replace') + "\n"
		s += "+TITULO      : " + self.titulo.encode('utf8','replace') + "\n"
		s += "+ANO         : " + str(self.ano) + "\n"
		s += "+NATUREZA    : " + self.natureza.encode('utf8','replace') + "\n"
		s += "+item        : " + self.item.encode('utf8','replace') + "\n"
		return s
