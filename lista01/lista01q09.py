
segundos = int(input('Quantos segundos? '))

d = segundos //(3600*24)
h = segundos%(3600*24)//3600
m = (segundos%3600)//60
s = (segundos%3600)%60

print('{} dia(s) {}h {}m {}s'.format(d,h,m,s))

