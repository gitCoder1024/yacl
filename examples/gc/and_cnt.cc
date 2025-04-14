

#include <fstream>
#include <iostream>
#include <regex>
#include <string>

int main() {
  std::ifstream file(
      "/home/dase212/lxy/yacl/yacl/io/circuit/data/sha256.txt");  // 你要读取的文件路径
  if (!file.is_open()) {
    std::cerr << "无法打开文件。" << std::endl;
    return 1;
  }

  std::string content((std::istreambuf_iterator<char>(file)),
                      std::istreambuf_iterator<char>());

  file.close();

  // 使用正则表达式匹配整个单词 "AND"
  std::regex word_regex(R"(\bAND\b)");
  std::sregex_iterator iter(content.begin(), content.end(), word_regex);
  std::sregex_iterator end;

  int count = std::distance(iter, end);
  std::cout << "文件中出现了 " << count << " 次 \"AND\"" << std::endl;

  return 0;
}