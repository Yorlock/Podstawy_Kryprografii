#ifndef CHANGEKEYWINDOW_H
#define CHANGEKEYWINDOW_H

#include <QMainWindow>
#include <QFile>
#include <QString>
#include <QTextStream>
#include <QMessageBox>
#include <mainwindow.h>

namespace Ui {
class changeKeyWindow;
}

class changeKeyWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit changeKeyWindow(QMainWindow *parent = nullptr);
    changeKeyWindow(QMainWindow *parent, QString text);
    ~changeKeyWindow();
    QString editedText;

private slots:
    void on_pushButton_clicked();

private:
    Ui::changeKeyWindow *ui;
};

#endif // CHANGEKEYWINDOW_H
