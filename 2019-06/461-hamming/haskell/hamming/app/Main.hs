module Main where

import           Data.Bits (shiftR, xor)
import           Lib

--hamming_distance :: Integral a => a -> a -> a
hamming_distance :: Integer -> Integer -> Integer
hamming_distance x y = count_binary_ones z
  where
    z = x `xor` y

count_binary_ones :: Integer -> Integer
count_binary_ones 0 = 0
count_binary_ones x = (x `rem` 2) + count_binary_ones (shiftR x 1)

main :: IO ()
main = do
  putStrLn "Expect to see 2"
  putStrLn $ show $ hamming_distance 1 4
