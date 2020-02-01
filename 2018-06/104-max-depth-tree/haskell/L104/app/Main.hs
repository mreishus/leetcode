module Main where

--import           Lib
data BinTree a
  = Node a
         (BinTree a)
         (BinTree a)
  | Empty
  deriving (Show, Eq)

leaf :: a -> BinTree a
leaf x = Node x Empty Empty

t1 = Node 3 (leaf 9) (Node 20 (leaf 15) (leaf 7))

max_depth :: BinTree a -> Int
max_depth Empty               = 0
max_depth (Node _ left right) = 1 + max (max_depth left) (max_depth right)

main :: IO ()
main = do
  putStrLn "Expected Result: 3"
  putStrLn $ "Actual result: " ++ (show $ max_depth t1)
