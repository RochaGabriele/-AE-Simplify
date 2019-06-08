#include "diaver.h"
#include "ui_diaver.h"

diaver::diaver(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::diaver)
{
    ui->setupUi(this);
}

diaver::~diaver()
{
    delete ui;
}
