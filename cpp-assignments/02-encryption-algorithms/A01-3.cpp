
// Name: Tanjim Ahmed Al Zabeer
// SSID: 1954925
// Assignment #: 1
// Submission Date: 9/29/2024
//
// Description: A program to encrypt and decrypt a message using a shift cipher
// The plaintext message must only contain lowercase alpha and digits 0-9
//
// command line arguments:
// -p theplaintextmessage1 - the plaintext (p) message to be encrypted
// -c PDALH7EJPATPIAOO7CA@ - the cipher (c) text to be decrypted
// -k 9                    - the key (k) shift value
// -e                      - the option to encrypt (e)
// -d                      - the option to decrypt (d)

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <algorithm>  // For std::find

// Define the codebook for shifting
char codebook[] = {
    'z', 'Z', 'y', 'Y', 'x', 'X', 'w', 'W', 'v', 'V', 'u', 'U', 't', 'T', 's', 'S', 'r', 'R', 'q', 'Q',
    'p', 'P', 'o', 'O', 'n', 'N', 'm', 'M', 'l', 'L', 'k', 'K', 'j', 'J', 'i', 'I', 'h', 'H', 'g', 'G',
    'f', 'F', 'e', 'E', 'd', 'D', 'c', 'C', 'b', 'B', 'a', 'A', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', ']'
};
const size_t CBL = sizeof(codebook) / sizeof(char);  // Use size_t to match the type returned by sizeof

// Function to encrypt the message using the shift key
std::string encrypt_message(const std::string& msg, int shift_key) {
    std::string encrypted_msg = msg;
    for (char& c : encrypted_msg) {
        auto it = std::find(std::begin(codebook), std::end(codebook), c);
        if (it != std::end(codebook)) {
            size_t pos = std::distance(std::begin(codebook), it);
            c = codebook[(pos + shift_key) % CBL];
        }
    }
    return encrypted_msg;
}

// Function to decrypt the message using the shift key
std::string decrypt_message(const std::string& msg, int shift_key) {
    std::string decrypted_msg = msg;
    for (char& c : decrypted_msg) {
        auto it = std::find(std::begin(codebook), std::end(codebook), c);
        if (it != std::end(codebook)) {
            size_t pos = std::distance(std::begin(codebook), it);
            int new_pos = (pos - shift_key) % CBL;
            if (new_pos < 0) new_pos += CBL;  // Handle negative wrap-around
            c = codebook[new_pos];
        }
    }
    return decrypted_msg;
}

int main(int argc, char* argv[]) {
    // Check if the number of arguments is less than the required 6
    if (argc < 6) {
        std::cerr << "Error: Not enough command line arguments.
";
        std::cerr << "Usage: " << argv[0] << " -p <plaintext> or -c <ciphertext> -k <shift key> -e or -d
";
        return -1;
    }

    std::string msg;
    int shift_key = 0;
    bool encrypt = false, decrypt = false;

    // Parsing command line arguments
    for (int i = 1; i < argc; ++i) {
        if (std::strcmp(argv[i], "-p") == 0) {
            if (i + 1 < argc) msg = argv[++i];  // Get plaintext message
            else {
                std::cerr << "Error: Missing plaintext value.
";
                return -1;
            }
        } else if (std::strcmp(argv[i], "-c") == 0) {
            if (i + 1 < argc) msg = argv[++i];  // Get ciphertext message
            else {
                std::cerr << "Error: Missing ciphertext value.
";
                return -1;
            }
        } else if (std::strcmp(argv[i], "-k") == 0) {
            if (i + 1 < argc) shift_key = std::atoi(argv[++i]);  // Get the shift key
            else {
                std::cerr << "Error: Missing shift key value.
";
                return -1;
            }
        } else if (std::strcmp(argv[i], "-e") == 0) {
            encrypt = true;  // Encrypt mode
        } else if (std::strcmp(argv[i], "-d") == 0) {
            decrypt = true;  // Decrypt mode
        }
    }

    // Check if both encryption and decryption are selected
    if (encrypt && decrypt) {
        std::cerr << "Error: Cannot select both encryption and decryption.
";
        return -1;
    }

    // Perform encryption or decryption
    if (encrypt) {
        std::string result = encrypt_message(msg, shift_key);
        std::cout << "Encrypted message: " << result << std::endl;
    } else if (decrypt) {
        std::string result = decrypt_message(msg, shift_key);
        std::cout << "Decrypted message: " << result << std::endl;
    } else {
        std::cerr << "Error: You must specify either encryption (-e) or decryption (-d).
";
        return -1;
    }

    return 0;
}
