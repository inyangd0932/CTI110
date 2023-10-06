''' Type your code here. '''
milespergallon = float(input())
dollarspergallon = float(input())

twenty_mile = 20
seventyf_mile = 75
fiveh_mile = 500

cost_for_20 = twenty_mile / milespergallon * dollarspergallon

cost_for_75 = seventyf_mile / milespergallon * dollarspergallon

cost_for_500 = fiveh_mile / milespergallon * dollarspergallon

print(f'{cost_for_20:.2f} {cost_for_75:.2f} {cost_for_500:.2f}')

