from __future__ import print_function
import tap

######################
# Token Creation
######################

data = {
  "card": {
    "number": 4508750015741019,
    "exp_month": 1,
    "exp_year": 39,
    "cvc": 100,
    "name": "test token",
    "address": {
      "country": "Kuwait",
      "line1": "Salmiya, 21",
      "city": "Kuwait city",
      "street": "Salim",
      "avenue": "Gulf"
    }
  },
  "client_ip": "192.168.1.20"
}


resp = tap.Token.create(**data)
print('Success: %r' % (resp))
token_id = resp.id

######################
# Customer Creation
######################

data = {
  "first_name": "test",
  "last_name": "test",
  "email": "test@test.com",
  "nationality": "Moroccan",
  "currency": "MAD"
}

resp = tap.Customer.create(**data)
customer_id = resp.id

######################
# Optional Create Card
######################
resp = tap.Customer.create_card(resp.id, **{'source': token_id})
card_id = resp.id

######################
# retrieve Card
######################

tap.Customer.retrieve_card(customer_id, card_id)

######################
# list Card
######################

tap.Customer.list_cards(customer_id)

######################
# Create Charge
######################
data = {
  "amount": 10,
  "currency": "KWD",
  "customer": {
    "id": customer_id
  },
  "source": {
    "id": "src_all"
  },
  "post": {
    "url": "http://your_website.com/post_url"
  },
  "redirect": {
    "url": "http://your_website.com/redirect_url"
  }
}

resp = tap.Charge.create(**data)
print('Success: %r' % (resp))
charge_id = resp.id

# ######################
# # retrieve Charge
# ######################

resp = tap.Charge.retrieve_charges(charge_id)
print('Success: %r' % (resp))
