#include <QCoreApplication>
#include <QFile>
#include <QDebug>

#include "lexicalanalyzer.h"
#include "syntacticalanalyzer.h"

const QString PATH_TO_FILE = ":/input/resourses/test_1.txt";

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    LexicalAnalyzer lexicalAnalyzer;
    lexicalAnalyzer.setPath(PATH_TO_FILE);

    QVector<Lexem> lexemBox = lexicalAnalyzer.run();
    qDebug() << lexemBox;

    SyntacticalAnalyzer syntacticalAnalyzer;
    syntacticalAnalyzer.setLexemBox(lexemBox);

//    qDebug() << "0";
//    QVector<Lexem>::iterator iter = 0;
//    qDebug() << *(lexemBox.begin());

    QVectorIterator<Lexem> iterator(lexemBox);
    iterator.toFront();
    syntacticalAnalyzer.declarationOfVariables(iterator);
//    qDebug() << "2";

    return a.exec();
}

/*
    TODO: перегрузить оператор << для класса Lexem
          проверить код. Указать на setters
          можно ли переименовать проект?
          добавить return в лексический анализатор
          переопределить readFileToString с void на bool (проверка на открытие файла)
          добавить enum.
          добавить enum в Lexem, проверять в синтаксисе по типу
*/