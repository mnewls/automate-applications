import quandl
import dtale

quandl.ApiConfig.api_key = 'GETUROWN'
my_table = quandl.get_table('ZILLOW/DATA', region_id='91253')

my_table_2 = quandl.get_table('ZILLOW/REGIONS')

table_loc_region = my_table_2[my_table_2['region'].str.contains('North Ridge; CA', regex = False)]

my_table_palmdale = quandl.get_table('ZILLOW/DATA', region_id='97344')

my_table_palmdale_2 = quandl.get_table('ZILLOW/DATA', region_id='97330')

#print(table_loc_region)

#print(my_table)

price_table = my_table['value']
price_table_pd = my_table_palmdale['value']
price_table_pd2 = my_table_palmdale_2['value']

#print(my_table_2)

#print(price_table.size)

average_inc_per_month = price_table[1:].mean() / price_table.size

average_inc_per_month_pd = price_table_pd[1:].mean() / price_table_pd.size

average_inc_per_month_pd2 = price_table_pd2[1:].mean() / price_table_pd2.size



print(price_table[1:].mean())

print(average_inc_per_month)

print(price_table_pd[1:].mean())

print(average_inc_per_month_pd)

print(price_table_pd2[1:].mean())

print(average_inc_per_month_pd2)


