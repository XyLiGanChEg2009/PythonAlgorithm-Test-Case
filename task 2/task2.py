import sys

def find_point_pos(x, y, x0, y0, a, b) -> str:  # Формула элипса (x - x0)^2/a^2 + (y-y0)^2/b^2 = 1
    left = (((x - x0) ** 2) * (b ** 2)) + (((y - y0)**2) * (a**2))
    right = a**2 * b**2
    if left - right < 0:
        return "1"
    elif left - right == 0:
        return "0"
    else:
        return "2"

def read_from_file(path: str) -> list[float]:
    with open(path, 'r') as file:
        content = file.read().split()
        if not content:
            print(f"Файл {path} пустой")
            sys.exit(1)
            
        try:
            list_of_all = list(map(float, content))
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
            sys.exit(1)
        
        return list_of_all

def read_ellipse(path: str) -> tuple[float, float, float, float]:
    nums = read_from_file(path)
    if len(nums) != 4:
        print("Файл эллипса должен содержать 4 числа: x0 y0 a b")
        sys.exit(1)
    
    return nums[0], nums[1], nums[2], nums[3]

def read_points(path: str) -> list[tuple[float, float]]:
    nums = read_from_file(path)
    if len(nums) % 2 != 0:
        print("Координаты точек должны быть парными.")
        sys.exit(1)
    
    points = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
    
    return points

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print("Ожидается 2 аргумента")
        sys.exit(1)
    
    points = read_points(args[1])
    x0, y0, a, b = read_from_file(args[0])
    for point in points:
        pos = find_point_pos(point[0], point[1], x0, y0, a, b)
        print(pos) 
    