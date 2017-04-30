fibTerm :: Int -> Int

fibTerm 1 = 1
fibTerm 2 = 2
fibTerm n = (fibTerm n - 1) + (fibTerm n - 2)
