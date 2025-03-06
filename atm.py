class atm:
    def __init__(self,name):
        self.name=name
    def acc_information(self):
        print('Account Information: ')
        print('Name: ', name, end='\n')
        print('Account Number: ', database[name][0], end='\n')
        print('Phone Number: ', database[name][1], end='\n')
    
    def acc_balance(self):
        print('Account Balance: ',database[name][3])
    def withdraw(self):
        print('Account Balance: ',database[name][3])
        amt=float(input('Enter Amount To Be Withdrawn: '))
        if amt<=database[name][3]:
            database[name][3]=database[name][3]-amt
            print('New Account Balance is : ', database[name][3])
        else:
            print('Insufficient Balance in Account!')
    def deposit(self):
        amt=float(input('Enter Amount To Be Deposited: '))
        database[name][3]=database[name][3]+amt
        print('New Account Balance: ', database[name][3])

database={"sai":[6781230987,9123454562,4005,45000.00], "ram":[4567890123,8200567895,8729,9000.00], 'venu':[90123456600,9573615719,1034,250000.00], "ashok":[4521857142,1237609412,8931,19000.00], "ravi":[7779378475,123986481,9471,99500.00]}
k=database.keys()
while (1):
    name=str(input('Enter Name: ')).lower()
    if name in k:
        i=3
        while(i>0):
            pin=int(input('Enter PIN: '))
            if pin==database[name][2]:
                a=atm(name)
                while(1):
                    print('Enter 1 For Account Info')
                    print('Enter 2 For Balance Enquiry')
                    print('Enter 3 For Withdrawal')
                    print('Enter 4 For Deposit')
                    s=int(input('Select Operation: '))
                    if s==1:
                        a.acc_information()
                    elif s==2:
                        a.acc_balance()
                    elif s==3:
                        a.withdraw()
                    elif s==4:
                        a.deposit()
                    else:
                        print('Invalid Option Selected! Choose Again')
                        continue
                    e=input('Enter Y to exit and N to continue operations: ')
                    if e=='y' or e=='Y':
                        print('Thank You!')
                        break
                    else:
                        continue
                break
            else:
                i=i-1
                print('Incorrect PIN, {} tries left'.format(i))
        if i==0:
            print('Try after 24 hours.')
        break
        
