-- HackerRank: https://www.hackerrank.com/challenges/pascals-triangle/problem
-- Passed the sample test; HackerRank closed Functional Programming submissions (Oct 2026).
main = do
  n <- readLn
  mapM_ (putStrLn . unwords . map show) (take n (iterate (\r -> zipWith (+) (0:r) (r ++ [0])) [1 :: Integer]))
