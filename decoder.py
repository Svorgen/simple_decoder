import random
import string


def get_password(encryption_matrix: list[str], encrypted_password: list[str]) -> str:
    """ Дешифрует пароль """
    password = ''
    for _ in range(len(encrypted_password)):
        password += ''.join(
            p for p, m in zip(list(''.join(encrypted_password)), list(''.join(encryption_matrix))) if m == 'X')
        encryption_matrix = rotate_matrix(encryption_matrix)
    return password


def get_encrypted_password(enc_matrix: list[str], password: str) -> list[str]:
    """ Шифрует пароль """
    result = [
        ''.join(random.sample(string.ascii_lowercase, len(enc_matrix))) for _ in range(len(enc_matrix))]
    cur_password_index = 0
    for _ in range(len(enc_matrix)):
        unfolded_matrix = [[p, m] for p, m in zip(list(''.join(result)), list(''.join(enc_matrix)))]
        for elem in unfolded_matrix:
            if elem[1] == 'X':
                elem[0] = password[cur_password_index]
                cur_password_index += 1
        unfolded_matrix = ''.join(p for p, m in unfolded_matrix)
        result = [unfolded_matrix[i: i + len(enc_matrix)] for i in range(0, len(unfolded_matrix), len(enc_matrix))]
        enc_matrix = rotate_matrix(enc_matrix)
    return result


def rotate_matrix(matrix: list[str]):
    """ Поворачивает матрицу на 90 градусов по часовой стрелке """
    return [''.join([matrix[j][i] for j in range(len(matrix)-1, -1, -1)]) for i in range(len(matrix))]
