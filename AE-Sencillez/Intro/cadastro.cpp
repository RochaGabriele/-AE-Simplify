#include "cadastro.h"
#include "ui_cadastro.h"

Cadastro::Cadastro(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Cadastro)
{
    ui->setupUi(this);
}

Cadastro::~Cadastro()
{
    delete ui;
}
