import pandas as pd

def getEmails(file):
    emails=[]
    names=[]
    if file=='gfg':
        data=pd.read_csv('data/'+file+'.csv')
        for i in range(0,118):
            emails.append(data['Email'][i])
            names.append(data['Name'][i])
    else:
        # data=pd.read_csv('data/mails.csv')
        # for i in range(data.shape[0]):
        #     if data[file][i] != 'empty':
        #         emails.append(data[file][i])
        raise(ValueError)
    return (emails,names)

# print(getEmails('all_mails'))
# print(getEmails('hello'))
# t=getEmails('gfg')
# for i in range(len(t[0])):
#     print(t[0][i],t[1][i],sep='\t\t')

