from sys import exit, argv
import os

def find_min_steps(nums: list):
    if not nums:
        print("Список пустой или в нем только 1 элемент")
        exit(1)
    
    if len(nums) == 1:
        return 0
        
    nums.sort()
    median = 0
    
    if len(nums) % 2 == 0:
        median = nums[len(nums) // 2 - 1]
    else:
        median = nums[len(nums) // 2]
    
    result_steps = sum(abs(median - elem) for elem in nums)
    
    return result_steps

def read_from_file(path: str) -> list[int]:
    if not os.path.exists(path):
        print(f"Файл {path} не найден")
        exit(1)

    try:
        with open(path, 'r') as f:
            content = f.read().split()
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        exit(1)

    if not content:
        print(f"Файл {path} пуст")
        exit(1)

    try:
        nums = list(map(int, content))
    except ValueError:
        print("В файле содержатся не целые числа")
        exit(1)

    return nums


if __name__ == "__main__":
    nums_path = argv[1:]
    if len(nums_path) != 1:
        print("На вход ожидается только 1 аргумент")
        exit(1)
    
    nums = read_from_file(nums_path[0])
    steps = find_min_steps(nums)
    
    if steps > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
        exit(1)
    else:
        print(steps)