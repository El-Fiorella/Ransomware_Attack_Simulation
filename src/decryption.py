with open("Milestone_1_Payload.txt", "r") as f: 
scrambled_data = f.read() 
# Applying the reverse operation again to decrypt 
original_data = scrambled_data[::-1] 
with open("Decrypted_Payload.txt", "w") as f: 
f.write(original_data)
