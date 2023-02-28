class SortableArray:
    def __init__(self, arr):
        self.arr = arr

    def partition(self, low, high):
        pivot_index = high

        pivot = self.arr[pivot_index]

        high -= 1

        while True:
            while self.arr[high] > pivot:
                high -= 1

            while self.arr[low] < pivot:
                low += 1

            if low >= high:
                break
            else:
                self.arr[high], self.arr[low] = self.arr[low], self.arr[high]
                low += 1

        self.arr[low], self.arr[pivot_index] = self.arr[pivot_index], self.arr[low]

        return low

    def quicksort(self, low, high):

        if high - low <= 0:
            return

        pivot_index = self.partition(low, high)

        self.quicksort(low, pivot_index - 1)
        self.quicksort(pivot_index + 1, high)

    def quickselect(self, kth_lowest_value, low, high):
        if high - low <= 0:
            return self.arr[low]

        pivot_index = self.partition(low, high)

        if kth_lowest_value < pivot_index:
            return self.quickselect(kth_lowest_value, low, pivot_index - 1)
        elif kth_lowest_value > pivot_index:
            return self.quickselect(kth_lowest_value, pivot_index + 1, high)
        else:
            return self.arr[pivot_index]


if __name__ == "__main__":
    array = [0, 5, 2, 1, 6, 3]
    array2 = [0, 50, 20, 10, 60, 30]

    sortable_array = SortableArray(array)
    sortable_array.quicksort(0, len(array) - 1)
    print(sortable_array.arr)

    sortable_array2 = SortableArray(array2)
    print(sortable_array2.quickselect(1, 0, len(array2) - 1))
    # print(sortable_array2.arr)
