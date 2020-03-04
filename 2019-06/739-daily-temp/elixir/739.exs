#! /usr/bin/env elixir

defmodule Solution do
  def daily_temps(temps) when is_list(temps) do
    answers = List.duplicate(0, length(temps))
    # Create answers looping from the right side
    # Rightmost is always 0, so we can skip it
    daily_temps(temps, answers, length(temps) - 2)
  end

  # If i < 0, we finished looping, return answers
  defp daily_temps(_temps, answers, i) when i < 0, do: answers

  # Use skip_right to find the answer for position i, update the answers list and keep looping
  defp daily_temps(temps, answers, i) do
    this_answer = skip_right(temps, answers, i, i + 1)
    answers = answers |> List.update_at(i, fn _x -> this_answer end)
    daily_temps(temps, answers, i - 1)
  end

  # If we skipped too far right, we can't find an answer, it's 0
  defp skip_right(temps, _answers, _i, j) when j > length(temps) - 1, do: 0

  # Look to the right to find a larger temperature.
  # Instead of looping by one, we can use the information we have in the answers array.
  # If answers[j] is 5, we can add 5 since we already know that's where a higher temperature is
  defp skip_right(temps, answers, i, j) do
    cond do
      Enum.at(temps, j) > Enum.at(temps, i) ->
        j - i

      # If 0, we can't skip by 0 (infinite loop).
      # It means that there is no answer to be found, so return 0 here quickly.
      Enum.at(answers, j) == 0 ->
        0

      true ->
        skip_right(temps, answers, i, j + Enum.at(answers, j))
    end
  end
end

actual_result = Solution.daily_temps([55, 38, 53, 81, 61, 93, 97, 32, 43, 78])
expected_result = [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]
IO.puts("Expected result")
expected_result |> IO.inspect()
IO.puts("Actual result")
actual_result |> IO.inspect()
IO.puts("Equal?")
(expected_result == actual_result) |> IO.inspect()
