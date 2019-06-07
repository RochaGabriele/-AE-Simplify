#ifndef DES_H
#define DES_H

#include <QDialog>

namespace Ui {
class des;
}

class des : public QDialog
{
    Q_OBJECT

public:
    explicit des(QWidget *parent = nullptr);
    ~des();
    int prifev = 0.0;
    int primar = 0.0;
    int priabr = 0.0;
    int primai = 0.0;
    int prijun = 0.0;
    int priago = 0.0;
    int priset = 0.0;
    int priout = 0.0;
    int prinov = 0.0;
    int pridez = 0.0;
    int segfev = 0.0;
    int segmar = 0.0;
    int segabr = 0.0;
    int segmai = 0.0;
    int segjun = 0.0;
    int segago = 0.0;
    int segset = 0.0;
    int segout = 0.0;
    int segnov = 0.0;
    int segdez = 0.0;
    int terfev = 0.0;
    int termar = 0.0;
    int terabr = 0.0;
    int termai = 0.0;
    int terjun = 0.0;
    int terago = 0.0;
    int terset = 0.0;
    int terout = 0.0;
    int ternov = 0.0;
    int terdez = 0.0;

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::des *ui;
};

#endif // DES_H
