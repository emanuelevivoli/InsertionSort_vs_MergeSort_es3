
import random
from random import shuffle
from timeit import default_timer as timer
import time

class The_War:

    def random_list(self, num):
        A = range(num)
        random.shuffle(A)
        return A

    def __init__(self, NumOfElem):

        self.num = NumOfElem
        self.A = self.random_list(self.num)
        self.B = self.A

    def Insertion_Sort(self):
        for j in range(2, len(self.A)):
            key = self.A[j]
            i = j-1
            while i>0 and self.A[i]>key:
                self.A[i+1]=self.A[i]
                i=i-1
            self.A[i+1]=key

    def Merge_Sort(self, x):
        if len(x) == 0 or len(x) == 1:
            return x
        else:
            middle = len(x) / 2
            a = self.Merge_Sort(x[:middle])
            b = self.Merge_Sort(x[middle:])
            return self.Merge(a, b)

    def Merge(self, a, b):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a[0])
                a.remove(a[0])
            else:
                c.append(b[0])
                b.remove(b[0])
        if len(a) == 0:
            c += b
        else:
            c += a
        return c

    def Battle(self):

        print  'DIMENSIONE ARRAY = '+(str)(self.num)
        print
        #INSERTION SORT
        print '     Ins_Sort [Array random]'
        start = timer()
        self.Insertion_Sort()
        end = timer()
        print '     time: '+(str)(end-start)+' s'
        print

        #MERGE SORT
        print '     Mer_Sort [Array random]'
        start = timer()
        self.Merge_Sort(self.B)
        end = timer()
        print '     time: '+(str)(end-start)+' s'
        print

        #INSERTION SORT ARRAY ORDINATO
        print '     Ins_Sort [Array Ordinato]'
        start = timer()
        self.Insertion_Sort()
        end = timer()
        print '     time: '+(str)(end-start)+' s'
        print

        #MERGE SORT ARRAY ORDINATO
        print '     Mer_Sort [Array Ordinato]'
        start = timer()
        self.Merge_Sort(self.B)
        end = timer()
        print '     time: '+(str)(end-start)+' s'
        print

        self.A = self.A[::-1]
        self.B = self.B[::-1]

        # INSERTION SORT ARRAY ORDINATO INVERSAMENTE
        print '     Ins_Sort [Array Ordinato Inversamente]'
        start = timer()
        self.Insertion_Sort()
        end = timer()
        print '     time: ' + (str)(end - start) + ' s'
        print

        # MERGE SORT ARRAY ORDINATO INVERSAMENTE
        print '     Mer_Sort [Array Ordinato Inversamente]'
        start = timer()
        self.Merge_Sort(self.B)
        end = timer()
        print '     time: ' + (str)(end - start) + ' s'
        print


e0 = The_War(100)
e1 = The_War(1000)
e2 = The_War(10000)
e3 = The_War(100000)

e0.Battle()
e1.Battle()
e2.Battle()
e3.Battle()
