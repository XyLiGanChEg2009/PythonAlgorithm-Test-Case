import sys

def calculate_path(n: int, m: int) -> list:
    result = [1]
    state = m if m <= n else m - n
    is_complete = False
    while not is_complete:
        result.append(state)
        state = (state + m - 1) % n if (state + m - 1) != n else state + m - 1
        if result[0] == state:
            is_complete = True
            
    return result 
    

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if len(args) != 4:
        print("Ожидается 4 элемента")
        sys.exit(1)
    
    try:
        n1, m1, n2, m2 = map(int, args)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)
        
    result_path = calculate_path(n1, m1) + calculate_path(n2, m2)
    print("".join(str(item) for item in result_path))