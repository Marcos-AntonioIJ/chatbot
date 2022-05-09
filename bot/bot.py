from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse


SECRET_KEY = 'dajedilajidajijdeaijdae'
app = Flask(__name__)
app.config.from_object(__name__)

  
@app.route('/bot', methods=['POST'])

def bot():
    
    incoming_msg = request.values.get('Body', '').lower()
    userName = session.get('userName',0)
    level = session.get('level',0)
    returning = session.get('returning',0)
    duvidareturn = session.get('duvidareturn',0)
    resp = MessagingResponse()
    responded = False
    

    while responded == False:
        
        if incoming_msg == 'sair': 
            session.clear()
            resp.message(f'Obrigado por entrar em contato {userName}!!.\n\nEstarei aqui se precisar de mim novamente, você será sempre bem-vindo!.')
            return str(resp)
            
        if level == 0:
            session['level'] = 'name'
            resp.message(f'Olá seja muito bem-vindo, eu sou o Buba o ajudante do Pet-Shop e irei te auxiliar, poderia me dizer seu nome?')
            responded = True
        
        elif level == 'name':
            if returning == 0 : 
                resp.message(f'{userName} você pode digitar "sair" a qualquer momento para encerrar nossa conversa, beleza?.')
                session['userName'] = incoming_msg.capitalize()
                userName = session.get('userName',0)                 
                resp.message(f'{userName} vamos começar, o que você deseja?\n\n1 - Ofertas\n2 - Banho e tosa (somente para cães e gatos)\n3 - Dúvidas\n4 - Outros')
            else :
                resp.message(f'{userName}, o que mais você deseja?\n\n1 - Ofertas\n2 - Banho e tosa (somente para cães e gatos)\n3 - Dúvidas\n4 - Outros')
                         
            session['level'] = 'home'   
            responded = True
            
        elif level == 'home':
            
            if incoming_msg == '1':
                
                session['level'] = 'oferta'
                resp.message(f'{userName} essas são as nossas categorias de produtos, o que você está buscando?\n\n1 - Medicamentos e produtos higienicos\n2 - Rações e petiscos\n3 - Brinquedos\n4 - Voltar')
                responded = True
                
            elif incoming_msg == '2':
                
                session['level'] = 'banho'
                resp.message(f'{userName} esses são os valores de nossos serviços, porém só estão disponiveis em locais que possuem nossa loja física que são:\n\nLambari MG - Rua Dr. José dos Santos, 50\n\nTabela de preços\nBanho porte pequeno: VALOR\nBanho porte médio: VALOR\nBanho porte grande: VALOR\nTosa porte pequeno: VALOR\nTosa porte medio:  VALOR\nTosa porte grande VALOR\n\n1 - Agendar horário com atendente\n2 - Voltar');
                responded = True
                
            elif incoming_msg == '3':
                
                session['level'] = 'duvida'               
                if duvidareturn == 0 :
                    resp.message(f'{userName} irei esclarecer suas dúvidas, pode me dizer o que você deseja saber?.\n\n1 - Devolução de produtos\n2 - Frete de produtos\n3 - Formas de pagamento\n4 - Locais do Petshop\n5 - Voltar')
                else:
                    resp.message(f'{userName} tem mais alguma dúvida?, pode me dizer estou aqui para te ajudar!.\n\n1 - Devolução de produtos\n2 - Frete de produtos\n3 - Formas de pagamento\n4 - Locais do Petshop\n5 - Voltar')               
                responded = True
                
            elif incoming_msg == '4':
                
                session['level'] = 'atendente'
                resp.message(f'Estou procurando uma atendente, porfavor aguarde {userName}...\n1- Cancelar')       
                responded = True
                
            elif incoming_msg != '1' and incoming_msg != '2' and incoming_msg != '3' and incoming_msg != '4' and incoming_msg != 'sair':
                resp.message('Não entendi sua resposta, poderia porfavor digitar o número de uma opção acima?')
                responded = True
                
        elif level == 'oferta':
            if incoming_msg == '1':
                resp.message('* Antipulgas e Carrapatos Bravecto MSD para Cães de 4,5 a 10 kg\n' +
                        '* Agemoxi CL 250mg Antibiótico 10 comprimidos Cães e Gatos Agener União\n' \
                        '* Vermífugo Ourofino Top Dog Para Cães 30kg\n'
                        '* Ball Free Suplemento Para Gatos 70g\n')
                level = 'home'
                session['level'] =  'home'
                incoming_msg = '1'
              
            
            elif incoming_msg == '2':
                resp.message('* Mordedor Ossinho Petz P - Cores Sortidas\n' +
                        '* Brinquedo Zee.Dog Brain Dead para Cães\n' \
                        '* Macaco Chalesco Brinquedo Para Cães Pelúcia Marrom\n'
                        '* Brinquedo Chalesco para Cães Corda Dental Bone Grande - Cores Sortidas\n')
                level = 'home'
                session['level'] =  'home'
                incoming_msg = '1'
            
            elif incoming_msg == '3':
                resp.message('* Ração Royal Canin Maxi - Cães Adultos - 15kg\n' +
                        '* Ração Royal Canin Bulldog Inglês para Cães Adultos - 12kg\n' \
                        '* Petisco Dog Chow Extra Life para Cães Adultos Sabor Carne e Cenoura - 75g\n'   
                        '* Biscoito Premier Cookie para Cães Adultos Sabor Frutas Vermelhas e Aveia 250g\n')
                level = 'home'
                session['level'] =  'home'
                incoming_msg = '1'
                       
            elif incoming_msg == '4':
                level = 'name'
                session['level'] = 'name'
                session['returning'] = 1
                returning = 1
            
            elif incoming_msg != '1' and incoming_msg != '2' and incoming_msg != '3' and incoming_msg != '4' and incoming_msg != 'sair':
                resp.message('Não entendi sua resposta, poderia porfavor digitar o número de uma opção acima?')
                responded = True
                
        elif level == 'banho':
            if incoming_msg == '1':
                level = 'atendente'
                session['level'] = 'atendente'
                resp.message(f'Estou procurando uma atendente, porfavor aguarde {userName}...\n1- Cancelar')    
                responded = True
                
            elif incoming_msg == '2':
                level = 'name'
                session['level'] = 'name'
                returning = 1
                session['returning'] = 1
            
            elif incoming_msg != '1' and incoming_msg != '2' and incoming_msg != 'sair':
                resp.message('Não entendi sua resposta, poderia porfavor digitar o número de uma opção acima?')
                responded = True
                
        elif level == 'duvida':
            if incoming_msg == '1':
                resp.message(f'Você tem 7 dias corridos a partir do recebimento do pedido, para solicitar a troca de seu produto. Para isso, entre em contato com a nossa Central de Atendimento\n\nDeseja falar com algum atendente sobre devolução?\n\n1 - Sim\n2 - Não')
                level = 'op-atendente'
                session['level'] =  'op-atendente'
                responded = True
               
                
            elif incoming_msg == '2':
                resp.message(f'O frete vai depender do local da entrega e do peso do produto, compras acima de $100,00 tem frete grátis em todo Brasil')
                level = 'home'
                session['level'] =  'home'
                incoming_msg = '3'
                session['duvidareturn'] = 1
                duvidareturn = 1
                
            elif incoming_msg == '3':
                resp.message(f'Aceitamos cartão de crédito, cartão de debito, boleto bancário e PIX')
                level = 'home'
                session['level'] =  'home'
                incoming_msg = '3'
                session['duvidareturn'] = 1
                duvidareturn = 1
                
            elif incoming_msg == '4':
                resp.message(f'Atualmente nossas lojas físicas estão localizadas em :\n\nLambari MG - Rua Dr. José dos Santos, 50\n')
                level = 'home'
                session['level'] =  'home'
                incoming_msg = '3'
                session['duvidareturn'] = 1
                duvidareturn = 1
                
            elif incoming_msg == '5':
                session['level'] = 'name'
                level = 'name'   
                session['duvidareturn'] = 1
                duvidareturn = 1
            
            elif incoming_msg != '1' and incoming_msg != '2' and incoming_msg != '3' and incoming_msg != '4' and incoming_msg != '5' and incoming_msg != 'sair':
                resp.message('Não entendi sua resposta, poderia porfavor digitar o número de uma opção acima?')
                responded = True
                
        elif level == 'atendente':  
            if incoming_msg == '1':
                level = 'name'
                session['level'] = 'name'
                session['returning'] = 1
                returning = 1
            
            elif incoming_msg != '1' and incoming_msg != 'sair':
                resp.message('Não entendi sua resposta, poderia porfavor digitar o número de uma opção acima?')
                responded = True
                
        elif level == 'op-atendente':
            
            if incoming_msg == '1':
                session['level'] = 'atendente'
                resp.message(f'Estou procurando uma atendente, porfavor aguarde {userName}...\n\n1 - Cancelar')
                responded = True 
                
            elif incoming_msg == '2':
                level = 'home'   
                session['level'] = 'home'
                session['duvidareturn'] = 1
                duvidareturn = 1              
                incoming_msg = '3'
                               
            elif incoming_msg != '1' and incoming_msg != '2' and incoming_msg != 'sair':
                resp.message('Não entendi sua resposta, poderia porfavor digitar o número de uma opção acima?')
                responded = True
        
        
    return str(resp)

if __name__ == '__main__':
       app.run()
