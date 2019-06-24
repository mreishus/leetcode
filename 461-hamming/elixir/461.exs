#! /usr/bin/env elixir
use Bitwise

defmodule Solution do
  def hamming_distance(x, y) do
    bxor(x, y)
    |> count_binary_ones()
  end

  def count_binary_ones(0), do: 0

  def count_binary_ones(x) when is_integer(x) do
    rem(x, 2) + count_binary_ones(x >>> 1)
  end
end

IO.puts("Expect to see 2")

Solution.hamming_distance(1, 4)
|> IO.puts()
