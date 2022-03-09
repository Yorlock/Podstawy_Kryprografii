#include "mainwindow.h"
#include "ui_mainwindow.h"
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QCoreApplication::setApplicationName("Szyfr Homofoniczny");
    setWindowTitle( QCoreApplication::applicationName() );
    srand(time(0));
    if(!getKeyFromFile()) exit(0);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_descriptionPushButton_clicked()
{
    descriptionDialog *description = new descriptionDialog();
    description->show();
}

void MainWindow::on_pushButton_clicked()
{
    fileWasEdited = true;
    changeKeyWindow *window = new changeKeyWindow(this, wholeText);
    window->show();
}

bool MainWindow::getKeyFromFile()
{
    std::map<std::string, std::vector<std::string>>::iterator itr = code.begin();
    while (itr != code.end()) {
        itr = code.erase(itr);
    }

    std::map<std::string, std::string>::iterator itr2 = decode.begin();
    while (itr2 != decode.end()) {
        itr2 = decode.erase(itr2);
    }

    wholeText = "";
    QFile mFile(":/resource/key.txt");
    try
    {
        if(!mFile.open(QFile::ReadOnly | QFile::Text))
        {
            QMessageBox errorMessage;
            errorMessage.setText("Nie znaleziono pliku z kluczem.");
            errorMessage.exec();
            return false;
        }

        QTextStream in(&mFile);
        while(!in.atEnd())
        {
            std::string line = in.readLine().toStdString();
            wholeText += QString::fromStdString(line) + "\n";
            std::vector<std::string> data = split(line, ' ');
            std::vector<std::string> helper(data.begin() + 1, data.end());
            code.insert(std::pair<std::string, std::vector<std::string>>(data[0], helper));

            for(unsigned long long i=1; i<data.size(); i++)
              decode.insert(std::pair<std::string, std::string>(data[i], data[0]));
        }
        mFile.close();
        checkKey();
        return true;
    }
    catch(const char* message)
    {
        if (mFile.open(QFile::ReadOnly | QFile::Text)) mFile.close();
        QMessageBox errorMessage;
        errorMessage.setText(message);
        errorMessage.exec();
        return false;
    }
}

void MainWindow::getKeyFromText()
{
    std::map<std::string, std::vector<std::string>>::iterator itr = code.begin();
    while (itr != code.end()) {
        itr = code.erase(itr);
    }

    std::map<std::string, std::string>::iterator itr2 = decode.begin();
    while (itr2 != decode.end()) {
        itr2 = decode.erase(itr2);
    }

    QStringList list = wholeText.split("\n");
    for(auto l : list)
    {
        if(l == "") continue;
        std::vector<std::string> data = split(l.toStdString(), ' ');
        std::vector<std::string> helper(data.begin() + 1, data.end());
        code.insert(std::pair<std::string, std::vector<std::string>>(data[0], helper));

        for(unsigned long long i=1; i<data.size(); i++)
          decode.insert(std::pair<std::string, std::string>(data[i], data[0]));
    }
    checkKey();
}

void MainWindow::checkKey()
{
    std::vector<std::string> checkMultipleKeys;
    std::vector<std::string> checkMultipleValues;
    for(auto pair : code)
    {
        checkMultipleKeys.push_back(pair.first);
        for(auto p : pair.second)
            checkMultipleValues.push_back(p);
    }
    std::sort(checkMultipleKeys.begin(), checkMultipleKeys.end());
    for(unsigned long long i = 0; i < checkMultipleKeys.size() - 1; i++) {
        if (checkMultipleKeys[i] == checkMultipleKeys[i + 1]) {
            QMessageBox errorMessage;
            std::string text = "Występuje błąd w znakach jawnych:\n " + checkMultipleKeys[i] + " " + checkMultipleKeys[i + 1];
            errorMessage.setText(QString::fromStdString(text));
            errorMessage.exec();
            break;
        }
    }

    std::sort(checkMultipleValues.begin(), checkMultipleValues.end());
    for(unsigned long long i = 0; i < checkMultipleValues.size() - 1; i++) {
        if (checkMultipleValues[i] == checkMultipleValues[i + 1]) {
            QMessageBox errorMessage;
            std::string text = "Występuje błąd w znakach tajnych:\n " + checkMultipleValues[i] + " " + checkMultipleValues[i + 1];
            errorMessage.setText(QString::fromStdString(text));
            errorMessage.exec();
            break;
        }
    }
}

void MainWindow::errorOccured()
{
    QCoreApplication::quit();
}

void MainWindow::on_codePushButton_clicked()
{
    if(fileWasEdited) getKeyFromText();
    std::string result;
    std::string text = ui->standardTextEdit->toPlainText().toStdString();
    std::vector<std::string> data = split(text, ' ');
    for(std::string d : data)
    {
        for(char c : d)
        {
            result += findCode(c) + " ";
        }
    }
    ui->codedTextEdit->setText(QString::fromStdString(result));
}

std::string MainWindow::findCode(char text)
{
    std::string helper(1, text);
    for(auto pair : code)
    {
        if(pair.first == helper)
        {
            if(pair.second.size() == 0)
                return helper;
            return pair.second[rand()%pair.second.size()];
        }
    }
    return helper;
}

void MainWindow::on_decodePushButton_clicked()
{
    if(fileWasEdited) getKeyFromText();
    std::string result;
    std::string text = ui->codedTextEdit->toPlainText().toStdString();
    std::vector<std::string> data = split(text, ' ');
    for(std::string d : data)
    {
        result += findDecode(d) + " ";
    }
    ui->standardTextEdit->setText(QString::fromStdString(result));
}

std::string MainWindow::findDecode(std::string text)
{
    for(auto pair : decode)
    {
        if(pair.first == text)
            return pair.second;
    }
    return text;
}

std::vector<std::string> MainWindow::split(const std::string& s, char delimiter)
{
   std::vector<std::string> splits;
   std::string split;
   std::istringstream ss(s);
   while (std::getline(ss, split, delimiter))
   {
      splits.push_back(split);
   }
   return splits;
}
