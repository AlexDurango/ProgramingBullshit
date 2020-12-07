class analysedText(object):
    
    def __init__ (self, text):
        self.fmtText=text.lower().replace('.','').replace(',','').replace('!','').replace('?','')

    
    def freqAll(self):
        textList = self.fmtText.split()
        dictionarie={}
        for i in range(len(textList)):
            if textList[i] not in dictionarie:
                dictionarie[str(textList[i])]= textList.count(textList[i])
        
        return dictionarie
        
            
    def freqOf(self,word):
        dictionarie = self.freqAll()
        if word in dictionarie:
            return dictionarie[str(word)]
        else:
            return 0

miTexto = analysedText("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")
print(miTexto.freqOf("diam"))