defmodule L338 do
  use Bitwise
  use Flow

  def count_bits(max) do
    0..max
    |> Flow.from_enumerable()
    |> Flow.map(&count_binary_ones/1)
    |> Enum.to_list()
  end

  def count_binary_ones(0), do: 0

  def count_binary_ones(n) do
    rem(n, 2) + count_binary_ones(n >>> 1)
  end

  def go do
    expected_result = [0, 1, 1, 2, 1, 2]
    # L338.count_bits(5)
    actual_result = []

    IO.puts("Expected: ")
    expected_result |> IO.inspect()
    IO.puts("Actual: ")
    actual_result |> IO.inspect()

    IO.puts("Equal?")
    (expected_result == actual_result) |> IO.inspect()

    # Runs quickly if you ignore the beam startup time
    # .570(with 500k) - .460(w/o) run time  = .11 seconds
    z = L338.count_bits(500_000)
    length(z) |> IO.inspect()
    IO.puts("DONE!")
  end
end
