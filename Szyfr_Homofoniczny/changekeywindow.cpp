#include "changekeywindow.h"
#include "ui_changekeywindow.h"

changeKeyWindow::changeKeyWindow(QMainWindow *parent, QString text) :
    QMainWindow(parent),
    ui(new Ui::changeKeyWindow)
{
    ui->setupUi(this);
    ui->textEdit->setText(text);
}

changeKeyWindow::~changeKeyWindow()
{
    delete ui;
}

void changeKeyWindow::on_pushButton_clicked()
{
    ((MainWindow*)(parent()))->wholeText = ui->textEdit->toPlainText();
    close();
}
