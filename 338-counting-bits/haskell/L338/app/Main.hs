module Main where

import           Data.Array (Array, elems, listArray, (!))
import           Data.Bits  ((.&.))

--import           Lib
input = [0, 1, 1, 2, 1, 2]

process :: Integer -> [Integer]
process n = elems r
  where
    r = listArray (0, n) (map num_binary_ones [0 .. n])
    num_binary_ones i
      | i == 0 = 0
      | otherwise = r ! ((i - 1) .&. i) + 1

main :: IO ()
main = do
  putStrLn "Expected: [0,1,1,2,1,2]"
  let a = process 5
  putStrLn $ "Actual: " ++ (show $ a)
