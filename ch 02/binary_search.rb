def binary_search(array, search_value)
  lower_bond = 0
  upper_bond = array.length - 1

  while lower_bond <= upper_bond
    mid = (lower_bond + upper_bond) / 2

    if array[mid] == search_value
      return mid
    elsif array[mid] < search_value
      lower_bond = mid + 1
    else
      upper_bond = mid - 1
    end
  end

  nil
end

puts binary_search([3, 17, 75, 80, 202], 202)
