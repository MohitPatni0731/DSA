def max_char(line: str) -> str:
    num_a = 0
    num_b = 0
    for c in line:
        if c == 'A':
            num_a += 1
        elif c == 'B':
            num_b += 1
        else:
            raise RuntimeError(f"Unexpected character: {c}")

    if num_a > num_b:
        return 'A'
    
    return 'B'
    

def main() -> None:
    n = int(input())
    for i in range(n):
        line = input().strip()

        print(max_char(line))

main()

# import pytest

# def test_max_char() -> None:
#     assert max_char('ABABB') == 'B'
#     assert max_char('ABABA') == 'A'
#     assert max_char('BBBAB') == 'B'
#     assert max_char('AAAAA') == 'A'
#     assert max_char('BBBBB') == 'B'
#     assert max_char('BABAA') == 'A'
#     assert max_char('AAAAB') == 'A'
#     assert max_char('BAAAA') == 'A'
    
#     with pytest.raises(RuntimeError, match="Unexpected character: C"):
#         assert max_char('CCCCC')

# # test_max_char()