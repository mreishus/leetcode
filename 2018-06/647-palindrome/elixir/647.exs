#! /usr/bin/env elixir
defmodule Solution do
  def expand_palin_count(s, i, j) do
    cond do
      i >= 0 && j < String.length(s) && String.at(s, i) == String.at(s, j) ->
        1 + expand_palin_count(s, i - 1, j + 1)

      true ->
        0
    end
  end

  def count_substrings(s) do
    0..String.length(s)
    |> Enum.map(fn i -> expand_palin_count(s, i, i) + expand_palin_count(s, i, i + 1) end)
    |> Enum.sum()
  end
end

IO.puts("Expect to see: 6")

Solution.count_substrings("aaa")
|> IO.inspect()
