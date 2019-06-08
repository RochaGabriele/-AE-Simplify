#include "repro.h"
#include "ui_repro.h"
#include "novtre.h"

repro::repro(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::repro)
{
    ui->setupUi(this);
}

repro::~repro()
{
    delete ui;
}

void repro::on_pushButton_clicked()
{
    close();
    novTre f;
    f.exec();
}
void repro::on_pushButton_2_clicked()
{
    close();
}
