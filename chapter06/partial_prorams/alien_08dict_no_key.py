# if dict no key-value run error
alien_dict = {'color':'green','points':5,'speed':'slow'}
print(alien_dict['cc'])
cc_value = alien_dict.get('cc','no cc value signed')
print(cc_value)