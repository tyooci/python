def leap_year(year: int) -> bool:
    """
    :rtype: bool
    :param year
    :return: True if year is leap, otherwise False.
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year: str, month: str) -> str or int:
    """
    
    :rtype: str or int
    :param year:
    :param month:
    :return: A quantidade de dias no mês do ano correspondente. Caso o ano seja bissexto, adiciona 1 dia em fevereiro
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not year.isnumeric() or not month.isnumeric():
        return 'Ano e mês devem ser escritos em números!'
    else:
        year = int(year)
        month = int(month)
    if 1 > month > 12:
        return 'Mês inválido!'
    else:
        month -= 1
    is_leap = leap_year(year)
    if is_leap:
        month_days[1] += 1
    return month_days[month]


print('O valor retornado será o número de dias no mês do ano informado\n')
user_year = input('Digite o ano: ')
user_month = input('Digite o mês: ')
days = days_in_month(user_year, user_month)
print(f'{days}')

leap_year(200)
