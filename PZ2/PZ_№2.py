{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMfSDf0Lt6PR0gOwhdMrP5e",
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
        "<a href=\"https://colab.research.google.com/github/roman-docktom434/Chimbai_Python/blob/main/PZ2/PZ_%E2%84%962.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
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
        "m = input(\"Введите массу в килограммах: \")\n",
        "while type(m) != int:\n",
        "    try:\n",
        "        m = int(m)\n",
        "    except ValueError:\n",
        "        print(\"Ошибка! Введите число!\")\n",
        "        m = input(\"Введите массу в килограммах: \")\n",
        "tons = m // 1000\n",
        "print(\"Полных тонн: \", tons)"
      ]
    }
  ]
}