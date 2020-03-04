module Main where

import           Data.Bits (xor)

single_number :: [Integer] -> Integer
single_number xs = foldl (xor) 0 xs

main :: IO ()
main = do
  putStrLn $ "Expect to see: 4"
  putStrLn $ show $ single_number [4, 1, 2, 1, 2]
