{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "9dd5e5fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x :  [14 42  0 14 42] \n",
      "y :  [147 427   7 147 427]\n",
      "p : [2058, 17934, 0, 2058, 17934]\n",
      "u : [196, 1764, 0, 196, 1764]\n",
      "sum of array xi^2 :  3920\n",
      "sum of array xi*yi :  39984\n",
      "sum of array x : 112 \n",
      "sum of array y : 1155\n",
      "z :  10.0 \n",
      "s :  7.0\n",
      "formula is : \n",
      "\n",
      "y =  10.0 x +  7.0\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import random\n",
    "\n",
    "i=0\n",
    "k=[]\n",
    "l=[]\n",
    "while i<5:\n",
    "    num=random.randrange(0, 50, 14)\n",
    "    k.append(num)\n",
    "    i+=1\n",
    "#print(k)\n",
    "\n",
    "x=np.array(k)\n",
    "i=0\n",
    "while i<5:\n",
    "   #num=random.randrange(0, 100, 3)\n",
    "    num=10*x[i]+7\n",
    "    l.append(num)\n",
    "    i+=1\n",
    "#print(l)\n",
    "y=np.array(l)\n",
    "print('x : ',x,'\\ny : ',y)\n",
    "plt.scatter(x, y)\n",
    "\n",
    "\n",
    "a=np.sum(x)\n",
    "b=np.sum(y)\n",
    "\n",
    "p=[]\n",
    "i=0\n",
    "while i<5:\n",
    "    p.append(x[i]*y[i])\n",
    "    i+=1\n",
    "print('p :',p)\n",
    "c=np.sum(p)\n",
    "\n",
    "i=0\n",
    "u=[]\n",
    "while i<5:\n",
    "    u.append(x[i]*x[i])\n",
    "    i+=1\n",
    "print('u :',u)\n",
    "d=np.sum(u)\n",
    "\n",
    "print('sum of array xi^2 : ',d)\n",
    "\n",
    "print('sum of array xi*yi : ',c)\n",
    "\n",
    "print('sum of array x :',a, '\\nsum of array y :',b)\n",
    "\n",
    "m=a\n",
    "n=b\n",
    "v=c\n",
    "r=d\n",
    "\n",
    "z=(m*n-5*v)/(m*m-5*r)\n",
    "s=(m*v-n*r)/(m*m-5*r)\n",
    "\n",
    "print(\"z : \",z,\"\\ns : \",s)\n",
    "print('formula is : \\n')\n",
    "print('y = ',z,'x + ',s)\n",
    "\n",
    "#plt.scatter(x, y)\n",
    "plt.xlabel(\"Avg Pulse\")\n",
    "plt.ylabel(\"Avg Life\")\n",
    "plt.show()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a39ffe85",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33c00487",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f72545ab",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87c80b05",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
