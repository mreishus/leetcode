module Main where

--import Lib
import           Data.List (foldl', sortBy)

reconstruct_queue xs =
  foldl' (\queue person -> insert_at (person !! 1) person queue) [] xs'
  where
    xs' = sortBy queue_sort xs

insert_at i elem xs = as ++ (elem : bs)
  where
    (as, bs) = splitAt i xs

queue_sort a b
  | compare0s == EQ = compare1s
  | otherwise = compare0s
  where
    a0 = a !! 0
    b0 = b !! 0
    a1 = a !! 1
    b1 = b !! 1
    compare0s = b0 `compare` a0
    compare1s = a1 `compare` b1

this_input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

expected_result = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

actual_result = reconstruct_queue this_input

main :: IO ()
main = do
  putStrLn $ "Expect to see: " ++ (show expected_result)
  putStrLn $ "Actual result: " ++ (show actual_result)
  putStrLn $ "Pass? " ++ (show $ actual_result == expected_result)
