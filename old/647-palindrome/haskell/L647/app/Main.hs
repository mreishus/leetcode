module Main where

expand_palin_count :: (Eq a, Num p) => [a] -> Int -> Int -> p
expand_palin_count xs i j
  | index_valid && letters_equal = 1 + (expand_palin_count xs (i - 1) (j + 1))
  | otherwise = 0
  where
    l = length xs - 1
    index_valid = i >= 0 && j <= l
    letters_equal = xs !! i == xs !! j

count_substrings :: (Num a1, Eq a2) => [a2] -> a1
count_substrings xs = sum $ map counter index_range
  where
    counter =
      (\i -> (expand_palin_count xs i i) + (expand_palin_count xs i (i + 1)))
    index_range = [0 .. (length xs - 1)]

main :: IO ()
main = do
  putStrLn "Expect to see 6"
  putStrLn $ show $ count_substrings "aaa"
