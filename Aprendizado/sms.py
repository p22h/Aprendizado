from twilio.rest import Client

account_sid = 'ACe4b21689004dea3224f93242dc5a581b'
token = '1a5bef47ca8b0e44ad2ff5fe04b99dd7'

client = Client(account_sid, token)

remetente = '+16187871872'
destino = '+5535998232283'

message = client.messages.create(
    to=destino,
    from_=remetente,
    body="Mensagem teste do Twilio!")

print(message.sid)