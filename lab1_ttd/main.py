def cal(numbers):
    if not numbers:
        return 0

    numbers = numbers.replace('\n', ',')

    numbers_list = numbers.split(',')

    if not isinstance(numbers_list, list):
        raise ValueError('List convertion failed.')

    if '' in numbers_list:
        raise ValueError('Invalid input value.')

    return sum(int(num) for num in numbers_list)