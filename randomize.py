{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d824d31d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import secrets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "182c1b6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.08559082070934565\n"
     ]
    }
   ],
   "source": [
    "print(random.random())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1d733f0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.713372053559655\n"
     ]
    }
   ],
   "source": [
    "print(random.uniform(1,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0394b0ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(random.randint(1,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "7817bee4",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print(secrets.randbelow(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "fe3c7590",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "print(secrets.randbits(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "b3a98eab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ram\n",
      "shyam\n",
      "sita\n"
     ]
    }
   ],
   "source": [
    "my_list = [\"ram\", \"shyam\", \"sita\"]\n",
    "for name in my_list:\n",
    "    print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ce3b9d4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sita', 'shyam', 'ram']\n"
     ]
    }
   ],
   "source": [
    "my_list.sort(reverse = True) # inplace\n",
    "print(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6c322e11",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ram', 'shyam', 'sita']\n"
     ]
    }
   ],
   "source": [
    "random.shuffle(my_list)\n",
    "print(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "37145598",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sita', 'shyam']\n",
      "['ram', 'shyam', 'sita']\n"
     ]
    }
   ],
   "source": [
    "print(random.sample(my_list,2))\n",
    "print(my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "496ead05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ram\n",
      "shyam\n"
     ]
    }
   ],
   "source": [
    "print(random.choice(my_list))\n",
    "print(secrets.choice(my_list))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "53dfae27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ram', 'shyam', 'hari', 'sita', 'ram']\n"
     ]
    }
   ],
   "source": [
    "names = [\"ram\", \"shyam\", \"hari\", \"sita\", \"ram\"]\n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "efdd5683",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['avengers', 'spiderman', 'starwars', 'jaari', 'spiderman', 'avengers']\n",
      "['kanchana', 'spiderman', 'starwars', 'jaari', 'spiderman', 'avengers']\n"
     ]
    }
   ],
   "source": [
    "movies = [\"avengers\", \"spiderman\", \"starwars\", \"jaari\", \"spiderman\", \"avengers\"]\n",
    "print(movies)\n",
    "movies[0] = \"kanchana\"\n",
    "print(movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4b19b59d",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies.append(\"Extraction\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "5345c71c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['kanchana', 'spiderman', 'starwars', 'jaari', 'spiderman', 'avengers', 'Extraction']\n"
     ]
    }
   ],
   "source": [
    "print(movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "6c24e524",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['kanchana', 'titanic', 'spiderman', 'starwars', 'jaari', 'spiderman', 'avengers', 'Extraction']\n"
     ]
    }
   ],
   "source": [
    "movies.insert(1, \"titanic\")\n",
    "print(movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "025ff8e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['avengers', 'thor', 'hulk', 'avengers', 'thor', 'hulk', 'avengers', 'thor', 'hulk']\n"
     ]
    }
   ],
   "source": [
    "my_list1 = [\"avengers\", \"thor\", \"hulk\"]\n",
    "my_list2 = [\"batman\", \"Titanic\", \"kanchana\"]\n",
    "print(my_list1*3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "0a6a65f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['avengers', 'thor', 'hulk', 'batman', 'Titanic', 'kanchana']\n"
     ]
    }
   ],
   "source": [
    "print(my_list1 + my_list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "54eb5fcc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# my_list1 = my_list2 # dont use this tp copy\n",
    "# my_list2.append(\"Veer\")\n",
    "# print(my_list1)\n",
    "# print(my_list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "fe167089",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['batman', 'Titanic', 'kanchana', 'Veer', 'Veer']\n",
      "['batman', 'Titanic', 'kanchana', 'Veer', 'Veer', 'Deathgame']\n"
     ]
    }
   ],
   "source": [
    "my_list1 = my_list2.copy()\n",
    "my_list2.append(\"Deathgame\")\n",
    "print(my_list1)\n",
    "print(my_list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "db6bc8b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['avengers', 'thor', 'hulk']\n",
      "['batman', 'Titanic', 'kanchana']\n"
     ]
    }
   ],
   "source": [
    "my_list1 = [\"avengers\", \"thor\", \"hulk\"]\n",
    "my_list2 = [\"batman\", \"Titanic\", \"kanchana\"]\n",
    "print(my_list1)\n",
    "print(my_list2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "d483bfe4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hulk', 'thor', 'avengers']\n"
     ]
    }
   ],
   "source": [
    "print(my_list1[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "1e5fe24b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(movies.count(\"spiderman\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "7090270f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[22, 44, 55, 66]\n"
     ]
    }
   ],
   "source": [
    "num = [22, 44, 55, 66]\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "2bcd2259",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22\n",
      "44\n"
     ]
    }
   ],
   "source": [
    "# indexed\n",
    "print(num[0])\n",
    "print(num[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "eed82e18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[55, 44]\n",
      "[22, 44, 55, 66]\n",
      "[66, 55, 44, 22]\n",
      "[22, 44, 55, 66]\n"
     ]
    }
   ],
   "source": [
    "# index slicing\n",
    "print(num[1:3])\n",
    "#sorting\n",
    "num.sort()\n",
    "print(num)\n",
    "# reverse\n",
    "num.sort(reverse = True)\n",
    "print(num)\n",
    "print(num[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "c072f87f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[66, 55, 44, 22, 777]\n"
     ]
    }
   ],
   "source": [
    "# adding at last\n",
    "num.append(777)\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "b2e61903",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[66, 7777, 55, 44, 22, 777]\n"
     ]
    }
   ],
   "source": [
    "# insert at any index\n",
    "num.insert(1, 7777)\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "bc1d2457",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[66, 7777, 55, 44, 22]\n"
     ]
    }
   ],
   "source": [
    "# remove\n",
    "num.remove(777)\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "c825ddf6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7777\n",
      "22\n"
     ]
    }
   ],
   "source": [
    "# max min in list\n",
    "print(max(num))\n",
    "print(min(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "eaf75aa1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7964\n"
     ]
    }
   ],
   "source": [
    "# sum of elements in list\n",
    "print(sum(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4843ca98",
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
