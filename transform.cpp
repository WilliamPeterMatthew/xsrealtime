#include <bits/stdc++.h>

using namespace std;

// 函数声明
vector<string> split(const string& s, char delimiter);
int stringToInt(const string& s);

// 用于将整数转换为字符串的替代版本
template <typename T>
string to_string(T value) {
    stringstream ss;
    ss << value;
    return ss.str();
}

void transformInput(const string& input_data) {
    try {
        // 拆分输入数据
        vector<string> data_list = split(input_data, '	');

        // 处理第一个数据
        int student_number = stringToInt(data_list[0].substr(6)) * 2;
        string classroom = data_list[0].substr(2, 4);

        // 处理第二个数据
        string file_name = data_list[1];
        int question_number = stringToInt(file_name.substr(10, 2));

        // 处理第五个数据
        string status = data_list[4];
        if (status != "pass") {
            throw invalid_argument("提交状态不为pass");
        }

        // 判断是否为首杀
        string first_blood = "";
        if (data_list[5] == "是") {
            first_blood = "【首杀】";
        }

        // 输出转化后的结果
        string result = "第" + to_string(question_number) + "题" + first_blood + " " + classroom + "座位" + to_string(student_number);
        cout << result << endl;
    } catch (const exception& e) {
        cerr << "发生错误：" << e.what() << endl;
    }
}

// 辅助函数：将字符串分割为单词
vector<string> split(const string& s, char delimiter) {
    vector<string> tokens;
    istringstream tokenStream(s);
    string token;
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

// 辅助函数：将字符串转换为整数
int stringToInt(const string& s) {
    istringstream iss(s);
    int result;
    iss >> result;
    return result;
}

int main() {
    // 测试例子
    string input_data;
    while (true) {
        getline(cin, input_data);
        transformInput(input_data);
    }

    return 0;
}

