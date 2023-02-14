def linear_search(array, search_value)
  i = 0
  while array[i]
    if array[i] == search_value
      return array[i]
    elsif array[i] > search_value
      break
    else
      i += 1
    end
  end
  puts 'not found'
  nil
end

puts linear_search([3, 17, 75, 80, 202], 22)
