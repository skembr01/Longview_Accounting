class employee:
    def __init__(self, name, hours):
        self.name = name
        if self.name != 'ross' and self.name != 'matt':
            self.hours = hours
        if self.name == 'amanda':
            self.gross = self.hours * 9
        elif self.name == 'ross':
            self.gross = 650
        elif self.name == 'matt':
            self.gross = 342.86
        else:
            self.gross = self.hours * 10
        self.social = self.gross * 0.062
        self.med = self.gross * 0.0145  
        self.child = 58.20   
    def state_tax(self):
        self.state = round((((int(self.gross / 10) - 5) * 0.5) + 0.09), 2)
    def fed_tax(self):
        if self.name != 'oscar':
            if 85 <= self.gross < 285:
                cycles = int((self.gross - 85) / 10)
                value = 0
                for i in range(0, cycles + 1):
                    value += 1
            elif 285 <= self.gross < 345:
                cycles = int((self.gross - 285) / 15)
                value = 19
                for i in range(0, cycles + 1):
                    value += 2
            # elif 345 <= self.gross < 855:
            else:
                cycles = int(((self.gross - 285) / 15) - 4)
                value = 28
                for i in range(1, cycles + 1):
                    if i % 5 == 0:
                        value += 1
                    elif i % 5 != 0:
                        value += 2
            self.fed = value
        else:
            if 175 <= self.gross < 285:
                cycles = int((self.gross - 175) / 10)
                value = 0
                for i in range(0, cycles + 1):
                    value += 1
            elif 285 <= self.gross < 345:
                cycles = int((self.gross - 285) / 15)
                value = 11
                for i in range(0, cycles + 1):
                    if i % 2 == 0:
                        value += 2
                    else: 
                        value += 1
            elif 345 <= self.gross < 855:
                cycles = int(((self.gross - 285) / 15) - 4)
                value = 19
                for i in range(1, cycles + 1):
                    if i % 5 == 0:
                        value += 1
                    elif i % 5 != 0:
                        value += 2
            self.oscarfed = value
    def final(self):
        if self.name == 'oscar':
            self.pay = self.gross - self.social - self.med - self.state - self.oscarfed
        elif self.name == 'mike':
            self.pay = self.gross - self.social - self.med - self.state - self.fed - self.child
        else:
            self.pay = self.gross - self.social - self.med - self.state - self.fed
    def print_statement(self):
        self.state_tax()
        self.fed_tax()
        self.final()
        vals = [self.gross, self.state, self.med, self.pay, self.social]
        for i in range(len(vals)):
            vals[i] = round(vals[i], 2)
        self.gross = round(self.gross, 2)
        self.state = round(self.state, 2)
        self.pay = round(self.pay, 2)
        self.social = round(self.social, 2)
        self.med = round(self.med, 2)
        if self.name == 'oscar':
            print('gross: '+str(self.gross)+'\n'+'ss: '+str(self.social)+'\n'+'med: '+str(self.med)+'\n'+'state: '+str(self.state)+'\n'+'fed: '+str(round(self.oscarfed, 2))+'\n'+'net: '+str(self.pay))
        elif self.name == 'mike':
            print('gross: '+str(self.gross)+'\n'+'ss: '+str(self.social)+'\n'+'med: '+str(self.med)+'\n'+'state: '+str(self.state)+'\n'+'fed: '+str(self.fed)+'\n'+'net: '+str(self.pay))
        else:
            print('gross: '+str(self.gross)+'\n'+'ss: '+str(self.social)+'\n'+'med: '+str(self.med)+'\n'+'state: '+str(self.state)+'\n'+'fed: '+str(self.fed)+'\n'+'net: '+str(self.pay))

 
name = input('name: ')
name = name.lower()
if name != 'ross' and name!= 'matt':
    hours = int(input('hours: '))
else:
    hours = 0
person = employee(name, hours)
person.print_statement()