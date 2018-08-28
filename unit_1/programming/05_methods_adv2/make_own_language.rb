class Encryptor
# Have class annotate entire class tomorrow
	def cipher
		{'a' => '0110001', 'b' => '01100010', 'c' => '01000011', 
		'd' => '01100100', 'e' => '01000101',  
		'f' => '01100110', 'g' => '01100111', 'h' => '01101000', 
		'i' => '01101001', 'j' => '01101010', 'k' => '01101011',
		'l' => '01101100', 'm' => '01101101', 'n' => '01101110', 
		'o' => '01101111', 'p' => '01110000', 'q' => '01110001',
		'r' => '01110010', 's' => '01110011', 't' => '01110100', 
		'u' => '01110101', 'v' => '01110110', 'w' => '01110111', 
		'x' => '01111000', 'y' => '01111001', 'z' => '01111010'}
	end

	def encrypt_letter(letter)
		lowercase_letter = letter.downcase
		cipher[lowercase_letter]
	end

	def encrypt(string)
  	# 1. Cut the input string into letters
  	letters = string.split("")

  	# 2. Encrypt those letters one at a time, gathering the results
  	results = []
  	letters.each do |letter|
    	encrypted_letter = encrypt_letter(letter)
    	results.push(encrypted_letter)
  		end

  	results.join
	end

	def decrypt_letter(letter)
		lowercase_letter = letter.downcase
		cipher.key(lowercase_letter)

	end

	def decrypt(string)
		results = [ ]
		split_string = string.slice(7)
		split_string = split_string.join
	
		for x in split_string do
			decrypted_letter = decrypt_letter(x)
			results.push(decrypted_letter)
		end
		results.join
	end
end