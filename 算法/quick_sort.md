# 快速排序

### 防止退化成O(n^2)的办法
- 随机选择一个元素作为基准元素 可大大减低退化的概率
- 选择 首元素 中间元素 尾元素的中间数

## 单向循环法
    从数组的一边循环遍历
    ```
    private static int partition(int[] arr, int l, int r) { // [l, r]
        int mark = l; // 小于基准元素的边界
        int temp = arr[l];
        for (int i = l+1; i <= r; i++) {
            if(arr[i] <= temp){
                mark ++;
                int p = arr[i];
                arr[i] = arr[mark];
                arr[mark] = p;
            }
        }
        arr[l] =arr[mark];
        arr[mark] = temp;
        return mark;
    }
    ```
## 两路快排
    数组两端同时出发

    ```
        private static int partition(int[] arr, int l, int r) { // [l, r]
            int temp = arr[l];
            while (l < r) {
                while (l < r && arr[r] > temp) r--;
                if (l < r) arr[l] = arr[r];
                while (l < r && arr[l] < temp) l++;
                if (l < r) arr[r] = arr[l];
            }
            arr[l] = temp;
            return l;
        }
    ```

## 三路快排
    [0, lt]<temp  ==temp  [gt, n]>temp
    

## 非递归算法