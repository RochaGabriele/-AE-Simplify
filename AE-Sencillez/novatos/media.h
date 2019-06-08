#ifndef MEDIA_H
#define MEDIA_H

#include <QDialog>

namespace Ui {
class media;
}

class media : public QDialog
{
    Q_OBJECT

public:
    explicit media(QWidget *parent = nullptr);
    ~media();

private slots:
    void on_pushButton_clicked();

private:
    Ui::media *ui;
};

#endif // MEDIA_H
