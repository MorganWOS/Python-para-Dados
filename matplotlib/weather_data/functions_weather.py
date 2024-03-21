from datetime import datetime
#Extrai o PRCP e as datas
def extraction_date_min_max(d, l, h, read, colum1, colum2):
    for row in read:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[colum1])
            low = int(row[colum2])
        except ValueError:
            print("Missing data")
        else:
            h.append(high)  
            l.append(low) 
            d.append(current_date)
    return d, h, l