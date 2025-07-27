
// Name: Your First Name & Last Name
// SSID: Student ID Number
// Assignment #: 1
// Submission Date: 9/29/2024
//
// Description: A program to encrypt and decrypt a message using a shift cipher
// The plaintext message must only contain lowercase alpha and digits 0-9
//
// command line arguments
// -p theplaintextmessage1 - the plaintext (p) message to be encrypted
// -c PDALH7EJPATPIAOO7CA@ - the cipher (c) text to be decrypted
// -k 9                    - the key (k) shift value
// -e                      - the option to encrypt (e)
// -d                      - the option to decrypt (d)

#include <iostream>
#include <cstring>
#include <cstdlib>
#include <string>

//Command line args reference:
//https://docs.microsoft.com/en-us/cpp/cpp/main-function-command-line-args
int main(int argc, char* argv[]) {
    // Check if the number of arguments is less than the required 6
    if (argc < 6) {
        // Print error message followed by usage instructions
        std::cerr << "Error: Not enough command line arguments.
";
        std::cerr << "Usage: " << argv[0] << " -p <plaintext> or -c <ciphertext> -k <shift key> -e or -d
";
        return -1;
    }

    // Remaining program logic (parsing, encryption, decryption) goes here.
    // ...
}
