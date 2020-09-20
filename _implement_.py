import os, sys

sys.path.append('../') # this enables us to grab PythonStructs folder
if os.path.exists('main.py')
    from PythonStructs.main import CreateStruct # since we appended into the main root of the terminal, we can now import the class CreateStruct
else: raise Exception('Cannot import CreateStruct. PythonStructs github repo not imported')

class Setup(object):

    def __init__(self, information: list, default_values: list = {}) -> None:
        self.Information = CreateStruct(information)
        self.all_names = self.Information._init_items_(names=True)[0]
        self.all_values = None

        if not default_values == {}:
            for i in default_values:
                if i in self.all_names:
                    if isinstance(default_values[i],list):
                        self.Information.AddInfo(i,default_values[i])
                    self.all_values = self.Information._init_items_(values=True)

        self.Information.add_items('Total')
        
        total = 0
        for i in self.all_values[0]:
            total += 1

        if self.all_values[0][0]:
            for i in self.all_values[0][0]:
                total += 1

        self.Information.update_name('Total','Total Items')

        self.Information.AddInfo('Total Items',total)
        self.all_values = self.Information._init_items_(values=True)
        self.Information.print_all(extra=False)                    

Set = Setup(['Names','Ages'],{'Names':['Aidan','Bob'],'Ages':[15,21]})
