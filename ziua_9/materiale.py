class  Material:
    def __init__(self,titlu,autor,disponibila):
        self.titlu=titlu
        self.autor=autor
        self.disponibila=disponibila
class Carte(Material):
    def __init__(self,titlu,autor,disponibila,nr_pagini):
        super().__init__(titlu,autor,disponibila)
        self.nr_pagini=nr_pagini
    def __str__(self):
        return f"Titlu:{self.titlu} | autor:{self.autor} | pagini:{self.nr_pagini}"
class Revista(Material):
    def __init__(self,titlu,autor,disponibila,nr_edit):
        super().__init__(titlu,autor,disponibila)
        self.nr_edit=nr_edit
    def __str__(self):
        return f"Titlu:{self.titlu} | autor:{self.autor} | pagini:{self.nr_edit}"