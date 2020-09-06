slovar ={
    'Ukraine':'Kiev',
    'Spain':'Madrid',
    'Portugal':'Lissabon',
    'UK':'London'
    }
strany=['Ukraine','Russia','UK','Belgium','Belarus','Portugal']

for k, v in slovar.items():
    for i in strany:
        if i==k:
            print(k, v)