{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cbf6ba32",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter current tempearture: 24\n",
      "24.0\n"
     ]
    }
   ],
   "source": [
    "temperature = float(input(\"enter current tempearture: \"))\n",
    "print(temperature)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "34f67708",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "normal day\n"
     ]
    }
   ],
   "source": [
    "if temperature > 30:\n",
    "    print(\"its a very hot day\")\n",
    "elif temperature >= 25:\n",
    "    print(\"Its a bit hot day\")\n",
    "else:\n",
    "    print(\"normal day\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "d8775b24",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cafe():\n",
    "    print(\"tea is ready\")\n",
    "    print(\"enjoy\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "da734b4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tea is ready\n",
      "enjoy\n"
     ]
    }
   ],
   "source": [
    "cafe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb8a7e25",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
