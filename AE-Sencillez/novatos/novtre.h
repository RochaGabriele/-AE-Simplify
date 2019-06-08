#ifndef NOVTRE_H
#define NOVTRE_H

#include <QDialog>

namespace Ui {
class novTre;
}

class novTre : public QDialog
{
    Q_OBJECT

public:
    explicit novTre(QWidget *parent = nullptr);
    ~novTre();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::novTre *ui;
};

#endif // NOVTRE_H
