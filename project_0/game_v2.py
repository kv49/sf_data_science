import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess a number

    Args:
        number (int, optional): a number to guess. Defaults to 1.

    Returns:
        int: number of tries
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

#print(f'Количество попыток: {random_predict()}')

def half_divide_predict(number: int = 1) -> int:
    """ Подбираем число методом деления интервала пополам 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    start_range = 1
    end_range = 100
    
    while True:
        count += 1
        range_size = end_range - start_range + 1
        predict_number = start_range + range_size // 2 # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number < predict_number:
            end_range = predict_number - 1
        else:
            start_range = predict_number + 1
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
#    score_game(random_predict)
    score_game(half_divide_predict)