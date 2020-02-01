#! /usr/bin/env elixir
defmodule BinTree do
  defstruct value: nil, left: nil, right: nil

  def merge(nil, nil), do: nil
  def merge(%BinTree{} = t1, nil), do: t1
  def merge(nil, %BinTree{} = t2), do: t2

  def merge(%BinTree{} = t1, %BinTree{} = t2) do
    %BinTree{
      value: t1.value + t2.value,
      left: merge(t1.left, t2.left),
      right: merge(t1.right, t2.right)
    }
  end
end

defmodule BinTreeTest do
  defp bt(value, left, right), do: %BinTree{value: value, left: left, right: right}
  defp leaf(value), do: %BinTree{value: value}

  defp t1, do: bt(1, bt(3, leaf(5), nil), leaf(2))
  defp t2, do: bt(2, bt(1, nil, leaf(4)), bt(3, nil, leaf(7)))

  defp t_expected, do: bt(3, bt(4, leaf(5), leaf(4)), bt(5, nil, leaf(7)))

  def go do
    (BinTree.merge(t1(), t2()) == t_expected())
    |> IO.inspect()
  end
end

BinTreeTest.go()
