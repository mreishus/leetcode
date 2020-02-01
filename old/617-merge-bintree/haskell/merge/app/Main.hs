module Main where

import           Control.Monad (forM_, join)
import           Lib

data BinTree a
  = Empty
  | Node a
         (BinTree a)
         (BinTree a)
  deriving (Show, Eq)

t1 = Node 1 (Node 3 (Node 5 Empty Empty) Empty) (Node 2 Empty Empty)

t2 =
  Node 2 (Node 1 Empty (Node 4 Empty Empty)) (Node 3 Empty (Node 7 Empty Empty))

mergeTrees :: Num a => BinTree a -> BinTree a -> BinTree a
mergeTrees t1 Empty = t1
mergeTrees Empty t2 = t2
mergeTrees (Node t1_root t1_left t1_right) (Node t2_root t2_left t2_right) =
  (Node (t1_root + t2_root) merged_left merged_right)
  where
    merged_left = mergeTrees t1_left t2_left
    merged_right = mergeTrees t1_right t2_right

t3 = mergeTrees t1 t2

challenges :: [(BinTree Integer, BinTree Integer)]
challenges = [(t1, t2)]

main :: IO ()
main =
  forM_
    challenges
    (\(t1, t2) ->
       let r = mergeTrees t1 t2
        in do putStrLn $ "t1 = " ++ show t1
              putStrLn $ "t2 = " ++ show t2
              putStrLn $ "r = " ++ show r
              putStrLn "")
