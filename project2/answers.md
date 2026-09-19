part 1
1. -pbkdf uses strong iterations to create a strong key from readable text. the passphrase is needed because that passphrase is used to make the key.

part 2
1. the encryption is different each time because the iterations created are randomly generated. this is a good thing because if everything was not randomly generated there would be significantly less keys availible in the world and much easier to break

part 3
1. there were 3 most distinct blocks for ecb and the most common one repeated 24 times. cbc had 37 distinct blocks and they were all unique
2. to the attacker the ecb encryption can show the patterns of the passphrase and potentially make it easier to bruteforce
3. are they using ecb or cbc blocking?

part 4
1. SHA-256 protects the integrity of the data but not the authenticity of it so if the attacker gets access they can modify it and send it to the other person while keeping everything intact
2. HMAC uses a secret key that only you and the other person know about so attempts to breach will not work as well
3. the attacker can modify the file when using SHA-256 and forward it without detection but they cannot do that with HMAC. both ways the attacker can intercept the message

part 5
1. the check proves that I am who I say I am because if I didn't have access to my email for whatever reason or if a person who was trying to use my email didnt have access they wouldnt be able to verify that it is actually me
2. contacting my classmate outside of the network (like meeting in person) would be an effective way to check if the key really belongs to them

part 6
1. the key packet has a randomly generated session key thats been encrypted. the data packet has the encrypted message inside
2. gpg uses this method because it's more efficient and can encrypt a lager amount of data in shorter periods of time compared to RSA
3. this is called hybrid encryption


part 7:
1. the senders private key
2. the senders public key
3. the recipients public key
4. the recipients private key
5. the authenticity and integrity of the message

part 8:
1. eliptic curves uses discrete logathricmic problems while RSA uses factorization so because of that 256 bit eliptic curves provide similar security to 3072 RSA key

part 9:
1. the ai i used (geminai) did not randomly generate a key using pdkbf and instead uses a hardcoded key that the user inputs
2. if the attacker got access to the source code they could instantly decrypt all of the ciphertexts they have access to
3. this violates the concept that the security of your message depends on the secrecy of your key 


part 10:
1. switched to AES-GCM , made sure to make a new key every time, and made a decrypt_file() function
2. I changed these things so the function would be more secure and guarentee both confidentiality and authenticity
3. Authentication encryption, preventing patterns to be leaked, and key reusage
