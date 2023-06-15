{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2e4952b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1ed90699",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5, 6])\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ee12430e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]]\n",
      "(2, 3)\n"
     ]
    }
   ],
   "source": [
    "b = np.array([[1, 2, 3],[4, 5, 6]])\n",
    "print(b)\n",
    "print(b.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d84d3f45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(b.size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a5c8dcb9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "print(b.nbytes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "15a3f7c4",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n",
      "(3, 3)\n"
     ]
    }
   ],
   "source": [
    "x = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])\n",
    "print(x)\n",
    "print(x.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "746b0fac",
   "metadata": {},
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
    "print(x.size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "79341e90",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(x[1][2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "553caa04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "45\n"
     ]
    }
   ],
   "source": [
    "print(x.sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7e2cfda3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12 15 18]\n"
     ]
    }
   ],
   "source": [
    "print(x.sum(axis= 0)) # column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9db4af7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 6 15 24]\n"
     ]
    }
   ],
   "source": [
    "print(x.sum(axis=1)) # row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ec9074fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([[1,2,3],[4,5,6],[7,8,9]])\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7e4505e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n"
     ]
    }
   ],
   "source": [
    "print(a[0,:]) # accessing particular row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "cb8a2a22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4 5 6]\n"
     ]
    }
   ],
   "source": [
    "print(a[1,:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bb80acb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4 5]\n"
     ]
    }
   ],
   "source": [
    "print(a[1,:2]) # accessing row by slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "1af6d926",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 6 9]\n"
     ]
    }
   ],
   "source": [
    "print(a[:,2]) # accessing particular column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2f774b35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]\n"
     ]
    }
   ],
   "source": [
    "x = np.arange(15) # provies array in range of input\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "70dc4403",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 0.]\n",
      "[1. 1. 1. 1. 1.]\n"
     ]
    }
   ],
   "source": [
    "x=np.zeros(5) # inserts zero in all indexes\n",
    "print(x)\n",
    "x=np.ones(5) # inserts one in all indexes\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "ae8cdf2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[9 9 9]\n",
      " [9 9 9]]\n"
     ]
    }
   ],
   "source": [
    "x = np.full([2,3],9) # inserting elements in matrix of particular dimension\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "c259efa4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 0. 0. 0.]\n",
      " [0. 1. 0. 0. 0.]\n",
      " [0. 0. 1. 0. 0.]\n",
      " [0. 0. 0. 1. 0.]\n",
      " [0. 0. 0. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "x = np.identity(5)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "643e0e66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6 7 8 9]\n",
      "[10 11 12 13 14 15 16 17 18]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5, 6,7,8,9])\n",
    "b = np.array([10,11,12,13,14,15,16,17,18])\n",
    "print(a)\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "224e15e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 3 4 5 6 7]\n"
     ]
    }
   ],
   "source": [
    "print(a[1:7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "cf9df710",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[9 8 7 6 5 4 3 2 1]\n"
     ]
    }
   ],
   "source": [
    "print(a[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "74ac1573",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "edfebe66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18]\n"
     ]
    }
   ],
   "source": [
    "c = np.hstack([a,b]) # horizontal stacking\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "f63ce340",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4  5  6  7  8  9]\n",
      " [10 11 12 13 14 15 16 17 18]]\n"
     ]
    }
   ],
   "source": [
    "c = np.vstack([a,b]) # vertical stacking\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "2fd3842e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1.  2.  3.  4.  5.]\n",
      " [ 6.  7.  8.  9. 10.]\n",
      " [11. 12. 13. 14. 15.]]\n"
     ]
    }
   ],
   "source": [
    "# importing from text file\n",
    "a = np.genfromtxt('data.txt',delimiter=',')\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26fc77ff",
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
