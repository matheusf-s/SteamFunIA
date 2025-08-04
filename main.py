import requests
import google.generativeai as genai

ErrorTime = False

def Steam():

    SteamKey = str(input("Digite sua KEY da API da Steam: "))
    ContaSteam = str(input("Digite o ID da conta da Steam que deseja gerar um texto divertido: "))
                
    try:
        url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={SteamKey}&steamid={ContaSteam}&include_appinfo=true&include_played_free_games=true"
        url2 = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={SteamKey}&steamids={ContaSteam}"
        retorno2 = requests.get(url2)
        dados2 = retorno2.json()


        retorno = requests.get(url)
        dados = retorno.json()
    except:
        print("Sua APIKEY ou o ID fornecido estão incorretos!")
        print("Tente novamente!")
        exit()

    try:
        QuantJogos = dados["response"]["game_count"]
        jogos = dados['response']['games']
        requestmaiortemp = sorted(jogos, key=lambda item: item['playtime_forever'], reverse=True)
        NomemaisJogado = requestmaiortemp[0]['name']
        TempMaisJogado = int((requestmaiortemp[0]['playtime_forever'] / 60))
        TMJ = round(TempMaisJogado)
        
        NomemaisJogado1 = requestmaiortemp[1]['name']
        TempMaisJogado1 = int((requestmaiortemp[1]['playtime_forever'] / 60))
        TMJ1 = round(TempMaisJogado1)


        NickName = dados2['response']['players'][0]['personaname']

        if TMJ <= 0 and QuantJogos > 5:
            print(f"Sua conta possui alguma configuração privada, impossibilitando a captura das horas jogadas. Acho improvavel você possuir {QuantJogos} jogos e nenhum ter uma hora sequer!")
            print("Mude as configurações de privacidade ou tente outro perfil!")
            ErrorTime = True
            exit()               


        #Para testar se está puxando as info corretamente
        print(f"Seu nick é {NickName}, você tem um total de {QuantJogos} jogos, seu jogo mais jogado é {NomemaisJogado}, com um total de {TMJ}, e o segundo é {NomemaisJogado1} com {TMJ1} horas")
        
        return(NickName, QuantJogos, NomemaisJogado, TMJ, NomemaisJogado1, TMJ1)

    except:
        if ErrorTime == True:
            exit()
        else:
            print("O ID fornecido pertence a uma conta privada, impossibilitando o acesso as informações necessárias!")
            print("Deixe a conta pública ou tente outro perfil!")
            exit()
    

def ConsultaIA():
    
    KeyBot = str(input("Digite sua key do Gemini 2.5-Flash: "))
    try:
        genai.configure(api_key=KeyBot)
    except:
        print("Sua APIKEY do Gemini está incorreta, tente novamente!")
        exit()

    model = genai.GenerativeModel('gemini-2.5-flash')
    Resposta = model.generate_content(f"Crie um texto brincando de forma leve e criativa com o usuário com o nick {NickName}, ele tem um total de {QuantJogos} jogos, e o jogo mais jogado da conta é {NomemaisJogado}, com um total de {TMJ}{', comente que com base nesse tempo baixo, ele joga algum outro jogo estranho, seja criativo, algum moda ou sei lá' if TMJ < 500 else ''}, e o segundo jogado é {NomemaisJogado1} com {TMJ1} horas")

    print(Resposta.text)


NickName, QuantJogos, NomemaisJogado, TMJ, NomemaisJogado1, TMJ1 = Steam()
ConsultaIA()