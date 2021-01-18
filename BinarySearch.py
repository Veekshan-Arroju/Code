{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pos=-1\n",
    "def search(list,n):\n",
    "    l=0\n",
    "    u=len(list)-1\n",
    "    \n",
    "    while l<=u:\n",
    "        mid=(1+u)//2\n",
    "        \n",
    "        if list[mid]==n:\n",
    "            globals()['pos']=mid\n",
    "            return True\n",
    "        else:\n",
    "            if list[mid]<n:\n",
    "                l=mid+1\n",
    "            else:\n",
    "                u=mid-1\n",
    "    return False\n",
    "\n",
    "list=[4,7,8,12,45,99,102,107,702,10987,5666]\n",
    "\n",
    "n= int(input('Enter the number: '))\n",
    "\n",
    "if search(list,n):\n",
    "    print(\"Found at \",pos+1)\n",
    "else:\n",
    "    print(\"Not found\")"
   ]
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
