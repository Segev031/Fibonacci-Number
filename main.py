def fib(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        arr = [0, 1]
        for i in range(2, n+1):
            arr.append(arr[i-2] + arr[i-1])
        return arr[-1]