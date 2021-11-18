sumOfSquares :: Int -> Int
sumOfSquares x = sum $ map (^2) [1..x]

squareOfSum :: Int -> Int
squareOfSum x = (^2) $ sum [1..x]

sumSquareDiff :: Int -> Int
sumSquareDiff x = squareOfSum x - sumOfSquares x

-- > sumSquareDiff 100
