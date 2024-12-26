#include <bits/stdc++.h>

using namespace std;

// ��������
vector<string> split(const string& s, char delimiter);
int stringToInt(const string& s);

// ���ڽ�����ת��Ϊ�ַ���������汾
template <typename T>
string to_string(T value) {
    stringstream ss;
    ss << value;
    return ss.str();
}

void transformInput(const string& input_data) {
    try {
        // �����������
        vector<string> data_list = split(input_data, '	');

        // �����һ������
        int student_number = stringToInt(data_list[0].substr(6)) * 2;
        string classroom = data_list[0].substr(2, 4);

        // ����ڶ�������
        string file_name = data_list[1];
        int question_number = stringToInt(file_name.substr(10, 2));

        // ������������
        string status = data_list[4];
        if (status != "pass") {
            throw invalid_argument("�ύ״̬��Ϊpass");
        }

        // �ж��Ƿ�Ϊ��ɱ
        string first_blood = "";
        if (data_list[5] == "��") {
            first_blood = "����ɱ��";
        }

        // ���ת����Ľ��
        string result = "��" + to_string(question_number) + "��" + first_blood + " " + classroom + "��λ" + to_string(student_number);
        cout << result << endl;
    } catch (const exception& e) {
        cerr << "��������" << e.what() << endl;
    }
}

// �������������ַ����ָ�Ϊ����
vector<string> split(const string& s, char delimiter) {
    vector<string> tokens;
    istringstream tokenStream(s);
    string token;
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

// �������������ַ���ת��Ϊ����
int stringToInt(const string& s) {
    istringstream iss(s);
    int result;
    iss >> result;
    return result;
}

int main() {
    // ��������
    string input_data;
    while (true) {
        getline(cin, input_data);
        transformInput(input_data);
    }

    return 0;
}

