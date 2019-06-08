/********************************************************************************
** Form generated from reading UI file 'diaver.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DIAVER_H
#define UI_DIAVER_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_diaver
{
public:

    void setupUi(QWidget *diaver)
    {
        if (diaver->objectName().isEmpty())
            diaver->setObjectName(QString::fromUtf8("diaver"));
        diaver->resize(431, 300);

        retranslateUi(diaver);

        QMetaObject::connectSlotsByName(diaver);
    } // setupUi

    void retranslateUi(QWidget *diaver)
    {
        diaver->setWindowTitle(QApplication::translate("diaver", "Form", nullptr));
    } // retranslateUi

};

namespace Ui {
    class diaver: public Ui_diaver {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DIAVER_H
