# as task I most to implement the other sort algorithms


class QuickSort:
    def __init__(self, arr, is_decrease=True):
        self.arr = arr
        self.is_decrease = is_decrease

    def get_arr(self):
        if len(self.arr) == 1:
            return self.arr
        if self.is_decrease:
            self.quick_sort_decrease(self.arr, 0, len(self.arr) - 1)
        else:
            self.quick_sort_increase(self.arr, 0, len(self.arr) - 1)
        return self.arr

    def quick_sort_decrease(self, arr, izq=0, der=0):
        i = izq
        j = der
        pivote = arr[int((izq + der) / 2)]
        while i <= j:
            while arr[i] < pivote:
                i += 1
            while arr[j] > pivote:
                j -= 1
            if i <= j:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
                i += 1
                j -= 1
        if izq < j:
            self.quick_sort_decrease(arr, izq, j)
        if i < der:
            self.quick_sort_decrease(arr, i, der)

    def quick_sort_increase(self, arr, izq=0, der=0):
        i = izq
        j = der
        pivote = arr[int((izq + der) / 2)]
        while i >= j:
            while arr[i] > pivote:
                i += 1
            while arr[j] < pivote:
                j -= 1
            if i <= j:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
                i += 1
                j -= 1
        if izq > j:
            self.quick_sort_increase(arr, izq, j)
        if i > der:
            self.quick_sort_increase(arr, i, der)
