class QuickSort:

    def sort(self, data, low, high):
        if(low < high):
            mid = self.partition(data, low, high)
            self.sort(data, low, mid - 1)
            self.sort(data, mid+1, high)
        
    def partition(self, data, low, high):
        pivot = data[low]
        left = low + 1
        right = high
        while True:
            while(left <= right and data[left] <= pivot):
                left += 1
            while(right >= left and data[right] >= pivot):
                print(high)
                right -= 1
            if(left > right):
                break
            else:
                self.swap(data, left, right)
        self.swap(data, low, right)
        return right    

    def swap(self, data, low, high):
        tmp = data[low]
        data[low] = data[high]
        data[high] = tmp
