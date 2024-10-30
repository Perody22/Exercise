max_sum=0
number_max=0
while True:
        number=int(input())
        if number==0:
            break
        summ=sum(int(digit) for digit in str(abs(number)))
        if summ>max_sum:
           max_sum=summ
           number_max=number
if number_max != 0:
    print('Число с максимальной суммой', number_max,'сумма цифр', max_sum)
else: 
    print('Не было введено чисел')