#include "novdoi.h"
#include "ui_novdoi.h"
#include "novtre.h"
novDoi::novDoi(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::novDoi)
{
    ui->setupUi(this);
}

novDoi::~novDoi()
{
    delete ui;
}

void novDoi::on_pushButton_clicked()
{
    close();
    novTre b;
    b.exec();
}
