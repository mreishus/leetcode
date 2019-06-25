#! /usr/bin/env elixir

defmodule BinTree do
  defstruct value: nil, left: nil, right: nil
  def node(v, l, r), do: %BinTree{value: v, left: l, right: r}
  def leaf(v), do: %BinTree{value: v, left: nil, right: nil}
end

defmodule Solution do
  def max_depth(nil), do: 0

  def max_depth(%BinTree{} = t) do
    1 + max(max_depth(t.left), max_depth(t.right))
  end
end

alias BinTree, as: BT
t1 = BT.node(3, BT.leaf(9), BT.node(20, BT.leaf(15), BT.leaf(7)))

IO.puts("Expected result: 3")
IO.puts("Actual result:")

t1
|> Solution.max_depth()
|> IO.inspect()
