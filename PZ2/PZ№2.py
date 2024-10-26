{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMY/tDBKwrlsRzYRwOOQOU8"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "S0sbqvDrgO6p"
      },
      "outputs": [],
      "source": [
        "try:\n",
        " massa = int(input(\"Введите вашу массу в килограммах: \")) #Ввод килограммов от пользователя\n",
        " tona = massa // 1000\n",
        " print(\"У вас целых\", tona, \"тонн\") #Вывод результата\n",
        "except ValueError:\n",
        "  print(\"Вы ввели не точное целое число в килограммах\") #Исключение на неправильный ввод от пользователя"
      ]
    }
  ]
}