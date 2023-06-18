import funcs as f

email = input("Digite um endereço de email.\n")

parts = f.valid_email(email)

if parts:
    print(f"Parabéns, seu email é válido.\nUsername detectado: {parts[0]}\nDomínio: {parts[1]}\n")
else:
    print("Email inválido. D:")