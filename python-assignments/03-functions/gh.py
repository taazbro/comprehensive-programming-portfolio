def generate_int_list(start, end):
    if start > end:
        return []  # Return an empty list if start is greater than end
    else:
        return list(range(start, end + 1))

# Example usage:
start_value = 3
end_value = 8

result_list = generate_int_list(start_value, end_value)
print(result_list)
