names = ['Илья','Даниил','Эмилия']
score = [70, 92, 95]

#for i in range(len(names)):
#    if score[i] > 90:
#        print(names[i])

for name, val in zip(names,score):
    if val > 90:
        print(name)
