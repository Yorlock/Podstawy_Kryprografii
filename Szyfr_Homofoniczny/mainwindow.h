#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <fstream>
#include <string>
#include <iostream>
#include <QMessageBox>
#include <map>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <cstdlib>
#include <QFile>
#include <QString>
#include <QTextStream>
#include <descriptiondialog.h>
#include <changekeywindow.h>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    QString wholeText = "";

private slots:
    void on_descriptionPushButton_clicked();

    void on_codePushButton_clicked();

    void on_decodePushButton_clicked();

    void on_pushButton_clicked();

private:
    Ui::MainWindow *ui;
    std::map<std::string, std::vector<std::string>> code;
    std::map<std::string, std::string> decode;
    bool getKeyFromFile();
    void getKeyFromText();
    void checkKey();
    void changeKey();
    void errorOccured();
    std::string findCode(char text);
    std::string findDecode(std::string text);
    std::vector<std::string> split(const std::string& s, char delimiter);
    bool fileWasEdited = false;
};
#endif // MAINWINDOW_H
