#ifndef DIAALU_H
#define DIAALU_H

#include <QDialog>

namespace Ui {
class diaalu;
}

class diaalu : public QDialog
{
    Q_OBJECT

public:
    explicit diaalu(QWidget *parent = nullptr);
    ~diaalu();

private:
    Ui::diaalu *ui;
};

#endif // DIAALU_H
