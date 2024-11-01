{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMjZjrrY9Xa5Avu1XcMK4my",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/roman-docktom434/Chimbai_Python/blob/main/PZ2/pz_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R7lYIzbqM3d4",
        "outputId": "66fb4904-8712-4c4a-8a19-118ee1e61725"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Введите массу в килограммах: f\n",
            "Ошибка! Введите число!\n",
            "Введите массу в килограммах: f\n",
            "Ошибка! Введите число!\n",
            "Введите массу в килограммах: f\n",
            "Ошибка! Введите число!\n",
            "Введите массу в килограммах: 43434\n",
            "Полных тонн:  43\n"
          ]
        }
      ],
      "source": [
        "m = input(\"Введите массу в килограммах: \") #получаем данные от пользователя\n",
        "while type(m) != int: #ЧИсловой цикл, для повторения программы\n",
        "    try: #Оьработка исключений\n",
        "        m = int(m)\n",
        "    except ValueError:\n",
        "        print(\"Ошибка! Введите число!\")\n",
        "        m = input(\"Введите массу в килограммах: \")\n",
        "tons = m // 1000 #Деление нацело\n",
        "print(\"Полных тонн: \", tons) #Вывод результата))"
      ]
    }
  ]
}