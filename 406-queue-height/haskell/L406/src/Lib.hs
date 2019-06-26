module Lib
  ( someFunc
  ) where

import           Data.List (sortBy)

reconstruct_queue xs = xs
  --where
  --  xs' = sortBy queue_sort xs

queue_sort a b
  | (a !! 0) compare (b !! 0) == EQ = (a !! 1) compare (b !! 1)
  | otherwise = (a !! 0) compare (b !! 0)

this_input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

expected_result = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

actual_result = reconstruct_queue this_input

someFunc :: IO ()
someFunc = do
  putStrLn $ "Expect to see: " ++ (show expected_result)
  putStrLn $ "Actual result: " ++ (show actual_result)
  putStrLn $ "Pass? " ++ (show $ actual_result == expected_result)
