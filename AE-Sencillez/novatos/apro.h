#ifndef APRO_H
#define APRO_H

#include <QDialog>

namespace Ui {
class apro;
}

class apro : public QDialog
{
    Q_OBJECT

public:
    explicit apro(QWidget *parent = nullptr);
    ~apro();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::apro *ui;
};

#endif // APRO_H
