#ifndef ALUNO_H_
#define ALUNO_H_
#include <string>
using namespace std;
class Aluno {
	// atributos privados por padrao da linguagem
	int atraso;
	int assiduo;
	int ocorrencia;
	int postura;
	int desempenho;
	int matricula;
	string dataNasc; //string para pessoa poder digitar barras. Ex.: 10 / 11 / 2003
	string nome;
	//privados por serem caracteristicas individuais de cada aluno
public:
	//encapsulamentos
	int getAtraso();
	int getAssiduo();
	int getOcorrencia();
	int getPostura();
	int getDesempenho();
	int getMatricula();
	int getDataNasc();
	int getNome();
	void setAtraso(int atraso);
	void setAssiduo(int assiduo);
	void setOcorrencia(int ocorrencia);
	void setPostura(int postura);
	void setDesempenho(int Desempenho);
	void setMatricula(int matricula);
	void setDataNasc(string dataNasc);
	void setNome(string nome);
};

#endif
