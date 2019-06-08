#include "entrada.h"
#include "ui_entrada.h"
#include "cadastro.h"

Entrada::Entrada(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Entrada)
{
    ui->setupUi(this);

    connect(ui->pushButton,SIGNAL(clicked()),this,SLOT(Entrada));
}

Entrada::~Entrada()
{
    delete ui;
}

void Entrada::on_pushButton_clicked()
{
        Cadastro cadastrinho;
        cadastrinho.show();
}
