#! /usr/bin/env elixir

defmodule BinTree do
  defstruct value: nil, left: nil, right: nil

  def node(x, y, z), do: %BinTree{value: x, left: y, right: z}
  def leaf(x), do: %BinTree{value: x, left: nil, right: nil}
end

defmodule Solution do
  def invert_tree(nil), do: nil

  def invert_tree(%BinTree{} = bt) do
    %BinTree{
      value: bt.value,
      left: invert_tree(bt.right),
      right: invert_tree(bt.left)
    }
  end
end

alias BinTree, as: BT
t1_left = BT.node(2, BT.leaf(1), BT.leaf(3))
t1_right = BT.node(7, BT.leaf(6), BT.leaf(9))
t1 = BT.node(4, t1_left, t1_right)

IO.puts("Before Invert")

t1
|> IO.inspect()

IO.puts("Inverted")

Solution.invert_tree(t1)
|> IO.inspect()
