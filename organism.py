class Organism:
    def __init__(self, food, kingdom, phylum, clas, order, family, genus, species):
        self.food = food
        self.kingdom = kingdom
        self.phylum = phylum
        self.clas = clas
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species

    def lineage(self):
        lineage = input('Enter the lineage you want to know (kingdom, phylum, clas, order, family, genus, species or all) : ') 
        if lineage == 'kingdom':
            print(self.food + ' is from the ' + lineage + ' ' + self.kingdom.upper())
        elif lineage == 'phylum':
            print (self.food + ' is from the ' + lineage + ' ' +  self.phylum.upper())
        elif lineage == 'clas':
            print (self.food + ' is from the ' + lineage + ' ' +  self.clas.upper())
        elif lineage == 'order':
            print (self.food + ' is from the ' + lineage + ' ' +  self.order.upper())
        elif lineage == 'family':
            print (self.food + ' is from the ' + lineage + ' ' +  self.family.upper())
        elif lineage == 'genus':
            print (self.food + ' is from the ' + lineage + ' ' +  self.genus.upper())
        elif lineage == 'species':
            print (self.food + ' is from the ' + lineage + ' ' +  self.species)
        elif lineage == 'all':
            print(self.food + ' is from the kingdom '+ self.kingdom.upper() + ', \n'
                  'phylum ' +  self.phylum.upper() + ", \n",
                  ' class ' +  self.clas.upper() + ", \n",
                  '  order ' +  self.order.upper() +  ", \n",
                  '   family ' +  self.family.upper() +  ", \n",
                  '    genus ' +  self.genus.upper() +  ", \n",
                  '     and species ' +  self.species)   
        else:
            print ('Unknown Lineage')

        

class LongOrganism:
    def __init__(self, food, kingdom, phylum, clas, order, family, genus, species, ploidy, genome_size, chromossome_number):
        Organism.__init__(self, food, kingdom, phylum, clas, order, family, genus, species)
        self.ploidy = ploidy
        self.genome_size = genome_size
        self.chromossome_number = chromossome_number

    def lineage(self):
        lineage = input('Enter the lineage you want to know (kingdom, phylum, clas, order, family, genus, species or all) : ') 
        if lineage == 'kingdom':
            print(self.food + ' is from the ' + lineage + ' ' + self.kingdom.upper())
        elif lineage == 'phylum':
            print (self.food + ' is from the ' + lineage + ' ' +  self.phylum.upper())
        elif lineage == 'clas':
            print (self.food + ' is from the ' + lineage + ' ' +  self.clas.upper())
        elif lineage == 'order':
            print (self.food + ' is from the ' + lineage + ' ' +  self.order.upper())
        elif lineage == 'family':
            print (self.food + ' is from the ' + lineage + ' ' +  self.family.upper())
        elif lineage == 'genus':
            print (self.food + ' is from the ' + lineage + ' ' +  self.genus.upper())
        elif lineage == 'species':
            print (self.food + ' is from the ' + lineage + ' ' +  self.species)
        elif lineage == 'all':
            print(self.food + ' is from the kingdom '+ self.kingdom.upper() + ', \n'
                  ' phylum ' +  self.phylum.upper() + ", \n",
                  '  class ' +  self.clas.upper() + ", \n",
                  '   order ' +  self.order.upper() +  ", \n",
                  '    family ' +  self.family.upper() +  ", \n",
                  '     genus ' +  self.genus.upper() +  ", \n",
                  '      and species ' +  self.species)   
        else:
            print ('Unknown Lineage')



              
soybean = LongOrganism('Soybean','Plantae', 'Angiosperms', 'Magnoliopsida','Fabales','Fabaceae','Glycine', 'Glycine Max', 'Paleotetraploid', 1.15, 20)

