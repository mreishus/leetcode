#! /usr/bin/env elixir

defmodule Solution do
  def reconstruct_queue(people) do
    people
    |> Enum.sort_by(fn x -> {Enum.at(x, 0) * -1, Enum.at(x, 1)} end)
    |> Enum.reduce([], fn person, acc ->
      acc
      |> List.insert_at(Enum.at(person, 1), person)
    end)
  end
end

this_input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
expected_result = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
actual_result = this_input |> Solution.reconstruct_queue()

IO.puts("Expected Result")
expected_result |> IO.inspect()
IO.puts("Actual Result")
actual_result |> IO.inspect()
IO.puts("Equal?")
(expected_result == actual_result) |> IO.inspect()
