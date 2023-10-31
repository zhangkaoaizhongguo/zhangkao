def naughty_or_nice(data):
    num1=0
    num2=0
    for i in data:
        for h in i:
            if i[h]=='Naughty':
                num1+=1
            elif i[h]=='Nice':
                num2+=1
    if num2>=num1:
        return 'Nice!'
    else:
        return 'Naughty!'