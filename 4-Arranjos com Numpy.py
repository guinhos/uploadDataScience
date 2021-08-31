{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Manipulação de arranjos com Numpy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1- Arranjos no Numpy."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Ao contrário das listas do Python, quando criamos um array no [Numpy](https://medium.com/ensina-ai/entendendo-a-biblioteca-numpy-4858fde63355), existe uma restrição de que todos os elementos devem ser do mesmo tipo. Isto faz com que os arrajosn do numpy sejam mais eficientes."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Vamos começar importando o pacote numpy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#! pip install numpy\n",
    "#! pip install packageName\n",
    "#from package import package.module"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Construír uma Lista, e checar que se trata de arranjos de inteiros instanciado a partir da lista."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "#help(np.array)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int32')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l = [1, 4, 2, 5, 3]\n",
    "#type(l)\n",
    "np.array(l).dtype"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Instanciar um arranjo a partir de uma lista literal de inteiros. O atributo [`.dtype`](https://numpy.org/doc/stable/reference/arranjos.dtypes.html) informa o tipo do elemento contido no arranjo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 4 2 5 3]\n",
      "int32\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 4, 2, 5, 3])\n",
    "print(a)\n",
    "print(a.dtype)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Se a lista do python contiver `integers` e `floats`, o arranjo do Numpy transforma tudo em `float` para uniformização dos tipo. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "float64\n",
      "[3.14 4.   2.   3.  ]\n"
     ]
    }
   ],
   "source": [
    "py_list = [3.14, 4, 2, 3]\n",
    "b = np.array(py_list)\n",
    "print(b.dtype)\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Checar o tipo dos dados."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array(py_list).dtype\n",
    "#print(py_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Tornar uma lista em um arranjo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3.14, 4.  , 2.  , 3.  ])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "py_list\n",
    "np.array(py_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Para criar arranjos específicos, o mais eficiente é fazer isso com os métodos próprios do Numpy. \n",
    "\n",
    "#### É possível criar arranjos de zeros, de uns, de uma seqüência, de valores aleatórios ou de valores com uma certa distribuição estatística, como por exemplo, a distribuição normal.\n",
    "\n",
    "#### Criar um arranjo de zeros:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Criar um array de longitude 10 cheio de zeros\n",
    "np.zeros(10, \n",
    "         dtype = int\n",
    "        )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Inicializar um arranjo vazio [`empty`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html#numpy-empty), que aloca um espaço na memória mas não a inicializa."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0.00e+000 0.00e+000]\n",
      "  [0.00e+000 0.00e+000]]\n",
      "\n",
      " [[0.00e+000 7.33e-321]\n",
      "  [0.00e+000 0.00e+000]]]\n"
     ]
    }
   ],
   "source": [
    "#my_array = np.empty([2, 2, 2])\n",
    "#my_array\n",
    "\n",
    "print(np.empty([2, 2, 2]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Criar um Array que contenha números com [distribuição normal](https://www.mathsisfun.com/data/standard-normal-distribution.html) com o método [`.normal()`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html?highlight=random%20normal#numpy.random.normal). \n",
    "\n",
    "#### Pode-se inicializar um array de números com distribuição normal, em que o primeiro parâmetro é a média da  distribuição, o segundo parâmetro é o desvio padrão e o terceiro parâmetro é o número de observações."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "norm = np.random.normal(loc = 0, \n",
    "                        scale = 1, \n",
    "                        size = 12\n",
    "                       )\n",
    "\n",
    "#norm = np.random.normal(0, 1, 12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.74741568, -0.59524886,  1.53602654,  1.23651991, -0.51189214,\n",
       "        0.05087955,  0.73503409,  0.26839512, -0.7397557 , -0.22791584,\n",
       "        0.48376428,  0.99846741])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "norm"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Também pode-se criar uma distribuição normal aleatória [`.random.normal()`](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html) e atribuí-la a uma matriz de dimensão $n \\times m$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.40834055,  0.19640901,  0.11499455,  0.26067449],\n",
       "       [-0.45788889,  1.69350424,  0.81673427,  0.78520041],\n",
       "       [ 0.10687852, -0.70526845,  0.18380587, -0.93294592]])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "norm = np.random.normal(loc = 0, \n",
    "                        scale = 1, \n",
    "                        size = (3, 4)\n",
    "                       )\n",
    "norm"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Opcionalmente, pode-se usar o método [`.random.seed()`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html?highlight=random%20seed#numpy.random.seed) para que as escolhas aleatórias sejam reproduzíveis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.76405235,  0.40015721,  0.97873798,  2.2408932 ],\n",
       "       [ 1.86755799, -0.97727788,  0.95008842, -0.15135721],\n",
       "       [-0.10321885,  0.4105985 ,  0.14404357,  1.45427351]])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.seed(0) \n",
    "norm = np.random.normal(loc = 0, \n",
    "                        scale = 1, \n",
    "                        size = (3,4)\n",
    "                       )\n",
    "norm"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2 - Atributos de um arranjo."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Um arranjo de $3$ dimensões com valores aleatórios entre $0$ e $9$ [`.random.randint()`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html?highlight=random%20randint#numpy-random-randint)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[10 11 11 11 11]\n",
      "  [10 11 10 10 11]\n",
      "  [12 10 12 10 11]\n",
      "  [11 12 10 11 11]]\n",
      "\n",
      " [[11 10 12 10 12]\n",
      "  [12 10 12 10 10]\n",
      "  [10 11 11 12 10]\n",
      "  [10 11 10 11 12]]\n",
      "\n",
      " [[12 10 11 11 11]\n",
      "  [11 12 12 12 10]\n",
      "  [12 11 10 11 12]\n",
      "  [10 10 12 10 10]]]\n"
     ]
    }
   ],
   "source": [
    "x3 = np.random.randint(low = 10, \n",
    "                       high = 13, \n",
    "                       size = (3, 4, 5)\n",
    "                      )  \n",
    "\n",
    "#x3 = np.random.randint(low = 10, size = (3, 4, 5))  \n",
    "\n",
    "print (x3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Imprimir o número de dimensões, a forma, o número de elementos, os tipos de elementos, o tamanho de cada elemento e o tamanho total do arranjo. Há uma coleção de [atributos Numpy](https://cloudxlab.com/assessment/displayslide/2503/numpy-arrays-attributes-of-a-numpy-array)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#x3.\"Tab Here\"\n",
    "#np.random.randint(\"Shift Tab Here\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x3 ndim:  3\n",
      "x3 shape: (3, 4, 5)\n",
      "x3 size:  60\n",
      "dtype: int32\n",
      "itemsize: 4 bytes\n",
      "nbytes: 240 bytes\n"
     ]
    }
   ],
   "source": [
    "# O número de dimensões do arranjo\n",
    "print(\"x3 ndim: \", x3.ndim)\n",
    "\n",
    "# A forma do arranjo\n",
    "print(\"x3 shape:\", x3.shape)\n",
    "\n",
    "# O número de elementos do arranjo\n",
    "print(\"x3 size: \", x3.size)\n",
    "\n",
    "# Os tipos dos elementos do arranjo\n",
    "print(\"dtype:\", x3.dtype)\n",
    "\n",
    "# O tamanho de cada elemento do array. Depende do tipo de dados.  \n",
    "print(\"itemsize:\", x3.itemsize, \"bytes\") \n",
    "\n",
    "# O tamanho de todo o array. É calculado desta forma: itemsize * size\n",
    "print(\"nbytes:\", x3.nbytes, \"bytes\") "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3- Seleção de elementos de um Arranjo.\n",
    "\n",
    "#### É um problema comum querer selecionar os elementos de um arranjo de acordo com algum critério. O Numpy nos oferece três formas de [acessar](https://numpy.org/devdocs/reference/arrays.indexing.html#indexing) <b> de forma eficiente </b> os elementos de um arranjo:\n",
    "* [Array Slicing](https://numpy.org/doc/stable/reference/arrays.indexing.html)\n",
    "* [Fancy Indexing](https://jakevdp.github.io/PythonDataScienceHandbook/02.07-fancy-indexing.html)\n",
    "* [Boolean Indexing](https://numpy.org/devdocs/reference/arrays.indexing.html#boolean-array-indexing)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3 -1 Array Slicing.\n",
    "\n",
    "#### [Slicing](https://medium.com/python-features/slicing-tricks-lists-str-bytes-6db10066bd23) sobre uma dimensão:  \n",
    "\n",
    "#### O [slicing](https://medium.com/@buch.willi/numpys-indexing-and-slicing-notation-explained-visually-67dc981c22c1) é similar ao das listas do python `[ start : stop : step ]`. \n",
    "\n",
    "#### O índice `stop` não é incluído, mas o `start` é incluído.  Por exemplo, `[1:3]` inclui o índice $1$ mas não o $3$. Funciona como um intervalo semifechado `[a, b)`.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Criamos um arranjo de uma dimensão, usando a função [`np.arange()`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one_d_array = np.arange(10)\n",
    "one_d_array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Start = 1: Começamos pelo segundo elemento\n",
    "- Stop: Não está definido, então chegamos até o final.\n",
    "- Step: 2 passo ou distância entre os elementos que será assumida."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 3, 5, 7, 9])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one_d_array[1::2]  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Para inverter a ordem do arranjo, pode  usar `Step = -1`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one_d_array[::-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Se quisermos fazer `slicing` em [ordem invertida](https://www.askpython.com/python/array/reverse-an-array-in-python)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([7, 6, 5])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "one_d_array[7:4:-1]  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### `Slicing` sobre arranjos de [mais dimensões](https://www.pythoninformer.com/python-libraries/numpy/index-and-slice/):"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Com a mesma lógica, é possível selecionar em duas dimensões."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[5, 0, 3, 3, 7, 9, 3, 5],\n",
       "       [2, 4, 7, 6, 8, 8, 1, 6],\n",
       "       [7, 7, 8, 1, 5, 9, 8, 9],\n",
       "       [4, 3, 0, 3, 5, 0, 2, 3],\n",
       "       [8, 1, 3, 3, 3, 7, 0, 1],\n",
       "       [9, 9, 0, 4, 7, 3, 2, 7],\n",
       "       [2, 0, 0, 4, 5, 5, 6, 8],\n",
       "       [4, 1, 4, 9, 8, 1, 1, 7]])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.seed(0)\n",
    "two_d_array = np.random.randint(10, \n",
    "                                size = (8, 8)\n",
    "                               )\n",
    "two_d_array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Quando temos mais de uma dimensão, podemos fazer slicing em cada uma delas separando-as com uma [vírgula](https://numpy.org/devdocs/user/quickstart.html#indexing-slicing-and-iterating). \n",
    "\n",
    "#### Acessar uma coluna: Aqui os dois pontos `:` indicam que acessamos todos os elementos de cada linha e o zero depois da vírgula indica que fazemos isso somente na coluna $0$ (a primeira)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([5, 3, 7])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#two_d_array[i, j]\n",
    "#two_d_array[0:5:2, 0]\n",
    "two_d_array[0, 0:5:2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Para acessar uma linha usamos o mesmo raciocínio."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7 7 8 1 5 9 8 9]\n",
      "[7 8 1 5 9 8 9]\n"
     ]
    }
   ],
   "source": [
    "print(two_d_array[2, :])\n",
    "print(two_d_array[2, 1:])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Outra forma de acessar uma linha."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([7, 7, 8, 1, 5, 9, 8, 9])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "two_d_array[2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Um slice de duas colunas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5 0 3 3 7 9 3 5]\n",
      " [2 4 7 6 8 8 1 6]\n",
      " [7 7 8 1 5 9 8 9]\n",
      " [4 3 0 3 5 0 2 3]\n",
      " [8 1 3 3 3 7 0 1]\n",
      " [9 9 0 4 7 3 2 7]\n",
      " [2 0 0 4 5 5 6 8]\n",
      " [4 1 4 9 8 1 1 7]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[4, 7, 6, 8, 8, 1],\n",
       "       [7, 8, 1, 5, 9, 8],\n",
       "       [3, 0, 3, 5, 0, 2]])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(two_d_array)\n",
    "two_d_array[1:4, 1:7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 3],\n",
       "       [4, 7],\n",
       "       [7, 8],\n",
       "       [3, 0],\n",
       "       [1, 3],\n",
       "       [9, 0],\n",
       "       [0, 0],\n",
       "       [1, 4]])"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "two_d_array[:, 1:3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Para acessar um elemento específico."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[4, 6],\n",
       "       [3, 3],\n",
       "       [9, 4]])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#two_d_array[1:2, 1:2]\n",
    "two_d_array[1:6:2, 1:4:2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Todas as colunas listadas em ordem inversa."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[5, 0, 3, 3, 7, 9, 3, 5],\n",
       "       [2, 4, 7, 6, 8, 8, 1, 6],\n",
       "       [7, 7, 8, 1, 5, 9, 8, 9],\n",
       "       [4, 3, 0, 3, 5, 0, 2, 3],\n",
       "       [8, 1, 3, 3, 3, 7, 0, 1],\n",
       "       [9, 9, 0, 4, 7, 3, 2, 7],\n",
       "       [2, 0, 0, 4, 5, 5, 6, 8],\n",
       "       [4, 1, 4, 9, 8, 1, 1, 7]])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "two_d_array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[7, 1, 1, 8, 9, 4, 1, 4],\n",
       "       [8, 6, 5, 5, 4, 0, 0, 2],\n",
       "       [7, 2, 3, 7, 4, 0, 9, 9],\n",
       "       [1, 0, 7, 3, 3, 3, 1, 8],\n",
       "       [3, 2, 0, 5, 3, 0, 3, 4],\n",
       "       [9, 8, 9, 5, 1, 8, 7, 7],\n",
       "       [6, 1, 8, 8, 6, 7, 4, 2],\n",
       "       [5, 3, 9, 7, 3, 3, 0, 5]])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#two_d_array[:, ::-1]\n",
    "two_d_array[::-1, ::-1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 3 - 2 Fancy Indexing.\n",
    "\n",
    "#### Esta [técnica](https://scipy-lectures.org/intro/numpy/array_object.html) consiste em gerar listas que contenham os índices dos elementos que queremos selecionar e utilizá-las para realizar a  indexação."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Instanciamos um [gerador](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState) de números pseudo-aleatórios, usando o método [`.RandomState`](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.RandomState.html).\n",
    "\n",
    "\n",
    "[Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "RandomState(MT19937)\n"
     ]
    }
   ],
   "source": [
    "rand = np.random.RandomState(42)\n",
    "print(rand)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Pedimos $10$ inteiros entre $0$ e $99$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[51 92 14 71 60 20 82 86 74 74]\n"
     ]
    }
   ],
   "source": [
    "x = rand.randint(100, \n",
    "                 size = 10\n",
    "                )\n",
    "#type(x)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Podemos alterar a forma do arranjo, dependendo da quantidade de elementos e da forma desejada."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[87, 99, 23,  2, 21],\n",
       "       [52,  1, 87, 29, 37]])"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = rand.randint(100, \n",
    "                 size = 10\n",
    "                )\n",
    "#y = rand.randint(100, size = 12)\n",
    "y = y.reshape((2, 5))\n",
    "#y = y.reshape((3, 4))\n",
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Pode-se acessar um conjunto de elementos criando uma lista com os índices a se acessar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([71, 86, 60])"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ind = [3, 7, 4]\n",
    "#type(ind)\n",
    "x[ind]\n",
    "#x[[3, 7, 4]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Também é possível optar por uma seleção por linha e coluna. Criamos um arranjo de $(3 \\times 4)$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3],\n",
       "       [ 4,  5,  6,  7],\n",
       "       [ 8,  9, 10, 11]])"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = np.arange(12).reshape((3, 4))\n",
    "#X = X.reshape((3, 4))\n",
    "#X = np.arange(12).reshape((4, 3))\n",
    "X"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Um arranjo de índices para acessar linhas determinadas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0,  1,  2,  3],\n",
       "       [ 8,  9, 10, 11]])"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mask = np.array([0, 2])\n",
    "#mask\n",
    "X[mask, :]\n",
    "#X[:, mask]\n",
    "#X[[0, 2], : ]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Acessamos posições específicas do arranjo, os índices estão dados pelos arranjos `row` e `col`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0  1  2  3]\n",
      " [ 4  5  6  7]\n",
      " [ 8  9 10 11]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([ 2, 11])"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(X)\n",
    "row = np.array([0, 2])\n",
    "col = np.array([2, 3])\n",
    "X[row, col]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Como exemplo de aplicação de `Fancy Indexing` vamos selecionar pontos aleatórios, usando parâmetros da [distribuição normal multivariada](https://support.minitab.com/pt-br/minitab/18/help-and-how-to/probability-distributions-and-random-data/supporting-topics/distributions/multivariate-normal-distribution/)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "rand = np.random.RandomState(42)\n",
    "\n",
    "mean = [0, 0]\n",
    "\n",
    "cov = [[1, 2],\n",
    "       [2, 5]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Pegamos 100 pontos (são amostras de duas dimensões) [`.multivariate_normal()`](https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.random.multivariate_normal.html#numpy-random-multivariate-normal)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-4.05992582e-01, -1.12980900e+00],\n",
       "       [-1.18122448e+00, -1.20321251e+00],\n",
       "       [ 3.05929845e-01,  4.85151964e-01],\n",
       "       [-1.75268695e+00, -3.40069525e+00],\n",
       "       [ 2.26109036e-01,  1.13313826e+00],\n",
       "       [ 6.06369182e-01,  9.59802450e-01],\n",
       "       [ 5.08636661e-01, -8.42962089e-01],\n",
       "       [ 1.80879440e+00,  3.75820034e+00],\n",
       "       [ 8.15476694e-01,  2.30887376e+00],\n",
       "       [ 1.37937009e+00,  1.80142746e+00],\n",
       "       [-1.26768205e+00, -3.30483370e+00],\n",
       "       [ 4.82839600e-01, -3.76458413e-01],\n",
       "       [ 4.60495820e-01,  1.23179700e+00],\n",
       "       [ 9.19606001e-01,  2.62677788e+00],\n",
       "       [ 6.66544157e-01,  1.29345291e+00],\n",
       "       [-1.52931750e-01,  1.63568156e+00],\n",
       "       [ 4.17238258e-01, -1.37555797e-01],\n",
       "       [-2.92735771e-01, -2.02815831e+00],\n",
       "       [ 5.56968489e-01, -7.76490778e-01],\n",
       "       [ 1.15174837e+00,  2.99364761e+00],\n",
       "       [-7.47833961e-01, -1.61994320e+00],\n",
       "       [ 2.22072477e-01,  2.10218094e-01],\n",
       "       [ 1.64144866e+00,  3.18365385e+00],\n",
       "       [ 2.10315704e-02,  1.19499555e+00],\n",
       "       [ 3.57224353e-01, -1.04588503e+00],\n",
       "       [-1.52049937e-01, -7.83891078e-01],\n",
       "       [ 3.91315999e-01,  1.60679404e+00],\n",
       "       [-1.30890483e+00, -2.15196545e+00],\n",
       "       [ 8.93666346e-01,  1.82281235e+00],\n",
       "       [-6.79372462e-01, -5.84227775e-01],\n",
       "       [ 5.13747885e-01,  1.03934128e+00],\n",
       "       [ 1.47988870e+00,  2.27800264e+00],\n",
       "       [-1.26968657e+00, -1.59731090e+00],\n",
       "       [-3.17506736e-01,  3.19687112e-01],\n",
       "       [-8.72314798e-02, -9.08868012e-01],\n",
       "       [-9.22467115e-01, -5.62273838e-01],\n",
       "       [-5.65664260e-01,  3.27923760e-01],\n",
       "       [ 2.10580041e+00,  5.97347277e+00],\n",
       "       [ 3.40041545e-02, -2.41549933e-01],\n",
       "       [ 6.75833791e-01, -5.19721987e-01],\n",
       "       [ 6.62892964e-02,  5.46572381e-01],\n",
       "       [-1.16706263e+00, -3.37851008e+00],\n",
       "       [ 9.38964800e-01,  1.72376364e+00],\n",
       "       [-9.71528884e-01, -1.98964057e+00],\n",
       "       [ 2.93015666e-01,  1.26295906e+00],\n",
       "       [-4.60372351e-01, -6.29833900e-02],\n",
       "       [ 7.74003359e-01,  1.51395046e+00],\n",
       "       [ 9.22323621e-01,  6.42589030e-01],\n",
       "       [-3.73480991e-01, -6.19098683e-01],\n",
       "       [ 8.50483915e-02, -4.85903033e-02],\n",
       "       [ 1.46860606e+00,  3.09022544e+00],\n",
       "       [ 6.23645146e-01,  6.37233912e-01],\n",
       "       [-5.61500084e-03,  4.23785685e-01],\n",
       "       [-1.80941659e+00, -4.17935640e+00],\n",
       "       [-2.09456316e-01, -5.86251957e-01],\n",
       "       [ 1.78285987e+00,  4.27550608e+00],\n",
       "       [-9.98287405e-01,  2.56115059e-01],\n",
       "       [ 6.23211862e-02,  4.76849144e-01],\n",
       "       [ 4.79303216e-01, -1.07827667e-01],\n",
       "       [-1.34358292e+00, -2.42980966e+00],\n",
       "       [-3.82810713e-01, -1.90850070e+00],\n",
       "       [-7.59547776e-01, -3.35106320e+00],\n",
       "       [-1.38043633e+00, -9.61736037e-01],\n",
       "       [ 1.13184900e+00,  2.11956895e+00],\n",
       "       [ 1.00605935e-01, -3.02073909e-01],\n",
       "       [ 1.40638829e+00,  3.46953372e+00],\n",
       "       [ 8.00204682e-01,  2.44447775e+00],\n",
       "       [ 2.56303014e-01,  2.29640712e+00],\n",
       "       [ 8.46879292e-01,  1.69595060e+00],\n",
       "       [-2.80560525e-01, -2.00961096e+00],\n",
       "       [-7.10367454e-01, -3.00137619e-01],\n",
       "       [ 1.41446454e+00,  3.61466573e+00],\n",
       "       [-5.39291055e-01, -4.55724799e-01],\n",
       "       [ 1.64811031e+00,  2.54963833e+00],\n",
       "       [-5.95862244e-01, -1.11708482e+00],\n",
       "       [-3.64005207e-01, -5.03793469e-01],\n",
       "       [ 5.39381280e-01,  1.55357119e+00],\n",
       "       [ 2.60679294e-03, -7.66915048e-01],\n",
       "       [-1.90507889e+00, -4.08639424e+00],\n",
       "       [ 8.49368730e-01,  2.76120601e+00],\n",
       "       [ 5.99284208e-01,  2.29873430e+00],\n",
       "       [-7.56341215e-01, -2.71426936e+00],\n",
       "       [-1.04800791e+00, -2.08332405e+00],\n",
       "       [-1.48535581e+00, -1.53289220e+00],\n",
       "       [ 5.15151400e-01,  4.27847352e-01],\n",
       "       [ 1.13400126e+00,  1.85469452e+00],\n",
       "       [-5.93205174e-02,  2.26047839e-01],\n",
       "       [-5.72178291e-01, -4.86023894e-01],\n",
       "       [-5.68255591e-01,  2.01403592e-01],\n",
       "       [-7.96452642e-01,  1.02148312e+00],\n",
       "       [-2.50021261e-01, -1.53138537e+00],\n",
       "       [ 8.04741461e-01,  2.46504213e+00],\n",
       "       [-6.67834661e-02,  6.11599016e-01],\n",
       "       [-4.09344137e-01, -1.06707361e+00],\n",
       "       [ 1.36204232e+00,  1.64860222e+00],\n",
       "       [ 8.47963951e-02,  1.13167598e+00],\n",
       "       [ 2.78926763e-01, -6.74989163e-01],\n",
       "       [-3.07452890e-01, -3.25192411e-01],\n",
       "       [ 7.57749744e-01,  1.99576056e+00],\n",
       "       [ 3.83617953e-01, -3.11006470e-01]])"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = rand.multivariate_normal(mean, \n",
    "                             cov, \n",
    "                             100\n",
    "                            )\n",
    "X\n",
    "#X.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Fazendo um `slice` de todas as linhas da coluna $0$ ou $1$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "#X[:, 0]\n",
    "#X[:, 1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Pode plotar os valores considerados acima com a ajuda da função [`plt.scatter()`](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib-pyplot-scatter)), do pacote [`MatPlotLib`](https://matplotlib.org/). Importamos a biblioteca [`seaborn`](https://seaborn.pydata.org/), para a visualização dos dados.\n",
    "\n",
    "#### Observe a seguir o comando mágico [%matplotlib inline](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html), que gera as imagens estáticas de seu plot, embutidas no caderno::"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn; seaborn.set()  \n",
    "\n",
    "plt.scatter(X[:, 0], \n",
    "            X[:, 1]\n",
    "           );"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Selecionando-se 20 dos 100 (X.shape[0] = 100) sem reposição [`.random.choice`](https://docs.scipy.org/doc/numpy-1.16.0/reference/generated/numpy.random.choice.html#numpy-random-choice), que gera uma amostra aleatória de uma determinada matriz `1D`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([26, 90, 67,  5, 24,  7, 44,  4, 56, 55, 89, 86, 77, 54, 38, 40, 33,\n",
       "       28, 71, 32])"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "indices = np.random.choice(X.shape[0], \n",
    "                           size = 20, \n",
    "                           replace = False\n",
    "                          )\n",
    "indices\n",
    "#print(X.shape[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Temos agora um arranjos de índices, que podemos usar para uma seleção de pontos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(20, 2)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "selection = X[indices] # fancy indexing!!\n",
    "#print(selection)\n",
    "selection.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### E essa seleção de pontos pode ser replotada."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(X[:, 0], \n",
    "            X[:, 1], \n",
    "            facecolor = 'blue'\n",
    "           )\n",
    "\n",
    "plt.scatter(selection[:, 0], \n",
    "            selection[:, 1], \n",
    "            facecolor = 'red'\n",
    "           );"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3 - 3 Boolean Indexing."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Essa [técnica](https://www.tutorialspoint.com/boolean-indexing-in-python) é baseada na criação da chamada [\"máscara booleana\"](https://www.python-course.eu/numpy_masking.php), que é uma lista de valores `True` e `False` usados para selecionar apenas elementos cujo índice corresponde a um valor `True`.  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![BooleanIndexing1.png](BooleanIndexing1.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![BooleanIndexing2.png](BooleanIndexing2.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Exemplo de aplicação boolean indexing: contar dias de chuva. Temos um dataset que representa a quantidade de precipitações de na cidade de Seattle (EUA), no ano de $2014$.\n",
    "\n",
    "#### Usamos [`Pandas`](https://realpython.com/pandas-python-explore-dataset/) para extrair os dados como um arranjo de [`Numpy`](https://realpython.com/python-data-cleaning-numpy-pandas/). O método [`.read_csv()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) lê um arquivo de valores separados por vírgula ([csv](https://docs.python.org/3/library/csv.html)) em um [`DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>STATION</th>\n",
       "      <th>STATION_NAME</th>\n",
       "      <th>DATE</th>\n",
       "      <th>PRCP</th>\n",
       "      <th>SNWD</th>\n",
       "      <th>SNOW</th>\n",
       "      <th>TMAX</th>\n",
       "      <th>TMIN</th>\n",
       "      <th>AWND</th>\n",
       "      <th>WDF2</th>\n",
       "      <th>WDF5</th>\n",
       "      <th>WSF2</th>\n",
       "      <th>WSF5</th>\n",
       "      <th>WT01</th>\n",
       "      <th>WT05</th>\n",
       "      <th>WT02</th>\n",
       "      <th>WT03</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20140101</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>72</td>\n",
       "      <td>33</td>\n",
       "      <td>12</td>\n",
       "      <td>340</td>\n",
       "      <td>310</td>\n",
       "      <td>36</td>\n",
       "      <td>40.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20140102</td>\n",
       "      <td>41</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>106</td>\n",
       "      <td>61</td>\n",
       "      <td>32</td>\n",
       "      <td>190</td>\n",
       "      <td>200</td>\n",
       "      <td>94</td>\n",
       "      <td>116.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20140103</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>89</td>\n",
       "      <td>28</td>\n",
       "      <td>26</td>\n",
       "      <td>30</td>\n",
       "      <td>50</td>\n",
       "      <td>63</td>\n",
       "      <td>72.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20140104</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>78</td>\n",
       "      <td>6</td>\n",
       "      <td>27</td>\n",
       "      <td>40</td>\n",
       "      <td>40</td>\n",
       "      <td>45</td>\n",
       "      <td>58.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20140105</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>83</td>\n",
       "      <td>-5</td>\n",
       "      <td>37</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>67</td>\n",
       "      <td>76.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>360</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20141227</td>\n",
       "      <td>33</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>94</td>\n",
       "      <td>44</td>\n",
       "      <td>49</td>\n",
       "      <td>210</td>\n",
       "      <td>210</td>\n",
       "      <td>112</td>\n",
       "      <td>161.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>361</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20141228</td>\n",
       "      <td>41</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>67</td>\n",
       "      <td>28</td>\n",
       "      <td>18</td>\n",
       "      <td>50</td>\n",
       "      <td>30</td>\n",
       "      <td>58</td>\n",
       "      <td>72.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>362</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20141229</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>61</td>\n",
       "      <td>6</td>\n",
       "      <td>43</td>\n",
       "      <td>350</td>\n",
       "      <td>350</td>\n",
       "      <td>76</td>\n",
       "      <td>103.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>363</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20141230</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>33</td>\n",
       "      <td>-21</td>\n",
       "      <td>36</td>\n",
       "      <td>90</td>\n",
       "      <td>70</td>\n",
       "      <td>63</td>\n",
       "      <td>76.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>-9999.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>364</th>\n",
       "      <td>GHCND:USW00024233</td>\n",
       "      <td>SEATTLE TACOMA INTERNATIONAL AIRPORT WA US</td>\n",
       "      <td>20141231</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>33</td>\n",
       "      <td>-27</td>\n",
       "      <td>30</td>\n",
       "      <td>30</td>\n",
       "      <td>-9999</td>\n",
       "      <td>58</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>365 rows × 17 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               STATION                                STATION_NAME      DATE  \\\n",
       "0    GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140101   \n",
       "1    GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140102   \n",
       "2    GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140103   \n",
       "3    GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140104   \n",
       "4    GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20140105   \n",
       "..                 ...                                         ...       ...   \n",
       "360  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20141227   \n",
       "361  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20141228   \n",
       "362  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20141229   \n",
       "363  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20141230   \n",
       "364  GHCND:USW00024233  SEATTLE TACOMA INTERNATIONAL AIRPORT WA US  20141231   \n",
       "\n",
       "     PRCP  SNWD  SNOW  TMAX  TMIN  AWND  WDF2  WDF5  WSF2   WSF5    WT01  \\\n",
       "0       0     0     0    72    33    12   340   310    36   40.0 -9999.0   \n",
       "1      41     0     0   106    61    32   190   200    94  116.0 -9999.0   \n",
       "2      15     0     0    89    28    26    30    50    63   72.0     1.0   \n",
       "3       0     0     0    78     6    27    40    40    45   58.0     1.0   \n",
       "4       0     0     0    83    -5    37    10    10    67   76.0 -9999.0   \n",
       "..    ...   ...   ...   ...   ...   ...   ...   ...   ...    ...     ...   \n",
       "360    33     0     0    94    44    49   210   210   112  161.0     1.0   \n",
       "361    41     0     0    67    28    18    50    30    58   72.0     1.0   \n",
       "362     0     0     0    61     6    43   350   350    76  103.0     1.0   \n",
       "363     0     0     0    33   -21    36    90    70    63   76.0 -9999.0   \n",
       "364     0     0     0    33   -27    30    30 -9999    58    NaN     NaN   \n",
       "\n",
       "       WT05    WT02    WT03  \n",
       "0   -9999.0 -9999.0 -9999.0  \n",
       "1   -9999.0 -9999.0 -9999.0  \n",
       "2   -9999.0 -9999.0 -9999.0  \n",
       "3   -9999.0 -9999.0 -9999.0  \n",
       "4   -9999.0 -9999.0 -9999.0  \n",
       "..      ...     ...     ...  \n",
       "360 -9999.0 -9999.0 -9999.0  \n",
       "361 -9999.0 -9999.0 -9999.0  \n",
       "362 -9999.0 -9999.0 -9999.0  \n",
       "363 -9999.0 -9999.0 -9999.0  \n",
       "364     NaN     NaN     NaN  \n",
       "\n",
       "[365 rows x 17 columns]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "r_df = pd.read_csv('Seattle2014.csv')\n",
    "#type(r_df)\n",
    "r_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Indexamos uma coluna ([Pandas Series](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html))."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       0\n",
       "1      41\n",
       "2      15\n",
       "3       0\n",
       "4       0\n",
       "       ..\n",
       "360    33\n",
       "361    41\n",
       "362     0\n",
       "363     0\n",
       "364     0\n",
       "Name: PRCP, Length: 365, dtype: int64"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "r_s = r_df['PRCP']\n",
    "r_s"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Transformamos a Série em um arranjo de Numpy. Usamos o atributo [`.values`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.values.html), que retornar séris Pandas como arranjos numpy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[  0  41  15   0   0   3 122  97  58  43 213  15   0   0   0   0   0   0\n",
      "   0   0   0   5   0   0   0   0   0  89 216   0  23  20   0   0   0   0\n",
      "   0   0  51   5 183 170  46  18  94 117 264 145 152  10  30  28  25  61\n",
      " 130   3   0   0   0   5 191 107 165 467  30   0 323  43 188   0   0   5\n",
      "  69  81 277   3   0   5   0   0   0   0   0  41  36   3 221 140   0   0\n",
      "   0   0  25   0  46   0   0  46   0   0   0   0   0   0   5 109 185   0\n",
      " 137   0  51 142  89 124   0  33  69   0   0   0   0   0 333 160  51   0\n",
      "   0 137  20   5   0   0   0   0   0   0   0   0   0   0   0   0  38   0\n",
      "  56   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0\n",
      "  18  64   0   5  36  13   0   8   3   0   0   0   0   0   0  18  23   0\n",
      "   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0\n",
      "   0   0   0   0   3 193   0   0   0   0   0   0   0   0   0   5   0   0\n",
      "   0   0   0   0   0   0   5 127 216   0  10   0   0   0   0   0   0   0\n",
      "   0   0   0   0   0   0   0  84  13   0  30   0   0   0   0   0   0   0\n",
      "   0   0   0   0   0   0   0   5   3   0   0   0   3 183 203  43  89   0\n",
      "   0   8   0   0   0   0   0   0   0   0   0   0   3  74   0  76  71  86\n",
      "   0  33 150   0 117  10 320  94  41  61  15   8 127   5 254 170   0  18\n",
      " 109  41  48  41   0   0  51   0   0   0   0   0   0   0   0   0   0  36\n",
      " 152   5 119  13 183   3  33 343  36   0   0   0   0   8  30  74   0  91\n",
      "  99 130  69   0   0   0   0   0  28 130  30 196   0   0 206  53   0   0\n",
      "  33  41   0   0   0]\n"
     ]
    }
   ],
   "source": [
    "rainfall = r_s.values\n",
    "#rainfall = np.array(rainfall)\n",
    "#rainfall\n",
    "#print (\"type:\", type (rainfall))\n",
    "#print (\"shape:\", rainfall.shape)\n",
    "print (rainfall)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Também pode-se explorar este arranjo utilizando um histograma. A funcionalidade da biblioteca [`MatPlotLib`](https://matplotlib.org/3.2.1/index.html)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn; seaborn.set()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Empregamos a o método [.hist()](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib-pyplot-hist) para criar um histograma."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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X2jVlS9xPQCQraKJ/OTUjCyrYtbrORoHYKKiiXx5WemcR+N/6G2Z80UAABajool8JnO9CAy+0PolrwYA8oN31wCAwYg8ABiMyAOAwTgnnwdzvXPnVn3XDu/9B4oDkc+DuX5om+ldO5liOleMFxLiTO/9X+i6AdwaiHyB5eOtm3O966dQv4SVad38AhiwOBQk8oODg/rlL3+p6elp/fjHP9a6desK8TRGyCams/mi00T/fXkxHm1nOo2UnJyRq7x01usTyel5P/ZinBeQSd4jH41G1d/frz/+8Y8qLy9XW1ub7rvvPn3961/P91MVvZv5C15z/RwiU4gzXZ/pRW++L4p8PAWKUd4jPzw8rPvvv1933HGHJKmpqUmhUEiPP/54VvcvKXHM+7nddy4p2PU3674LeezyslL933Ovf+F1+7u9C3reTI8923WZrl/ouianZlReVjrrC1Cmx57v37+lS78i1zz/BZLxRTE5rXg8kfOastmXuda90Bfr+a47nxbSk3zL+HekQF9nh23bds6POodf/epX+vTTT7VlyxZJ0quvvqqTJ0/qpz/9aT6fBgCQhby/Tz6VSsnh+M8ri23b110GAHx58h75yspKxWKx9OVYLCa3253vpwEAZCHvkf/Od76jt99+Wx999JEmJib0+uuvy+Px5PtpAABZyPsPXr/61a9qy5Ytam9v19TUlB566CF961vfyvfTAACykPcfvAIAbh18QBkAGIzIA4DBiDwAGIzIA4DBjIj84OCgHnjgAXm9Xh04cOBmL6eg4vG4WlpadO7cOUnXPkbC7/fL6/Wqv78/fbuRkREFAgE1NTWpq6tL09Ozf3DXYrN37175fD75fD7t3r1bUvHN4Re/+IUeeOAB+Xw+vfTSS5KKbwaf+fnPf67t27dLKt4ZzMle5D788EN79erV9scff2xfvXrV9vv99unTp2/2sgriH//4h93S0mLX1dXZH3zwgT0xMWE3Njba//73v+2pqSl7w4YN9l/+8hfbtm3b5/PZf//7323btu0dO3bYBw4cuJlLz5u//vWv9g9/+EM7mUzak5OTdnt7uz04OFhUc/jb3/5mt7W12VNTU/bExIS9evVqe2RkpKhm8Jnh4WH7vvvus59++umi/H7IxqI/kv/vD0S77bbb0h+IZqKBgQH19PSkf4P45MmTWr58uaqrq+V0OuX3+xUKhTQ6OqpEIqH6+npJUiAQMGYmlmVp+/btKi8vV1lZmWpqahSJRIpqDt/+9rf129/+Vk6nU+Pj45qZmdHly5eLagaS9Mknn6i/v18/+clPJBXn90M2Fn3kL168KMuy0pfdbrei0ehNXFHh7Nq1S/fee2/68mz7/vntlmUZM5Pa2tr0N2skEtHRo0flcDiKbg5lZWXas2ePfD6fGhoaivLvws6dO7Vlyxbdfvvtkorz+yEbiz7yxfyBaLPtezHM5PTp09qwYYO2bdum6urqopzD5s2b9fbbb+vChQuKRCJFNYNXX31Vd999txoaGtLbivn7YS6L/r//q6ys1Lvvvpu+XEwfiDbbh8F9fvvY2JhRMwmHw9q8ebM6Ozvl8/n0zjvvFNUc/vnPf2pyclLf/OY3tWTJEnm9XoVCIZWW/uez3U2fwZEjRxSLxdTa2qpLly7p008/1ejoaFHNIFuL/ki+mD8QbeXKlTpz5ozOnj2rmZkZDQ0NyePxqKqqSi6XS+FwWJIUDAaNmcmFCxe0ceNG9fX1yefzSSq+OZw7d07d3d2anJzU5OSk/vSnP6mtra2oZvDSSy9paGhIwWBQmzdv1ne/+139+te/LqoZZGvRH8kX8weiuVwu9fb2atOmTUomk2psbFRzc7Mkqa+vT93d3YrH46qrq1N7e/tNXm1+7N+/X8lkUr29veltbW1tRTWHxsZGnTx5Ug8++KBKS0vl9Xrl8/l01113Fc0Mvkgxfj9kgw8oAwCDLfrTNQCA2RF5ADAYkQcAgxF5ADAYkQcAgxF5ADAYkQcAgxF5ADDY/wPdeaJL/I3t5gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(rainfall, \n",
    "         bins = 40\n",
    "        );"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Se aplicarmos uma condição booleana sobre um arranjo de Numpy e ele retorna um novo arranjo com `True` ou `False`. É uma vetorização da operação de comparação."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ True False False  True  True False False False False False False False\n",
      "  True  True  True  True  True  True  True  True  True False  True  True\n",
      "  True  True  True False False  True False False  True  True  True  True\n",
      "  True  True False False False False False False False False False False\n",
      " False False False False False False False False  True  True  True False\n",
      " False False False False False  True False False False  True  True False\n",
      " False False False False  True False  True  True  True  True  True False\n",
      " False False False False  True  True  True  True False  True False  True\n",
      "  True False  True  True  True  True  True  True False False False  True\n",
      " False  True False False False False  True False False  True  True  True\n",
      "  True  True False False False  True  True False False False  True  True\n",
      "  True  True  True  True  True  True  True  True  True  True False  True\n",
      " False  True  True  True  True  True  True  True  True  True  True  True\n",
      "  True  True  True  True  True  True False False  True False False False\n",
      "  True False False  True  True  True  True  True  True False False  True\n",
      "  True  True  True  True  True  True  True  True  True  True  True  True\n",
      "  True  True  True  True  True  True  True  True  True  True False False\n",
      "  True  True  True  True  True  True  True  True  True False  True  True\n",
      "  True  True  True  True  True  True False False False  True False  True\n",
      "  True  True  True  True  True  True  True  True  True  True  True  True\n",
      "  True False False  True False  True  True  True  True  True  True  True\n",
      "  True  True  True  True  True  True  True False False  True  True  True\n",
      " False False False False False  True  True False  True  True  True  True\n",
      "  True  True  True  True  True  True False False  True False False False\n",
      "  True False False  True False False False False False False False False\n",
      " False False False False  True False False False False False  True  True\n",
      " False  True  True  True  True  True  True  True  True  True  True False\n",
      " False False False False False False False False False  True  True  True\n",
      "  True False False False  True False False False False  True  True  True\n",
      "  True  True False False False False  True  True False False  True  True\n",
      " False False  True  True  True]\n"
     ]
    }
   ],
   "source": [
    "print(rainfall == 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Em vez de fazer um loop e definir um contador, pode-se descrever os valores que nos interessam deste dataset utilizando Numpy:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Primeiro vejamos este comportamento dos booleanos em python nativo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Soma de Booleanos:  2\n"
     ]
    }
   ],
   "source": [
    "print(\"Soma de Booleanos: \", True + False + True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Soma vetorizada de valores booleanos com Numpy, conta a quantidade de ocorrências do valor `True` na lista."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Soma de numpy:  3\n"
     ]
    }
   ],
   "source": [
    "print(\"Soma de numpy: \", np.sum([True, False, True, True]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Testando o dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Número de dias sem chuva:  215\n",
      "Número de dias com chuva:  150\n",
      "Número de dias com mais de 100 cm de chuva: 47\n",
      "Número de dias com chuva, mas não maior do que 100cm : 103\n"
     ]
    }
   ],
   "source": [
    "print(\"Número de dias sem chuva: \", np.sum(rainfall == 0))\n",
    "print(\"Número de dias com chuva: \", np.sum(rainfall != 0))\n",
    "print(\"Número de dias com mais de 100 cm de chuva:\", np.sum(rainfall > 100))\n",
    "print(\"Número de dias com chuva, mas não maior do que 100cm :\", np.sum((rainfall > 0) & \n",
    "                                                                       (rainfall < 100)\n",
    "                                                                      ))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
