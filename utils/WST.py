import time
import pyautogui

class WST():
    def __init__(self,browser=None):
        self.br = browser

    def elementary(self,xpath_list=list,key=None):
        b = 0
        for xpaths in xpath_list:
            if '#time' in xpaths:
                xpaths = xpaths.replace("#time","")
                tt = xpaths[-1]
                tt = float(tt)
                time.sleep(tt)
                tt = len(xpaths) - 1
                xpaths = xpaths[0:tt]
            if '#clickhere' in xpaths:
                newp = xpaths.replace("#clickhere", "")
                elen = self.br.find_element_by_xpath(newp).click()   
            if '#textme' in xpaths:
                newp = xpaths.replace("#textme", "")
                elen = self.br.find_element_by_xpath(newp).text          
                return elen                
            if '#skeys' in xpaths:
                newp = xpaths.replace("#skeys", "")
                newp = newp.replace("#clear","")
                elen = self.br.find_element_by_xpath(newp).clear()
                elen = self.br.find_element_by_xpath(newp).send_keys(key[b])
                b += 1      

    def uniclick(self,xpath_list=str):
        self.br.find_element_by_xpath(xpath_list).click()

    def unitext(self,xpath_list=str):
        elen = self.br.find_element_by_xpath(xpath_list).text          
        return elen

    def unikey(self,xpath_list=str,key=str):
        self.br.find_element_by_xpath(xpath_list).send_keys(key)

    def remotary(self,command_list=list): 
        #Função do Pyautogui
        #forma de usar: WST.remotary([*comandos*])

        #Comandos: 
        #time: serve para dar um time de 0 à 9
        #Forma de uso: "#time9" 

        #key: serve para ser digitar algo em um input ou textbox selecionado
        #Forma de uso: "#keyOlá tudo bem?"

        #hkey: serve para somente usar hotkeys
        #Forma de uso: "#hkeyctrl c" ou até "#hkeyalt f4"

        #(x,y,d): se você adiciocar uma tupla com dois valores dentro da lista, ele irá mover o curso até as coordenadas
        # caso adicionar 3 valores, o ultimo deles "d", irá definir quantos clicks será dados, ou seja, 2 clicks, d = 2
        #Forma de uso: 
        #   1) primeiro posicione seu curso no local desejado
        #   2) abra uma instancia python
        #   3) importe pyautogui e em seguida utilize: pyautogui.position()
        #   4) isso irá retornar a posição do mouse, com os dados na mão, agora é só adicinar na tupla
        #   5) caso queira dar mais de 1 click, coloque a quantidade de clicks na ultima posição da tupla
        #   (x,y,d)

        #exemplo de uso geral: 
        #
        #   from WST import WST
        #   control = WST()
        #   comandos = [(50,50,3),"#time3","#keyTudo bem?","#hkeyalt f4"]
        #   control.remotary(comandos)
        #
        pyautogui.FAILSAFE = False
        for command in command_list:
            if '#c' in command:
                time.sleep(10)
            if '#d' in command:
                time.sleep(5)                
            if '#time' in command:
                command = command.replace("#time","")
                tt = command[-1]
                tt = float(tt)
                time.sleep(tt)
                tt = len(command) - 1
                command = command[0:tt]
            if type(command) == tuple:
                if len(command) == 3:
                    pyautogui.click(command[:2],clicks=command[-1], duration=0.5)
                else:
                    pyautogui.click(command,duration=0.5)
            if '#key' in command:
                newp = command.replace('#key',"")
                pyautogui.typewrite(newp)
            if "#hkey" in command:
                newp = command.replace("#hkey","")
                newp = newp.split();newp = tuple(newp)
                if len(newp) == 1:
                    pyautogui.hotkey(newp[0])   
                if len(newp) == 2:
                    pyautogui.hotkey(newp[0],newp[1])
                if len(newp) == 3:
                    pyautogui.hotkey(newp[0],newp[1],newp[2])  
                if len(newp) == 4:
                    pyautogui.hotkey(newp[0],newp[1],newp[2],newp[3])                                      

    def unihotkey(self,newp=list): #Função para mandar uma hotkey
        newp = tuple(newp)
        
        if len(newp) == 1:
            pyautogui.hotkey(newp[0]) 
        if len(newp) == 2:
            pyautogui.hotkey(newp[0],newp[1])
        if len(newp) == 3:
            pyautogui.hotkey(newp[0],newp[1],newp[2])  
        if len(newp) == 4:
            pyautogui.hotkey(newp[0],newp[1],newp[2],newp[3])         
        if len(newp) == 5:
            pyautogui.hotkey(newp[0],newp[1],newp[2],newp[3],newp[4])             