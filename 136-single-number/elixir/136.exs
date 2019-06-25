#! /usr/bin/env elixir
defmodule Solution do
  use Bitwise

  def single_number(nums) when is_list(nums) do
    nums
    |> Enum.reduce(fn x, acc -> x ^^^ acc end)
  end
end

IO.puts("Expect to see: 4")

[4, 1, 2, 1, 2]
|> Solution.single_number()
|> IO.puts()
