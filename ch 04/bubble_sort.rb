def bubble_sort_while_loop(array)
  unsorted_until_index = array.length - 1
  sorted = false

  until sorted
    sorted = true
    i = 0

    while i < unsorted_until_index
      if array[i] > array[i + 1]
        array[i], array[i + 1] = array[i + 1], array[i]
        sorted = false
      end
      i += 1
    end

    unsorted_until_index -= 1
  end

  array
end

def bubble_sort(array)
  unsorted_until_index = array.length - 2
  sorted = false

  until sorted
    sorted = true
    i = 0

    for i in 0..unsorted_until_index
      if array[i] > array[i + 1]
        array[i], array[i + 1] = array[i + 1], array[i]
        sorted = false
      end
        end

    unsorted_until_index -= 1
  end

  array
end

puts bubble_sort([65, 55, 45, 35, 25, 15, 10])
