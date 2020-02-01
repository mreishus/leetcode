module Main where

--import           Lib
data BinTree a
  = Empty
  | Node a
         (BinTree a)
         (BinTree a)
  deriving (Show, Eq)

leaf :: x -> BinTree x
leaf x = Node x Empty Empty

t1_left = Node 2 (leaf 1) (leaf 3)

t1_right = Node 7 (leaf 6) (leaf 9)

t1 = Node 4 t1_left t1_right

invert_tree :: BinTree x -> BinTree x
invert_tree Empty = Empty
invert_tree (Node val left right) =
  Node val (invert_tree $ right) (invert_tree $left)

main :: IO ()
main = do
  putStrLn "Before Invert"
  putStrLn $ show t1
  putStrLn "After Invert"
  putStrLn $ show $ invert_tree t1
