# 冒泡排序的优化

1. 每一轮循环结束后判断是否已经有序

2. 在1的基础上 每一轮循环结束后记录最后一次元素交换的位置
    ```
        public static void bubbleSort(int[] arr){
        boolean isSorted;
        int sortBorder = arr.length -1; // 无序序列的边界
        int lastExchangeInex = arr.length-2; // 上一次交换的边界
        for (int i = 0; i < arr.length-1; i++) {
            isSorted = true;
            for (int j = 0; j < sortBorder; j++) {
                if ( arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    isSorted = false;
                    lastExchangeInex = j;
                }
            }
            sortBorder = lastExchangeInex;
            if ( isSorted )
                break;
        }
    }

    ```
3. 鸡尾酒排序 -> 元素比较和交换过程是双向的