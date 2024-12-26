def transform_input(input_data):
    try:
        # 拆分输入数据
        data_list = input_data.split()

        # 处理第一个数据
        student_number = int(data_list[0][4:]) * 2
        classroom = data_list[0][2:5]

        # 处理第二个数据
        file_name = data_list[1]
        question_number = int(file_name[10:12])

        # 处理第五个数据
        status = data_list[4]
        if status != "pass":
            raise ValueError("提交状态不为pass")

        # 判断是否为首杀
        first_blood = ""
        if data_list[5] == "是":
            first_blood = "【首杀】"

        # 输出转化后的结果
        result = f"第{question_number}题{first_blood} {classroom}座位{student_number}"
        print(result)

    except Exception as e:
        print(f"发生错误：{e}")

# 测试例子
while True:
    transform_input(input())
