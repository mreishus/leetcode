#! /usr/bin/env elixir
IO.puts("Hello!")

defmodule Solution do
  use Bitwise

  # Created an elixir project to use the "Flow" module
  # to run in parallel
  def count_bits(max) do
    0..max
    |> Enum.to_list()
    |> Enum.map(&count_binary_ones/1)
  end

  def count_binary_ones(0), do: 0

  def count_binary_ones(n) do
    rem(n, 2) + count_binary_ones(n >>> 1)
  end
end

expected_result = [0, 1, 1, 2, 1, 2]
actual_result = Solution.count_bits(5)

IO.puts("Expected: ")
expected_result |> IO.inspect()
IO.puts("Actual: ")
actual_result |> IO.inspect()

IO.puts("Equal?")
(expected_result == actual_result) |> IO.inspect()

z = Solution.count_bits(500_000)
IO.puts("DONE!")
