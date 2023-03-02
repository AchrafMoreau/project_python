import csv

class Account:
    all_account = dict()
    def __init__(self, name, pw, sold):
        self.useraccount = name 
        self.password = pw
        self.sold = sold
        Account.all_account[len(Account.all_account) + 1] = [self.useraccount, self.password, self.sold]
        
        
    def All_account(self):
        return Account.all_account
    def __str__(self):
        return f'your account number is {self.useraccount}, your password is {self.password}, and your sold is {self.sold}'
    
    @classmethod    
    def data_csv(self):
        self.mylist = []
        for k,v in Account.all_account.items():
            self.mydata = dict()
            self.mydata['number_of_account'] = k
            self.mydata['username'] = v[0]
            self.mydata['password'] = v[1]
            self.mydata['sold'] = v[2]
            self.mylist.append(self.mydata)
        return self.mylist
    
    


# ------------ Admin --------------------    
class Admin(Account):
    admins ={
        'Achraf': '0210moreau',
        'Avatar': "007avatar"
    }
    isAdmin = False
    def __init__(self, name, pw):
        self.username = name
        self.password = pw
        for k,v in Admin.admins.items():
            if(name in k and pw in v):
                Admin.isAdmin = True
        
    # this code work only if isAdmin is True

    def Add_account(self, num, pw, sold):
        if Admin.isAdmin : 
            super().__init__(num, pw, sold)
        else:
            print ('you are not Admin')
    def Delet_account(self, code):
        if Admin.isAdmin:
            del Account.all_account[code]
        else:
            print('you are not Admin')

    
            
            
            
        
# ------------ USER ------------------
class User(Account):
    def __init__(self, name, pw):
        self.username = name
        self.password = pw
        self.key = None
        
        for k,v in Account.all_account.items():
            if self.username == v[0] and self.password == v[1]:
                self.key = k
            

    # this code dosn't run if u don't have an account 

    def puting_money(self, money_honey):
        if self.key != None:
            super().all_account.get(self.key)[2] += money_honey
        else:
            print ("this account dosn't exist")
        
    def pull_money(self, money_honey):
        if self.key != None:
            if super().all_account.get(self.key)[2] >= money_honey:
                super().all_account.get(self.key)[2] -= money_honey
            else:
                print("you don't have that amount of money :(")
        else:
                print("this account dosn't exist")
    def show(self):
        if self.key != None:
            print(f"Hello {self.username} your password is : {self.password}, you have {super().all_account.get(self.key)[2]} MAD in your sold")
        else:
                print("this account dosn't exist")
    def change_password(self, newpw, lastpw):
        if self.key != None:
            if lastpw == super().all_account.get(self.key)[1]:
                super().all_account.get(self.key)[1] = newpw
            else:
                print("sorry this's not the last password ")
        else:
                print ("this account dosn't exist")
    
        
# ---------- __name__ == __Main__  ---------------

obj = Admin('Achraf', '0210moreau')
obj.Add_account('user_one', 'mypw', 500)
# obj.Add_account('user_two', 'omasdas', 250)
# obj.Add_account("user_three", '0210asa', 700)
# obj.Delet_account(2)
print(obj.All_account())

obj2 = User('asdas', 'sda')
obj2.puting_money(500)
# obj2.pull_money(1000)
# obj2.change_password('dasdas', 'mydasdapw')







# --------------------------- uoloading file ---------------------------

with open('C:/Users/PC/OneDrive/Desktop/project_py/data.csv', 'w', newline='') as f:
    data = Admin.data_csv()
    names = ['number_of_account','username','password', 'sold']
    my_file = csv.DictWriter(f, fieldnames=names)
    my_file.writeheader()
    for row in data:
        my_file.writerow(row)
        
    

