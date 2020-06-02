def convert_time_info(value):
    value = value

    month_dic = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    month_info = month_dic[value[3:6]]
    date_info = value[:2]
    time_info = value[6:]
    result = '2020-'+month_info+'-'+date_info+' '+time_info
    print(result)


value = '12 May23:29'
convert_time_info(value)
