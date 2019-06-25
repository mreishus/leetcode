module Main where

import           Data.Array (Array, elems, listArray, (!))

daily_temps :: [Int] -> [Int]
daily_temps temps_l = elems answers
  where
    n = length temps_l
    -- Fill in answers from the right, working towards the left
    answers = listArray (0, n - 1) (reverse $ map f [(n - 1),(n - 2) .. 0])
    temps = listArray (0, n - 1) temps_l
    f i
      | i == (n - 1) = 0
      | otherwise = look_right temps answers i (i + 1)

-- Move to the right, looking for a larger temperature than I
-- Instead of looping by J += 1, we increment by (answers ! j) to reuse the
-- info we already have
look_right :: Array Int Int -> Array Int Int -> Int -> Int -> Int
look_right temps answers i j
  | (temps ! j) > (temps ! i) = j - i
  | answers ! j == 0 = 0
  | otherwise = look_right temps answers i (j + answers ! j)

input = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]

expected_result = [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]

actual_result = daily_temps input

--import           Lib
main :: IO ()
main = do
  putStrLn $ "Expect to see " <> show expected_result
  putStrLn $ "Actual result " <> show actual_result
  putStrLn $ "Equal? " <> show (actual_result == expected_result)
