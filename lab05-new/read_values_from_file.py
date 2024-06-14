def read_file(file_path):
    with open(file_path, 'r') as file:
        line = file.readline()
        number_of_points = int(line)
        matrix = [[0, 0] for y in range(number_of_points)]
        if number_of_points == 0:
            return

        for i in range(number_of_points):
            line = file.readline()
            matrix[i][0] = float(line.split()[0])
            matrix[i][1] = float(line.split()[1])

        x_arr = []
        y_arr = []
        for i in range(number_of_points):
            x_arr.append(matrix[i][0])
            y_arr.append(matrix[i][1])

        return {'x_arr': x_arr, 'y_arr': y_arr}
