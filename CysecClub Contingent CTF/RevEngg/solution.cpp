#include <iostream>
#include <string>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <bitset>
#include <stdexcept>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;
struct HuffmanNode {
    char data;
    unsigned frequency;
    HuffmanNode* left;
    HuffmanNode* right;
    HuffmanNode(char data, unsigned frequency)
        : data(data), frequency(frequency), left(nullptr), right(nullptr) {}
    ~HuffmanNode() {
        delete left;
        delete right;
    }
};
struct Compare {
    bool operator()(HuffmanNode* left, HuffmanNode* right) {
        return left->frequency > right->frequency;
    }
};
void buildCodes(HuffmanNode* root, const std::string& code, std::unordered_map<char, std::string>& codes) {
    if (!root)
        return;
    if (root->data != '\0')
        codes[root->data] = code;
    buildCodes(root->left, code + "0", codes);
    buildCodes(root->right, code + "1", codes);
}
HuffmanNode* buildHuffmanTree(const std::unordered_map<char, unsigned>& freqMap) {
    std::priority_queue<HuffmanNode*, std::vector<HuffmanNode*>, Compare> pq;
    for (const auto& pair : freqMap) {
        pq.push(new HuffmanNode(pair.first, pair.second));
    }
    while (pq.size() != 1) {
        HuffmanNode* left = pq.top(); pq.pop();
        HuffmanNode* right = pq.top(); pq.pop();
        HuffmanNode* parent = new HuffmanNode('\0', left->frequency + right->frequency);
        parent->left = left;
        parent->right = right;
        pq.push(parent);
    }
    return pq.top();
}
std::string encode(const std::string& data, const std::unordered_map<char, std::string>& codes) {
    std::string encoded;
    for (char c : data) {
        encoded += codes.at(c);
    }
    return encoded;
}
std::string decodeHuffman(const std::string& encodedStr, HuffmanNode* root) {
    std::string result;
    HuffmanNode* current = root;
    for (char bit : encodedStr) {
        if (bit == '0') current = current->left;
        else current = current->right;
        if (!current->left && !current->right) {
            result += current->data;
            current = root;
        }
    }
    return result;
}
int main(){
  std::unordered_map<char, unsigned> mp;
  mp['5'] = '1';
  mp['R'] = '1';
  mp['n'] = '1';
  mp['K'] = '1';
  mp['4'] = '1';
  mp['C'] = '1';
  mp['T'] = '2';
  mp['I'] = '2';
  mp['0'] = '1';
  mp['u'] = '1';
  mp['F'] = '1';
  mp['M'] = '1';
  mp['{'] = '1';
  mp['_'] = '1';
  mp['H'] = '1';
  mp['}'] = '1';
  mp['f'] = '2';
  mp['m'] = '1';
  std::string encoded_flag = "1773 1166 1693 1110 795 1561 115 1879";
  
  /*
  we know it has 8 rows (cause 8 numbers here)... How do we figure out the number of characters?
  The thing about huffman codes is, as long as the frequencies remain the same, the encoded string is the same... --> make a random string from the
  frequency table, say "5RnK4CTTII0uFM{_}Hffm", then encode it using huffman encoding
*/
  std::string data = "5RnK4CTTII0uFM{_}Hffm";
  HuffmanNode* root = buildHuffmanTree(mp); // build the tree
  std::unordered_map<char, std::string> codes; // build the codes
    buildCodes(root, "", codes);
    
    std::string encoded = encode(data, codes);
    std::cout << encoded.size(); // Now we have the size of the encoded flag
    int cols = encoded.size();
    int rows = 8;
    // now we want to convert each number in encoded_flag to its binary form and pad that to "cols" size. for example, base2 of 317 is 100111101 which is 9 digits, but i need 11
    // so, i will make 317 as 00100111101... and so on for each of them 
    std::stringstream ss(encoded_flag);
    std::vector<int> numbers;
    std::string temp;
                                // break the string into numbers
    while (ss >> temp) {
        numbers.push_back(std::stoi(temp)); // Convert to integer and store
    }
    std::vector<std::string> binaryStrings;														// convert to binary, pad to length 11, and store it in the binaryStrings vector
    for (int num : numbers) {
        std::string binary = std::bitset<11>(num).to_string();
        binaryStrings.push_back(binary);
    }
/*
    for (const std::string &binary : binaryStrings) {													// print em
        std::cout << binary;
    }
*/
    // with this you get the huffman encoded string of the FLAG itself and you have the frequency table of the flag...
    // 1101110110110010001110110100111011000101011001100011011110000110010000111001111101010111
    std::string encodedString = "1101110110110010001110110100111011000101011001100011011110000110010000111001111101010111";
    // now write the decode function and decode it using the frequency table and the encoded string to get the flag.
    std::string flagDecoded = decodeHuffman(encodedString, root);
    std::cout << flagDecoded;
}
